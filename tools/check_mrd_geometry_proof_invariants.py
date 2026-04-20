#!/usr/bin/env python3
"""Check MRD resistance geometry proof-readiness invariants.

The checks here are structural and safety-boundary checks. They do not validate
medical claims, rank mechanisms, interpret MRD, or support treatment decisions.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
MECHANISMS = Path("disease-programs/multiple-myeloma/mechanisms")
TASKS = Path("disease-programs/multiple-myeloma/public-tasks")
EXAMPLES = Path("examples")

PROOF_PLAN = MECHANISMS / "mrd-resistance-geometry-proof-plan-v0.json"
COVERAGE = MECHANISMS / "mrd-resistance-geometry-coverage-v0.json"
CONTRADICTION_QUEUE = TASKS / "mrd-resistance-geometry-contradiction-mining-task-queue-v0.json"
SECOND_SOURCE_QUEUE = TASKS / "mrd-resistance-geometry-second-source-task-queue-v0.json"
MOVEMENT_LEDGER = MECHANISMS / "mrd-resistance-geometry-movement-ledger-v0.json"
FIXTURE = EXAMPLES / "myeloma-residual-state-object-public-source-fixture-v0.json"
NEGATIVE_FIXTURES = EXAMPLES / "mrd-geometry-negative-safety-fixtures-v0.json"

REQUIRED_PROOF_TESTS = {
    "structural-separability-test-v0",
    "productive-movement-test-v0",
    "contradiction-response-test-v0",
    "state-object-fit-test-v0",
    "safety-invariance-test-v0",
}

REQUIRED_CONTRADICTION_TASKS = {
    "mrd-trajectory-contradiction-mining-task-v0",
    "clone-state-coupling-contradiction-mining-task-v0",
}

REQUIRED_SECOND_SOURCE_TASKS = {
    "metabolic-resistance-state-second-source-extraction-task-v0",
    "nfkb-selective-state-second-source-extraction-task-v0",
}

REQUIRED_COVERED_MECHANISMS = {
    "metabolic-resistance-state-v0",
    "nfkb-selective-state-v0",
}

REQUIRED_COMPLETED_OUTPUTS = {
    "mrd-trajectory-contradiction-mining-note-v0",
    "clone-state-coupling-contradiction-mining-note-v0",
    "wang-2025-lipid-metabolism-geometry-v0",
    "lu-2024-signaling-pathways-geometry-v0",
    "myeloma-residual-state-object-public-source-fixture-v0",
    "mrd-geometry-proof-invariant-check-v0",
}

REQUIRED_FALSE_BOUNDARY_FIELDS = {
    "uses_real_case_data",
    "contains_identifiers",
    "contains_predictions",
    "contains_recommendations",
    "contains_matching_or_ranking",
    "contains_clinical_decisions",
}

REQUIRED_BLOCKED_OUTPUTS = {
    "diagnosis",
    "prognosis",
    "relapse_risk",
    "mrd_interpretation",
    "monitoring_guidance",
    "treatment_guidance",
    "target_selection",
    "trial_guidance",
    "patient_matching",
    "mechanism_ranking",
    "evidence_ranking",
    "clinical_validation",
    "cure_claim",
}


@dataclass
class CheckResult:
    check_id: str
    passed: bool
    detail: str


def load_json(root: Path, rel_path: Path) -> Any:
    path = root / rel_path
    return json.loads(path.read_text(encoding="utf-8"))


def values(doc: dict[str, Any], key: str) -> list[str]:
    raw = doc.get(key)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, str)]


def task_statuses(queue: dict[str, Any]) -> dict[str, str]:
    statuses: dict[str, str] = {}
    tasks = queue.get("tasks")
    if not isinstance(tasks, list):
        return statuses
    for task in tasks:
        if not isinstance(task, dict):
            continue
        task_id = task.get("task_id")
        status = task.get("status")
        if isinstance(task_id, str) and isinstance(status, str):
            statuses[task_id] = status
    return statuses


def coverage_statuses(report: dict[str, Any]) -> dict[str, str]:
    statuses: dict[str, str] = {}
    rows = report.get("mechanism_coverage")
    if not isinstance(rows, list):
        return statuses
    for row in rows:
        if not isinstance(row, dict):
            continue
        mechanism_id = row.get("mechanism_group_id")
        status = row.get("coverage_status")
        if isinstance(mechanism_id, str) and isinstance(status, str):
            statuses[mechanism_id] = status
    return statuses


def boundary_failures(data_boundary: dict[str, Any] | None) -> list[str]:
    if not isinstance(data_boundary, dict):
        return sorted(REQUIRED_FALSE_BOUNDARY_FIELDS)
    return sorted(field for field in REQUIRED_FALSE_BOUNDARY_FIELDS if data_boundary.get(field) is not False)


def blocked_output_failures(blocked_manifest: dict[str, Any] | None) -> list[str]:
    if not isinstance(blocked_manifest, dict):
        return sorted(REQUIRED_BLOCKED_OUTPUTS)
    return sorted(output for output in REQUIRED_BLOCKED_OUTPUTS if blocked_manifest.get(output) != "blocked")


def negative_fixture_failed_check_ids(fixture_pack: dict[str, Any], fixture: dict[str, Any]) -> set[str]:
    pack_boundary = fixture_pack.get("data_boundary")
    fixture_boundary = fixture.get("data_boundary")
    merged_boundary: dict[str, Any] = {}
    if isinstance(pack_boundary, dict):
        merged_boundary.update(pack_boundary)
    if isinstance(fixture_boundary, dict):
        merged_boundary.update(fixture_boundary)

    failed: set[str] = set()
    if boundary_failures(merged_boundary):
        failed.add("fixture-data-boundary-fail-closed")
    if blocked_output_failures(fixture.get("blocked_output_manifest")):
        failed.add("fixture-blocked-output-manifest")
    return failed


def has_required_set(found: set[str], required: set[str]) -> tuple[bool, str]:
    missing = sorted(required - found)
    if missing:
        return False, f"missing: {', '.join(missing)}"
    return True, f"found {len(required)} required items"


def run_checks(root: Path) -> list[CheckResult]:
    proof_plan = load_json(root, PROOF_PLAN)
    coverage = load_json(root, COVERAGE)
    contradiction_queue = load_json(root, CONTRADICTION_QUEUE)
    second_source_queue = load_json(root, SECOND_SOURCE_QUEUE)
    movement_ledger = load_json(root, MOVEMENT_LEDGER)
    fixture = load_json(root, FIXTURE)
    negative_fixture_pack = load_json(root, NEGATIVE_FIXTURES)

    results: list[CheckResult] = []

    proof_tests = {
        test.get("test_id")
        for test in proof_plan.get("proof_tests", [])
        if isinstance(test, dict) and isinstance(test.get("test_id"), str)
    }
    passed, detail = has_required_set(proof_tests, REQUIRED_PROOF_TESTS)
    results.append(CheckResult("proof-plan-has-required-tests", passed, detail))

    contradiction_statuses = task_statuses(contradiction_queue)
    incomplete_contradiction = sorted(
        task_id for task_id in REQUIRED_CONTRADICTION_TASKS if contradiction_statuses.get(task_id) != "done"
    )
    results.append(
        CheckResult(
            "contradiction-mining-tasks-done",
            not incomplete_contradiction,
            "done" if not incomplete_contradiction else f"not done: {', '.join(incomplete_contradiction)}",
        )
    )

    second_source_statuses = task_statuses(second_source_queue)
    incomplete_second_sources = sorted(
        task_id for task_id in REQUIRED_SECOND_SOURCE_TASKS if second_source_statuses.get(task_id) != "done"
    )
    results.append(
        CheckResult(
            "second-source-tasks-done",
            not incomplete_second_sources,
            "done" if not incomplete_second_sources else f"not done: {', '.join(incomplete_second_sources)}",
        )
    )

    mechanism_statuses = coverage_statuses(coverage)
    uncovered_mechanisms = sorted(
        mechanism_id
        for mechanism_id in REQUIRED_COVERED_MECHANISMS
        if mechanism_statuses.get(mechanism_id) != "covered-for-v0-navigation"
    )
    results.append(
        CheckResult(
            "pathway-branches-covered-for-v0-navigation",
            not uncovered_mechanisms,
            "covered" if not uncovered_mechanisms else f"not covered: {', '.join(uncovered_mechanisms)}",
        )
    )

    ledger_status = movement_ledger.get("ledger_status")
    results.append(
        CheckResult(
            "movement-ledger-proof-readiness-status",
            ledger_status == "proof-readiness-v0",
            f"ledger_status={ledger_status!r}",
        )
    )

    completed_outputs = set(values(movement_ledger, "completed_output_ids"))
    passed, detail = has_required_set(completed_outputs, REQUIRED_COMPLETED_OUTPUTS)
    results.append(CheckResult("movement-ledger-required-outputs", passed, detail))

    false_failures = boundary_failures(fixture.get("data_boundary"))
    results.append(
        CheckResult(
            "fixture-data-boundary-fail-closed",
            not false_failures,
            "all required fields false" if not false_failures else f"not false: {', '.join(false_failures)}",
        )
    )

    blocked_failures = blocked_output_failures(fixture.get("blocked_output_manifest"))
    results.append(
        CheckResult(
            "fixture-blocked-output-manifest",
            not blocked_failures,
            "all required outputs blocked" if not blocked_failures else f"not blocked: {', '.join(blocked_failures)}",
        )
    )

    negative_fixture_failures: list[str] = []
    negative_fixtures = negative_fixture_pack.get("negative_fixtures")
    if not isinstance(negative_fixtures, list) or not negative_fixtures:
        negative_fixture_failures.append("negative_fixtures missing or empty")
    else:
        for fixture_index, negative_fixture in enumerate(negative_fixtures):
            if not isinstance(negative_fixture, dict):
                negative_fixture_failures.append(f"negative_fixtures[{fixture_index}] must be an object")
                continue
            fixture_id = negative_fixture.get("fixture_id", f"negative_fixtures[{fixture_index}]")
            expected = set(values(negative_fixture, "expected_failed_check_ids"))
            actual = negative_fixture_failed_check_ids(negative_fixture_pack, negative_fixture)
            if not expected:
                negative_fixture_failures.append(f"{fixture_id}: no expected_failed_check_ids")
            missing = sorted(expected - actual)
            if missing:
                negative_fixture_failures.append(
                    f"{fixture_id}: expected failures not detected: {', '.join(missing)}"
                )
            if not actual:
                negative_fixture_failures.append(f"{fixture_id}: no fail-closed checks triggered")
    results.append(
        CheckResult(
            "negative-fixtures-fail-closed",
            not negative_fixture_failures,
            (
                f"{len(negative_fixtures)} negative fixtures fail closed"
                if isinstance(negative_fixtures, list) and not negative_fixture_failures
                else "; ".join(negative_fixture_failures)
            ),
        )
    )

    return results


def print_text(results: list[CheckResult]) -> None:
    print("MRD geometry proof invariant check")
    print("Boundary: structural research checks only; not clinical validation.")
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
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL load-inputs: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(
            json.dumps(
                {
                    "check_id": "mrd-geometry-proof-invariant-check-v0",
                    "clinical_use_boundary": "research-use-only",
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
