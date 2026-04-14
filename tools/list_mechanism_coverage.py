#!/usr/bin/env python3
"""List mechanism bucket extraction coverage for the public myeloma lane."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_MAP = Path("disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-map-v0.json")
DEFAULT_EXTRACTIONS = Path("disease-programs/multiple-myeloma/mechanisms/extractions")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def values(doc: dict[str, Any], key: str) -> list[str]:
    raw = doc.get(key)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, str)]


def mechanism_groups(root: Path, map_path: Path) -> list[dict[str, Any]]:
    doc = load_json(root / map_path)
    groups = doc.get("mechanism_groups")
    if not isinstance(groups, list):
        return []
    return [group for group in groups if isinstance(group, dict)]


def extraction_records(root: Path, extractions_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted((root / extractions_dir).glob("*.json")):
        doc = load_json(path)
        if isinstance(doc, dict) and "extraction_record_id" in doc:
            records.append(doc)
    return records


def coverage_status(record_count: int) -> str:
    if record_count == 0:
        return "needs-first-extraction"
    if record_count == 1:
        return "needs-second-source-extraction"
    return "covered-for-v0-navigation"


def coverage_reason(status: str) -> str:
    if status == "needs-first-extraction":
        return "No extracted signals currently map to this mechanism bucket."
    if status == "needs-second-source-extraction":
        return "Only one extraction record currently maps to this mechanism bucket."
    return "At least two extraction records currently map to this mechanism bucket."


def next_need(status: str, label: str) -> str:
    if status == "needs-first-extraction":
        return f"Add the first source-specific extraction for {label}."
    if status == "needs-second-source-extraction":
        return f"Add at least one additional public source extraction for {label} before comparison."
    return f"Use current {label} coverage for navigation only; do not rank biological importance from counts."


def build_coverage(groups: list[dict[str, Any]], records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for group in groups:
        mechanism_id = group.get("mechanism_id")
        if not isinstance(mechanism_id, str):
            continue

        signal_ids: list[str] = []
        record_ids: set[str] = set()
        covered_sources: set[str] = set()
        for record in records:
            record_id = record.get("extraction_record_id")
            source_ids = values(record, "source_ids")
            signals = record.get("extracted_signals")
            if not isinstance(record_id, str) or not isinstance(signals, list):
                continue
            for signal in signals:
                if not isinstance(signal, dict) or signal.get("mechanism_group_id") != mechanism_id:
                    continue
                signal_id = signal.get("signal_id")
                if isinstance(signal_id, str):
                    signal_ids.append(signal_id)
                record_ids.add(record_id)
                covered_sources.update(source_ids)

        label = str(group.get("label", mechanism_id))
        status = coverage_status(len(record_ids))
        map_sources = set(values(group, "source_ids"))
        rows.append(
            {
                "mechanism_group_id": mechanism_id,
                "label": label,
                "signal_count": len(signal_ids),
                "extraction_record_count": len(record_ids),
                "covered_source_count": len(covered_sources),
                "coverage_status": status,
                "under_coverage_flag": status != "covered-for-v0-navigation",
                "under_coverage_reason": coverage_reason(status),
                "source_ids": sorted(map_sources | covered_sources),
                "covered_source_ids": sorted(covered_sources),
                "extraction_record_ids": sorted(record_ids),
                "extraction_signal_ids": sorted(signal_ids),
                "next_extraction_need": next_need(status, label),
            }
        )
    return rows


def keep_row(row: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.status and row.get("coverage_status") != args.status:
        return False
    if args.under_covered and not row.get("under_coverage_flag"):
        return False
    return True


def print_text(rows: list[dict[str, Any]]) -> None:
    print("Mechanism coverage summary")
    print(f"Mechanism buckets: {len(rows)}")
    print(f"Extraction records represented: {len({record for row in rows for record in row['extraction_record_ids']})}")
    print(f"Extraction signals represented: {sum(int(row['signal_count']) for row in rows)}")
    print()
    print("Boundary: coverage counts are public artifact coverage metrics only.")
    print("They are not evidence-strength, frequency, or biological-importance rankings.")
    print()

    for row in rows:
        print(f"{row['mechanism_group_id']} - {row['label']}")
        print(f"  status: {row['coverage_status']}")
        print(f"  signals: {row['signal_count']}")
        print(f"  extraction_records: {row['extraction_record_count']}")
        print(f"  covered_sources: {row['covered_source_count']}")
        print(f"  next_need: {row['next_extraction_need']}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--map", type=Path, default=DEFAULT_MAP)
    parser.add_argument("--extractions", type=Path, default=DEFAULT_EXTRACTIONS)
    parser.add_argument(
        "--status",
        choices=[
            "needs-first-extraction",
            "needs-second-source-extraction",
            "covered-for-v0-navigation",
        ],
        help="Only show buckets with this coverage status.",
    )
    parser.add_argument("--under-covered", action="store_true", help="Only show buckets that need more extraction.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    rows = [row for row in build_coverage(mechanism_groups(root, args.map), extraction_records(root, args.extractions)) if keep_row(row, args)]

    if args.json:
        print(json.dumps({"mechanism_coverage": rows}, indent=2, sort_keys=True))
    else:
        print_text(rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
