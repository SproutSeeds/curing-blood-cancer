#!/usr/bin/env python3
"""Check measurement-refusal wrapper state-machine negative safety fixtures.

The fixtures are synthetic mutations of the public wrapper state machine. They
must make the state-machine checker fail closed without using real reports,
clinical interpretation, ranking, recommendations, model output, publication
authorization, or patient-specific decisions.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import check_measurement_refusal_wrapper_integration_dry_run as dry_run
import check_measurement_refusal_wrapper_state_machine as state_machine


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
NEGATIVE_FIXTURES = Path("examples/measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0.json")

FIXTURE_SET_ID = "measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0"
FIXTURE_STATUS = "synthetic-state-machine-negative-safety-fixtures"
TARGET_CHECKER_ID = "measurement-refusal-wrapper-state-machine-check-v0"
TARGET_STATE_MACHINE_ID = "measurement-refusal-wrapper-state-machine-v0"
NEXT_SUCCESSOR = "measurement-refusal-wrapper-state-machine-falsification-audit-v0"
HUMAN_GATE = "machine-representation-expert-validation-human-authorization-blocker-v0"

REQUIRED_NEGATIVE_FIXTURE_IDS = {
    "mrsmns_00_prediction_boundary_flag_v0",
    "mrsmns_01_clinical_boundary_missing_v0",
    "mrsmns_02_missing_required_state_v0",
    "mrsmns_03_duplicate_state_id_v0",
    "mrsmns_04_terminal_state_unmarked_v0",
    "mrsmns_05_state_permission_enabled_v0",
    "mrsmns_06_missing_required_transition_v0",
    "mrsmns_07_transition_emits_output_v0",
    "mrsmns_08_transition_unknown_destination_v0",
    "mrsmns_09_public_trace_private_terminal_v0",
    "mrsmns_10_private_trace_public_terminal_v0",
    "mrsmns_11_trace_blocked_use_gap_v0",
    "mrsmns_12_missing_blocked_transition_rule_v0",
    "mrsmns_13_wrong_blocked_terminal_v0",
    "mrsmns_14_missing_transition_invariant_v0",
    "mrsmns_15_forbidden_output_field_v0",
    "mrsmns_16_handoff_gate_changed_v0",
}

ALLOWED_MUTATION_OPS = {
    "drop_blocked_transition_rule",
    "drop_invariant",
    "drop_state",
    "drop_trace",
    "drop_transition",
    "duplicate_state",
    "remove_list_value",
    "remove_trace_blocked_use",
    "set",
    "set_blocked_transition_rule_field",
    "set_state_field",
    "set_trace_field",
    "set_transition_field",
}

REQUIRED_SOURCE_ARTIFACTS = {
    "disease-programs/multiple-myeloma/measurements/measurement-refusal-wrapper-state-machine-v0.md",
    "examples/measurement-refusal-wrapper-state-machine-v0.json",
    "tools/check_measurement_refusal_wrapper_state_machine.py",
    "disease-programs/multiple-myeloma/measurements/measurement-refusal-wrapper-negative-safety-fixtures-v0.md",
    "examples/measurement-refusal-wrapper-negative-safety-fixtures-v0.json",
    "tools/check_measurement_refusal_wrapper_negative_safety_fixtures.py",
    "disease-programs/multiple-myeloma/model-output-boundary-wrapper-v0.md",
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


def at_path(doc: Any, path: list[Any]) -> Any:
    current = doc
    for part in path:
        if isinstance(part, int):
            if not isinstance(current, list):
                raise ValueError(f"path segment {part} does not resolve through a list")
            current = current[part]
        elif isinstance(part, str):
            if not isinstance(current, dict):
                raise ValueError(f"path segment {part} does not resolve through an object")
            current = current[part]
        else:
            raise ValueError("path segments must be strings or integers")
    return current


def set_at_path(doc: Any, path: list[Any], value: Any) -> None:
    if not path:
        raise ValueError("set mutation requires a non-empty path")
    parent = at_path(doc, path[:-1]) if len(path) > 1 else doc
    final = path[-1]
    if isinstance(final, int):
        if not isinstance(parent, list):
            raise ValueError("set mutation final integer segment requires a list parent")
        parent[final] = value
    elif isinstance(final, str):
        if not isinstance(parent, dict):
            raise ValueError("set mutation final string segment requires an object parent")
        parent[final] = value
    else:
        raise ValueError("path segments must be strings or integers")


def remove_value(items: Any, value: str, label: str) -> None:
    if not isinstance(items, list):
        raise ValueError(f"{label} must be a list")
    try:
        items.remove(value)
    except ValueError as exc:
        raise ValueError(f"{label} does not contain {value}") from exc


def object_rows(doc: dict[str, Any], key: str) -> list[dict[str, Any]]:
    rows = doc.get(key)
    if not isinstance(rows, list):
        raise ValueError(f"{key} must be a list")
    return [row for row in rows if isinstance(row, dict)]


def row_for(doc: dict[str, Any], rows_key: str, id_key: str, id_value: str) -> dict[str, Any]:
    for row in object_rows(doc, rows_key):
        if row.get(id_key) == id_value:
            return row
    raise ValueError(f"{rows_key}.{id_key} not found: {id_value}")


def drop_row(doc: dict[str, Any], rows_key: str, id_key: str, id_value: str) -> None:
    rows = object_rows(doc, rows_key)
    original_len = len(rows)
    doc[rows_key] = [row for row in rows if row.get(id_key) != id_value]
    if len(doc[rows_key]) == original_len:
        raise ValueError(f"{rows_key}.{id_key} not found: {id_value}")


def apply_mutation(machine_doc: dict[str, Any], mutation: dict[str, Any]) -> None:
    op = mutation.get("op")
    if op not in ALLOWED_MUTATION_OPS:
        raise ValueError(f"unsupported mutation op: {op!r}")

    if op == "set":
        path = mutation.get("path")
        if not isinstance(path, list):
            raise ValueError("set mutation requires path")
        set_at_path(machine_doc, path, mutation.get("value"))
        return

    if op == "remove_list_value":
        path = mutation.get("path")
        value = mutation.get("value")
        if not isinstance(path, list) or not isinstance(value, str):
            raise ValueError("remove_list_value mutation requires path and value")
        remove_value(at_path(machine_doc, path), value, ".".join(str(part) for part in path))
        return

    if op == "drop_state":
        state_id = mutation.get("state_id")
        if not isinstance(state_id, str):
            raise ValueError("drop_state mutation requires state_id")
        drop_row(machine_doc, "states", "state_id", state_id)
        return

    if op == "duplicate_state":
        state_id = mutation.get("state_id")
        new_state_id = mutation.get("new_state_id")
        if not isinstance(state_id, str) or not isinstance(new_state_id, str):
            raise ValueError("duplicate_state mutation requires state_id and new_state_id")
        duplicate = copy.deepcopy(row_for(machine_doc, "states", "state_id", state_id))
        duplicate["state_id"] = new_state_id
        machine_doc["states"].append(duplicate)
        return

    if op == "set_state_field":
        state_id = mutation.get("state_id")
        field = mutation.get("field")
        if not isinstance(state_id, str) or not isinstance(field, str):
            raise ValueError("set_state_field mutation requires state_id and field")
        row_for(machine_doc, "states", "state_id", state_id)[field] = mutation.get("value")
        return

    if op == "drop_transition":
        transition_id = mutation.get("transition_id")
        if not isinstance(transition_id, str):
            raise ValueError("drop_transition mutation requires transition_id")
        drop_row(machine_doc, "transitions", "transition_id", transition_id)
        return

    if op == "set_transition_field":
        transition_id = mutation.get("transition_id")
        field = mutation.get("field")
        if not isinstance(transition_id, str) or not isinstance(field, str):
            raise ValueError("set_transition_field mutation requires transition_id and field")
        row_for(machine_doc, "transitions", "transition_id", transition_id)[field] = mutation.get("value")
        return

    if op == "drop_trace":
        source_output_id = mutation.get("source_output_id")
        if not isinstance(source_output_id, str):
            raise ValueError("drop_trace mutation requires source_output_id")
        drop_row(machine_doc, "wrapper_record_traces", "source_output_id", source_output_id)
        return

    if op == "set_trace_field":
        source_output_id = mutation.get("source_output_id")
        field = mutation.get("field")
        if not isinstance(source_output_id, str) or not isinstance(field, str):
            raise ValueError("set_trace_field mutation requires source_output_id and field")
        row_for(machine_doc, "wrapper_record_traces", "source_output_id", source_output_id)[field] = mutation.get("value")
        return

    if op == "remove_trace_blocked_use":
        source_output_id = mutation.get("source_output_id")
        blocked_use = mutation.get("blocked_use")
        if not isinstance(source_output_id, str) or not isinstance(blocked_use, str):
            raise ValueError("remove_trace_blocked_use mutation requires source_output_id and blocked_use")
        trace = row_for(machine_doc, "wrapper_record_traces", "source_output_id", source_output_id)
        remove_value(trace.get("blocked_downstream_uses"), blocked_use, "blocked_downstream_uses")
        return

    if op == "drop_blocked_transition_rule":
        source_negative_fixture_id = mutation.get("source_negative_fixture_id")
        if not isinstance(source_negative_fixture_id, str):
            raise ValueError("drop_blocked_transition_rule mutation requires source_negative_fixture_id")
        drop_row(machine_doc, "blocked_transition_rules", "source_negative_fixture_id", source_negative_fixture_id)
        return

    if op == "set_blocked_transition_rule_field":
        source_negative_fixture_id = mutation.get("source_negative_fixture_id")
        field = mutation.get("field")
        if not isinstance(source_negative_fixture_id, str) or not isinstance(field, str):
            raise ValueError("set_blocked_transition_rule_field mutation requires source_negative_fixture_id and field")
        row_for(machine_doc, "blocked_transition_rules", "source_negative_fixture_id", source_negative_fixture_id)[field] = mutation.get("value")
        return

    if op == "drop_invariant":
        invariant_id = mutation.get("invariant_id")
        if not isinstance(invariant_id, str):
            raise ValueError("drop_invariant mutation requires invariant_id")
        drop_row(machine_doc, "transition_invariants", "invariant_id", invariant_id)
        return


def failed_check_ids(root: Path, mutated_machine: dict[str, Any]) -> set[str]:
    dry_run_report = load_json(root, dry_run.DEFAULT_REPORT)
    negative_fixture_pack = load_json(root, state_machine.NEGATIVE_FIXTURES)

    with tempfile.TemporaryDirectory(prefix="cbc-wrapper-state-machine-negative-") as tmp:
        tmp_root = Path(tmp)
        examples = tmp_root / "examples"
        examples.mkdir(parents=True)
        (tmp_root / state_machine.STATE_MACHINE).write_text(
            json.dumps(mutated_machine, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
        (tmp_root / dry_run.DEFAULT_REPORT).write_text(
            json.dumps(dry_run_report, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
        (tmp_root / state_machine.NEGATIVE_FIXTURES).write_text(
            json.dumps(negative_fixture_pack, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
        results = state_machine.run_checks(tmp_root)

    return {result.check_id for result in results if not result.passed}


def run_checks(root: Path) -> list[CheckResult]:
    fixture_pack = load_json(root, NEGATIVE_FIXTURES)
    machine_doc = load_json(root, state_machine.STATE_MACHINE)
    if not isinstance(fixture_pack, dict) or not isinstance(machine_doc, dict):
        raise ValueError("state-machine negative fixtures and target state machine must be JSON objects")

    results: list[CheckResult] = []
    results.append(
        CheckResult(
            "wrapper-state-machine-negative-fixture-set-id",
            fixture_pack.get("fixture_set_id") == FIXTURE_SET_ID,
            f"fixture_set_id={fixture_pack.get('fixture_set_id')!r}",
        )
    )
    results.append(
        CheckResult(
            "wrapper-state-machine-negative-fixture-targets",
            fixture_pack.get("fixture_status") == FIXTURE_STATUS
            and fixture_pack.get("target_checker_id") == TARGET_CHECKER_ID
            and fixture_pack.get("target_state_machine_id") == TARGET_STATE_MACHINE_ID,
            f"fixture_status={fixture_pack.get('fixture_status')!r}; target_checker_id={fixture_pack.get('target_checker_id')!r}; target_state_machine_id={fixture_pack.get('target_state_machine_id')!r}",
        )
    )

    boundary = fixture_pack.get("data_boundary")
    boundary_failures = dry_run.boundary_failures(boundary if isinstance(boundary, dict) else None)
    results.append(
        CheckResult(
            "wrapper-state-machine-negative-fixture-pack-public-synthetic-only",
            not boundary_failures,
            "all required data-boundary fields false"
            if not boundary_failures
            else f"not false: {', '.join(boundary_failures)}",
        )
    )

    clinical_boundaries = set(values(fixture_pack, "clinical_use_boundary"))
    missing_clinical = sorted(dry_run.REQUIRED_CLINICAL_BOUNDARIES - clinical_boundaries)
    results.append(
        CheckResult(
            "wrapper-state-machine-negative-fixture-clinical-boundary-complete",
            not missing_clinical,
            "required clinical boundaries present"
            if not missing_clinical
            else f"missing: {', '.join(missing_clinical)}",
        )
    )

    sources = set(values(fixture_pack, "source_artifacts"))
    missing_sources = sorted(REQUIRED_SOURCE_ARTIFACTS - sources)
    results.append(
        CheckResult(
            "wrapper-state-machine-negative-fixture-source-artifacts-linked",
            not missing_sources,
            "required source artifacts present"
            if not missing_sources
            else f"missing: {', '.join(missing_sources)}",
        )
    )

    fixture_rows = fixture_pack.get("negative_fixtures")
    if not isinstance(fixture_rows, list) or not fixture_rows:
        results.append(CheckResult("wrapper-state-machine-negative-fixtures-present", False, "negative_fixtures missing or empty"))
        return results

    fixture_ids = [row.get("fixture_id") for row in fixture_rows if isinstance(row, dict)]
    fixture_id_set = {value for value in fixture_ids if isinstance(value, str)}
    missing_fixture_ids = sorted(REQUIRED_NEGATIVE_FIXTURE_IDS - fixture_id_set)
    duplicate_ids = sorted({fixture_id for fixture_id in fixture_ids if fixture_ids.count(fixture_id) > 1})
    results.append(
        CheckResult(
            "wrapper-state-machine-negative-fixture-required-cases-present",
            not missing_fixture_ids and not duplicate_ids and len(fixture_rows) == len(REQUIRED_NEGATIVE_FIXTURE_IDS),
            f"{len(REQUIRED_NEGATIVE_FIXTURE_IDS)} required fixtures present"
            if not missing_fixture_ids and not duplicate_ids and len(fixture_rows) == len(REQUIRED_NEGATIVE_FIXTURE_IDS)
            else f"missing={missing_fixture_ids}; duplicate={duplicate_ids}; count={len(fixture_rows)}",
        )
    )

    fixture_failures: list[str] = []
    for index, fixture in enumerate(fixture_rows):
        if not isinstance(fixture, dict):
            fixture_failures.append(f"negative_fixtures[{index}] must be an object")
            continue
        fixture_id = fixture.get("fixture_id", f"negative_fixtures[{index}]")
        expected = set(values(fixture, "expected_failed_check_ids"))
        mutations = fixture.get("mutations")
        blocked_if_not_detected = fixture.get("blocked_if_not_detected")
        if not expected:
            fixture_failures.append(f"{fixture_id}: expected_failed_check_ids missing")
            continue
        if not isinstance(mutations, list) or not mutations:
            fixture_failures.append(f"{fixture_id}: mutations missing or empty")
            continue
        if not isinstance(blocked_if_not_detected, list) or not blocked_if_not_detected:
            fixture_failures.append(f"{fixture_id}: blocked_if_not_detected missing or empty")
            continue

        mutated_machine = copy.deepcopy(machine_doc)
        try:
            for mutation in mutations:
                if not isinstance(mutation, dict):
                    raise ValueError("mutation must be an object")
                apply_mutation(mutated_machine, mutation)
        except (KeyError, TypeError, ValueError) as exc:
            fixture_failures.append(f"{fixture_id}: mutation error: {exc}")
            continue

        actual = failed_check_ids(root, mutated_machine)
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        if not actual:
            fixture_failures.append(f"{fixture_id}: wrapper state-machine checker did not fail")
        if missing:
            fixture_failures.append(f"{fixture_id}: expected failures not detected: {', '.join(missing)}")
        if unexpected:
            fixture_failures.append(f"{fixture_id}: unexpected failures: {', '.join(unexpected)}")

    results.append(
        CheckResult(
            "wrapper-state-machine-negative-fixtures-fail-closed",
            not fixture_failures,
            f"{len(fixture_rows)} wrapper state-machine negative fixtures fail closed"
            if not fixture_failures
            else "; ".join(fixture_failures[:12]),
        )
    )

    handoff = fixture_pack.get("handoff")
    handoff_failures: list[str] = []
    if isinstance(handoff, dict):
        if handoff.get("completed_phase") != FIXTURE_SET_ID:
            handoff_failures.append("completed_phase mismatch")
        if handoff.get("target_completed_phase") != TARGET_STATE_MACHINE_ID:
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
            "wrapper-state-machine-negative-fixture-handoff-preserves-blocker",
            not handoff_failures,
            "handoff preserves human gate and names next successor"
            if not handoff_failures
            else "; ".join(handoff_failures),
        )
    )

    return results


def print_text(results: list[CheckResult]) -> None:
    print("Measurement refusal wrapper state-machine negative safety fixture check")
    print("Boundary: synthetic wrapper transition fail-closed checks only; not clinical validation.")
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
                    "check_id": "measurement-refusal-wrapper-state-machine-negative-safety-fixture-check-v0",
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
