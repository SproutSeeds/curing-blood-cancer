#!/usr/bin/env python3
"""Check MRD geometry Phase 6 falsification invariants.

These checks validate research structure only. They do not validate medical
claims, rank mechanisms, interpret MRD, recommend treatment, or claim a cure.
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
EXAMPLES = Path("examples")

COVERAGE = MECHANISMS / "mrd-resistance-geometry-coverage-v0.json"
FALSIFICATION_MATRIX = MECHANISMS / "mrd-geometry-falsification-matrix-v0.json"
TRANSITION_MODEL = MECHANISMS / "mrd-geometry-transition-model-v0.json"
HYPOTHESIS_LEDGER = MECHANISMS / "mrd-geometry-hypothesis-candidate-ledger-v0.json"
BENCHMARK_FIXTURES = EXAMPLES / "mrd-geometry-benchmark-fixtures-v0.json"

REQUIRED_TRANSITION_TYPES = {
    "coverage-status-movement",
    "weaken-edge",
    "split-node",
    "merge-linked-context",
    "block-claim",
    "retain-source-bounded-state",
    "route-to-source-extraction",
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

REQUIRED_FALSE_BOUNDARY_FIELDS = {
    "uses_real_case_data",
    "contains_identifiers",
    "contains_predictions",
    "contains_recommendations",
    "contains_matching_or_ranking",
    "contains_clinical_decisions",
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


def coverage_mechanisms(report: dict[str, Any]) -> dict[str, str]:
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


def transition_type_ids(model: dict[str, Any]) -> set[str]:
    found: set[str] = set()
    rows = model.get("allowed_transition_types")
    if not isinstance(rows, list):
        return found
    for row in rows:
        if not isinstance(row, dict):
            continue
        transition_id = row.get("transition_type_id")
        if isinstance(transition_id, str):
            found.add(transition_id)
    return found


def matrix_rows(matrix: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    raw_rows = matrix.get("matrix_rows")
    if not isinstance(raw_rows, list):
        return rows
    for row in raw_rows:
        if not isinstance(row, dict):
            continue
        mechanism_id = row.get("mechanism_group_id")
        if isinstance(mechanism_id, str):
            rows[mechanism_id] = row
    return rows


def boundary_failures(data_boundary: dict[str, Any] | None) -> list[str]:
    if not isinstance(data_boundary, dict):
        return sorted(REQUIRED_FALSE_BOUNDARY_FIELDS)
    return sorted(field for field in REQUIRED_FALSE_BOUNDARY_FIELDS if data_boundary.get(field) is not False)


def has_required_set(found: set[str], required: set[str]) -> tuple[bool, str]:
    missing = sorted(required - found)
    if missing:
        return False, f"missing: {', '.join(missing)}"
    return True, f"found {len(required)} required items"


def run_checks(root: Path) -> list[CheckResult]:
    coverage = load_json(root, COVERAGE)
    matrix = load_json(root, FALSIFICATION_MATRIX)
    transition_model = load_json(root, TRANSITION_MODEL)
    hypothesis_ledger = load_json(root, HYPOTHESIS_LEDGER)
    benchmark_fixtures = load_json(root, BENCHMARK_FIXTURES)

    results: list[CheckResult] = []

    mechanism_statuses = coverage_mechanisms(coverage)
    uncovered = sorted(
        mechanism_id
        for mechanism_id, status in mechanism_statuses.items()
        if status != "covered-for-v0-navigation"
    )
    results.append(
        CheckResult(
            "all-mechanism-buckets-covered-for-v0-navigation",
            not uncovered and bool(mechanism_statuses),
            "covered" if not uncovered and mechanism_statuses else f"not covered: {', '.join(uncovered)}",
        )
    )

    matrix_by_mechanism = matrix_rows(matrix)
    passed, detail = has_required_set(set(matrix_by_mechanism), set(mechanism_statuses))
    results.append(CheckResult("falsification-matrix-covers-coverage-buckets", passed, detail))

    matrix_failures: list[str] = []
    for mechanism_id, row in matrix_by_mechanism.items():
        tests = row.get("falsification_tests")
        if not isinstance(tests, dict):
            matrix_failures.append(f"{mechanism_id}: missing falsification_tests")
            continue
        for key in (
            "evidence_that_would_weaken",
            "evidence_that_would_split",
            "evidence_that_would_merge",
            "evidence_that_would_block",
        ):
            if not values(tests, key):
                matrix_failures.append(f"{mechanism_id}: missing {key}")
        missing_blocked = sorted(REQUIRED_BLOCKED_OUTPUTS - set(values(row, "blocked_outputs")))
        if missing_blocked:
            matrix_failures.append(f"{mechanism_id}: missing blocked outputs {', '.join(missing_blocked)}")
    results.append(
        CheckResult(
            "falsification-rows-have-required-tests-and-blocks",
            not matrix_failures,
            "complete" if not matrix_failures else "; ".join(matrix_failures),
        )
    )

    found_transition_types = transition_type_ids(transition_model)
    passed, detail = has_required_set(found_transition_types, REQUIRED_TRANSITION_TYPES)
    results.append(CheckResult("transition-model-has-required-types", passed, detail))

    hypothesis_failures: list[str] = []
    hypotheses = hypothesis_ledger.get("hypotheses")
    if not isinstance(hypotheses, list) or not hypotheses:
        hypothesis_failures.append("hypotheses missing or empty")
    else:
        for index, hypothesis in enumerate(hypotheses):
            if not isinstance(hypothesis, dict):
                hypothesis_failures.append(f"hypotheses[{index}] must be an object")
                continue
            hypothesis_id = hypothesis.get("hypothesis_id", f"hypotheses[{index}]")
            if hypothesis.get("status") != "candidate-research-hypothesis-only":
                hypothesis_failures.append(f"{hypothesis_id}: status not research-only")
            if hypothesis.get("claim_level") != "open-question":
                hypothesis_failures.append(f"{hypothesis_id}: claim_level not open-question")
            if not values(hypothesis, "falsification_conditions"):
                hypothesis_failures.append(f"{hypothesis_id}: missing falsification_conditions")
            if not values(hypothesis, "required_next_evidence"):
                hypothesis_failures.append(f"{hypothesis_id}: missing required_next_evidence")
            unknown_transitions = sorted(set(values(hypothesis, "transition_model_links")) - found_transition_types)
            if unknown_transitions:
                hypothesis_failures.append(
                    f"{hypothesis_id}: unknown transition links {', '.join(unknown_transitions)}"
                )
            missing_prohibited = sorted(REQUIRED_BLOCKED_OUTPUTS - set(values(hypothesis, "prohibited_inferences")))
            if missing_prohibited:
                hypothesis_failures.append(
                    f"{hypothesis_id}: missing prohibited inferences {', '.join(missing_prohibited)}"
                )
    results.append(
        CheckResult(
            "hypotheses-remain-research-only",
            not hypothesis_failures,
            f"{len(hypotheses)} hypotheses checked" if isinstance(hypotheses, list) and not hypothesis_failures else "; ".join(hypothesis_failures),
        )
    )

    benchmark_failures: list[str] = []
    false_failures = boundary_failures(benchmark_fixtures.get("data_boundary"))
    if false_failures:
        benchmark_failures.append(f"data_boundary not false: {', '.join(false_failures)}")
    fixtures = benchmark_fixtures.get("benchmark_fixtures")
    if not isinstance(fixtures, list) or not fixtures:
        benchmark_failures.append("benchmark_fixtures missing or empty")
    else:
        for index, fixture in enumerate(fixtures):
            if not isinstance(fixture, dict):
                benchmark_failures.append(f"benchmark_fixtures[{index}] must be an object")
                continue
            fixture_id = fixture.get("fixture_id", f"benchmark_fixtures[{index}]")
            expected_transition = fixture.get("expected_transition_type_id")
            if expected_transition not in found_transition_types:
                benchmark_failures.append(f"{fixture_id}: unknown expected transition {expected_transition!r}")
            missing_blocks = sorted(REQUIRED_BLOCKED_OUTPUTS - set(values(fixture, "expected_blocked_outputs")))
            if missing_blocks:
                benchmark_failures.append(f"{fixture_id}: missing expected blocked outputs {', '.join(missing_blocks)}")
    results.append(
        CheckResult(
            "benchmark-fixtures-resolve-to-safe-transitions",
            not benchmark_failures,
            f"{len(fixtures)} fixtures checked" if isinstance(fixtures, list) and not benchmark_failures else "; ".join(benchmark_failures),
        )
    )

    return results


def print_text(results: list[CheckResult]) -> None:
    print("MRD geometry falsification invariant check")
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
                    "check_id": "mrd-geometry-falsification-check-v0",
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
