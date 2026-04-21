#!/usr/bin/env python3
"""Check measurement-refusal wrapper negative safety fixtures.

The fixtures are synthetic mutations of the public wrapper integration dry-run
report. They must make the wrapper dry-run checker fail closed without using
real reports, clinical interpretation, ranking, recommendations, model output,
publication authorization, or patient-specific decisions.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import check_measurement_refusal_wrapper_integration_dry_run as dry_run


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
NEGATIVE_FIXTURES = Path("examples/measurement-refusal-wrapper-negative-safety-fixtures-v0.json")

FIXTURE_SET_ID = "measurement-refusal-wrapper-negative-safety-fixtures-v0"
TARGET_CHECKER_ID = "measurement-refusal-wrapper-integration-dry-run-check-v0"
TARGET_DRY_RUN_ID = "measurement-refusal-wrapper-integration-dry-run-v0"
NEXT_SUCCESSOR = "measurement-refusal-wrapper-state-machine-v0"

REQUIRED_NEGATIVE_FIXTURE_IDS = {
    "mrwns_00_prediction_boundary_flag_v0",
    "mrwns_01_clinical_boundary_missing_v0",
    "mrwns_02_missing_wrapper_record_v0",
    "mrwns_03_duplicate_wrapper_record_v0",
    "mrwns_04_wrong_wrapper_id_v0",
    "mrwns_05_unsafe_output_family_v0",
    "mrwns_06_clinical_output_enabled_v0",
    "mrwns_07_prediction_output_enabled_v0",
    "mrwns_08_private_review_unblocked_v0",
    "mrwns_09_wrapper_boundary_expanded_v0",
    "mrwns_10_blocked_downstream_use_gap_v0",
    "mrwns_11_forbidden_clinical_field_v0",
    "mrwns_12_forbidden_ranking_field_v0",
}

ALLOWED_MUTATION_OPS = {
    "add_wrapper_field",
    "drop_wrapper_record",
    "duplicate_wrapper_record",
    "remove_list_value",
    "remove_wrapper_blocked_use",
    "set",
    "set_wrapper_field",
}


@dataclass
class CheckResult:
    check_id: str
    passed: bool
    detail: str


def load_json(root: Path, rel_path: Path) -> Any:
    return json.loads((root / rel_path).read_text(encoding="utf-8"))


def values(doc: dict[str, Any], key: str) -> list[str]:
    raw = doc.get(key)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, str)]


def at_path(doc: Any, path: list[Any]) -> Any:
    current = doc
    for part in path:
        if isinstance(part, int):
            if not isinstance(current, list):
                raise ValueError(f"path segment {part} does not resolve through a list")
            current = current[part]
        elif isinstance(part, str):
            if not isinstance(current, dict):
                raise ValueError(f"path segment {part} does not resolve through an object")
            current = current[part]
        else:
            raise ValueError("path segments must be strings or integers")
    return current


def set_at_path(doc: Any, path: list[Any], value: Any) -> None:
    if not path:
        raise ValueError("set mutation requires a non-empty path")
    parent = at_path(doc, path[:-1]) if len(path) > 1 else doc
    final = path[-1]
    if isinstance(final, int):
        if not isinstance(parent, list):
            raise ValueError("set mutation final integer segment requires a list parent")
        parent[final] = value
    elif isinstance(final, str):
        if not isinstance(parent, dict):
            raise ValueError("set mutation final string segment requires an object parent")
        parent[final] = value
    else:
        raise ValueError("path segments must be strings or integers")


def remove_value(items: Any, value: str, label: str) -> None:
    if not isinstance(items, list):
        raise ValueError(f"{label} must be a list")
    try:
        items.remove(value)
    except ValueError as exc:
        raise ValueError(f"{label} does not contain {value}") from exc


def wrapper_records(report: dict[str, Any]) -> list[dict[str, Any]]:
    rows = report.get("wrapper_records")
    if not isinstance(rows, list):
        raise ValueError("wrapper_records must be a list")
    return [row for row in rows if isinstance(row, dict)]


def wrapper_record_for(report: dict[str, Any], source_output_id: str) -> dict[str, Any]:
    for record in wrapper_records(report):
        if record.get("source_output_id") == source_output_id:
            return record
    raise ValueError(f"source_output_id not found: {source_output_id}")


def apply_mutation(report: dict[str, Any], mutation: dict[str, Any]) -> None:
    op = mutation.get("op")
    if op not in ALLOWED_MUTATION_OPS:
        raise ValueError(f"unsupported mutation op: {op!r}")

    if op == "set":
        path = mutation.get("path")
        if not isinstance(path, list):
            raise ValueError("set mutation requires path")
        set_at_path(report, path, mutation.get("value"))
        return

    if op == "remove_list_value":
        path = mutation.get("path")
        value = mutation.get("value")
        if not isinstance(path, list) or not isinstance(value, str):
            raise ValueError("remove_list_value mutation requires path and value")
        remove_value(at_path(report, path), value, ".".join(str(part) for part in path))
        return

    if op == "drop_wrapper_record":
        source_output_id = mutation.get("source_output_id")
        if not isinstance(source_output_id, str):
            raise ValueError("drop_wrapper_record mutation requires source_output_id")
        rows = wrapper_records(report)
        original_len = len(rows)
        report["wrapper_records"] = [
            record for record in rows if record.get("source_output_id") != source_output_id
        ]
        if len(report["wrapper_records"]) == original_len:
            raise ValueError(f"drop_wrapper_record did not remove {source_output_id}")
        return

    if op == "duplicate_wrapper_record":
        source_output_id = mutation.get("source_output_id")
        new_wrapper_record_id = mutation.get("new_wrapper_record_id")
        if not isinstance(source_output_id, str) or not isinstance(new_wrapper_record_id, str):
            raise ValueError("duplicate_wrapper_record mutation requires source_output_id and new_wrapper_record_id")
        duplicate = copy.deepcopy(wrapper_record_for(report, source_output_id))
        duplicate["wrapper_record_id"] = new_wrapper_record_id
        report["wrapper_records"].append(duplicate)
        return

    if op == "set_wrapper_field":
        source_output_id = mutation.get("source_output_id")
        field = mutation.get("field")
        if not isinstance(source_output_id, str) or not isinstance(field, str):
            raise ValueError("set_wrapper_field mutation requires source_output_id and field")
        wrapper_record_for(report, source_output_id)[field] = mutation.get("value")
        return

    if op == "remove_wrapper_blocked_use":
        source_output_id = mutation.get("source_output_id")
        blocked_use = mutation.get("blocked_use")
        if not isinstance(source_output_id, str) or not isinstance(blocked_use, str):
            raise ValueError("remove_wrapper_blocked_use mutation requires source_output_id and blocked_use")
        record = wrapper_record_for(report, source_output_id)
        remove_value(record.get("blocked_downstream_uses"), blocked_use, "blocked_downstream_uses")
        return

    if op == "add_wrapper_field":
        source_output_id = mutation.get("source_output_id")
        field = mutation.get("field")
        if not isinstance(source_output_id, str) or not isinstance(field, str):
            raise ValueError("add_wrapper_field mutation requires source_output_id and field")
        record = wrapper_record_for(report, source_output_id)
        record[field] = mutation.get("value")
        return


def failed_check_ids(report: dict[str, Any], output_doc: dict[str, Any], route_doc: dict[str, Any]) -> set[str]:
    failures = dry_run.validate_report(report, output_doc, route_doc)
    wrapper_rows = report.get("wrapper_records")
    wrapper_count = len(wrapper_rows) if isinstance(wrapper_rows, list) else 0

    failed: set[str] = set()
    if report.get("wrapper_integration_dry_run_id") != dry_run.DRY_RUN_ID:
        failed.add("wrapper-dry-run-id")
    if report.get("target_wrapper_id") != dry_run.WRAPPER_ID:
        failed.add("wrapper-dry-run-target")
    if dry_run.boundary_failures(report.get("data_boundary") if isinstance(report.get("data_boundary"), dict) else None):
        failed.add("wrapper-dry-run-public-synthetic-only")
    if wrapper_count != len(dry_run.output_rows(output_doc)):
        failed.add("wrapper-dry-run-record-coverage")
    if failures:
        failed.add("wrapper-dry-run-preserves-refusal-boundaries")
    return failed


def run_checks(root: Path) -> list[CheckResult]:
    fixture_pack = load_json(root, NEGATIVE_FIXTURES)
    dry_run_report = load_json(root, dry_run.DEFAULT_REPORT)
    output_doc = load_json(root, dry_run.OUTPUT_FIXTURE)
    route_doc = load_json(root, dry_run.ROUTE_TABLE)
    if (
        not isinstance(fixture_pack, dict)
        or not isinstance(dry_run_report, dict)
        or not isinstance(output_doc, dict)
        or not isinstance(route_doc, dict)
    ):
        raise ValueError("wrapper negative fixture inputs must be JSON objects")

    results: list[CheckResult] = []
    results.append(
        CheckResult(
            "wrapper-negative-fixture-set-id",
            fixture_pack.get("fixture_set_id") == FIXTURE_SET_ID,
            f"fixture_set_id={fixture_pack.get('fixture_set_id')!r}",
        )
    )
    results.append(
        CheckResult(
            "wrapper-negative-fixture-target-checker",
            fixture_pack.get("target_checker_id") == TARGET_CHECKER_ID
            and fixture_pack.get("target_dry_run_id") == TARGET_DRY_RUN_ID,
            f"target_checker_id={fixture_pack.get('target_checker_id')!r}; target_dry_run_id={fixture_pack.get('target_dry_run_id')!r}",
        )
    )

    boundary = fixture_pack.get("data_boundary")
    boundary_failures = (
        sorted(field for field in dry_run.REQUIRED_FALSE_BOUNDARY_FIELDS if boundary.get(field) is not False)
        if isinstance(boundary, dict)
        else sorted(dry_run.REQUIRED_FALSE_BOUNDARY_FIELDS)
    )
    results.append(
        CheckResult(
            "wrapper-negative-fixture-pack-public-synthetic-only",
            not boundary_failures,
            "all required data-boundary fields false"
            if not boundary_failures
            else f"not false: {', '.join(boundary_failures)}",
        )
    )

    fixture_rows = fixture_pack.get("negative_fixtures")
    if not isinstance(fixture_rows, list) or not fixture_rows:
        results.append(CheckResult("wrapper-negative-fixtures-present", False, "negative_fixtures missing or empty"))
        return results

    fixture_ids = {row.get("fixture_id") for row in fixture_rows if isinstance(row, dict)}
    missing_fixture_ids = sorted(REQUIRED_NEGATIVE_FIXTURE_IDS - {value for value in fixture_ids if isinstance(value, str)})
    results.append(
        CheckResult(
            "wrapper-negative-fixture-required-cases-present",
            not missing_fixture_ids,
            f"{len(REQUIRED_NEGATIVE_FIXTURE_IDS)} required fixtures present"
            if not missing_fixture_ids
            else f"missing: {', '.join(missing_fixture_ids)}",
        )
    )

    fixture_failures: list[str] = []
    for index, fixture in enumerate(fixture_rows):
        if not isinstance(fixture, dict):
            fixture_failures.append(f"negative_fixtures[{index}] must be an object")
            continue
        fixture_id = fixture.get("fixture_id", f"negative_fixtures[{index}]")
        expected = set(values(fixture, "expected_failed_check_ids"))
        mutations = fixture.get("mutations")
        if not expected:
            fixture_failures.append(f"{fixture_id}: expected_failed_check_ids missing")
            continue
        if not isinstance(mutations, list) or not mutations:
            fixture_failures.append(f"{fixture_id}: mutations missing or empty")
            continue

        mutated_report = copy.deepcopy(dry_run_report)
        try:
            for mutation in mutations:
                if not isinstance(mutation, dict):
                    raise ValueError("mutation must be an object")
                apply_mutation(mutated_report, mutation)
        except (KeyError, TypeError, ValueError) as exc:
            fixture_failures.append(f"{fixture_id}: mutation error: {exc}")
            continue

        actual = failed_check_ids(mutated_report, output_doc, route_doc)
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        if not actual:
            fixture_failures.append(f"{fixture_id}: wrapper dry-run checker did not fail")
        if missing:
            fixture_failures.append(f"{fixture_id}: expected failures not detected: {', '.join(missing)}")
        if unexpected:
            fixture_failures.append(f"{fixture_id}: unexpected failures: {', '.join(unexpected)}")

    results.append(
        CheckResult(
            "wrapper-negative-fixtures-fail-closed",
            not fixture_failures,
            f"{len(fixture_rows)} wrapper negative fixtures fail closed"
            if not fixture_failures
            else "; ".join(fixture_failures[:12]),
        )
    )

    return results


def print_text(results: list[CheckResult]) -> None:
    print("Measurement refusal wrapper negative safety fixture check")
    print("Boundary: synthetic wrapper fail-closed checks only; not clinical validation.")
    print()
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status} {result.check_id}: {result.detail}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--json", action="store_true", help="Print machine-readable check results.")
    args = parser.parse_args()

    root = args.root.resolve()
    try:
        results = run_checks(root)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL load-or-check-inputs: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(
            json.dumps(
                {
                    "check_id": "measurement-refusal-wrapper-negative-safety-fixture-check-v0",
                    "clinical_use_boundary": "research-use-only",
                    "next_no_outreach_successor_if_selected": NEXT_SUCCESSOR,
                    "results": [result.__dict__ for result in results],
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print_text(results)

    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
