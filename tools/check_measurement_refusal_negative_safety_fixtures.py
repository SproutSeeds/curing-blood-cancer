#!/usr/bin/env python3
"""Check measurement-refusal negative safety fixtures.

The fixtures are synthetic mutations of the public measurement-refusal route
table. They must make the validator fail closed without using real reports,
clinical interpretation, ranking, recommendations, or patient-specific output.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import measurement_refusal_validator_skeleton as validator


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
NEGATIVE_FIXTURES = Path("examples/measurement-refusal-negative-safety-fixtures-v0.json")

FIXTURE_SET_ID = "measurement-refusal-negative-safety-fixtures-v0"
TARGET_VALIDATOR_ID = "measurement-refusal-validator-skeleton-v0"
NEXT_SUCCESSOR = "measurement-refusal-wrapper-state-machine-v0"

REQUIRED_NEGATIVE_FIXTURE_IDS = {
    "mrns_00_prediction_boundary_flag_v0",
    "mrns_01_clinical_boundary_missing_v0",
    "mrns_02_missing_route_v0",
    "mrns_03_duplicate_route_v0",
    "mrns_04_blocked_manifest_gap_v0",
    "mrns_05_destination_contract_gap_v0",
    "mrns_06_unsafe_route_family_v0",
    "mrns_07_clinical_output_enabled_v0",
    "mrns_08_private_review_unblocked_v0",
    "mrns_09_forbidden_clinical_field_v0",
    "mrns_10_forbidden_ranking_field_v0",
}

ALLOWED_MUTATION_OPS = {
    "add_route_family",
    "drop_route",
    "duplicate_route",
    "remove_blocked_manifest_entry",
    "remove_destination_contract",
    "remove_list_value",
    "remove_route_blocked_route",
    "set",
    "set_route_field",
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


def at_path(doc: dict[str, Any], path: list[str]) -> Any:
    current: Any = doc
    for part in path:
        if not isinstance(current, dict):
            raise ValueError(f"path {'.'.join(path)} does not resolve through objects")
        current = current[part]
    return current


def set_at_path(doc: dict[str, Any], path: list[str], value: Any) -> None:
    if not path:
        raise ValueError("set mutation requires a non-empty path")
    parent = at_path(doc, path[:-1]) if len(path) > 1 else doc
    if not isinstance(parent, dict):
        raise ValueError(f"path {'.'.join(path[:-1])} does not resolve to an object")
    parent[path[-1]] = value


def routes(route_doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = route_doc.get("route_records")
    if not isinstance(rows, list):
        raise ValueError("route_records must be a list")
    return [row for row in rows if isinstance(row, dict)]


def route_for(route_doc: dict[str, Any], source_output_id: str) -> dict[str, Any]:
    for route in routes(route_doc):
        if route.get("source_output_id") == source_output_id:
            return route
    raise ValueError(f"source_output_id not found: {source_output_id}")


def remove_value(items: Any, value: str, label: str) -> None:
    if not isinstance(items, list):
        raise ValueError(f"{label} must be a list")
    try:
        items.remove(value)
    except ValueError as exc:
        raise ValueError(f"{label} does not contain {value}") from exc


def apply_mutation(
    output_doc: dict[str, Any],
    route_doc: dict[str, Any],
    mutation: dict[str, Any],
) -> None:
    op = mutation.get("op")
    if op not in ALLOWED_MUTATION_OPS:
        raise ValueError(f"unsupported mutation op: {op!r}")

    if op == "set":
        artifact = mutation.get("artifact")
        path = mutation.get("path")
        if artifact not in {"output_fixture", "route_table"} or not isinstance(path, list):
            raise ValueError("set mutation requires artifact and path")
        target = output_doc if artifact == "output_fixture" else route_doc
        set_at_path(target, [part for part in path if isinstance(part, str)], mutation.get("value"))
        return

    if op == "remove_list_value":
        artifact = mutation.get("artifact")
        path = mutation.get("path")
        value = mutation.get("value")
        if artifact not in {"output_fixture", "route_table"} or not isinstance(path, list) or not isinstance(value, str):
            raise ValueError("remove_list_value mutation requires artifact, path, and value")
        target = output_doc if artifact == "output_fixture" else route_doc
        remove_value(at_path(target, [part for part in path if isinstance(part, str)]), value, ".".join(path))
        return

    if op == "drop_route":
        source_output_id = mutation.get("source_output_id")
        if not isinstance(source_output_id, str):
            raise ValueError("drop_route mutation requires source_output_id")
        original_len = len(routes(route_doc))
        route_doc["route_records"] = [
            route for route in routes(route_doc) if route.get("source_output_id") != source_output_id
        ]
        if len(routes(route_doc)) == original_len:
            raise ValueError(f"drop_route did not remove {source_output_id}")
        return

    if op == "duplicate_route":
        source_output_id = mutation.get("source_output_id")
        new_route_id = mutation.get("new_route_id")
        if not isinstance(source_output_id, str) or not isinstance(new_route_id, str):
            raise ValueError("duplicate_route mutation requires source_output_id and new_route_id")
        duplicate = copy.deepcopy(route_for(route_doc, source_output_id))
        duplicate["route_id"] = new_route_id
        route_doc["route_records"].append(duplicate)
        return

    if op == "remove_blocked_manifest_entry":
        blocked_route = mutation.get("blocked_route")
        if not isinstance(blocked_route, str):
            raise ValueError("remove_blocked_manifest_entry mutation requires blocked_route")
        rows = route_doc.get("blocked_route_manifest")
        if not isinstance(rows, list):
            raise ValueError("blocked_route_manifest must be a list")
        original_len = len(rows)
        route_doc["blocked_route_manifest"] = [
            row for row in rows if not (isinstance(row, dict) and row.get("blocked_route") == blocked_route)
        ]
        if len(route_doc["blocked_route_manifest"]) == original_len:
            raise ValueError(f"blocked_route_manifest did not contain {blocked_route}")
        return

    if op == "remove_route_blocked_route":
        source_output_id = mutation.get("source_output_id")
        blocked_route = mutation.get("blocked_route")
        if not isinstance(source_output_id, str) or not isinstance(blocked_route, str):
            raise ValueError("remove_route_blocked_route mutation requires source_output_id and blocked_route")
        remove_value(route_for(route_doc, source_output_id).get("blocked_routes"), blocked_route, "blocked_routes")
        return

    if op == "remove_destination_contract":
        contract = mutation.get("contract")
        scope = mutation.get("scope")
        if not isinstance(contract, str):
            raise ValueError("remove_destination_contract mutation requires contract")
        if scope in {"top_level", "all"}:
            remove_value(route_doc.get("required_destination_contracts"), contract, "required_destination_contracts")
        if scope in {"route", "all"}:
            source_output_id = mutation.get("source_output_id")
            target_routes = routes(route_doc) if scope == "all" else [route_for(route_doc, str(source_output_id))]
            for route in target_routes:
                remove_value(route.get("destination_contracts"), contract, "destination_contracts")
        return

    if op == "add_route_family":
        source_output_id = mutation.get("source_output_id")
        route_family = mutation.get("route_family")
        if not isinstance(source_output_id, str) or not isinstance(route_family, str):
            raise ValueError("add_route_family mutation requires source_output_id and route_family")
        families = route_for(route_doc, source_output_id).get("allowed_route_families")
        if not isinstance(families, list):
            raise ValueError("allowed_route_families must be a list")
        families.append(route_family)
        return

    if op == "set_route_field":
        source_output_id = mutation.get("source_output_id")
        field = mutation.get("field")
        if not isinstance(source_output_id, str) or not isinstance(field, str):
            raise ValueError("set_route_field mutation requires source_output_id and field")
        route_for(route_doc, source_output_id)[field] = mutation.get("value")
        return


def failed_rule_ids(report: dict[str, Any]) -> set[str]:
    rows = report.get("rule_results")
    if not isinstance(rows, list):
        return set()
    return {
        row.get("rule_id")
        for row in rows
        if isinstance(row, dict) and row.get("status") != "pass" and isinstance(row.get("rule_id"), str)
    }


def run_checks(root: Path) -> list[CheckResult]:
    fixture_pack = load_json(root, NEGATIVE_FIXTURES)
    output_doc = load_json(root, validator.OUTPUT_FIXTURE)
    route_doc = load_json(root, validator.ROUTE_TABLE)
    if not isinstance(fixture_pack, dict) or not isinstance(output_doc, dict) or not isinstance(route_doc, dict):
        raise ValueError("negative fixture inputs must be JSON objects")

    results: list[CheckResult] = []

    results.append(
        CheckResult(
            "negative-fixture-set-id",
            fixture_pack.get("fixture_set_id") == FIXTURE_SET_ID,
            f"fixture_set_id={fixture_pack.get('fixture_set_id')!r}",
        )
    )
    results.append(
        CheckResult(
            "negative-fixture-target-validator",
            fixture_pack.get("target_validator_id") == TARGET_VALIDATOR_ID,
            f"target_validator_id={fixture_pack.get('target_validator_id')!r}",
        )
    )

    boundary = fixture_pack.get("data_boundary")
    boundary_failures = (
        sorted(field for field in validator.REQUIRED_FALSE_BOUNDARY_FIELDS if boundary.get(field) is not False)
        if isinstance(boundary, dict)
        else sorted(validator.REQUIRED_FALSE_BOUNDARY_FIELDS)
    )
    results.append(
        CheckResult(
            "negative-fixture-pack-public-synthetic-only",
            not boundary_failures,
            "all required data-boundary fields false" if not boundary_failures else f"not false: {', '.join(boundary_failures)}",
        )
    )

    fixture_rows = fixture_pack.get("negative_fixtures")
    if not isinstance(fixture_rows, list) or not fixture_rows:
        results.append(CheckResult("negative-fixtures-present", False, "negative_fixtures missing or empty"))
        return results
    fixture_ids = {row.get("fixture_id") for row in fixture_rows if isinstance(row, dict)}
    missing_fixture_ids = sorted(REQUIRED_NEGATIVE_FIXTURE_IDS - {value for value in fixture_ids if isinstance(value, str)})
    results.append(
        CheckResult(
            "negative-fixture-required-cases-present",
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
        expected = set(values(fixture, "expected_failed_rule_ids"))
        mutations = fixture.get("mutations")
        if not expected:
            fixture_failures.append(f"{fixture_id}: expected_failed_rule_ids missing")
            continue
        if not isinstance(mutations, list) or not mutations:
            fixture_failures.append(f"{fixture_id}: mutations missing or empty")
            continue

        mutated_output = copy.deepcopy(output_doc)
        mutated_routes = copy.deepcopy(route_doc)
        try:
            for mutation in mutations:
                if not isinstance(mutation, dict):
                    raise ValueError("mutation must be an object")
                apply_mutation(mutated_output, mutated_routes, mutation)
            report = validator.build_validator_report_from_docs(mutated_output, mutated_routes)
        except (KeyError, TypeError, ValueError) as exc:
            fixture_failures.append(f"{fixture_id}: mutation error: {exc}")
            continue

        actual = failed_rule_ids(report)
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        if report.get("report_status") != "fail":
            fixture_failures.append(f"{fixture_id}: report_status did not fail")
        if missing:
            fixture_failures.append(f"{fixture_id}: expected failures not detected: {', '.join(missing)}")
        if unexpected:
            fixture_failures.append(f"{fixture_id}: unexpected failures: {', '.join(unexpected)}")

    results.append(
        CheckResult(
            "negative-fixtures-fail-closed",
            not fixture_failures,
            f"{len(fixture_rows)} negative fixtures fail closed"
            if not fixture_failures
            else "; ".join(fixture_failures[:12]),
        )
    )

    return results


def print_text(results: list[CheckResult]) -> None:
    print("Measurement refusal negative safety fixture check")
    print("Boundary: synthetic fail-closed checks only; not clinical validation.")
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
                    "check_id": "measurement-refusal-negative-safety-fixture-check-v0",
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
    raise SystemExit(main())
