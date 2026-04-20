#!/usr/bin/env python3
"""Check measurement-refusal output route-table invariants.

These checks validate public synthetic routing only. They do not interpret MRD,
validate an assay, review a report, rank modalities, recommend treatment, or
claim a cure.
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

FORBIDDEN_ROUTE_KEYS = {
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


def boundary_failures(data_boundary: dict[str, Any] | None) -> list[str]:
    if not isinstance(data_boundary, dict):
        return sorted(REQUIRED_FALSE_BOUNDARY_FIELDS)
    return sorted(field for field in REQUIRED_FALSE_BOUNDARY_FIELDS if data_boundary.get(field) is not False)


def blocked_manifest_values(route_doc: dict[str, Any]) -> set[str]:
    rows = route_doc.get("blocked_route_manifest")
    if not isinstance(rows, list):
        return set()
    blocked: set[str] = set()
    for row in rows:
        if not isinstance(row, dict):
            continue
        if row.get("status") != "blocked":
            continue
        blocked_route = row.get("blocked_route")
        if isinstance(blocked_route, str):
            blocked.add(blocked_route)
    return blocked


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


def run_checks(root: Path) -> list[CheckResult]:
    output_doc = load_json(root, OUTPUT_FIXTURE)
    route_doc = load_json(root, ROUTE_TABLE)

    results: list[CheckResult] = []

    false_failures = boundary_failures(route_doc.get("data_boundary") if isinstance(route_doc, dict) else None)
    results.append(
        CheckResult(
            "route-table-data-boundary-is-public-synthetic-only",
            not false_failures,
            "all required boundary fields false"
            if not false_failures
            else f"data_boundary not false: {', '.join(false_failures)}",
        )
    )

    clinical_boundaries = set(values(route_doc, "clinical_use_boundary")) if isinstance(route_doc, dict) else set()
    missing_clinical = sorted(REQUIRED_CLINICAL_BOUNDARIES - clinical_boundaries)
    results.append(
        CheckResult(
            "route-table-clinical-boundary-is-complete",
            not missing_clinical,
            f"found {len(REQUIRED_CLINICAL_BOUNDARIES)} required boundary labels"
            if not missing_clinical
            else f"missing clinical boundary labels: {', '.join(missing_clinical)}",
        )
    )

    manifest_missing = sorted(REQUIRED_BLOCKED_ROUTES - blocked_manifest_values(route_doc))
    results.append(
        CheckResult(
            "blocked-route-manifest-complete",
            not manifest_missing,
            "all required blocked routes present"
            if not manifest_missing
            else f"missing blocked routes: {', '.join(manifest_missing)}",
        )
    )

    allowed_families = set(values(route_doc, "allowed_route_families"))
    unknown_allowed = sorted(allowed_families - ALLOWED_ROUTE_FAMILIES)
    missing_allowed = sorted(ALLOWED_ROUTE_FAMILIES - allowed_families)
    results.append(
        CheckResult(
            "allowed-route-families-are-explicit-and-safe",
            not unknown_allowed and not missing_allowed,
            "allowed route families match expected safe set"
            if not unknown_allowed and not missing_allowed
            else f"missing: {', '.join(missing_allowed)}; unknown: {', '.join(unknown_allowed)}",
        )
    )

    destination_contracts = set(values(route_doc, "required_destination_contracts"))
    missing_contracts = sorted(REQUIRED_DESTINATION_CONTRACTS - destination_contracts)
    results.append(
        CheckResult(
            "required-destination-contracts-present",
            not missing_contracts,
            "required destination contracts present"
            if not missing_contracts
            else f"missing destination contracts: {', '.join(missing_contracts)}",
        )
    )

    outputs = output_rows(output_doc) if isinstance(output_doc, dict) else []
    routes = route_rows(route_doc) if isinstance(route_doc, dict) else []
    outputs_by_id = {row.get("output_id"): row for row in outputs if isinstance(row.get("output_id"), str)}
    routes_by_output: dict[str, dict[str, Any]] = {}
    duplicate_outputs: list[str] = []
    for route in routes:
        source_output_id = route.get("source_output_id")
        if not isinstance(source_output_id, str):
            continue
        if source_output_id in routes_by_output:
            duplicate_outputs.append(source_output_id)
        routes_by_output[source_output_id] = route

    missing_routes = sorted(set(outputs_by_id) - set(routes_by_output))
    unknown_routes = sorted(set(routes_by_output) - set(outputs_by_id))
    coverage_passed = bool(outputs_by_id) and not missing_routes and not unknown_routes and not duplicate_outputs
    coverage_parts: list[str] = []
    if missing_routes:
        coverage_parts.append(f"missing routes: {', '.join(missing_routes)}")
    if unknown_routes:
        coverage_parts.append(f"unknown output ids: {', '.join(unknown_routes)}")
    if duplicate_outputs:
        coverage_parts.append(f"duplicate output ids: {', '.join(sorted(duplicate_outputs))}")
    results.append(
        CheckResult(
            "every-refused-output-has-one-route",
            coverage_passed,
            f"{len(outputs_by_id)} refused outputs routed"
            if coverage_passed
            else "; ".join(coverage_parts) or "route coverage missing",
        )
    )

    route_failures: list[str] = []
    for output_id, output in sorted(outputs_by_id.items()):
        route = routes_by_output.get(output_id)
        if not isinstance(route, dict):
            continue
        route_id = route.get("route_id", output_id)
        if route.get("source_fixture_id") != output.get("source_fixture_id"):
            route_failures.append(f"{route_id}: source_fixture_id mismatch")
        if route.get("source_checklist_row_id") != output.get("source_checklist_row_id"):
            route_failures.append(f"{route_id}: source_checklist_row_id mismatch")
        if route.get("assay_specimen_quality_state") != output.get("assay_specimen_quality_state"):
            route_failures.append(f"{route_id}: assay_specimen_quality_state mismatch")
        if route.get("refusal_reason") != output.get("refusal_reason"):
            route_failures.append(f"{route_id}: refusal_reason mismatch")
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
        unknown_route_families = sorted(route_families - ALLOWED_ROUTE_FAMILIES)
        if unknown_route_families:
            route_failures.append(f"{route_id}: unknown route families {', '.join(unknown_route_families)}")

        private_review = output.get("assay_specimen_quality_state") == "private_lab_or_clinical_review_needed"
        if private_review:
            if route.get("route_status") != "private_or_real_quality_review_blocked":
                route_failures.append(f"{route_id}: private review route_status must be private_or_real_quality_review_blocked")
            if route.get("public_processing_allowed") is not False:
                route_failures.append(f"{route_id}: private review must set public_processing_allowed false")
            if route_families != PRIVATE_REVIEW_ROUTE_FAMILIES:
                route_failures.append(f"{route_id}: private review route families must be blocker-only")
        else:
            if route.get("route_status") != "routed_refusal_only":
                route_failures.append(f"{route_id}: route_status must be routed_refusal_only")
            if route.get("public_processing_allowed") is not True:
                route_failures.append(f"{route_id}: synthetic public route must set public_processing_allowed true")
            if route_families != NORMAL_ROUTE_FAMILIES:
                route_failures.append(f"{route_id}: normal route families must match safe refusal set")

    results.append(
        CheckResult(
            "routes-preserve-refusal-boundaries",
            not route_failures,
            f"{len(routes)} routes checked" if routes and not route_failures else "; ".join(route_failures[:12]),
        )
    )

    forbidden_locations: list[str] = []
    for key in sorted(FORBIDDEN_ROUTE_KEYS):
        for location in find_key(route_doc, key):
            if location.startswith("$.forbidden_route_fields"):
                continue
            forbidden_locations.append(f"{location} ({key})")
    results.append(
        CheckResult(
            "forbidden-route-fields-absent",
            not forbidden_locations,
            "no forbidden clinical, ranking, prediction, or recommendation keys present"
            if not forbidden_locations
            else "; ".join(forbidden_locations[:12]),
        )
    )

    return results


def print_text(results: list[CheckResult]) -> None:
    print("Measurement refusal output route-table check")
    print("Boundary: structural synthetic routing checks only; not clinical validation.")
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
                    "check_id": "measurement-refusal-output-route-table-check-v0",
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
