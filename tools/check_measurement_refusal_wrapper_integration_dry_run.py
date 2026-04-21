#!/usr/bin/env python3
"""Check the measurement-refusal wrapper integration dry run.

This dry run connects public synthetic measurement-refusal outputs to the
model-output boundary wrapper as refusal metadata only. It must not emit model
outputs, scores, clinical interpretation, ranking, recommendations, real-report
review, publication authorization, or patient-specific decisions.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = Path("examples")
MEASUREMENTS = Path("disease-programs/multiple-myeloma/measurements")

OUTPUT_FIXTURE = EXAMPLES / "measurement-refusal-output-fixture-v0.json"
ROUTE_TABLE = MEASUREMENTS / "measurement-refusal-output-route-table-v0.json"
VALIDATOR_REPORT = EXAMPLES / "measurement-refusal-validator-skeleton-report-v0.json"
DEFAULT_REPORT = EXAMPLES / "measurement-refusal-wrapper-integration-dry-run-v0.json"

DRY_RUN_ID = "measurement-refusal-wrapper-integration-dry-run-v0"
WRAPPER_ID = "model-output-boundary-wrapper-v0"
COMPLETED_SUCCESSOR = "measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0"
NEXT_SUCCESSOR = "measurement-refusal-wrapper-state-machine-falsification-audit-v0"
HUMAN_GATE = "machine-representation-expert-validation-human-authorization-blocker-v0"

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

REQUIRED_CLINICAL_BOUNDARIES = {
    "not-medical-advice",
    "not-diagnostic",
    "not-treatment-recommendation",
    "not-trial-recommendation",
    "research-use-only",
}

REQUIRED_BLOCKED_USES = {
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

REQUIRED_SOURCE_ARTIFACTS = {
    OUTPUT_FIXTURE.as_posix(),
    ROUTE_TABLE.as_posix(),
    VALIDATOR_REPORT.as_posix(),
    "disease-programs/multiple-myeloma/model-output-boundary-wrapper-v0.md",
}

FORBIDDEN_WRAPPER_KEYS = {
    "accession",
    "accession_number",
    "actionability",
    "actionability_score",
    "assay_rank",
    "biopsy_interpretation",
    "case_id",
    "clinical_decision",
    "clinical_guidance",
    "clinical_interpretation",
    "clinical_priority",
    "clinical_priority_score",
    "date_of_birth",
    "diagnosis",
    "dose",
    "dosing",
    "eligibility",
    "eligibility_guidance",
    "endpoint_interpretation",
    "evidence_rank",
    "evidence_strength",
    "evidence_strength_score",
    "free_text_note",
    "image_interpretation",
    "interpretation",
    "lab_validity_conclusion",
    "medical_record_number",
    "modality_rank",
    "monitoring_guidance",
    "monitoring_plan",
    "mrd_interpretation",
    "mrd_label",
    "option_rank",
    "patient_fit",
    "patient_id",
    "patient_matching",
    "patient_relevance",
    "probability",
    "prognosis",
    "prognosis_text",
    "publication_authorization",
    "ranking",
    "raw_record",
    "recommendation",
    "residual_disease_comparison",
    "response_category",
    "risk_category",
    "risk_score",
    "score",
    "treatment_action",
    "treatment_choice",
    "treatment_guidance",
    "treatment_recommendation",
    "trial_guidance",
    "trial_match",
    "trial_matching",
    "trial_recommendation",
    "urgency",
    "urgency_score",
}

BLOCKED_ACTIONS = [
    "expert-validation execution",
    "issue operations",
    "outreach",
    "response intake",
    "real-report quality review",
    "private-lab work",
    "clinical interpretation",
    "model-governance clearance",
    "publication authorization",
    "claim upgrade",
]


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


def output_rows(output_doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = output_doc.get("outputs")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def route_rows(route_doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = route_doc.get("route_records")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def wrapper_record_id(output_id: str) -> str:
    if output_id.startswith("mro_"):
        return f"mrw_{output_id[len('mro_'):]}"
    return f"mrw_{output_id}"


def find_key(value: Any, key: str, loc: str = "$") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for child_key, child_value in value.items():
            child_loc = f"{loc}.{child_key}"
            if child_key == key:
                found.append(child_loc)
            found.extend(find_key(child_value, key, child_loc))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(find_key(item, key, f"{loc}[{index}]"))
    return found


def boundary_failures(data_boundary: dict[str, Any] | None) -> list[str]:
    if not isinstance(data_boundary, dict):
        return sorted(REQUIRED_FALSE_BOUNDARY_FIELDS)
    return sorted(field for field in REQUIRED_FALSE_BOUNDARY_FIELDS if data_boundary.get(field) is not False)


def build_wrapper_record(output: dict[str, Any], route: dict[str, Any]) -> dict[str, Any]:
    output_id = str(output["output_id"])
    private_review = output.get("assay_specimen_quality_state") == "private_lab_or_clinical_review_needed"
    return {
        "wrapper_record_id": wrapper_record_id(output_id),
        "source_output_id": output_id,
        "source_route_id": route.get("route_id"),
        "source_fixture_id": output.get("source_fixture_id"),
        "source_checklist_row_id": output.get("source_checklist_row_id"),
        "wrapper_id": WRAPPER_ID,
        "output_family_id": "mrd_head",
        "requested_use": "synthetic_fixture_check",
        "state_object_schema_id": "myeloma-state-object-schema-v0",
        "synthetic_fixture_ids": [output.get("source_fixture_id")],
        "head_status": "assay_specimen_quality_needed",
        "source_context_state": "synthetic_source",
        "input_missingness_state": "unknown_visible",
        "residual_disease_modality_state": "private_lab_needed" if private_review else "assay_specimen_quality_needed",
        "uncertainty_state": "assay_specimen_quality_needed",
        "review_status": "privacy_review_needed" if private_review else "measurement_review_needed",
        "gate_status": "private_lab_needed" if private_review else "public_fixture_only",
        "assay_specimen_quality_state": output.get("assay_specimen_quality_state"),
        "refusal_reason": output.get("refusal_reason"),
        "allowed_public_successor": "blocked_only",
        "route_status": route.get("route_status"),
        "public_processing_allowed": route.get("public_processing_allowed"),
        "wrapper_boundary": "refusal-wrapper-metadata-only",
        "no_interpretive_text": True,
        "clinical_output_allowed": False,
        "prediction_output_allowed": False,
        "comparison_allowed": False,
        "matching_or_ranking_allowed": False,
        "real_review_output_allowed": False,
        "publication_authorization_allowed": False,
        "blocked_downstream_uses": output.get("blocked_downstream_uses", []),
    }


def build_dry_run_report(root: Path) -> dict[str, Any]:
    output_doc = load_json(root, OUTPUT_FIXTURE)
    route_doc = load_json(root, ROUTE_TABLE)
    validator_report = load_json(root, VALIDATOR_REPORT)
    if not isinstance(output_doc, dict) or not isinstance(route_doc, dict) or not isinstance(validator_report, dict):
        raise ValueError("wrapper dry-run inputs must be JSON objects")

    routes_by_output = {
        route.get("source_output_id"): route
        for route in route_rows(route_doc)
        if isinstance(route.get("source_output_id"), str)
    }
    wrapper_records: list[dict[str, Any]] = []
    for output in output_rows(output_doc):
        output_id = output.get("output_id")
        if not isinstance(output_id, str):
            continue
        route = routes_by_output.get(output_id)
        if not isinstance(route, dict):
            continue
        wrapper_records.append(build_wrapper_record(output, route))

    private_count = sum(
        1
        for record in wrapper_records
        if record.get("route_status") == "private_or_real_quality_review_blocked"
    )
    public_count = len(wrapper_records) - private_count
    return {
        "wrapper_integration_dry_run_id": DRY_RUN_ID,
        "title": "Measurement Refusal Wrapper Integration Dry Run v0",
        "date": "2026-04-20",
        "disease_program": "multiple-myeloma",
        "dry_run_status": "pass",
        "dry_run_type": "synthetic-refusal-wrapper-integration-only",
        "target_wrapper_id": WRAPPER_ID,
        "source_output_set_id": output_doc.get("measurement_refusal_output_set_id"),
        "source_route_table_id": route_doc.get("measurement_refusal_route_table_id"),
        "source_validator_report_id": validator_report.get("measurement_refusal_validator_report_id"),
        "source_validator_report_status": validator_report.get("report_status"),
        "clinical_use_boundary": [
            "not-medical-advice",
            "not-diagnostic",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        ],
        "data_boundary": {
            "uses_real_case_data": False,
            "contains_identifiers": False,
            "contains_raw_records": False,
            "contains_uploads": False,
            "contains_exact_person_linked_dates": False,
            "contains_free_text_case_details": False,
            "contains_private_correspondence": False,
            "contains_model_weights": False,
            "contains_predictions": False,
            "contains_recommendations": False,
            "contains_matching_or_ranking": False,
            "contains_clinical_decisions": False,
        },
        "source_artifacts": sorted(REQUIRED_SOURCE_ARTIFACTS),
        "summary": {
            "source_output_count": len(output_rows(output_doc)),
            "source_route_count": len(route_rows(route_doc)),
            "wrapper_record_count": len(wrapper_records),
            "public_refusal_wrapper_records": public_count,
            "private_review_blocker_wrapper_records": private_count,
            "clinical_output_allowed": False,
            "prediction_output_allowed": False,
            "matching_or_ranking_allowed": False,
            "real_review_output_allowed": False,
            "publication_authorization_allowed": False,
            "no_interpretive_text": True,
        },
        "wrapper_contract": {
            "required_wrapper_id": WRAPPER_ID,
            "allowed_output_family_ids": ["mrd_head"],
            "allowed_requested_use": "synthetic_fixture_check",
            "allowed_head_status": "assay_specimen_quality_needed",
            "allowed_wrapper_boundary": "refusal-wrapper-metadata-only",
            "blocked_downstream_uses": sorted(REQUIRED_BLOCKED_USES),
        },
        "wrapper_records": wrapper_records,
        "forbidden_wrapper_fields": sorted(FORBIDDEN_WRAPPER_KEYS),
        "handoff": {
            "completed_phase": DRY_RUN_ID,
            "completed_successor": COMPLETED_SUCCESSOR,
            "next_no_outreach_successor_if_selected": NEXT_SUCCESSOR,
            "human_gate_state": HUMAN_GATE,
            "blocked_actions": BLOCKED_ACTIONS,
        },
    }


def validate_report(report: dict[str, Any], output_doc: dict[str, Any], route_doc: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if report.get("wrapper_integration_dry_run_id") != DRY_RUN_ID:
        failures.append("wrapper_integration_dry_run_id mismatch")
    if report.get("target_wrapper_id") != WRAPPER_ID:
        failures.append("target_wrapper_id mismatch")
    if report.get("dry_run_status") != "pass":
        failures.append("dry_run_status must be pass")
    if report.get("source_validator_report_status") != "pass":
        failures.append("source_validator_report_status must be pass")

    missing_boundary = boundary_failures(report.get("data_boundary") if isinstance(report.get("data_boundary"), dict) else None)
    if missing_boundary:
        failures.append(f"data_boundary fields must be false: {', '.join(missing_boundary)}")

    clinical_boundaries = set(values(report, "clinical_use_boundary"))
    missing_clinical = sorted(REQUIRED_CLINICAL_BOUNDARIES - clinical_boundaries)
    if missing_clinical:
        failures.append(f"clinical_use_boundary missing: {', '.join(missing_clinical)}")

    source_artifacts = set(values(report, "source_artifacts"))
    missing_sources = sorted(REQUIRED_SOURCE_ARTIFACTS - source_artifacts)
    if missing_sources:
        failures.append(f"source_artifacts missing: {', '.join(missing_sources)}")

    outputs = output_rows(output_doc)
    routes = route_rows(route_doc)
    outputs_by_id = {row.get("output_id"): row for row in outputs if isinstance(row.get("output_id"), str)}
    routes_by_output = {row.get("source_output_id"): row for row in routes if isinstance(row.get("source_output_id"), str)}
    wrapper_rows_raw = report.get("wrapper_records")
    wrapper_rows = [row for row in wrapper_rows_raw if isinstance(row, dict)] if isinstance(wrapper_rows_raw, list) else []
    wrappers_by_output = {
        row.get("source_output_id"): row for row in wrapper_rows if isinstance(row.get("source_output_id"), str)
    }

    if set(wrappers_by_output) != set(outputs_by_id):
        missing = sorted(set(outputs_by_id) - set(wrappers_by_output))
        extra = sorted(set(wrappers_by_output) - set(outputs_by_id))
        failures.append(f"wrapper coverage mismatch; missing={missing}; extra={extra}")

    summary = report.get("summary")
    if isinstance(summary, dict):
        if summary.get("wrapper_record_count") != len(wrapper_rows):
            failures.append("summary.wrapper_record_count must match wrapper_records length")
        if summary.get("source_output_count") != len(outputs):
            failures.append("summary.source_output_count must match output fixture length")
        if summary.get("source_route_count") != len(routes):
            failures.append("summary.source_route_count must match route table length")
        for field in (
            "clinical_output_allowed",
            "prediction_output_allowed",
            "matching_or_ranking_allowed",
            "real_review_output_allowed",
            "publication_authorization_allowed",
        ):
            if summary.get(field) is not False:
                failures.append(f"summary.{field} must be false")
        if summary.get("no_interpretive_text") is not True:
            failures.append("summary.no_interpretive_text must be true")
    else:
        failures.append("summary must be an object")

    record_failures: list[str] = []
    for output_id, output in sorted(outputs_by_id.items()):
        route = routes_by_output.get(output_id)
        record = wrappers_by_output.get(output_id)
        if not isinstance(route, dict) or not isinstance(record, dict):
            continue
        record_id = record.get("wrapper_record_id", output_id)
        private_review = output.get("assay_specimen_quality_state") == "private_lab_or_clinical_review_needed"
        expected = {
            "wrapper_id": WRAPPER_ID,
            "output_family_id": "mrd_head",
            "requested_use": "synthetic_fixture_check",
            "state_object_schema_id": "myeloma-state-object-schema-v0",
            "head_status": "assay_specimen_quality_needed",
            "source_context_state": "synthetic_source",
            "input_missingness_state": "unknown_visible",
            "uncertainty_state": "assay_specimen_quality_needed",
            "assay_specimen_quality_state": output.get("assay_specimen_quality_state"),
            "refusal_reason": output.get("refusal_reason"),
            "allowed_public_successor": "blocked_only",
            "source_route_id": route.get("route_id"),
            "route_status": route.get("route_status"),
            "public_processing_allowed": route.get("public_processing_allowed"),
            "wrapper_boundary": "refusal-wrapper-metadata-only",
        }
        for field, value in expected.items():
            if record.get(field) != value:
                record_failures.append(f"{record_id}: {field} mismatch")
        for field in (
            "clinical_output_allowed",
            "prediction_output_allowed",
            "comparison_allowed",
            "matching_or_ranking_allowed",
            "real_review_output_allowed",
            "publication_authorization_allowed",
        ):
            if record.get(field) is not False:
                record_failures.append(f"{record_id}: {field} must be false")
        if record.get("no_interpretive_text") is not True:
            record_failures.append(f"{record_id}: no_interpretive_text must be true")
        if private_review:
            if record.get("gate_status") != "private_lab_needed":
                record_failures.append(f"{record_id}: private review gate_status must be private_lab_needed")
            if record.get("review_status") != "privacy_review_needed":
                record_failures.append(f"{record_id}: private review review_status must be privacy_review_needed")
            if record.get("residual_disease_modality_state") != "private_lab_needed":
                record_failures.append(f"{record_id}: private review residual state must be private_lab_needed")
            if record.get("public_processing_allowed") is not False:
                record_failures.append(f"{record_id}: private review public processing must stay false")
        else:
            if record.get("gate_status") != "public_fixture_only":
                record_failures.append(f"{record_id}: gate_status must be public_fixture_only")
            if record.get("review_status") != "measurement_review_needed":
                record_failures.append(f"{record_id}: review_status must be measurement_review_needed")
            if record.get("residual_disease_modality_state") != "assay_specimen_quality_needed":
                record_failures.append(f"{record_id}: residual state must be assay_specimen_quality_needed")
            if record.get("public_processing_allowed") is not True:
                record_failures.append(f"{record_id}: public synthetic processing must stay true")

        blocked = set(values(record, "blocked_downstream_uses"))
        missing_blocks = sorted(REQUIRED_BLOCKED_USES - blocked)
        if missing_blocks:
            record_failures.append(f"{record_id}: missing blocked uses {', '.join(missing_blocks)}")

    failures.extend(record_failures[:20])

    forbidden_locations: list[str] = []
    for key in sorted(FORBIDDEN_WRAPPER_KEYS):
        for location in find_key(report, key):
            if location.startswith("$.forbidden_wrapper_fields"):
                continue
            forbidden_locations.append(f"{location} ({key})")
    if forbidden_locations:
        failures.append("; ".join(forbidden_locations[:12]))

    handoff = report.get("handoff")
    if isinstance(handoff, dict):
        if handoff.get("completed_phase") != DRY_RUN_ID:
            failures.append("handoff.completed_phase mismatch")
        if handoff.get("completed_successor") != COMPLETED_SUCCESSOR:
            failures.append("handoff.completed_successor mismatch")
        if handoff.get("next_no_outreach_successor_if_selected") != NEXT_SUCCESSOR:
            failures.append("handoff.next_no_outreach_successor_if_selected mismatch")
        if handoff.get("human_gate_state") != HUMAN_GATE:
            failures.append("handoff.human_gate_state mismatch")
    else:
        failures.append("handoff must be an object")

    return failures


def run_checks(root: Path, report_path: Path) -> list[CheckResult]:
    output_doc = load_json(root, OUTPUT_FIXTURE)
    route_doc = load_json(root, ROUTE_TABLE)
    report = load_json(root, report_path)
    if not isinstance(output_doc, dict) or not isinstance(route_doc, dict) or not isinstance(report, dict):
        raise ValueError("wrapper dry-run check inputs must be JSON objects")

    failures = validate_report(report, output_doc, route_doc)
    wrapper_records = report.get("wrapper_records")
    wrapper_count = len(wrapper_records) if isinstance(wrapper_records, list) else 0
    return [
        CheckResult(
            "wrapper-dry-run-id",
            report.get("wrapper_integration_dry_run_id") == DRY_RUN_ID,
            f"wrapper_integration_dry_run_id={report.get('wrapper_integration_dry_run_id')!r}",
        ),
        CheckResult(
            "wrapper-dry-run-target",
            report.get("target_wrapper_id") == WRAPPER_ID,
            f"target_wrapper_id={report.get('target_wrapper_id')!r}",
        ),
        CheckResult(
            "wrapper-dry-run-public-synthetic-only",
            not boundary_failures(report.get("data_boundary") if isinstance(report.get("data_boundary"), dict) else None),
            "all required data-boundary fields false",
        ),
        CheckResult(
            "wrapper-dry-run-record-coverage",
            wrapper_count == len(output_rows(output_doc)),
            f"{wrapper_count} wrapper records for {len(output_rows(output_doc))} refused outputs",
        ),
        CheckResult(
            "wrapper-dry-run-preserves-refusal-boundaries",
            not failures,
            "wrapper records preserve refusal-only metadata"
            if not failures
            else "; ".join(failures[:12]),
        ),
    ]


def print_text(results: list[CheckResult]) -> None:
    print("Measurement refusal wrapper integration dry-run check")
    print("Boundary: synthetic wrapper metadata only; not clinical validation.")
    print()
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status} {result.check_id}: {result.detail}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--write-report", action="store_true", help="Regenerate the dry-run report fixture.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable check results.")
    args = parser.parse_args()

    root = args.root.resolve()
    report_path = args.report
    try:
        if args.write_report:
            report = build_dry_run_report(root)
            output_path = root / report_path
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")
        results = run_checks(root, report_path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL load-or-check-inputs: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(
            json.dumps(
                {
                    "check_id": "measurement-refusal-wrapper-integration-dry-run-check-v0",
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
