#!/usr/bin/env python3
"""Diff MRD resistance geometry coverage states.

This is a structural artifact diff. It does not rank mechanisms, validate
clinical utility, interpret MRD, recommend treatment, or support patient
matching.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
COVERAGE_REL = Path("disease-programs/multiple-myeloma/mechanisms/mrd-resistance-geometry-coverage-v0.json")
METRIC_KEYS = ("signal_count", "extraction_record_count", "covered_source_count")
SET_KEYS = ("source_ids", "covered_source_ids", "extraction_record_ids", "extraction_signal_ids")


def load_json_file(path: Path) -> dict[str, Any]:
    doc = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return doc


def load_git_json(root: Path, ref: str, rel_path: Path) -> dict[str, Any]:
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"{ref}:{rel_path.as_posix()}"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise ValueError(result.stderr.strip() or f"could not read {rel_path} at {ref}")
    doc = json.loads(result.stdout)
    if not isinstance(doc, dict):
        raise ValueError(f"{rel_path} at {ref} must contain a JSON object")
    return doc


def rows_by_mechanism(doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for row in doc.get("mechanism_coverage", []):
        if not isinstance(row, dict):
            continue
        mechanism_id = row.get("mechanism_group_id")
        if isinstance(mechanism_id, str):
            rows[mechanism_id] = row
    return rows


def strings(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {item for item in value if isinstance(item, str)}


def metric(row: dict[str, Any] | None, key: str) -> int:
    if row is None:
        return 0
    value = row.get(key)
    return value if isinstance(value, int) else 0


def state_diff(before: dict[str, Any], after: dict[str, Any]) -> list[dict[str, Any]]:
    before_rows = rows_by_mechanism(before)
    after_rows = rows_by_mechanism(after)
    mechanism_ids = sorted(set(before_rows) | set(after_rows))
    diffs: list[dict[str, Any]] = []

    for mechanism_id in mechanism_ids:
        before_row = before_rows.get(mechanism_id)
        after_row = after_rows.get(mechanism_id)
        row_diff: dict[str, Any] = {
            "mechanism_group_id": mechanism_id,
            "label": (after_row or before_row or {}).get("label", mechanism_id),
            "status_before": None if before_row is None else before_row.get("coverage_status"),
            "status_after": None if after_row is None else after_row.get("coverage_status"),
            "metric_deltas": {},
            "added": {},
            "removed": {},
        }

        for key in METRIC_KEYS:
            before_value = metric(before_row, key)
            after_value = metric(after_row, key)
            delta = after_value - before_value
            if delta:
                row_diff["metric_deltas"][key] = delta

        for key in SET_KEYS:
            before_values = strings(None if before_row is None else before_row.get(key))
            after_values = strings(None if after_row is None else after_row.get(key))
            added = sorted(after_values - before_values)
            removed = sorted(before_values - after_values)
            if added:
                row_diff["added"][key] = added
            if removed:
                row_diff["removed"][key] = removed

        if (
            row_diff["status_before"] != row_diff["status_after"]
            or row_diff["metric_deltas"]
            or row_diff["added"]
            or row_diff["removed"]
        ):
            diffs.append(row_diff)

    return diffs


def print_text(diff_rows: list[dict[str, Any]], before_label: str, after_label: str) -> None:
    print("MRD geometry state diff")
    print("Boundary: structural artifact diff only; not clinical validation.")
    print(f"Before: {before_label}")
    print(f"After:  {after_label}")
    print()

    if not diff_rows:
        print("No mechanism coverage movements detected.")
        return

    for row in diff_rows:
        print(f"{row['mechanism_group_id']} ({row['label']})")
        if row["status_before"] != row["status_after"]:
            print(f"  status: {row['status_before']} -> {row['status_after']}")
        for key, delta in row["metric_deltas"].items():
            sign = "+" if delta > 0 else ""
            print(f"  {key}: {sign}{delta}")
        for key, values in row["added"].items():
            print(f"  added {key}: {', '.join(values)}")
        for key, values in row["removed"].items():
            print(f"  removed {key}: {', '.join(values)}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--before", type=Path, help="Path to a before coverage report JSON.")
    parser.add_argument("--after", type=Path, help="Path to an after coverage report JSON.")
    parser.add_argument("--before-ref", default="HEAD", help="Git ref for default before state.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable diff.")
    args = parser.parse_args()

    root = args.root.resolve()
    after_path = args.after.resolve() if args.after else root / COVERAGE_REL

    try:
        if args.before:
            before = load_json_file(args.before.resolve())
            before_label = str(args.before)
        else:
            before = load_git_json(root, args.before_ref, after_path.relative_to(root))
            before_label = f"{args.before_ref}:{after_path.relative_to(root).as_posix()}"
        after = load_json_file(after_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL load-inputs: {exc}", file=sys.stderr)
        return 1

    after_label = str(after_path)
    diff_rows = state_diff(before, after)

    if args.json:
        print(
            json.dumps(
                {
                    "diff_id": "mrd-geometry-state-diff-v0",
                    "clinical_use_boundary": "research-use-only",
                    "interpretation_boundary": [
                        "Structural artifact diff only.",
                        "Not clinical validation.",
                        "Not evidence-strength ranking.",
                        "Not mechanism-frequency ranking.",
                        "Not patient-specific MRD interpretation.",
                        "Not treatment, trial, monitoring, target, or cure guidance."
                    ],
                    "before": before_label,
                    "after": after_label,
                    "changes": diff_rows,
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print_text(diff_rows, before_label, after_label)

    return 0


if __name__ == "__main__":
    sys.exit(main())
