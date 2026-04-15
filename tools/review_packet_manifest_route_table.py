#!/usr/bin/env python3
"""Dry-run copied-reference routing for review-packet builder manifests.

This tool is intentionally not a review-packet builder. It reads a public
placeholder manifest, checks that public references and safety boundaries are
present, and emits only copied route-table data plus missing-input or refusal
records.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_MANIFEST = Path("schemas/review-packet-builder-manifest-template-v0.json")
DEFAULT_CATALOG = Path("artifacts/public-artifact-catalog-v0.json")
DEFAULT_SOURCE_REGISTRY = Path("sources/source-registry-v0.json")

REQUIRED_CLINICAL_BOUNDARIES = {
    "not-medical-advice",
    "not-diagnostic",
    "not-treatment-recommendation",
    "not-trial-recommendation",
    "research-use-only",
}

REQUIRED_FALSE_FLAGS = {
    "builder_code_allowed",
    "generated_claims_allowed",
    "patient_specific_outputs_allowed",
    "publication_authorization_allowed",
}

FORBIDDEN_KEYS = {
    "actionability",
    "actionability_score",
    "availability_for_patient",
    "builder_output",
    "candidate_option",
    "candidate_options",
    "candidate_option_ids",
    "case_id",
    "clinical_importance",
    "clinical_priority",
    "clinical_priority_score",
    "date_of_birth",
    "dose",
    "dosing",
    "eligibility",
    "eligibility_guidance",
    "enrollment_advice",
    "enrollment_guidance",
    "evidence_rank",
    "evidence_strength",
    "evidence_strength_score",
    "expanded_access_guidance",
    "free_text_note",
    "generated_claim_text",
    "generated_public_explainer",
    "medical_record_number",
    "option_rank",
    "patient_fit",
    "patient_id",
    "patient_relevance",
    "publication_authorization",
    "raw_record",
    "real_case_data",
    "recommendation",
    "reviewer_email",
    "reviewer_identity",
    "reviewer_name",
    "sponsor_access",
    "sponsor_access_instruction",
    "sponsor_access_instructions",
    "treatment_choice",
    "treatment_recommendation",
    "trial_choice",
    "trial_match",
    "trial_matching",
    "trial_recommendation",
    "urgency",
    "urgency_score",
}

DO_NOT_INFER = [
    "Do not infer that route-table output is a review packet.",
    "Do not infer expert review, evidence strength, clinical priority, patient relevance, actionability, or publication authorization.",
    "Do not use route-table output for treatment selection, trial selection, expanded-access decisions, monitoring decisions, or cure claims.",
    "Do not rank artifacts, sources, mechanisms, targets, therapies, trials, tasks, gaps, claims, or questions from route-table order.",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def relative_repo_path(root: Path, raw_path: Any) -> tuple[Path | None, str | None]:
    if not isinstance(raw_path, str) or not raw_path.strip():
        return None, "missing path"
    path = Path(raw_path)
    if path.is_absolute():
        return None, "absolute paths are not allowed"
    candidate = (root / path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None, "path escapes repository root"
    if not candidate.exists():
        return candidate, "path does not exist"
    return candidate, None


def find_forbidden_keys(value: Any, location: str = "$") -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    if isinstance(value, dict):
        for key, item in value.items():
            item_location = f"{location}.{key}"
            if key in FORBIDDEN_KEYS:
                findings.append(
                    {
                        "location": item_location,
                        "field": key,
                        "reason": "forbidden manifest field",
                    }
                )
            findings.extend(find_forbidden_keys(item, item_location))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            findings.extend(find_forbidden_keys(item, f"{location}[{index}]"))
    return findings


def catalog_index(catalog: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(catalog, dict):
        return {}
    entries = catalog.get("entries")
    if not isinstance(entries, list):
        return {}
    return {
        entry["artifact_id"]: entry
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("artifact_id"), str)
    }


def source_index(registry: Any) -> set[str]:
    if not isinstance(registry, dict):
        return set()
    records = registry.get("records")
    if not isinstance(records, list):
        return set()
    return {
        record["source_id"]
        for record in records
        if isinstance(record, dict) and isinstance(record.get("source_id"), str)
    }


def refusal(kind: str, location: str, reason: str, value: Any | None = None) -> dict[str, Any]:
    record: dict[str, Any] = {
        "refusal_kind": kind,
        "location": location,
        "reason": reason,
    }
    if isinstance(value, (str, int, float, bool)) or value is None:
        record["value"] = value
    return record


def check_repo_path(
    root: Path,
    raw_path: Any,
    location: str,
    refusals: list[dict[str, Any]],
    checks: list[dict[str, Any]],
) -> str | None:
    candidate, error = relative_repo_path(root, raw_path)
    if error:
        refusals.append(refusal("missing-or-unsafe-path", location, error, raw_path))
        checks.append({"check": location, "status": "refused", "reason": error})
        return raw_path if isinstance(raw_path, str) else None
    checks.append({"check": location, "status": "passed", "path": str(raw_path)})
    return str(raw_path)


def append_route(
    routes: list[dict[str, Any]],
    section: str,
    decision: str,
    copied_fields: dict[str, Any],
    output_boundary: str,
) -> None:
    routes.append(
        {
            "route_id": f"route-{len(routes) + 1:03d}-{section}",
            "manifest_section": section,
            "decision": decision,
            "copied_fields": copied_fields,
            "output_boundary": output_boundary,
        }
    )


def build_route_table(root: Path, manifest: Any, catalog: Any, registry: Any) -> tuple[dict[str, Any], int]:
    routes: list[dict[str, Any]] = []
    refusals: list[dict[str, Any]] = []
    checks: list[dict[str, Any]] = []

    if not isinstance(manifest, dict):
        output = refusal_output("unidentified-input", refusals + [refusal("shape", "$", "manifest must be a JSON object")])
        return output, 2

    forbidden = find_forbidden_keys(manifest)
    if forbidden:
        output = refusal_output(str(manifest.get("review_packet_builder_manifest_id", "unidentified-input")), forbidden)
        return output, 2

    manifest_id = manifest.get("review_packet_builder_manifest_id")
    if not isinstance(manifest_id, str) or not manifest_id:
        output = refusal_output("unidentified-input", [refusal("shape", "$.review_packet_builder_manifest_id", "missing manifest id")])
        return output, 2

    artifact_records = catalog_index(catalog)
    known_sources = source_index(registry)

    append_route(
        routes,
        "manifest-identity",
        "copy",
        {
            "review_packet_builder_manifest_id": manifest_id,
            "date": manifest.get("date"),
            "title": manifest.get("title"),
            "disease_program": manifest.get("disease_program"),
            "packet_type": manifest.get("packet_type"),
            "claim_level": manifest.get("claim_level"),
        },
        "Copied manifest identity only; no inference about review completion, publication readiness, or clinical use.",
    )

    target_packet = manifest.get("target_packet")
    if isinstance(target_packet, dict):
        target_id = target_packet.get("artifact_id")
        if isinstance(target_id, str) and target_id not in artifact_records:
            refusals.append(refusal("unknown-artifact-id", "$.target_packet.artifact_id", "artifact id is not in catalog", target_id))
        check_repo_path(root, target_packet.get("path"), "$.target_packet.path", refusals, checks)
        append_route(
            routes,
            "target-packet",
            "reference",
            {
                "artifact_id": target_id,
                "path": target_packet.get("path"),
                "review_status": target_packet.get("review_status"),
                "packet_boundary": target_packet.get("packet_boundary"),
            },
            "Reference packet template only; do not fill sections or generate packet text.",
        )
    else:
        refusals.append(refusal("shape", "$.target_packet", "target_packet must be an object"))

    artifact_inputs = manifest.get("artifact_inputs")
    if isinstance(artifact_inputs, list):
        for index, artifact_input in enumerate(artifact_inputs):
            if not isinstance(artifact_input, dict):
                refusals.append(refusal("shape", f"$.artifact_inputs[{index}]", "artifact input must be an object"))
                continue
            artifact_id = artifact_input.get("artifact_id")
            catalog_record = artifact_records.get(artifact_id) if isinstance(artifact_id, str) else None
            if catalog_record is None:
                refusals.append(
                    refusal("unknown-artifact-id", f"$.artifact_inputs[{index}].artifact_id", "artifact id is not in catalog", artifact_id)
                )
            else:
                for field in ("metadata_path", "artifact_class", "claim_level"):
                    if artifact_input.get(field) != catalog_record.get(field):
                        refusals.append(
                            refusal(
                                "catalog-mismatch",
                                f"$.artifact_inputs[{index}].{field}",
                                f"value does not match catalog {field}",
                                artifact_input.get(field),
                            )
                        )
            if not artifact_input.get("limitations"):
                refusals.append(refusal("missing-boundary", f"$.artifact_inputs[{index}].limitations", "artifact limitations are required"))
            check_repo_path(root, artifact_input.get("path"), f"$.artifact_inputs[{index}].path", refusals, checks)
            check_repo_path(root, artifact_input.get("metadata_path"), f"$.artifact_inputs[{index}].metadata_path", refusals, checks)
            append_route(
                routes,
                f"artifact-input-{index + 1}",
                "copy",
                {
                    "artifact_id": artifact_id,
                    "path": artifact_input.get("path"),
                    "metadata_path": artifact_input.get("metadata_path"),
                    "artifact_class": artifact_input.get("artifact_class"),
                    "claim_level": artifact_input.get("claim_level"),
                    "review_status": artifact_input.get("review_status"),
                    "required_sections": artifact_input.get("required_sections", []),
                    "limitations": artifact_input.get("limitations", []),
                },
                "Copied artifact reference only; do not summarize, rewrite, strengthen, rank, or clinically interpret artifact content.",
            )
    else:
        refusals.append(refusal("shape", "$.artifact_inputs", "artifact_inputs must be a list"))

    schema_inputs = manifest.get("schema_inputs")
    if isinstance(schema_inputs, list):
        for index, schema_input in enumerate(schema_inputs):
            if not isinstance(schema_input, dict):
                refusals.append(refusal("shape", f"$.schema_inputs[{index}]", "schema input must be an object"))
                continue
            check_repo_path(root, schema_input.get("schema_path"), f"$.schema_inputs[{index}].schema_path", refusals, checks)
            if schema_input.get("template_path"):
                check_repo_path(root, schema_input.get("template_path"), f"$.schema_inputs[{index}].template_path", refusals, checks)
            append_route(
                routes,
                f"schema-input-{index + 1}",
                "reference",
                {
                    "schema_id": schema_input.get("schema_id"),
                    "schema_path": schema_input.get("schema_path"),
                    "template_path": schema_input.get("template_path"),
                    "validation_scope": schema_input.get("validation_scope"),
                },
                "Reference schema inputs only; schema validity is not expert review, evidence strength, or publication readiness.",
            )
    else:
        refusals.append(refusal("shape", "$.schema_inputs", "schema_inputs must be a list"))

    source_values = manifest.get("source_ids")
    source_set = {value for value in source_values if isinstance(value, str)} if isinstance(source_values, list) else set()
    source_inputs = manifest.get("source_inputs")
    if isinstance(source_inputs, dict):
        check_repo_path(root, source_inputs.get("source_registry_path"), "$.source_inputs.source_registry_path", refusals, checks)
        nested_sources = source_inputs.get("source_ids")
        if isinstance(nested_sources, list):
            for index, source_id in enumerate(nested_sources):
                if not isinstance(source_id, str):
                    continue
                if source_id not in known_sources:
                    refusals.append(
                        refusal("unknown-source-id", f"$.source_inputs.source_ids[{index}]", "source id is not in source registry", source_id)
                    )
                if source_id not in source_set:
                    refusals.append(
                        refusal("source-id-mismatch", f"$.source_inputs.source_ids[{index}]", "source id is missing from top-level source_ids", source_id)
                    )
        append_route(
            routes,
            "source-inputs",
            "reference",
            {
                "source_registry_path": source_inputs.get("source_registry_path"),
                "source_ids": nested_sources if isinstance(nested_sources, list) else [],
                "source_use": source_inputs.get("source_use"),
            },
            "Reference public source IDs only; source presence does not imply actionability, efficacy, safety, eligibility, availability, or patient fit.",
        )
    else:
        refusals.append(refusal("shape", "$.source_inputs", "source_inputs must be an object"))

    reference_ids = manifest.get("reference_ids")
    if isinstance(reference_ids, dict):
        for key, value in reference_ids.items():
            append_route(
                routes,
                f"reference-ids-{key}",
                "reference",
                {key: value if isinstance(value, list) else []},
                "Reference IDs only; inclusion is not ranking, priority, evidence strength, clinical importance, or actionability.",
            )

    missing_inputs = manifest.get("missing_inputs") if isinstance(manifest.get("missing_inputs"), list) else []
    for index, missing_input in enumerate(missing_inputs):
        if not isinstance(missing_input, dict):
            refusals.append(refusal("shape", f"$.missing_inputs[{index}]", "missing input must be an object"))
            continue
        append_route(
            routes,
            f"missing-input-{index + 1}",
            "omit",
            {
                "missing_input_id": missing_input.get("missing_input_id"),
                "missing_kind": missing_input.get("missing_kind"),
                "reason_missing": missing_input.get("reason_missing"),
                "blocking_state": missing_input.get("blocking_state"),
                "next_public_task_ids": missing_input.get("next_public_task_ids", []),
            },
            "Report missingness explicitly; do not invent substitutes, generated claims, or fallback clinical text.",
        )

    validation_expectations = manifest.get("validation_expectations")
    if isinstance(validation_expectations, dict):
        required_checks = validation_expectations.get("required_checks")
        fail_closed_conditions = validation_expectations.get("fail_closed_conditions")
        forbidden_fields = validation_expectations.get("forbidden_fields")
        if not required_checks:
            refusals.append(refusal("missing-boundary", "$.validation_expectations.required_checks", "required checks are missing"))
        if not fail_closed_conditions:
            refusals.append(refusal("missing-boundary", "$.validation_expectations.fail_closed_conditions", "fail-closed conditions are missing"))
        if not forbidden_fields:
            refusals.append(refusal("missing-boundary", "$.validation_expectations.forbidden_fields", "forbidden fields are missing"))
        append_route(
            routes,
            "validation-expectations",
            "copy",
            {
                "validation_command": validation_expectations.get("validation_command"),
                "required_checks": required_checks if isinstance(required_checks, list) else [],
                "fail_closed_conditions": fail_closed_conditions if isinstance(fail_closed_conditions, list) else [],
                "forbidden_fields": forbidden_fields if isinstance(forbidden_fields, list) else [],
            },
            "Copy validation expectations only; validation is not expert review or clinical endorsement.",
        )
    else:
        refusals.append(refusal("shape", "$.validation_expectations", "validation_expectations must be an object"))

    clinical_boundaries = manifest.get("clinical_use_boundary")
    if isinstance(clinical_boundaries, list):
        missing = sorted(REQUIRED_CLINICAL_BOUNDARIES - {value for value in clinical_boundaries if isinstance(value, str)})
        if missing:
            refusals.append(refusal("missing-boundary", "$.clinical_use_boundary", "required clinical-use boundaries are missing", ", ".join(missing)))
    else:
        refusals.append(refusal("shape", "$.clinical_use_boundary", "clinical_use_boundary must be a list"))

    builder_boundary = manifest.get("builder_code_boundary")
    if isinstance(builder_boundary, dict):
        for flag in sorted(REQUIRED_FALSE_FLAGS):
            if builder_boundary.get(flag) is not False:
                refusals.append(refusal("boundary-violation", f"$.builder_code_boundary.{flag}", "builder boundary flag must be false", builder_boundary.get(flag)))
        append_route(
            routes,
            "builder-code-boundary",
            "copy",
            {
                flag: builder_boundary.get(flag)
                for flag in sorted(REQUIRED_FALSE_FLAGS)
            }
            | {"implementation_boundary": builder_boundary.get("implementation_boundary")},
            "Copy false builder-boundary flags only; output does not authorize builder code, generated claims, patient-specific outputs, or publication decisions.",
        )
    else:
        refusals.append(refusal("shape", "$.builder_code_boundary", "builder_code_boundary must be an object"))

    for field in ("limitations", "do_not_infer"):
        if not manifest.get(field):
            refusals.append(refusal("missing-boundary", f"$.{field}", f"{field} is required"))

    status = "refused" if refusals else "route-table-ready-with-missing-inputs" if missing_inputs else "route-table-ready"
    output = {
        "route_table_id": f"{manifest_id}-route-table-v0",
        "date": manifest.get("date"),
        "input_manifest_id": manifest_id,
        "tool": "tools/review_packet_manifest_route_table.py",
        "route_table_status": status,
        "claim_level": manifest.get("claim_level"),
        "clinical_use_boundary": clinical_boundaries if isinstance(clinical_boundaries, list) else [],
        "output_boundary": [
            "copied-reference routing only",
            "not a review packet",
            "not expert review",
            "not generated biomedical prose",
            "not medical advice",
            "not publication-ready",
        ],
        "copied_reference_routes": routes,
        "missing_input_records": missing_inputs,
        "refusal_records": refusals,
        "validation_checks": checks,
        "do_not_infer": DO_NOT_INFER,
    }
    return output, 2 if refusals else 0


def refusal_output(input_id: str, refusals: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "route_table_id": f"{input_id}-route-table-refusal-v0",
        "input_manifest_id": input_id,
        "tool": "tools/review_packet_manifest_route_table.py",
        "route_table_status": "refused",
        "output_boundary": [
            "copied-reference routing only",
            "not a review packet",
            "not expert review",
            "not generated biomedical prose",
            "not medical advice",
            "not publication-ready",
        ],
        "copied_reference_routes": [],
        "missing_input_records": [],
        "refusal_records": refusals,
        "validation_checks": [],
        "do_not_infer": DO_NOT_INFER,
    }


def print_text(output: dict[str, Any]) -> None:
    print("Review-packet manifest route-table dry run")
    print(f"Status: {output.get('route_table_status')}")
    print(f"Input manifest: {output.get('input_manifest_id')}")
    print(f"Routes: {len(output.get('copied_reference_routes', []))}")
    print(f"Missing inputs: {len(output.get('missing_input_records', []))}")
    print(f"Refusals: {len(output.get('refusal_records', []))}")
    print("Boundary: copied-reference routing only; not a review packet, not expert review, not generated biomedical prose, not medical advice, not publication-ready.")
    refusals = output.get("refusal_records", [])
    if isinstance(refusals, list) and refusals:
        print()
        print("Refusal records:")
        for record in refusals:
            if not isinstance(record, dict):
                continue
            print(f"- {record.get('location')}: {record.get('reason')}")
    missing = output.get("missing_input_records", [])
    if isinstance(missing, list) and missing:
        print()
        print("Missing inputs:")
        for record in missing:
            if not isinstance(record, dict):
                continue
            print(f"- {record.get('missing_input_id')}: {record.get('blocking_state')}")


def run_self_test(root: Path, manifest: Any, catalog: Any, registry: Any) -> int:
    cases: list[tuple[str, Any, bool]] = []

    cases.append(("valid placeholder manifest", manifest, False))

    forbidden = deepcopy(manifest)
    forbidden["patient_id"] = "forbidden-placeholder-no-real-person"
    cases.append(("forbidden patient identifier field", forbidden, True))

    missing_path = deepcopy(manifest)
    missing_path["artifact_inputs"][0]["path"] = "examples/nonexistent-route-table-fixture-input.md"
    cases.append(("missing artifact path", missing_path, True))

    missing_source = deepcopy(manifest)
    missing_source["source_ids"].append("unknown_source_fixture")
    missing_source["source_inputs"]["source_ids"].append("unknown_source_fixture")
    cases.append(("unknown source id", missing_source, True))

    missing_boundary = deepcopy(manifest)
    missing_boundary["clinical_use_boundary"] = [
        value for value in missing_boundary["clinical_use_boundary"] if value != "not-trial-recommendation"
    ]
    cases.append(("missing clinical-use boundary", missing_boundary, True))

    failed: list[str] = []
    for name, candidate, should_refuse in cases:
        output, exit_code = build_route_table(root, candidate, catalog, registry)
        refused = exit_code != 0 or output.get("route_table_status") == "refused"
        if refused != should_refuse:
            failed.append(f"{name}: expected refused={should_refuse}, observed refused={refused}")

    if failed:
        print("Route-table self-test failed:")
        for item in failed:
            print(f"- {item}")
        return 1

    print("Route-table self-test passed.")
    print("Checked valid placeholder, forbidden field, missing path, unknown source ID, and missing boundary cases.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_SOURCE_REGISTRY)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--self-test", action="store_true", help="Run focused fail-closed checks without writing outputs.")
    args = parser.parse_args()

    root = args.root.resolve()
    manifest_path = args.manifest if args.manifest.is_absolute() else root / args.manifest
    catalog_path = args.catalog if args.catalog.is_absolute() else root / args.catalog
    source_registry_path = args.source_registry if args.source_registry.is_absolute() else root / args.source_registry

    manifest = load_json(manifest_path)
    catalog = load_json(catalog_path)
    registry = load_json(source_registry_path)
    if args.self_test:
        return run_self_test(root, manifest, catalog, registry)
    output, exit_code = build_route_table(root, manifest, catalog, registry)

    if args.json:
        print(json.dumps(output, indent=2, sort_keys=True))
    else:
        print_text(output)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
