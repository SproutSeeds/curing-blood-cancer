#!/usr/bin/env python3
"""Check the measurement-refusal wrapper state machine.

The state machine is a synthetic-only transition model over public wrapper
metadata. It must preserve refusal-only behavior and route every path to a
metadata-only public terminal, a private-review blocker terminal, or an unsafe
reuse blocker terminal.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import check_measurement_refusal_wrapper_integration_dry_run as dry_run


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
STATE_MACHINE = Path("examples/measurement-refusal-wrapper-state-machine-v0.json")
NEGATIVE_FIXTURES = Path("examples/measurement-refusal-wrapper-negative-safety-fixtures-v0.json")

STATE_MACHINE_ID = "measurement-refusal-wrapper-state-machine-v0"
STATE_MACHINE_STATUS = "synthetic-wrapper-transition-state-machine"
TARGET_DRY_RUN_ID = "measurement-refusal-wrapper-integration-dry-run-v0"
TARGET_NEGATIVE_FIXTURE_SET_ID = "measurement-refusal-wrapper-negative-safety-fixtures-v0"
NEXT_SUCCESSOR = "measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0"
HUMAN_GATE = "machine-representation-expert-validation-human-authorization-blocker-v0"

REQUIRED_STATE_IDS = {
    "mrsms_00_refused_output_received",
    "mrsms_01_route_validated_refusal_only",
    "mrsms_02_wrapper_metadata_assembled",
    "mrsms_03_public_refusal_wrapper_ready",
    "mrsms_04_private_or_real_review_blocker_ready",
    "mrsms_05_metadata_only_public_terminal",
    "mrsms_06_private_or_real_review_blocker_terminal",
    "mrsms_07_unsafe_wrapper_reuse_blocked_terminal",
}

TERMINAL_STATE_IDS = {
    "mrsms_05_metadata_only_public_terminal",
    "mrsms_06_private_or_real_review_blocker_terminal",
    "mrsms_07_unsafe_wrapper_reuse_blocked_terminal",
}

REQUIRED_TRANSITIONS = {
    ("mrsms_00_refused_output_received", "mrsms_01_route_validated_refusal_only", "route_record_validated"),
    ("mrsms_01_route_validated_refusal_only", "mrsms_02_wrapper_metadata_assembled", "wrapper_metadata_created"),
    ("mrsms_02_wrapper_metadata_assembled", "mrsms_03_public_refusal_wrapper_ready", "public_synthetic_refusal_ready"),
    ("mrsms_02_wrapper_metadata_assembled", "mrsms_04_private_or_real_review_blocker_ready", "private_or_real_review_detected"),
    ("mrsms_03_public_refusal_wrapper_ready", "mrsms_05_metadata_only_public_terminal", "metadata_only_export_boundary_reached"),
    ("mrsms_04_private_or_real_review_blocker_ready", "mrsms_06_private_or_real_review_blocker_terminal", "private_or_real_review_blocker_reached"),
    ("mrsms_02_wrapper_metadata_assembled", "mrsms_07_unsafe_wrapper_reuse_blocked_terminal", "unsafe_wrapper_mutation_detected"),
}

PUBLIC_TRACE = [
    "mrsms_00_refused_output_received",
    "mrsms_01_route_validated_refusal_only",
    "mrsms_02_wrapper_metadata_assembled",
    "mrsms_03_public_refusal_wrapper_ready",
    "mrsms_05_metadata_only_public_terminal",
]

PRIVATE_TRACE = [
    "mrsms_00_refused_output_received",
    "mrsms_01_route_validated_refusal_only",
    "mrsms_02_wrapper_metadata_assembled",
    "mrsms_04_private_or_real_review_blocker_ready",
    "mrsms_06_private_or_real_review_blocker_terminal",
]

REQUIRED_INVARIANT_IDS = {
    "mrsmi_00_public_synthetic_only",
    "mrsmi_01_state_coverage_complete",
    "mrsmi_02_transition_terminal_safety",
    "mrsmi_03_wrapper_trace_coverage",
    "mrsmi_04_private_review_routes_block_public_processing",
    "mrsmi_05_negative_fixtures_route_to_blocked_terminal",
    "mrsmi_06_forbidden_outputs_absent",
    "mrsmi_07_human_gate_preserved",
}

REQUIRED_SOURCE_ARTIFACTS = {
    "disease-programs/multiple-myeloma/measurements/measurement-refusal-wrapper-integration-dry-run-v0.md",
    "disease-programs/multiple-myeloma/measurements/measurement-refusal-wrapper-negative-safety-fixtures-v0.md",
    "disease-programs/multiple-myeloma/model-output-boundary-wrapper-v0.md",
    "examples/measurement-refusal-wrapper-integration-dry-run-v0.json",
    "examples/measurement-refusal-wrapper-negative-safety-fixtures-v0.json",
    "tools/check_measurement_refusal_wrapper_integration_dry_run.py",
    "tools/check_measurement_refusal_wrapper_negative_safety_fixtures.py",
}

BLOCKED_ACTIONS = {
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
}

UNSAFE_PERMISSION_FIELDS = {
    "clinical_output_allowed",
    "prediction_output_allowed",
    "comparison_allowed",
    "matching_or_ranking_allowed",
    "real_review_output_allowed",
    "publication_authorization_allowed",
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


def state_rows(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = doc.get("states")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def transition_rows(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = doc.get("transitions")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def trace_rows(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = doc.get("wrapper_record_traces")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def wrapper_rows(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = doc.get("wrapper_records")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def negative_fixture_rows(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = doc.get("negative_fixtures")
    if not isinstance(rows, list):
        return []
    return [row for row in rows if isinstance(row, dict)]


def index_by(rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for row in rows:
        value = row.get(key)
        if isinstance(value, str):
            indexed[value] = row
    return indexed


def permission_failures(row: dict[str, Any], prefix: str) -> list[str]:
    return [f"{prefix}.{field}" for field in sorted(UNSAFE_PERMISSION_FIELDS) if row.get(field) is not False]


def run_checks(root: Path) -> list[CheckResult]:
    state_machine = load_json(root, STATE_MACHINE)
    dry_run_report = load_json(root, dry_run.DEFAULT_REPORT)
    negative_fixture_pack = load_json(root, NEGATIVE_FIXTURES)
    if not isinstance(state_machine, dict) or not isinstance(dry_run_report, dict) or not isinstance(negative_fixture_pack, dict):
        raise ValueError("state machine, dry-run report, and negative fixtures must be JSON objects")

    results: list[CheckResult] = []
    results.append(
        CheckResult(
            "wrapper-state-machine-id",
            state_machine.get("state_machine_id") == STATE_MACHINE_ID,
            f"state_machine_id={state_machine.get('state_machine_id')!r}",
        )
    )
    results.append(
        CheckResult(
            "wrapper-state-machine-targets",
            state_machine.get("state_machine_status") == STATE_MACHINE_STATUS
            and state_machine.get("target_dry_run_id") == TARGET_DRY_RUN_ID
            and state_machine.get("target_negative_fixture_set_id") == TARGET_NEGATIVE_FIXTURE_SET_ID,
            "targets and status match expected values",
        )
    )

    boundary = state_machine.get("data_boundary")
    boundary_failures = dry_run.boundary_failures(boundary if isinstance(boundary, dict) else None)
    results.append(
        CheckResult(
            "wrapper-state-machine-public-synthetic-only",
            not boundary_failures,
            "all required data-boundary fields false"
            if not boundary_failures
            else f"not false: {', '.join(boundary_failures)}",
        )
    )

    clinical_boundaries = set(values(state_machine, "clinical_use_boundary"))
    missing_clinical = sorted(dry_run.REQUIRED_CLINICAL_BOUNDARIES - clinical_boundaries)
    results.append(
        CheckResult(
            "wrapper-state-machine-clinical-boundary-complete",
            not missing_clinical,
            "required clinical boundaries present"
            if not missing_clinical
            else f"missing: {', '.join(missing_clinical)}",
        )
    )

    sources = set(values(state_machine, "source_artifacts"))
    missing_sources = sorted(REQUIRED_SOURCE_ARTIFACTS - sources)
    results.append(
        CheckResult(
            "wrapper-state-machine-source-artifacts-linked",
            not missing_sources,
            "required source artifacts present"
            if not missing_sources
            else f"missing: {', '.join(missing_sources)}",
        )
    )

    states = state_rows(state_machine)
    state_ids = {row.get("state_id") for row in states if isinstance(row.get("state_id"), str)}
    missing_states = sorted(REQUIRED_STATE_IDS - state_ids)
    duplicate_states = sorted({state_id for state_id in state_ids if [row.get("state_id") for row in states].count(state_id) > 1})
    state_failures: list[str] = []
    if missing_states:
        state_failures.append(f"missing states: {', '.join(missing_states)}")
    if duplicate_states:
        state_failures.append(f"duplicate states: {', '.join(duplicate_states)}")
    for row in states:
        state_id = row.get("state_id", "<missing-state-id>")
        terminal = row.get("terminal_state")
        if state_id in TERMINAL_STATE_IDS and terminal is not True:
            state_failures.append(f"{state_id}: terminal_state must be true")
        if state_id not in TERMINAL_STATE_IDS and terminal is True:
            state_failures.append(f"{state_id}: non-terminal state marked terminal")
        state_failures.extend(permission_failures(row, str(state_id)))
    results.append(
        CheckResult(
            "wrapper-state-machine-required-states-safe",
            not state_failures,
            f"{len(REQUIRED_STATE_IDS)} required states present and safe"
            if not state_failures
            else "; ".join(state_failures[:10]),
        )
    )

    transitions = transition_rows(state_machine)
    transition_keys = {
        (row.get("from_state_id"), row.get("to_state_id"), row.get("event"))
        for row in transitions
        if isinstance(row.get("from_state_id"), str)
        and isinstance(row.get("to_state_id"), str)
        and isinstance(row.get("event"), str)
    }
    missing_transitions = sorted(REQUIRED_TRANSITIONS - transition_keys)
    transition_failures: list[str] = []
    if missing_transitions:
        transition_failures.append(
            "missing transitions: "
            + ", ".join(f"{src}->{dst}:{event}" for src, dst, event in missing_transitions)
        )
    for index, row in enumerate(transitions):
        src = row.get("from_state_id")
        dst = row.get("to_state_id")
        if src not in state_ids:
            transition_failures.append(f"transitions[{index}].from_state_id unknown: {src!r}")
        if dst not in state_ids:
            transition_failures.append(f"transitions[{index}].to_state_id unknown: {dst!r}")
        if row.get("emits_output") is not False:
            transition_failures.append(f"transitions[{index}].emits_output must be false")
        if row.get("clinical_or_prediction_output_allowed") is not False:
            transition_failures.append(f"transitions[{index}].clinical_or_prediction_output_allowed must be false")
    results.append(
        CheckResult(
            "wrapper-state-machine-transitions-safe",
            not transition_failures,
            f"{len(REQUIRED_TRANSITIONS)} required transitions present and safe"
            if not transition_failures
            else "; ".join(transition_failures[:10]),
        )
    )

    wrapper_records = wrapper_rows(dry_run_report)
    traces = trace_rows(state_machine)
    traces_by_output = index_by(traces, "source_output_id")
    trace_failures: list[str] = []
    if len(traces) != len(wrapper_records):
        trace_failures.append(f"expected {len(wrapper_records)} traces, found {len(traces)}")
    for record in wrapper_records:
        source_output_id = record.get("source_output_id")
        if not isinstance(source_output_id, str):
            continue
        trace = traces_by_output.get(source_output_id)
        if not trace:
            trace_failures.append(f"{source_output_id}: trace missing")
            continue
        if trace.get("wrapper_record_id") != record.get("wrapper_record_id"):
            trace_failures.append(f"{source_output_id}: wrapper_record_id mismatch")
        expected_trace = PRIVATE_TRACE if record.get("public_processing_allowed") is False else PUBLIC_TRACE
        expected_terminal = expected_trace[-1]
        if trace.get("trace_state_ids") != expected_trace:
            trace_failures.append(f"{source_output_id}: trace_state_ids mismatch")
        if trace.get("terminal_state_id") != expected_terminal:
            trace_failures.append(f"{source_output_id}: terminal_state_id mismatch")
        if trace.get("public_processing_allowed") != record.get("public_processing_allowed"):
            trace_failures.append(f"{source_output_id}: public_processing_allowed mismatch")
        if sorted(values(trace, "blocked_downstream_uses")) != sorted(dry_run.REQUIRED_BLOCKED_USES):
            trace_failures.append(f"{source_output_id}: blocked_downstream_uses incomplete")
        if record.get("public_processing_allowed") is False and trace.get("terminal_state_id") != "mrsms_06_private_or_real_review_blocker_terminal":
            trace_failures.append(f"{source_output_id}: private review did not reach blocker terminal")
    results.append(
        CheckResult(
            "wrapper-state-machine-wrapper-traces-complete",
            not trace_failures,
            f"{len(wrapper_records)} wrapper traces terminate safely"
            if not trace_failures
            else "; ".join(trace_failures[:10]),
        )
    )

    negative_rows = negative_fixture_rows(negative_fixture_pack)
    negative_ids = {row.get("fixture_id") for row in negative_rows if isinstance(row.get("fixture_id"), str)}
    rules = state_machine.get("blocked_transition_rules")
    rule_failures: list[str] = []
    if not isinstance(rules, list):
        rule_failures.append("blocked_transition_rules must be a list")
        rules = []
    rule_ids = {rule.get("source_negative_fixture_id") for rule in rules if isinstance(rule, dict)}
    missing_rule_ids = sorted(negative_ids - {value for value in rule_ids if isinstance(value, str)})
    if missing_rule_ids:
        rule_failures.append(f"missing negative fixture rules: {', '.join(missing_rule_ids)}")
    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            rule_failures.append(f"blocked_transition_rules[{index}] must be an object")
            continue
        if rule.get("blocked_terminal_state_id") != "mrsms_07_unsafe_wrapper_reuse_blocked_terminal":
            rule_failures.append(f"blocked_transition_rules[{index}].blocked_terminal_state_id mismatch")
        if not values(rule, "required_detected_by"):
            rule_failures.append(f"blocked_transition_rules[{index}].required_detected_by missing")
        if rule.get("clinical_or_prediction_output_allowed") is not False:
            rule_failures.append(f"blocked_transition_rules[{index}].clinical_or_prediction_output_allowed must be false")
    results.append(
        CheckResult(
            "wrapper-state-machine-negative-fixtures-blocked",
            not rule_failures,
            f"{len(negative_ids)} negative fixtures route to unsafe blocked terminal"
            if not rule_failures
            else "; ".join(rule_failures[:10]),
        )
    )

    invariant_ids = {row.get("invariant_id") for row in state_machine.get("transition_invariants", []) if isinstance(row, dict)}
    missing_invariants = sorted(REQUIRED_INVARIANT_IDS - {value for value in invariant_ids if isinstance(value, str)})
    results.append(
        CheckResult(
            "wrapper-state-machine-invariants-present",
            not missing_invariants,
            f"{len(REQUIRED_INVARIANT_IDS)} invariants present"
            if not missing_invariants
            else f"missing: {', '.join(missing_invariants)}",
        )
    )

    forbidden_locations: list[str] = []
    for key in sorted(dry_run.FORBIDDEN_WRAPPER_KEYS):
        for location in dry_run.find_key(state_machine, key):
            forbidden_locations.append(location)
    results.append(
        CheckResult(
            "wrapper-state-machine-forbidden-output-fields-absent",
            not forbidden_locations,
            "no forbidden clinical, ranking, prediction, or recommendation keys present"
            if not forbidden_locations
            else "; ".join(forbidden_locations[:10]),
        )
    )

    handoff = state_machine.get("handoff")
    handoff_failures: list[str] = []
    if isinstance(handoff, dict):
        if handoff.get("completed_phase") != STATE_MACHINE_ID:
            handoff_failures.append("completed_phase mismatch")
        if handoff.get("target_completed_phase") != TARGET_NEGATIVE_FIXTURE_SET_ID:
            handoff_failures.append("target_completed_phase mismatch")
        if handoff.get("next_no_outreach_successor_if_selected") != NEXT_SUCCESSOR:
            handoff_failures.append("next successor mismatch")
        if handoff.get("human_gate_state") != HUMAN_GATE:
            handoff_failures.append("human gate mismatch")
        blocked_actions = set(values(handoff, "blocked_actions"))
        missing_actions = sorted(BLOCKED_ACTIONS - blocked_actions)
        if missing_actions:
            handoff_failures.append(f"blocked_actions missing: {', '.join(missing_actions)}")
    else:
        handoff_failures.append("handoff missing")
    results.append(
        CheckResult(
            "wrapper-state-machine-handoff-preserves-blocker",
            not handoff_failures,
            "handoff preserves human gate and names next successor"
            if not handoff_failures
            else "; ".join(handoff_failures),
        )
    )

    return results


def print_text(results: list[CheckResult]) -> None:
    print("Measurement refusal wrapper state-machine check")
    print("Boundary: synthetic wrapper transition checks only; not clinical validation.")
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
                    "check_id": "measurement-refusal-wrapper-state-machine-check-v0",
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
