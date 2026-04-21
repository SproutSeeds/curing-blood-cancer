#!/usr/bin/env python3
"""Run the synthetic measurement-refusal validator skeleton.

This validator checks public synthetic refusal routes only. It does not
interpret MRD, validate assays or specimens, review reports, rank modalities,
recommend treatment, match a patient, or claim a cure.
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
DEFAULT_REPORT = EXAMPLES / "measurement-refusal-validator-skeleton-report-v0.json"

VALIDATOR_ID = "measurement-refusal-validator-skeleton-v0"
REPORT_ID = "measurement-refusal-validator-skeleton-report-v0"
NEXT_SUCCESSOR = "measurement-refusal-wrapper-negative-safety-fixtures-v0"
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

REQUIRED_BLOCKED_ROUTES = {
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

REQUIRED_DESTINATION_CONTRACTS = {
    "measurement-refusal-output-schema-v0",
    "myeloma-state-validator-rule-map-v0",
    "model-output-boundary-wrapper-v0",
}

ALLOWED_ROUTE_FAMILIES = {
    "structural_validator_input",
    "model_output_boundary_refusal_surface",
    "public_navigation_index",
    "synthetic_regression_fixture",
    "private_review_blocker_notice",
}

NORMAL_ROUTE_FAMILIES = {
    "structural_validator_input",
    "model_output_boundary_refusal_surface",
    "public_navigation_index",
    "synthetic_regression_fixture",
}

PRIVATE_REVIEW_ROUTE_FAMILIES = {
    "private_review_blocker_notice",
    "public_navigation_index",
    "synthetic_regression_fixture",
}

ALLOWED_EMITTED_FIELDS = {
    "route_id",
    "source_output_id",
    "source_fixture_id",
    "source_checklist_row_id",
    "assay_specimen_quality_state",
    "route_status",
    "public_processing_allowed",
    "allowed_route_families",
    "destination_contracts",
    "route_boundary",
    "clinical_output_allowed",
    "comparison_allowed",
    "no_interpretive_text",
    "blocked_routes",
    "validator_decision",
}

FORBIDDEN_KEYS = {
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
class RuleResult:
    rule_id: str
    status: str
    detail: str
    blocked_if_failed: list[str]


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


def false_boundary_failures(doc: dict[str, Any]) -> list[str]:
    boundary = doc.get("data_boundary")
    if not isinstance(boundary, dict):
        return sorted(REQUIRED_FALSE_BOUNDARY_FIELDS)
    return sorted(field for field in REQUIRED_FALSE_BOUNDARY_FIELDS if boundary.get(field) is not False)


def missing_clinical_boundaries(doc: dict[str, Any]) -> list[str]:
    return sorted(REQUIRED_CLINICAL_BOUNDARIES - set(values(doc, "clinical_use_boundary")))


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


def blocked_manifest_values(route_doc: dict[str, Any]) -> set[str]:
    rows = route_doc.get("blocked_route_manifest")
    if not isinstance(rows, list):
        return set()
    return {
        row.get("blocked_route")
        for row in rows
        if isinstance(row, dict) and row.get("status") == "blocked" and isinstance(row.get("blocked_route"), str)
    }


def pass_fail(failures: list[str]) -> str:
    return "fail" if failures else "pass"


def result(rule_id: str, failures: list[str], ok_detail: str, blocked: list[str]) -> RuleResult:
    detail = ok_detail if not failures else "; ".join(failures[:12])
    return RuleResult(rule_id, pass_fail(failures), detail, blocked)


def route_decision(route: dict[str, Any]) -> str:
    if route.get("route_status") == "private_or_real_quality_review_blocked":
        return "blocked_private_review_notice_only"
    return "accepted_refusal_metadata_only"


def emitted_route_record(route: dict[str, Any]) -> dict[str, Any]:
    emitted = {key: route.get(key) for key in sorted(ALLOWED_EMITTED_FIELDS) if key in route}
    emitted["validator_decision"] = route_decision(route)
    return emitted


def build_validator_report_from_docs(output_doc: dict[str, Any], route_doc: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(output_doc, dict) or not isinstance(route_doc, dict):
        raise ValueError("validator inputs must be JSON objects")

    outputs = output_rows(output_doc)
    routes = route_rows(route_doc)
    outputs_by_id = {row.get("output_id"): row for row in outputs if isinstance(row.get("output_id"), str)}
    routes_by_output: dict[str, dict[str, Any]] = {}
    duplicate_routes: list[str] = []
    for route in routes:
        source_output_id = route.get("source_output_id")
        if not isinstance(source_output_id, str):
            continue
        if source_output_id in routes_by_output:
            duplicate_routes.append(source_output_id)
        routes_by_output[source_output_id] = route

    rule_results: list[RuleResult] = []

    boundary_failures = [
        f"output fixture {field} must be false" for field in false_boundary_failures(output_doc)
    ] + [f"route table {field} must be false" for field in false_boundary_failures(route_doc)]
    rule_results.append(
        result(
            "mrvs_00_public_synthetic_only",
            boundary_failures,
            "input artifacts are public synthetic only",
            ["public_export_blocked", "private_review_needed"],
        )
    )

    clinical_failures = [
        f"output fixture missing {field}" for field in missing_clinical_boundaries(output_doc)
    ] + [f"route table missing {field}" for field in missing_clinical_boundaries(route_doc)]
    rule_results.append(
        result(
            "mrvs_01_clinical_boundary_complete",
            clinical_failures,
            "required no-advice clinical boundary labels are present",
            ["clinical_output_blocked"],
        )
    )

    missing_routes = sorted(set(outputs_by_id) - set(routes_by_output))
    unknown_routes = sorted(set(routes_by_output) - set(outputs_by_id))
    coverage_failures = []
    if missing_routes:
        coverage_failures.append(f"missing routes: {', '.join(missing_routes)}")
    if unknown_routes:
        coverage_failures.append(f"unknown output ids: {', '.join(unknown_routes)}")
    if duplicate_routes:
        coverage_failures.append(f"duplicate output ids: {', '.join(sorted(duplicate_routes))}")
    if not outputs_by_id:
        coverage_failures.append("no refused output records found")
    rule_results.append(
        result(
            "mrvs_02_every_refused_output_has_one_route",
            coverage_failures,
            f"{len(outputs_by_id)} refused output records have one route",
            ["validator_report_blocked"],
        )
    )

    blocked_manifest = blocked_manifest_values(route_doc)
    manifest_failures = sorted(REQUIRED_BLOCKED_ROUTES - blocked_manifest)
    rule_results.append(
        result(
            "mrvs_03_blocked_route_manifest_complete",
            [f"missing blocked routes: {', '.join(manifest_failures)}"] if manifest_failures else [],
            "blocked route manifest carries all required blocked outputs",
            ["downstream_route_blocked"],
        )
    )

    contract_values = set(values(route_doc, "required_destination_contracts"))
    missing_contracts = sorted(REQUIRED_DESTINATION_CONTRACTS - contract_values)
    rule_results.append(
        result(
            "mrvs_04_destination_contracts_present",
            [f"missing destination contracts: {', '.join(missing_contracts)}"] if missing_contracts else [],
            "required destination contracts are present",
            ["validator_report_blocked"],
        )
    )

    route_failures: list[str] = []
    route_results: list[dict[str, Any]] = []
    for key in sorted(FORBIDDEN_KEYS):
        for location in find_key(output_doc, key):
            route_failures.append(f"output fixture forbidden key {location} ({key})")
        for location in find_key(route_doc, key):
            route_failures.append(f"route table forbidden key {location} ({key})")

    for output_id, output in sorted(outputs_by_id.items()):
        route = routes_by_output.get(output_id)
        if not isinstance(route, dict):
            continue
        route_id = route.get("route_id", output_id)

        for field in ("source_fixture_id", "source_checklist_row_id", "assay_specimen_quality_state", "refusal_reason"):
            if route.get(field) != output.get(field):
                route_failures.append(f"{route_id}: {field} mismatch")
        if route.get("public_processing_allowed") != output.get("public_processing_allowed"):
            route_failures.append(f"{route_id}: public_processing_allowed mismatch")
        if route.get("clinical_output_allowed") is not False:
            route_failures.append(f"{route_id}: clinical_output_allowed must be false")
        if route.get("comparison_allowed") is not False:
            route_failures.append(f"{route_id}: comparison_allowed must be false")
        if route.get("no_interpretive_text") is not True:
            route_failures.append(f"{route_id}: no_interpretive_text must be true")
        if route.get("route_boundary") != "refusal-metadata-only":
            route_failures.append(f"{route_id}: route_boundary must be refusal-metadata-only")

        route_blocks = set(values(route, "blocked_routes"))
        missing_blocks = sorted(REQUIRED_BLOCKED_ROUTES - route_blocks)
        if missing_blocks:
            route_failures.append(f"{route_id}: missing blocked routes {', '.join(missing_blocks)}")

        route_destinations = set(values(route, "destination_contracts"))
        missing_destinations = sorted(REQUIRED_DESTINATION_CONTRACTS - route_destinations)
        if missing_destinations:
            route_failures.append(f"{route_id}: missing destination contracts {', '.join(missing_destinations)}")

        route_families = set(values(route, "allowed_route_families"))
        unknown_families = sorted(route_families - ALLOWED_ROUTE_FAMILIES)
        if unknown_families:
            route_failures.append(f"{route_id}: unknown route families {', '.join(unknown_families)}")

        private_review = output.get("assay_specimen_quality_state") == "private_lab_or_clinical_review_needed"
        if private_review:
            if route.get("route_status") != "private_or_real_quality_review_blocked":
                route_failures.append(f"{route_id}: private review route_status must be blocked")
            if route.get("public_processing_allowed") is not False:
                route_failures.append(f"{route_id}: private review public processing must be false")
            if route_families != PRIVATE_REVIEW_ROUTE_FAMILIES:
                route_failures.append(f"{route_id}: private review route families must be blocker-only")
        else:
            if route.get("route_status") != "routed_refusal_only":
                route_failures.append(f"{route_id}: route_status must be routed_refusal_only")
            if route.get("public_processing_allowed") is not True:
                route_failures.append(f"{route_id}: synthetic route public processing must be true")
            if route_families != NORMAL_ROUTE_FAMILIES:
                route_failures.append(f"{route_id}: normal route families must match safe refusal set")

        route_results.append(emitted_route_record(route))

    rule_results.append(
        result(
            "mrvs_05_routes_preserve_refusal_metadata_only",
            route_failures,
            f"{len(route_results)} routes preserve refusal-only metadata",
            ["validator_report_blocked", "downstream_route_blocked"],
        )
    )

    report_forbidden_locations: list[str] = []
    provisional_report = {
        "route_results": route_results,
        "forbidden_output_fields": sorted(FORBIDDEN_KEYS),
    }
    for key in sorted(FORBIDDEN_KEYS):
        for location in find_key(provisional_report, key):
            if location.startswith("$.forbidden_output_fields"):
                continue
            report_forbidden_locations.append(f"{location} ({key})")
    rule_results.append(
        result(
            "mrvs_06_report_emits_no_forbidden_fields",
            report_forbidden_locations,
            "validator report emits no forbidden clinical, ranking, prediction, or recommendation fields",
            ["validator_report_blocked"],
        )
    )

    report_status = "pass" if all(item.status == "pass" for item in rule_results) else "fail"
    private_blocker_count = sum(
        1 for route in route_results if route.get("validator_decision") == "blocked_private_review_notice_only"
    )
    accepted_refusal_count = sum(
        1 for route in route_results if route.get("validator_decision") == "accepted_refusal_metadata_only"
    )

    return {
        "measurement_refusal_validator_report_id": REPORT_ID,
        "validator_id": VALIDATOR_ID,
        "title": "Measurement Refusal Validator Skeleton Report v0",
        "disease_program": "multiple-myeloma",
        "report_status": report_status,
        "report_type": "synthetic-structural-validation-only",
        "clinical_use_boundary": sorted(REQUIRED_CLINICAL_BOUNDARIES),
        "data_boundary": {field: False for field in sorted(REQUIRED_FALSE_BOUNDARY_FIELDS)},
        "source_artifacts": [
            OUTPUT_FIXTURE.as_posix(),
            ROUTE_TABLE.as_posix(),
        ],
        "validation_contract": {
            "allowed_input_state": "public-synthetic-fixtures-only",
            "allowed_output_type": "structural-validation-report",
            "route_boundary": "refusal-metadata-only",
            "allowed_emitted_route_fields": sorted(ALLOWED_EMITTED_FIELDS),
            "required_destination_contracts": sorted(REQUIRED_DESTINATION_CONTRACTS),
            "allowed_route_families": sorted(ALLOWED_ROUTE_FAMILIES),
        },
        "summary": {
            "refused_output_count": len(outputs_by_id),
            "route_count": len(routes),
            "accepted_refusal_metadata_only_count": accepted_refusal_count,
            "blocked_private_review_notice_only_count": private_blocker_count,
            "clinical_output_allowed": False,
            "comparison_allowed": False,
            "no_interpretive_text": True,
        },
        "rule_results": [
            {
                "rule_id": item.rule_id,
                "status": item.status,
                "detail": item.detail,
                "blocked_if_failed": item.blocked_if_failed,
            }
            for item in rule_results
        ],
        "route_results": route_results,
        "blocked_output_manifest": sorted(REQUIRED_BLOCKED_ROUTES),
        "forbidden_output_fields": sorted(FORBIDDEN_KEYS),
        "handoff": {
            "completed_phase": VALIDATOR_ID,
            "completed_successor": "measurement-refusal-wrapper-integration-dry-run-v0",
            "next_no_outreach_successor_if_selected": NEXT_SUCCESSOR,
            "human_gate_state": HUMAN_GATE,
            "blocked_actions": BLOCKED_ACTIONS,
        },
    }


def build_validator_report(root: Path) -> dict[str, Any]:
    output_doc = load_json(root, OUTPUT_FIXTURE)
    route_doc = load_json(root, ROUTE_TABLE)
    if not isinstance(output_doc, dict) or not isinstance(route_doc, dict):
        raise ValueError("validator inputs must be JSON objects")
    return build_validator_report_from_docs(output_doc, route_doc)


def print_text(report: dict[str, Any]) -> None:
    print("Measurement refusal validator skeleton")
    print("Boundary: structural synthetic validation only; not clinical validation.")
    print()
    for item in report.get("rule_results", []):
        if not isinstance(item, dict):
            continue
        status = "PASS" if item.get("status") == "pass" else "FAIL"
        print(f"{status} {item.get('rule_id')}: {item.get('detail')}")
    print()
    summary = report.get("summary", {})
    if isinstance(summary, dict):
        print(
            "Routes: "
            f"{summary.get('accepted_refusal_metadata_only_count', 0)} refusal metadata, "
            f"{summary.get('blocked_private_review_notice_only_count', 0)} private-review blocker"
        )
    print(f"Report status: {report.get('report_status')}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--json", action="store_true", help="Print the full validation report as JSON.")
    parser.add_argument(
        "--write-report",
        type=Path,
        nargs="?",
        const=DEFAULT_REPORT,
        help="Write the validation report JSON. Defaults to the public synthetic report fixture path.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    try:
        report = build_validator_report(root)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL load-or-validate-inputs: {exc}", file=sys.stderr)
        return 1

    if args.write_report is not None:
        report_path = args.write_report
        if not report_path.is_absolute():
            report_path = root / report_path
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_text(report)

    return 0 if report.get("report_status") == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
