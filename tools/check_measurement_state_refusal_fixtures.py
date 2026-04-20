#!/usr/bin/env python3
"""Check measurement-state refusal fixture invariants.

These checks validate public synthetic fixture structure only. They do not
interpret MRD, validate an assay, review a report, rank modalities, recommend
treatment, or claim a cure.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
MEASUREMENTS = Path("disease-programs/multiple-myeloma/measurements")
EXAMPLES = Path("examples")

ASSAY_CHECKLIST = MEASUREMENTS / "assay-specimen-quality-failure-mode-checklist-v0.json"
REFUSAL_FIXTURES = EXAMPLES / "measurement-state-refusal-fixtures-v0.json"

REQUIRED_FALSE_BOUNDARY_FIELDS = {
    "uses_real_case_data",
    "contains_identifiers",
    "contains_raw_records",
    "contains_uploads",
    "contains_exact_person_linked_dates",
    "contains_free_text_case_details",
    "contains_private_correspondence",
    "contains_model_weights",
    "contains_predictions",
    "contains_recommendations",
    "contains_matching_or_ranking",
    "contains_clinical_decisions",
}

REQUIRED_BLOCKED_OUTPUTS = {
    "diagnosis",
    "prognosis",
    "endpoint_interpretation",
    "mrd_interpretation",
    "residual_disease_comparison",
    "monitoring_guidance",
    "treatment_guidance",
    "trial_guidance",
    "patient_matching",
    "assay_ranking",
    "modality_ranking",
    "evidence_ranking",
    "clinical_decision",
    "publication_authorization",
    "cure_claim",
    "report_interpretation",
    "lab_validity_conclusion",
    "image_interpretation",
    "biopsy_interpretation",
}

REQUIRED_PUBLIC_ARTIFACT_IDS = {
    "measurement-normalization-contract-v0",
    "assay-specimen-quality-failure-mode-checklist-v0",
    "model-output-boundary-wrapper-v0",
    "myeloma-state-validator-rule-map-v0",
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


def checklist_state_by_row(checklist: dict[str, Any]) -> dict[str, str]:
    found: dict[str, str] = {}
    rows = checklist.get("checklist_rows")
    if not isinstance(rows, list):
        return found
    for row in rows:
        if not isinstance(row, dict):
            continue
        row_id = row.get("row_id")
        state = row.get("fail_closed_state")
        if isinstance(row_id, str) and isinstance(state, str):
            found[row_id] = state
    return found


def fixture_rows(fixture_doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = fixture_doc.get("fixtures")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def boundary_failures(data_boundary: dict[str, Any] | None) -> list[str]:
    if not isinstance(data_boundary, dict):
        return sorted(REQUIRED_FALSE_BOUNDARY_FIELDS)
    return sorted(field for field in REQUIRED_FALSE_BOUNDARY_FIELDS if data_boundary.get(field) is not False)


def blocked_manifest_failures(manifest: dict[str, Any] | None) -> list[str]:
    if not isinstance(manifest, dict):
        return sorted(REQUIRED_BLOCKED_OUTPUTS)
    return sorted(field for field in REQUIRED_BLOCKED_OUTPUTS if manifest.get(field) != "blocked")


def run_checks(root: Path) -> list[CheckResult]:
    checklist = load_json(root, ASSAY_CHECKLIST)
    fixtures_doc = load_json(root, REFUSAL_FIXTURES)

    results: list[CheckResult] = []

    false_failures = boundary_failures(fixtures_doc.get("data_boundary"))
    results.append(
        CheckResult(
            "fixture-set-data-boundary-is-public-synthetic-only",
            not false_failures,
            "all required boundary fields false"
            if not false_failures
            else f"data_boundary not false: {', '.join(false_failures)}",
        )
    )

    manifest_failures = blocked_manifest_failures(fixtures_doc.get("shared_blocked_output_manifest"))
    results.append(
        CheckResult(
            "shared-blocked-output-manifest-complete",
            not manifest_failures,
            "all required blocked outputs present"
            if not manifest_failures
            else f"missing or unblocked outputs: {', '.join(manifest_failures)}",
        )
    )

    source_context = fixtures_doc.get("source_context")
    public_ids = set(values(source_context, "public_artifact_ids")) if isinstance(source_context, dict) else set()
    missing_public_ids = sorted(REQUIRED_PUBLIC_ARTIFACT_IDS - public_ids)
    results.append(
        CheckResult(
            "fixture-set-links-required-owner-artifacts",
            not missing_public_ids,
            f"found {len(REQUIRED_PUBLIC_ARTIFACT_IDS)} required owner artifacts"
            if not missing_public_ids
            else f"missing owner artifacts: {', '.join(missing_public_ids)}",
        )
    )

    checklist_states = checklist_state_by_row(checklist)
    fixtures = fixture_rows(fixtures_doc)
    fixtures_by_row: dict[str, dict[str, Any]] = {}
    duplicate_rows: list[str] = []
    for fixture in fixtures:
        row_id = fixture.get("source_checklist_row_id")
        if not isinstance(row_id, str):
            continue
        if row_id in fixtures_by_row:
            duplicate_rows.append(row_id)
        fixtures_by_row[row_id] = fixture

    missing_rows = sorted(set(checklist_states) - set(fixtures_by_row))
    unknown_rows = sorted(set(fixtures_by_row) - set(checklist_states))
    coverage_passed = bool(checklist_states) and not missing_rows and not unknown_rows and not duplicate_rows
    coverage_detail_parts: list[str] = []
    if missing_rows:
        coverage_detail_parts.append(f"missing rows: {', '.join(missing_rows)}")
    if unknown_rows:
        coverage_detail_parts.append(f"unknown rows: {', '.join(unknown_rows)}")
    if duplicate_rows:
        coverage_detail_parts.append(f"duplicate rows: {', '.join(sorted(duplicate_rows))}")
    results.append(
        CheckResult(
            "every-assay-quality-checklist-state-has-refusal-fixture",
            coverage_passed,
            f"{len(checklist_states)} checklist states covered"
            if coverage_passed
            else "; ".join(coverage_detail_parts) or "checklist states missing",
        )
    )

    fixture_failures: list[str] = []
    for index, fixture in enumerate(fixtures):
        fixture_id = fixture.get("fixture_id", f"fixtures[{index}]")
        if not isinstance(fixture_id, str):
            fixture_id = f"fixtures[{index}]"
        row_id = fixture.get("source_checklist_row_id")
        expected_state = checklist_states.get(row_id) if isinstance(row_id, str) else None
        measurement_input = fixture.get("measurement_state_input")
        expected_refusal = fixture.get("expected_refusal")
        if not isinstance(measurement_input, dict):
            fixture_failures.append(f"{fixture_id}: missing measurement_state_input")
            continue
        if not isinstance(expected_refusal, dict):
            fixture_failures.append(f"{fixture_id}: missing expected_refusal")
            continue
        input_state = measurement_input.get("assay_specimen_quality_state")
        refusal_state = expected_refusal.get("specific_state")
        if input_state != expected_state:
            fixture_failures.append(f"{fixture_id}: input state {input_state!r} does not match checklist {expected_state!r}")
        if refusal_state != expected_state:
            fixture_failures.append(
                f"{fixture_id}: refusal state {refusal_state!r} does not match checklist {expected_state!r}"
            )
        if expected_refusal.get("wrapper_state") != "assay_specimen_quality_needed":
            fixture_failures.append(f"{fixture_id}: wrapper_state must be assay_specimen_quality_needed")
        if expected_refusal.get("comparison_allowed") is not False:
            fixture_failures.append(f"{fixture_id}: comparison_allowed must be false")
        if expected_refusal.get("clinical_output_allowed") is not False:
            fixture_failures.append(f"{fixture_id}: clinical_output_allowed must be false")
        if measurement_input.get("limitation_note_required") is not True:
            fixture_failures.append(f"{fixture_id}: limitation_note_required must be true")
        missing_blocks = sorted(REQUIRED_BLOCKED_OUTPUTS - set(values(expected_refusal, "required_blocked_outputs")))
        if missing_blocks:
            fixture_failures.append(f"{fixture_id}: missing blocked outputs {', '.join(missing_blocks)}")

    results.append(
        CheckResult(
            "fixtures-preserve-fail-closed-refusal-shape",
            not fixture_failures,
            f"{len(fixtures)} fixtures checked" if fixtures and not fixture_failures else "; ".join(fixture_failures),
        )
    )

    private_fixture = fixtures_by_row.get("asq_08_private_or_real_quality_review_needed")
    private_passed = False
    private_detail = "private-review fixture missing"
    if isinstance(private_fixture, dict):
        measurement_input = private_fixture.get("measurement_state_input")
        expected_refusal = private_fixture.get("expected_refusal")
        private_passed = (
            isinstance(measurement_input, dict)
            and isinstance(expected_refusal, dict)
            and measurement_input.get("real_or_private_quality_review_requested") is True
            and expected_refusal.get("public_processing_allowed") is False
        )
        private_detail = (
            "private review request stops public processing"
            if private_passed
            else "private review fixture must request real/private review and set public_processing_allowed false"
        )
    results.append(CheckResult("real-or-private-quality-review-stops-public-path", private_passed, private_detail))

    return results


def print_text(results: list[CheckResult]) -> None:
    print("Measurement state refusal fixture check")
    print("Boundary: structural synthetic checks only; not clinical validation.")
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
                    "check_id": "measurement-state-refusal-fixture-check-v0",
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
