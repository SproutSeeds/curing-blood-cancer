#!/usr/bin/env python3
"""Check measurement-refusal output schema invariants.

These checks validate public synthetic output shape only. They do not interpret
MRD, validate an assay, review a report, rank modalities, recommend treatment,
or claim a cure.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = Path("examples")
SCHEMAS = Path("schemas")

SOURCE_FIXTURES = EXAMPLES / "measurement-state-refusal-fixtures-v0.json"
OUTPUT_FIXTURE = EXAMPLES / "measurement-refusal-output-fixture-v0.json"
OUTPUT_SCHEMA = SCHEMAS / "measurement-refusal-output.schema.json"

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

REQUIRED_CLINICAL_BOUNDARIES = {
    "not-medical-advice",
    "not-diagnostic",
    "not-treatment-recommendation",
    "not-trial-recommendation",
    "research-use-only",
}

FORBIDDEN_OUTPUT_KEYS = {
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


def fixture_rows(fixture_doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = fixture_doc.get("fixtures")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def output_rows(output_doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = output_doc.get("outputs")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def boundary_failures(data_boundary: dict[str, Any] | None) -> list[str]:
    if not isinstance(data_boundary, dict):
        return sorted(REQUIRED_FALSE_BOUNDARY_FIELDS)
    return sorted(field for field in REQUIRED_FALSE_BOUNDARY_FIELDS if data_boundary.get(field) is not False)


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


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return True


def validate_format(value: str, fmt: str) -> bool:
    if fmt == "date":
        try:
            date.fromisoformat(value)
            return True
        except ValueError:
            return False
    if fmt == "uri":
        parsed = urlparse(value)
        return bool(parsed.scheme and parsed.netloc)
    if fmt == "uri-reference":
        return bool(value)
    return True


def validate_against_schema(value: Any, schema: dict[str, Any], loc: str = "$") -> list[str]:
    failures: list[str] = []

    expected_type = schema.get("type")
    if isinstance(expected_type, str) and not type_matches(value, expected_type):
        return [f"{loc} expected type {expected_type}, got {type(value).__name__}"]

    enum = schema.get("enum")
    if enum is not None and value not in enum:
        failures.append(f"{loc} value {value!r} is not in enum {enum!r}")

    pattern = schema.get("pattern")
    if isinstance(pattern, str) and isinstance(value, str) and re.fullmatch(pattern, value) is None:
        failures.append(f"{loc} value {value!r} does not match pattern {pattern}")

    min_length = schema.get("minLength")
    if isinstance(min_length, int) and isinstance(value, str) and len(value) < min_length:
        failures.append(f"{loc} must have length >= {min_length}")

    fmt = schema.get("format")
    if isinstance(fmt, str) and isinstance(value, str) and not validate_format(value, fmt):
        failures.append(f"{loc} is not a valid {fmt}: {value!r}")

    if isinstance(value, dict):
        required = schema.get("required", [])
        if isinstance(required, list):
            for key in required:
                if key not in value:
                    failures.append(f"{loc}.{key} is required")
        props = schema.get("properties", {})
        if isinstance(props, dict):
            for key, subschema in props.items():
                if key in value and isinstance(subschema, dict):
                    failures.extend(validate_against_schema(value[key], subschema, f"{loc}.{key}"))
        if schema.get("additionalProperties") is False and isinstance(props, dict):
            allowed = set(props)
            for key in value:
                if key not in allowed:
                    failures.append(f"{loc}.{key} is not an allowed property")

    if isinstance(value, list):
        min_items = schema.get("minItems")
        if isinstance(min_items, int) and len(value) < min_items:
            failures.append(f"{loc} must contain at least {min_items} item(s)")
        if schema.get("uniqueItems") is True:
            seen: set[str] = set()
            for item in value:
                marker = json.dumps(item, sort_keys=True)
                if marker in seen:
                    failures.append(f"{loc} contains duplicate item {item!r}")
                seen.add(marker)
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                failures.extend(validate_against_schema(item, item_schema, f"{loc}[{index}]"))

    return failures


def run_checks(root: Path) -> list[CheckResult]:
    schema = load_json(root, OUTPUT_SCHEMA)
    source_doc = load_json(root, SOURCE_FIXTURES)
    output_doc = load_json(root, OUTPUT_FIXTURE)

    results: list[CheckResult] = []

    schema_failures = validate_against_schema(output_doc, schema) if isinstance(schema, dict) else ["schema missing"]
    results.append(
        CheckResult(
            "output-fixture-validates-against-schema",
            not schema_failures,
            "schema validation passed" if not schema_failures else "; ".join(schema_failures[:8]),
        )
    )

    false_failures = boundary_failures(output_doc.get("data_boundary") if isinstance(output_doc, dict) else None)
    results.append(
        CheckResult(
            "output-data-boundary-is-public-synthetic-only",
            not false_failures,
            "all required boundary fields false"
            if not false_failures
            else f"data_boundary not false: {', '.join(false_failures)}",
        )
    )

    clinical_boundaries = set(values(output_doc, "clinical_use_boundary")) if isinstance(output_doc, dict) else set()
    missing_clinical = sorted(REQUIRED_CLINICAL_BOUNDARIES - clinical_boundaries)
    results.append(
        CheckResult(
            "clinical-use-boundary-is-complete",
            not missing_clinical,
            f"found {len(REQUIRED_CLINICAL_BOUNDARIES)} required boundary labels"
            if not missing_clinical
            else f"missing clinical boundary labels: {', '.join(missing_clinical)}",
        )
    )

    shared_blocks = set(values(output_doc, "shared_blocked_downstream_uses")) if isinstance(output_doc, dict) else set()
    missing_shared_blocks = sorted(REQUIRED_BLOCKED_OUTPUTS - shared_blocks)
    results.append(
        CheckResult(
            "shared-blocked-downstream-uses-complete",
            not missing_shared_blocks,
            "all required blocked downstream uses present"
            if not missing_shared_blocks
            else f"missing blocked downstream uses: {', '.join(missing_shared_blocks)}",
        )
    )

    source_fixtures = fixture_rows(source_doc) if isinstance(source_doc, dict) else []
    outputs = output_rows(output_doc) if isinstance(output_doc, dict) else []
    source_by_id = {row.get("fixture_id"): row for row in source_fixtures if isinstance(row.get("fixture_id"), str)}
    output_by_source: dict[str, dict[str, Any]] = {}
    duplicate_source_ids: list[str] = []
    for output in outputs:
        source_id = output.get("source_fixture_id")
        if not isinstance(source_id, str):
            continue
        if source_id in output_by_source:
            duplicate_source_ids.append(source_id)
        output_by_source[source_id] = output

    missing_outputs = sorted(set(source_by_id) - set(output_by_source))
    unknown_outputs = sorted(set(output_by_source) - set(source_by_id))
    coverage_passed = bool(source_by_id) and not missing_outputs and not unknown_outputs and not duplicate_source_ids
    coverage_failures: list[str] = []
    if missing_outputs:
        coverage_failures.append(f"missing outputs: {', '.join(missing_outputs)}")
    if unknown_outputs:
        coverage_failures.append(f"unknown source fixture ids: {', '.join(unknown_outputs)}")
    if duplicate_source_ids:
        coverage_failures.append(f"duplicate source fixture ids: {', '.join(sorted(duplicate_source_ids))}")
    results.append(
        CheckResult(
            "every-source-refusal-fixture-has-one-output",
            coverage_passed,
            f"{len(source_by_id)} source fixtures covered"
            if coverage_passed
            else "; ".join(coverage_failures) or "source fixture coverage missing",
        )
    )

    output_failures: list[str] = []
    for source_id, source in sorted(source_by_id.items()):
        output = output_by_source.get(source_id)
        if not isinstance(output, dict):
            continue
        measurement_input = source.get("measurement_state_input")
        expected_refusal = source.get("expected_refusal")
        if not isinstance(measurement_input, dict) or not isinstance(expected_refusal, dict):
            output_failures.append(f"{source_id}: source fixture missing measurement_state_input or expected_refusal")
            continue

        expected_state = expected_refusal.get("specific_state")
        if output.get("source_checklist_row_id") != source.get("source_checklist_row_id"):
            output_failures.append(f"{source_id}: source_checklist_row_id mismatch")
        if output.get("output_family") != "measurement_state_refusal":
            output_failures.append(f"{source_id}: output_family must be measurement_state_refusal")
        if output.get("output_status") != "refused":
            output_failures.append(f"{source_id}: output_status must be refused")
        if output.get("clinical_use_boundary") != "research-use-only":
            output_failures.append(f"{source_id}: clinical_use_boundary must be research-use-only")
        if output.get("wrapper_state") != expected_refusal.get("wrapper_state"):
            output_failures.append(f"{source_id}: wrapper_state mismatch")
        if output.get("wrapper_state") != "assay_specimen_quality_needed":
            output_failures.append(f"{source_id}: wrapper_state must be assay_specimen_quality_needed")
        if output.get("assay_specimen_quality_state") != expected_state:
            output_failures.append(f"{source_id}: assay_specimen_quality_state mismatch")
        if output.get("refusal_reason") != expected_state:
            output_failures.append(f"{source_id}: refusal_reason mismatch")
        if output.get("public_processing_allowed") != expected_refusal.get("public_processing_allowed"):
            output_failures.append(f"{source_id}: public_processing_allowed mismatch")
        if output.get("comparison_allowed") is not False:
            output_failures.append(f"{source_id}: comparison_allowed must be false")
        if output.get("clinical_output_allowed") is not False:
            output_failures.append(f"{source_id}: clinical_output_allowed must be false")
        if output.get("limitation_note_required") is not True:
            output_failures.append(f"{source_id}: limitation_note_required must be true")
        if output.get("no_interpretive_text") is not True:
            output_failures.append(f"{source_id}: no_interpretive_text must be true")

        output_blocks = set(values(output, "blocked_downstream_uses"))
        missing_blocks = sorted(REQUIRED_BLOCKED_OUTPUTS - output_blocks)
        if missing_blocks:
            output_failures.append(f"{source_id}: missing blocked downstream uses {', '.join(missing_blocks)}")

    results.append(
        CheckResult(
            "outputs-preserve-fail-closed-refusal-contract",
            not output_failures,
            f"{len(outputs)} outputs checked" if outputs and not output_failures else "; ".join(output_failures[:12]),
        )
    )

    forbidden_locations: list[str] = []
    for key in sorted(FORBIDDEN_OUTPUT_KEYS):
        for location in find_key(output_doc, key):
            if location.startswith("$.forbidden_output_fields"):
                continue
            forbidden_locations.append(f"{location} ({key})")
    results.append(
        CheckResult(
            "forbidden-output-fields-absent",
            not forbidden_locations,
            "no forbidden clinical, ranking, prediction, or recommendation keys present"
            if not forbidden_locations
            else "; ".join(forbidden_locations[:12]),
        )
    )

    private_output = None
    for output in outputs:
        if output.get("assay_specimen_quality_state") == "private_lab_or_clinical_review_needed":
            private_output = output
            break
    private_passed = isinstance(private_output, dict) and private_output.get("public_processing_allowed") is False
    results.append(
        CheckResult(
            "real-or-private-quality-review-stops-public-output",
            private_passed,
            "private review output sets public_processing_allowed false"
            if private_passed
            else "private review output must set public_processing_allowed false",
        )
    )

    return results


def print_text(results: list[CheckResult]) -> None:
    print("Measurement refusal output schema check")
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
                    "check_id": "measurement-refusal-output-schema-check-v0",
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
