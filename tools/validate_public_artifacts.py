#!/usr/bin/env python3
"""Validate public Curing Blood Cancer artifacts.

This intentionally uses only the Python standard library so the public repo can
check itself before it has a package manager or CI stack.
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


SKIP_SCHEMA_VALIDATION = {
    "schemas/evidence-claim-template-v0.json",
    "disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-extraction-template-v0.json",
}


@dataclass
class Issue:
    path: Path
    message: str


class Validator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.errors: list[Issue] = []
        self.warnings: list[Issue] = []
        self.json_docs: dict[Path, Any] = {}

    def run(self) -> int:
        self.load_json_files()
        if self.errors:
            self.report()
            return 1

        source_ids = self.collect_source_ids()
        artifact_metadata = self.validate_artifact_metadata()
        taxonomy_ids = self.collect_taxonomy_ids()
        query_record_ids = self.collect_query_record_ids()
        mechanism_group_ids = self.collect_mechanism_group_ids()
        extraction_record_ids = self.collect_extraction_record_ids()
        extraction_signal_ids = self.collect_extraction_signal_ids()
        measurement_term_ids = self.collect_measurement_term_ids()
        claim_set_ids = self.collect_claim_set_ids()
        claim_ids = self.collect_claim_ids()
        gap_register_ids = self.collect_gap_register_ids()
        gap_ids = self.collect_gap_ids()

        self.validate_claim_sets()
        self.validate_artifact_catalogs(artifact_metadata)
        self.validate_evidence_claims()
        self.validate_evidence_gap_registers()
        self.validate_public_task_queues()
        self.validate_expert_review_packets()
        self.validate_mechanism_extractions()
        self.validate_measurement_context_audits()
        self.validate_measurement_glossaries()
        self.validate_mechanism_maps()
        self.validate_mechanism_coverage_reports()
        self.validate_opportunity_maps()
        self.validate_disease_maps()
        self.validate_target_records()
        self.validate_therapy_records()
        self.validate_trial_landscape_records(source_ids)
        self.validate_open_question_records()
        self.validate_review_packet_builder_manifest_records(source_ids, artifact_metadata)
        self.validate_review_packet_route_table_outputs()
        self.validate_measurement_refusal_outputs()
        self.validate_measurement_refusal_route_tables()
        self.validate_measurement_refusal_validator_reports()
        self.validate_case_to_cure_synthetic_pipelines()
        self.validate_source_references(source_ids)
        self.validate_taxonomy_references(taxonomy_ids)
        self.validate_mechanism_group_references(mechanism_group_ids)
        self.validate_extraction_record_references(extraction_record_ids)
        self.validate_extraction_signal_references(extraction_signal_ids)
        self.validate_measurement_term_references(measurement_term_ids)
        self.validate_claim_set_references(claim_set_ids)
        self.validate_claim_references(claim_ids)
        self.validate_gap_register_references(gap_register_ids)
        self.validate_gap_references(gap_ids)
        self.validate_query_record_references(query_record_ids)
        self.validate_query_records()

        self.report()
        return 1 if self.errors else 0

    def rel(self, path: Path) -> Path:
        return path.relative_to(self.root)

    def add_error(self, path: Path, message: str) -> None:
        self.errors.append(Issue(self.rel(path), message))

    def add_warning(self, path: Path, message: str) -> None:
        self.warnings.append(Issue(self.rel(path), message))

    def load_json_files(self) -> None:
        for path in sorted(self.root.rglob("*.json")):
            if ".git" in path.parts:
                continue
            try:
                self.json_docs[path] = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                self.add_error(path, f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")

    def collect_source_ids(self) -> set[str]:
        registry = self.root / "sources" / "source-registry-v0.json"
        doc = self.json_docs.get(registry)
        if not isinstance(doc, dict):
            self.add_error(registry, "missing source registry JSON object")
            return set()
        records = doc.get("records")
        if not isinstance(records, list):
            self.add_error(registry, "source registry must contain a records array")
            return set()

        ids: set[str] = set()
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                self.add_error(registry, f"records[{index}] must be an object")
                continue
            source_id = record.get("source_id")
            if not isinstance(source_id, str) or not source_id:
                self.add_error(registry, f"records[{index}] missing source_id")
                continue
            if source_id in ids:
                self.add_error(registry, f"duplicate source_id: {source_id}")
            ids.add(source_id)
        return ids

    def validate_artifact_metadata(self) -> dict[str, tuple[Path, dict[str, Any]]]:
        schema_path = self.root / "schemas" / "artifact-metadata.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            self.add_error(schema_path, "missing artifact metadata schema")
            return {}

        metadata_by_id: dict[str, tuple[Path, dict[str, Any]]] = {}
        for path, doc in self.json_docs.items():
            if not self.is_artifact_metadata_path(path):
                continue
            if not isinstance(doc, dict):
                self.add_error(path, "artifact metadata must be an object")
                continue

            self.validate_against_schema(path, doc, schema)
            artifact_id = doc.get("artifact_id")
            if not isinstance(artifact_id, str) or not artifact_id:
                self.add_error(path, "artifact_id must be a non-empty string")
                continue
            if artifact_id in metadata_by_id:
                self.add_error(path, f"duplicate artifact_id: {artifact_id}")
                continue
            metadata_by_id[artifact_id] = (path, doc)
        return metadata_by_id

    def collect_taxonomy_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if "taxonomies" not in path.parts or not isinstance(doc, dict):
                continue
            classes = doc.get("classes")
            if not isinstance(classes, list):
                continue
            for index, item in enumerate(classes):
                if not isinstance(item, dict):
                    self.add_error(path, f"classes[{index}] must be an object")
                    continue
                class_id = item.get("class_id")
                if not isinstance(class_id, str) or not class_id:
                    self.add_error(path, f"classes[{index}] missing class_id")
                    continue
                if class_id in ids:
                    self.add_error(path, f"duplicate taxonomy class_id: {class_id}")
                ids.add(class_id)
        return ids

    def collect_query_record_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "query_record_id" not in doc:
                continue
            query_id = doc.get("query_record_id")
            if not query_id:
                if path.name.endswith("template-v0.json"):
                    continue
                self.add_error(path, "query_record_id must be non-empty")
                continue
            if not isinstance(query_id, str):
                self.add_error(path, "query_record_id must be a string")
                continue
            if query_id in ids:
                self.add_error(path, f"duplicate query_record_id: {query_id}")
            ids.add(query_id)
        return ids

    def collect_mechanism_group_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict):
                continue
            groups = doc.get("mechanism_groups")
            if not isinstance(groups, list):
                continue
            for index, group in enumerate(groups):
                if not isinstance(group, dict):
                    self.add_error(path, f"mechanism_groups[{index}] must be an object")
                    continue
                mechanism_id = group.get("mechanism_id")
                if not isinstance(mechanism_id, str) or not mechanism_id:
                    self.add_error(path, f"mechanism_groups[{index}] missing mechanism_id")
                    continue
                if mechanism_id in ids:
                    self.add_error(path, f"duplicate mechanism_id: {mechanism_id}")
                ids.add(mechanism_id)
        return ids

    def collect_extraction_record_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "extraction_record_id" not in doc:
                continue
            extraction_id = doc.get("extraction_record_id")
            if not extraction_id:
                if path.name.endswith("template-v0.json"):
                    continue
                self.add_error(path, "extraction_record_id must be non-empty")
                continue
            if not isinstance(extraction_id, str):
                self.add_error(path, "extraction_record_id must be a string")
                continue
            if extraction_id in ids:
                self.add_error(path, f"duplicate extraction_record_id: {extraction_id}")
            ids.add(extraction_id)
        return ids

    def collect_extraction_signal_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "extraction_record_id" not in doc:
                continue
            signals = doc.get("extracted_signals")
            if not isinstance(signals, list):
                continue
            for index, signal in enumerate(signals):
                if not isinstance(signal, dict):
                    self.add_error(path, f"extracted_signals[{index}] must be an object")
                    continue
                signal_id = signal.get("signal_id")
                if not signal_id:
                    if path.name.endswith("template-v0.json"):
                        continue
                    self.add_error(path, f"extracted_signals[{index}] missing signal_id")
                    continue
                if not isinstance(signal_id, str):
                    self.add_error(path, f"extracted_signals[{index}].signal_id must be a string")
                    continue
                if signal_id in ids:
                    self.add_error(path, f"duplicate extraction signal_id: {signal_id}")
                ids.add(signal_id)
        return ids

    def collect_measurement_term_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "glossary_id" not in doc:
                continue
            terms = doc.get("terms")
            if not isinstance(terms, list):
                continue
            for index, term in enumerate(terms):
                if not isinstance(term, dict):
                    self.add_error(path, f"terms[{index}] must be an object")
                    continue
                term_id = term.get("term_id")
                if not isinstance(term_id, str) or not term_id:
                    self.add_error(path, f"terms[{index}] missing term_id")
                    continue
                if term_id in ids:
                    self.add_error(path, f"duplicate measurement term_id: {term_id}")
                ids.add(term_id)
        return ids

    def collect_claim_set_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "claim_set_id" not in doc:
                continue
            claim_set_id = doc.get("claim_set_id")
            if not isinstance(claim_set_id, str) or not claim_set_id:
                self.add_error(path, "claim_set_id must be a non-empty string")
                continue
            if claim_set_id in ids:
                self.add_error(path, f"duplicate claim_set_id: {claim_set_id}")
            ids.add(claim_set_id)
        return ids

    def collect_claim_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if "schemas" in path.parts or "examples" in path.parts:
                continue
            if not isinstance(doc, dict):
                continue
            if "claim_set_id" in doc:
                claims = doc.get("claims")
                if not isinstance(claims, list):
                    continue
                for index, claim in enumerate(claims):
                    if not isinstance(claim, dict):
                        self.add_error(path, f"claims[{index}] must be an object")
                        continue
                    claim_id = claim.get("claim_id")
                    if not isinstance(claim_id, str) or not claim_id:
                        self.add_error(path, f"claims[{index}] missing claim_id")
                        continue
                    if claim_id in ids:
                        self.add_error(path, f"duplicate claim_id: {claim_id}")
                    ids.add(claim_id)
            elif {"claim_id", "claim_text"}.issubset(doc):
                claim_id = doc.get("claim_id")
                if not isinstance(claim_id, str) or not claim_id:
                    self.add_error(path, "claim_id must be a non-empty string")
                    continue
                if claim_id in ids:
                    self.add_error(path, f"duplicate claim_id: {claim_id}")
                ids.add(claim_id)
        return ids

    def collect_gap_register_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "gap_register_id" not in doc:
                continue
            register_id = doc.get("gap_register_id")
            if not isinstance(register_id, str) or not register_id:
                self.add_error(path, "gap_register_id must be a non-empty string")
                continue
            if register_id in ids:
                self.add_error(path, f"duplicate gap_register_id: {register_id}")
            ids.add(register_id)
        return ids

    def collect_gap_ids(self) -> set[str]:
        ids: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "gap_register_id" not in doc:
                continue
            gaps = doc.get("gaps")
            if not isinstance(gaps, list):
                continue
            for index, gap in enumerate(gaps):
                if not isinstance(gap, dict):
                    self.add_error(path, f"gaps[{index}] must be an object")
                    continue
                gap_id = gap.get("gap_id")
                if not isinstance(gap_id, str) or not gap_id:
                    self.add_error(path, f"gaps[{index}] missing gap_id")
                    continue
                if gap_id in ids:
                    self.add_error(path, f"duplicate gap_id: {gap_id}")
                ids.add(gap_id)
        return ids

    def validate_claim_sets(self) -> None:
        schema_path = self.root / "schemas" / "claim-set.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "claim_set_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            self.validate_claim_set_claim_ids(path, doc)

    def validate_claim_set_claim_ids(self, path: Path, doc: dict[str, Any]) -> None:
        claims = doc.get("claims")
        if not isinstance(claims, list):
            return

        seen_ids: set[str] = set()
        for index, claim in enumerate(claims):
            if not isinstance(claim, dict):
                continue
            claim_id = claim.get("claim_id")
            if not isinstance(claim_id, str):
                continue
            if claim_id in seen_ids:
                self.add_error(path, f"claims[{index}] duplicate claim_id: {claim_id}")
            seen_ids.add(claim_id)

    def validate_artifact_catalogs(self, metadata_by_id: dict[str, tuple[Path, dict[str, Any]]]) -> None:
        schema_path = self.root / "schemas" / "artifact-catalog.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        seen_catalogs: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "catalog_id" not in doc:
                continue

            self.validate_against_schema(path, doc, schema)
            catalog_id = doc.get("catalog_id")
            if isinstance(catalog_id, str):
                if catalog_id in seen_catalogs:
                    self.add_error(path, f"duplicate catalog_id: {catalog_id}")
                seen_catalogs.add(catalog_id)

            entries = doc.get("entries")
            if not isinstance(entries, list):
                continue

            entry_ids: set[str] = set()
            for index, entry in enumerate(entries):
                if not isinstance(entry, dict):
                    continue
                artifact_id = entry.get("artifact_id")
                if not isinstance(artifact_id, str) or not artifact_id:
                    continue
                if artifact_id in entry_ids:
                    self.add_error(path, f"entries[{index}] duplicate artifact_id: {artifact_id}")
                entry_ids.add(artifact_id)

                metadata_record = metadata_by_id.get(artifact_id)
                if metadata_record is None:
                    self.add_error(path, f"entries[{index}] references unknown artifact_id: {artifact_id}")
                    continue
                self.validate_artifact_catalog_entry(path, index, entry, metadata_record)

            if doc.get("generated_from") == "*.metadata.json files tracked in the public repo":
                missing = sorted(set(metadata_by_id) - entry_ids)
                for artifact_id in missing:
                    self.add_error(path, f"catalog missing artifact_id from metadata: {artifact_id}")

    def validate_artifact_catalog_entry(
        self,
        path: Path,
        index: int,
        entry: dict[str, Any],
        metadata_record: tuple[Path, dict[str, Any]],
    ) -> None:
        metadata_path, metadata = metadata_record
        metadata_rel = self.rel(metadata_path).as_posix()
        expected = {
            "title": metadata.get("title"),
            "artifact_class": metadata.get("artifact_class"),
            "claim_level": metadata.get("claim_level"),
            "metadata_path": metadata_rel,
            "source_count": len(metadata.get("sources", [])) if isinstance(metadata.get("sources"), list) else 0,
            "limitation_count": (
                len(metadata.get("limitations", [])) if isinstance(metadata.get("limitations"), list) else 0
            ),
        }
        if isinstance(metadata.get("blood_cancer_scope"), list):
            expected["blood_cancer_scope"] = metadata.get("blood_cancer_scope")

        for key, expected_value in expected.items():
            if entry.get(key) != expected_value:
                self.add_error(
                    path,
                    f"entries[{index}].{key} is {entry.get(key)!r}, expected {expected_value!r}",
                )

        for key in ("path", "metadata_path"):
            value = entry.get(key)
            if isinstance(value, str) and not (self.root / value).exists():
                self.add_error(path, f"entries[{index}].{key} does not exist: {value}")

    def validate_evidence_gap_registers(self) -> None:
        schema_path = self.root / "schemas" / "evidence-gap-register.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        seen_registers: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "gap_register_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            register_id = doc.get("gap_register_id")
            if isinstance(register_id, str):
                if register_id in seen_registers:
                    self.add_error(path, f"duplicate gap_register_id: {register_id}")
                seen_registers.add(register_id)
            self.validate_gap_ids(path, doc)

    def validate_gap_ids(self, path: Path, doc: dict[str, Any]) -> None:
        gaps = doc.get("gaps")
        if not isinstance(gaps, list):
            return

        seen_ids: set[str] = set()
        for index, gap in enumerate(gaps):
            if not isinstance(gap, dict):
                continue
            gap_id = gap.get("gap_id")
            if not isinstance(gap_id, str):
                continue
            if gap_id in seen_ids:
                self.add_error(path, f"gaps[{index}] duplicate gap_id: {gap_id}")
            seen_ids.add(gap_id)

    def validate_public_task_queues(self) -> None:
        schema_path = self.root / "schemas" / "public-task-queue.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        seen_queues: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "task_queue_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            queue_id = doc.get("task_queue_id")
            if isinstance(queue_id, str):
                if queue_id in seen_queues:
                    self.add_error(path, f"duplicate task_queue_id: {queue_id}")
                seen_queues.add(queue_id)
            self.validate_public_task_ids(path, doc)

    def validate_public_task_ids(self, path: Path, doc: dict[str, Any]) -> None:
        tasks = doc.get("tasks")
        if not isinstance(tasks, list):
            return

        seen_ids: set[str] = set()
        seen_issue_urls: set[str] = set()
        for index, task in enumerate(tasks):
            if not isinstance(task, dict):
                continue
            task_id = task.get("task_id")
            if not isinstance(task_id, str):
                continue
            if task_id in seen_ids:
                self.add_error(path, f"tasks[{index}] duplicate task_id: {task_id}")
            seen_ids.add(task_id)

            issue_draft_path = task.get("issue_draft_path")
            if isinstance(issue_draft_path, str) and not (self.root / issue_draft_path).exists():
                self.add_error(path, f"tasks[{index}].issue_draft_path does not exist: {issue_draft_path}")

            issue_url = task.get("github_issue_url")
            if isinstance(issue_url, str):
                if issue_url in seen_issue_urls:
                    self.add_error(path, f"tasks[{index}] duplicate github_issue_url: {issue_url}")
                seen_issue_urls.add(issue_url)

    def validate_expert_review_packets(self) -> None:
        schema_path = self.root / "schemas" / "expert-review-packet.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        seen_packets: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "review_packet_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            packet_id = doc.get("review_packet_id")
            if isinstance(packet_id, str):
                if packet_id in seen_packets:
                    self.add_error(path, f"duplicate review_packet_id: {packet_id}")
                seen_packets.add(packet_id)
            self.validate_expert_review_packet_items(path, doc)

    def validate_expert_review_packet_items(self, path: Path, doc: dict[str, Any]) -> None:
        status_boundary = " ".join(
            item for item in doc.get("review_status_boundary", []) if isinstance(item, str)
        ).lower()
        if "source-checked" not in status_boundary or "expert-reviewed" not in status_boundary:
            self.add_error(path, "review_status_boundary must separate source-checked from expert-reviewed status")

        completion_gate = " ".join(item for item in doc.get("completion_gate", []) if isinstance(item, str)).lower()
        if "qualified" not in completion_gate or "reviewer" not in completion_gate:
            self.add_error(path, "completion_gate must require qualified reviewer completion")

        review = doc.get("review")
        review_status = review.get("review_status") if isinstance(review, dict) else None
        items = doc.get("review_items")
        if not isinstance(items, list):
            return

        seen_items: set[str] = set()
        has_needs_expert_review = False
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                continue

            item_id = item.get("review_item_id")
            if isinstance(item_id, str):
                if item_id in seen_items:
                    self.add_error(path, f"review_items[{index}] duplicate review_item_id: {item_id}")
                seen_items.add(item_id)

            if item.get("current_public_status") == "expert-review-needed":
                has_needs_expert_review = True

            for key in ("linked_claim_ids", "linked_gap_ids", "source_ids"):
                values = item.get(key)
                if not isinstance(values, list) or not values:
                    self.add_error(path, f"review_items[{index}].{key} must map to at least one ID")

            safety_boundary = " ".join(
                value for value in item.get("safety_boundary", []) if isinstance(value, str)
            ).lower()
            if "not" not in safety_boundary or "recommendation" not in safety_boundary:
                self.add_error(path, f"review_items[{index}].safety_boundary must preserve no-recommendation language")

        if has_needs_expert_review and review_status == "expert-reviewed":
            self.add_error(path, "packet cannot be expert-reviewed while review items still need expert review")

    def validate_evidence_claims(self) -> None:
        schema_path = self.root / "schemas" / "evidence-claim.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            self.add_error(schema_path, "missing evidence claim schema")
            return
        for path, doc in self.json_docs.items():
            if self.rel(path).as_posix() in SKIP_SCHEMA_VALIDATION:
                continue
            if isinstance(doc, dict) and {"claim_id", "claim_text"}.issubset(doc):
                self.validate_against_schema(path, doc, schema)

    def validate_mechanism_extractions(self) -> None:
        schema_path = self.root / "schemas" / "mechanism-extraction.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        for path, doc in self.json_docs.items():
            if self.rel(path).as_posix() in SKIP_SCHEMA_VALIDATION:
                continue
            if not isinstance(doc, dict) or "extraction_record_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            self.validate_extraction_signal_ids(path, doc)
            self.validate_denominator_contexts(path, doc)
            self.validate_translation_safety_contexts(path, doc)

    def validate_extraction_signal_ids(self, path: Path, doc: dict[str, Any]) -> None:
        signals = doc.get("extracted_signals")
        if not isinstance(signals, list):
            return

        seen_ids: set[str] = set()
        for index, signal in enumerate(signals):
            if not isinstance(signal, dict):
                continue
            signal_id = signal.get("signal_id")
            if not isinstance(signal_id, str):
                continue
            if signal_id in seen_ids:
                self.add_error(path, f"extracted_signals[{index}] duplicate signal_id: {signal_id}")
            seen_ids.add(signal_id)

    def validate_denominator_contexts(self, path: Path, doc: dict[str, Any]) -> None:
        signals = doc.get("extracted_signals")
        if not isinstance(signals, list):
            return

        required_when_count_only = [
            "denominator_basis",
            "cohort_context",
            "product_or_class_context",
            "prior_bcma_exposure_context",
            "assay_method",
            "specimen_source",
            "target_assay_timing",
            "relapse_or_response_state",
            "frequency_claim_boundary",
        ]
        for index, signal in enumerate(signals):
            if not isinstance(signal, dict):
                continue
            context = signal.get("denominator_context")
            if context is None:
                continue
            if not isinstance(context, dict):
                self.add_error(path, f"extracted_signals[{index}].denominator_context must be an object")
                continue

            denominator = context.get("population_denominator")
            numerator = context.get("numerator_observed")
            if isinstance(denominator, int) and denominator < 0:
                self.add_error(path, f"extracted_signals[{index}].population_denominator must be >= 0")
            if isinstance(numerator, int) and numerator < 0:
                self.add_error(path, f"extracted_signals[{index}].numerator_observed must be >= 0")
            if isinstance(denominator, int) and isinstance(numerator, int) and numerator > denominator:
                self.add_error(path, f"extracted_signals[{index}].numerator_observed exceeds denominator")

            if context.get("frequency_claim_support") == "source-cohort-count-only":
                for key in required_when_count_only:
                    value = context.get(key)
                    if not isinstance(value, str) or not value.strip():
                        self.add_error(path, f"extracted_signals[{index}].denominator_context.{key} must be non-empty")

    def validate_translation_safety_contexts(self, path: Path, doc: dict[str, Any]) -> None:
        signals = doc.get("extracted_signals")
        if not isinstance(signals, list):
            return

        required_text_fields = [
            "tumor_target_context",
            "normal_tissue_context",
            "model_context",
            "clinical_translation_status",
            "trial_registry_context",
            "efficacy_claim_boundary",
            "safety_claim_boundary",
        ]
        for index, signal in enumerate(signals):
            if not isinstance(signal, dict):
                continue
            context = signal.get("translation_safety_context")
            if context is None:
                continue
            if not isinstance(context, dict):
                self.add_error(path, f"extracted_signals[{index}].translation_safety_context must be an object")
                continue

            for key in required_text_fields:
                value = context.get(key)
                if not isinstance(value, str) or not value.strip():
                    self.add_error(
                        path,
                        f"extracted_signals[{index}].translation_safety_context.{key} must be non-empty",
                    )

            evidence_domain = context.get("evidence_domain")
            efficacy_boundary = str(context.get("efficacy_claim_boundary", "")).lower()
            safety_boundary = str(context.get("safety_claim_boundary", "")).lower()
            registry_context = str(context.get("trial_registry_context", "")).lower()

            if evidence_domain == "preclinical-activity":
                has_preclinical_boundary = "not" in efficacy_boundary and (
                    "clinical" in efficacy_boundary or "patient" in efficacy_boundary
                )
                if not has_preclinical_boundary:
                    self.add_error(
                        path,
                        f"extracted_signals[{index}].translation_safety_context.efficacy_claim_boundary must separate preclinical activity from clinical or patient benefit",
                    )

            if evidence_domain == "normal-tissue-safety":
                has_safety_boundary = "not" in safety_boundary and ("clinical safety" in safety_boundary or "safety" in safety_boundary)
                if not has_safety_boundary:
                    self.add_error(
                        path,
                        f"extracted_signals[{index}].translation_safety_context.safety_claim_boundary must state that safety context does not establish clinical safety",
                    )

            if "trial" in registry_context and "registry" in registry_context:
                has_registry_boundary = (
                    "no registry" in registry_context
                    or "registry id" in registry_context
                    or "protocol" in registry_context
                    or "not captured" in registry_context
                )
                if not has_registry_boundary:
                    self.add_error(
                        path,
                        f"extracted_signals[{index}].translation_safety_context.trial_registry_context must preserve registry or protocol status",
                    )

    def validate_measurement_context_audits(self) -> None:
        schema_path = self.root / "schemas" / "measurement-context-audit.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        seen_audits: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "audit_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            audit_id = doc.get("audit_id")
            if isinstance(audit_id, str):
                if audit_id in seen_audits:
                    self.add_error(path, f"duplicate audit_id: {audit_id}")
                seen_audits.add(audit_id)
            self.validate_measurement_context_audit_records(path, doc)

    def validate_measurement_context_audit_records(self, path: Path, doc: dict[str, Any]) -> None:
        required_fields = doc.get("required_fields")
        if isinstance(required_fields, list):
            seen_fields: set[str] = set()
            for index, field in enumerate(required_fields):
                if not isinstance(field, dict):
                    continue
                field_id = field.get("field_id")
                if not isinstance(field_id, str):
                    continue
                if field_id in seen_fields:
                    self.add_error(path, f"required_fields[{index}] duplicate field_id: {field_id}")
                seen_fields.add(field_id)

        records = doc.get("records")
        if not isinstance(records, list):
            return

        seen_records: set[str] = set()
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                continue
            record_id = record.get("audit_record_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"records[{index}] duplicate audit_record_id: {record_id}")
                seen_records.add(record_id)
            record_path = record.get("record_path")
            if isinstance(record_path, str) and not (self.root / record_path).exists():
                self.add_error(path, f"records[{index}].record_path does not exist: {record_path}")

            field_status = record.get("field_status")
            notes = record.get("missing_context_notes")
            if isinstance(field_status, dict) and isinstance(notes, list):
                has_gap = any(value in {"missing", "partially-captured"} for value in field_status.values())
                if has_gap and not notes:
                    self.add_error(path, f"records[{index}] has missing or partial fields without notes")

    def validate_measurement_glossaries(self) -> None:
        schema_path = self.root / "schemas" / "measurement-glossary.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        seen_glossaries: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "glossary_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            glossary_id = doc.get("glossary_id")
            if isinstance(glossary_id, str):
                if glossary_id in seen_glossaries:
                    self.add_error(path, f"duplicate glossary_id: {glossary_id}")
                seen_glossaries.add(glossary_id)
            self.validate_measurement_term_ids(path, doc)

    def validate_measurement_term_ids(self, path: Path, doc: dict[str, Any]) -> None:
        terms = doc.get("terms")
        if not isinstance(terms, list):
            return

        seen_ids: set[str] = set()
        for index, term in enumerate(terms):
            if not isinstance(term, dict):
                continue
            term_id = term.get("term_id")
            if not isinstance(term_id, str):
                continue
            if term_id in seen_ids:
                self.add_error(path, f"terms[{index}] duplicate term_id: {term_id}")
            seen_ids.add(term_id)

        for index, term in enumerate(terms):
            if not isinstance(term, dict):
                continue
            related = term.get("related_term_ids")
            if not isinstance(related, list):
                continue
            for value in related:
                if isinstance(value, str) and value not in seen_ids:
                    self.add_error(path, f"terms[{index}].related_term_ids references unknown term_id: {value}")

    def validate_mechanism_maps(self) -> None:
        schema_path = self.root / "schemas" / "mechanism-map.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or not {"map_id", "mechanism_groups"}.issubset(doc):
                continue
            self.validate_against_schema(path, doc, schema)
            self.validate_mechanism_group_ids(path, doc)

    def validate_mechanism_group_ids(self, path: Path, doc: dict[str, Any]) -> None:
        mechanism_groups = doc.get("mechanism_groups")
        if not isinstance(mechanism_groups, list):
            return

        seen_ids: set[str] = set()
        for index, group in enumerate(mechanism_groups):
            if not isinstance(group, dict):
                continue
            mechanism_id = group.get("mechanism_id")
            if not isinstance(mechanism_id, str):
                continue
            if mechanism_id in seen_ids:
                self.add_error(path, f"mechanism_groups[{index}] duplicate mechanism_id: {mechanism_id}")
            seen_ids.add(mechanism_id)

    def validate_mechanism_coverage_reports(self) -> None:
        schema_path = self.root / "schemas" / "mechanism-coverage-report.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        seen_reports: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "coverage_report_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            report_id = doc.get("coverage_report_id")
            if isinstance(report_id, str):
                if report_id in seen_reports:
                    self.add_error(path, f"duplicate coverage_report_id: {report_id}")
                seen_reports.add(report_id)
            self.validate_mechanism_coverage_rows(path, doc)

    def validate_mechanism_coverage_rows(self, path: Path, doc: dict[str, Any]) -> None:
        boundary = " ".join(item for item in doc.get("interpretation_boundary", []) if isinstance(item, str)).lower()
        if "biological" not in boundary or "not" not in boundary:
            self.add_error(path, "interpretation_boundary must state that coverage counts are not biological rankings")

        rows = doc.get("mechanism_coverage")
        if not isinstance(rows, list):
            return

        seen_mechanisms: set[str] = set()
        for index, row in enumerate(rows):
            if not isinstance(row, dict):
                continue

            mechanism_id = row.get("mechanism_group_id")
            if isinstance(mechanism_id, str):
                if mechanism_id in seen_mechanisms:
                    self.add_error(path, f"mechanism_coverage[{index}] duplicate mechanism_group_id: {mechanism_id}")
                seen_mechanisms.add(mechanism_id)

            signal_ids = row.get("extraction_signal_ids")
            if isinstance(signal_ids, list) and isinstance(row.get("signal_count"), int):
                if row["signal_count"] != len(set(signal_ids)):
                    self.add_error(path, f"mechanism_coverage[{index}].signal_count does not match extraction_signal_ids")

            record_ids = row.get("extraction_record_ids")
            if isinstance(record_ids, list) and isinstance(row.get("extraction_record_count"), int):
                if row["extraction_record_count"] != len(set(record_ids)):
                    self.add_error(path, f"mechanism_coverage[{index}].extraction_record_count does not match extraction_record_ids")

            covered_source_ids = row.get("covered_source_ids")
            if isinstance(covered_source_ids, list) and isinstance(row.get("covered_source_count"), int):
                if row["covered_source_count"] != len(set(covered_source_ids)):
                    self.add_error(path, f"mechanism_coverage[{index}].covered_source_count does not match covered_source_ids")

            status = row.get("coverage_status")
            under_flag = row.get("under_coverage_flag")
            if status in {"needs-first-extraction", "needs-second-source-extraction"} and under_flag is not True:
                self.add_error(path, f"mechanism_coverage[{index}] needs status must set under_coverage_flag true")
            if status == "covered-for-v0-navigation" and under_flag is not False:
                self.add_error(path, f"mechanism_coverage[{index}] covered status must set under_coverage_flag false")

    def validate_opportunity_maps(self) -> None:
        schema_path = self.root / "schemas" / "opportunity-map.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or not {"map_id", "opportunities"}.issubset(doc):
                continue
            self.validate_against_schema(path, doc, schema)
            self.validate_opportunity_scores(path, doc)

    def validate_opportunity_scores(self, path: Path, doc: dict[str, Any]) -> None:
        opportunities = doc.get("opportunities")
        if not isinstance(opportunities, list):
            return

        seen_ids: set[str] = set()
        seen_ranks: set[int] = set()
        for index, opportunity in enumerate(opportunities):
            if not isinstance(opportunity, dict):
                continue

            opportunity_id = opportunity.get("opportunity_id")
            if isinstance(opportunity_id, str):
                if opportunity_id in seen_ids:
                    self.add_error(path, f"opportunities[{index}] duplicate opportunity_id: {opportunity_id}")
                seen_ids.add(opportunity_id)

            rank = opportunity.get("rank")
            if isinstance(rank, int):
                if rank <= 0:
                    self.add_error(path, f"opportunities[{index}].rank must be positive")
                if rank in seen_ranks:
                    self.add_error(path, f"opportunities[{index}] duplicate rank: {rank}")
                seen_ranks.add(rank)

            scores = opportunity.get("scores")
            score_total = opportunity.get("score_total")
            if not isinstance(scores, dict):
                continue
            calculated = 0
            for key, value in scores.items():
                if not isinstance(value, int):
                    continue
                if value < 0 or value > 5:
                    self.add_error(path, f"opportunities[{index}].scores.{key} must be between 0 and 5")
                calculated += value
            if isinstance(score_total, int) and score_total != calculated:
                self.add_error(
                    path,
                    f"opportunities[{index}].score_total is {score_total}, expected {calculated}",
                )

    def validate_disease_maps(self) -> None:
        schema_path = self.root / "schemas" / "disease-map.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        forbidden_keys = {
            "patient_id",
            "case_id",
            "date_of_birth",
            "medical_record_number",
            "raw_record",
            "free_text_note",
            "candidate_option",
            "candidate_options",
            "candidate_option_ids",
        }
        required_boundaries = {
            "not-medical-advice",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        seen_maps: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "disease_map_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            map_id = doc.get("disease_map_id")
            if isinstance(map_id, str):
                if map_id in seen_maps:
                    self.add_error(path, f"duplicate disease_map_id: {map_id}")
                seen_maps.add(map_id)

            boundaries = doc.get("clinical_use_boundary")
            if isinstance(boundaries, list):
                missing = sorted(required_boundaries - {value for value in boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    self.add_error(path, f"{location} is not allowed in public disease-map records")

    def validate_target_records(self) -> None:
        schema_path = self.root / "schemas" / "target-record.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        forbidden_keys = {
            "actionability_score",
            "candidate_option",
            "candidate_options",
            "candidate_option_ids",
            "case_id",
            "date_of_birth",
            "free_text_note",
            "medical_record_number",
            "patient_id",
            "patient_target_expression",
            "raw_record",
            "real_case_data",
            "treatment_choice",
            "trial_match",
            "trial_matching",
        }
        required_boundaries = {
            "not-medical-advice",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        seen_records: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "target_record_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            record_id = doc.get("target_record_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"duplicate target_record_id: {record_id}")
                seen_records.add(record_id)

            boundaries = doc.get("clinical_use_boundary")
            if isinstance(boundaries, list):
                missing = sorted(required_boundaries - {value for value in boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    self.add_error(path, f"{location} is not allowed in public target-record records")

    def validate_therapy_records(self) -> None:
        schema_path = self.root / "schemas" / "therapy-record.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        forbidden_keys = {
            "actionability_score",
            "availability_for_patient",
            "candidate_option",
            "candidate_options",
            "candidate_option_ids",
            "case_id",
            "date_of_birth",
            "dose",
            "dosing",
            "eligibility",
            "expanded_access_guidance",
            "free_text_note",
            "medical_record_number",
            "option_rank",
            "patient_id",
            "raw_record",
            "real_case_data",
            "treatment_choice",
            "treatment_recommendation",
            "trial_match",
            "trial_matching",
        }
        required_boundaries = {
            "not-medical-advice",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        seen_records: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "therapy_record_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            record_id = doc.get("therapy_record_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"duplicate therapy_record_id: {record_id}")
                seen_records.add(record_id)

            boundaries = doc.get("clinical_use_boundary")
            if isinstance(boundaries, list):
                missing = sorted(required_boundaries - {value for value in boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    self.add_error(path, f"{location} is not allowed in public therapy-record records")

    def validate_trial_landscape_records(self, known_source_ids: set[str]) -> None:
        schema_path = self.root / "schemas" / "trial-landscape-record.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        forbidden_keys = {
            "actionability_score",
            "availability_for_patient",
            "candidate_option",
            "candidate_options",
            "candidate_option_ids",
            "case_id",
            "date_of_birth",
            "dose",
            "dosing",
            "eligibility",
            "eligibility_guidance",
            "enrollment_advice",
            "enrollment_guidance",
            "expanded_access_guidance",
            "free_text_note",
            "medical_record_number",
            "option_rank",
            "patient_fit",
            "patient_id",
            "raw_record",
            "real_case_data",
            "sponsor_access",
            "sponsor_access_instruction",
            "sponsor_access_instructions",
            "treatment_choice",
            "treatment_recommendation",
            "trial_match",
            "trial_matching",
            "trial_recommendation",
        }
        required_boundaries = {
            "not-medical-advice",
            "not-diagnostic",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        seen_records: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "trial_landscape_record_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            record_id = doc.get("trial_landscape_record_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"duplicate trial_landscape_record_id: {record_id}")
                seen_records.add(record_id)

            boundaries = doc.get("clinical_use_boundary")
            if isinstance(boundaries, list):
                missing = sorted(required_boundaries - {value for value in boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")

            source_values = doc.get("source_ids")
            source_set = {value for value in source_values if isinstance(value, str)} if isinstance(source_values, list) else set()
            provenance = doc.get("registry_provenance")
            if isinstance(provenance, dict):
                registry_source_ids = provenance.get("registry_source_ids")
                if isinstance(registry_source_ids, list):
                    for index, value in enumerate(registry_source_ids):
                        if not isinstance(value, str):
                            continue
                        if value not in known_source_ids:
                            self.add_error(
                                path,
                                f"registry_provenance.registry_source_ids[{index}] references unknown source_id: {value}",
                            )
                        if value not in source_set:
                            self.add_error(
                                path,
                                f"registry_provenance.registry_source_ids[{index}] must also appear in source_ids: {value}",
                            )

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    self.add_error(path, f"{location} is not allowed in public trial-landscape records")

    def validate_open_question_records(self) -> None:
        schema_path = self.root / "schemas" / "open-question-record.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        forbidden_keys = {
            "actionability",
            "actionability_score",
            "availability_for_patient",
            "candidate_option",
            "candidate_options",
            "candidate_option_ids",
            "case_id",
            "clinical_importance",
            "clinical_priority",
            "clinical_priority_score",
            "date_of_birth",
            "evidence_rank",
            "evidence_strength",
            "evidence_strength_score",
            "expanded_access_guidance",
            "free_text_note",
            "medical_record_number",
            "option_rank",
            "patient_id",
            "patient_relevance",
            "raw_record",
            "real_case_data",
            "treatment_choice",
            "treatment_recommendation",
            "trial_choice",
            "trial_match",
            "trial_matching",
            "trial_recommendation",
            "urgency",
            "urgency_score",
        }
        required_boundaries = {
            "not-medical-advice",
            "not-diagnostic",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        seen_records: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "open_question_record_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            record_id = doc.get("open_question_record_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"duplicate open_question_record_id: {record_id}")
                seen_records.add(record_id)

            boundaries = doc.get("clinical_use_boundary")
            if isinstance(boundaries, list):
                missing = sorted(required_boundaries - {value for value in boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    self.add_error(path, f"{location} is not allowed in public open-question records")

    def validate_review_packet_builder_manifest_records(
        self,
        known_source_ids: set[str],
        artifact_metadata: dict[str, tuple[Path, dict[str, Any]]],
    ) -> None:
        schema_path = self.root / "schemas" / "review-packet-builder-manifest.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        forbidden_keys = {
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
        required_boundaries = {
            "not-medical-advice",
            "not-diagnostic",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        required_false_flags = {
            "builder_code_allowed",
            "generated_claims_allowed",
            "patient_specific_outputs_allowed",
            "publication_authorization_allowed",
        }
        seen_records: set[str] = set()
        known_artifact_ids = set(artifact_metadata)

        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "review_packet_builder_manifest_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            record_id = doc.get("review_packet_builder_manifest_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"duplicate review_packet_builder_manifest_id: {record_id}")
                seen_records.add(record_id)

            boundaries = doc.get("clinical_use_boundary")
            if isinstance(boundaries, list):
                missing = sorted(required_boundaries - {value for value in boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")

            builder_boundary = doc.get("builder_code_boundary")
            if isinstance(builder_boundary, dict):
                for flag in sorted(required_false_flags):
                    if builder_boundary.get(flag) is not False:
                        self.add_error(path, f"builder_code_boundary.{flag} must be false")

            source_values = doc.get("source_ids")
            source_set = {value for value in source_values if isinstance(value, str)} if isinstance(source_values, list) else set()
            source_inputs = doc.get("source_inputs")
            if isinstance(source_inputs, dict):
                nested_source_ids = source_inputs.get("source_ids")
                if isinstance(nested_source_ids, list):
                    for index, value in enumerate(nested_source_ids):
                        if not isinstance(value, str):
                            continue
                        if value not in known_source_ids:
                            self.add_error(path, f"source_inputs.source_ids[{index}] references unknown source_id: {value}")
                        if value not in source_set:
                            self.add_error(path, f"source_inputs.source_ids[{index}] must also appear in source_ids: {value}")

            target_packet = doc.get("target_packet")
            if isinstance(target_packet, dict):
                artifact_id = target_packet.get("artifact_id")
                if isinstance(artifact_id, str) and artifact_id not in known_artifact_ids:
                    self.add_error(path, f"target_packet.artifact_id references unknown artifact_id: {artifact_id}")
                packet_path = target_packet.get("path")
                if isinstance(packet_path, str) and not (self.root / packet_path).exists():
                    self.add_error(path, f"target_packet.path does not exist: {packet_path}")

            artifact_inputs = doc.get("artifact_inputs")
            if isinstance(artifact_inputs, list):
                for index, artifact_input in enumerate(artifact_inputs):
                    if not isinstance(artifact_input, dict):
                        continue
                    artifact_id = artifact_input.get("artifact_id")
                    if isinstance(artifact_id, str):
                        metadata_record = artifact_metadata.get(artifact_id)
                        if metadata_record is None:
                            self.add_error(path, f"artifact_inputs[{index}].artifact_id references unknown artifact_id: {artifact_id}")
                        else:
                            metadata_path, metadata = metadata_record
                            expected_metadata_path = self.rel(metadata_path).as_posix()
                            if artifact_input.get("metadata_path") != expected_metadata_path:
                                self.add_error(
                                    path,
                                    f"artifact_inputs[{index}].metadata_path is {artifact_input.get('metadata_path')!r}, expected {expected_metadata_path!r}",
                                )
                            if artifact_input.get("artifact_class") != metadata.get("artifact_class"):
                                self.add_error(
                                    path,
                                    f"artifact_inputs[{index}].artifact_class is {artifact_input.get('artifact_class')!r}, expected {metadata.get('artifact_class')!r}",
                                )
                            if artifact_input.get("claim_level") != metadata.get("claim_level"):
                                self.add_error(
                                    path,
                                    f"artifact_inputs[{index}].claim_level is {artifact_input.get('claim_level')!r}, expected {metadata.get('claim_level')!r}",
                                )
                    input_path = artifact_input.get("path")
                    if isinstance(input_path, str) and not (self.root / input_path).exists():
                        self.add_error(path, f"artifact_inputs[{index}].path does not exist: {input_path}")
                    input_metadata_path = artifact_input.get("metadata_path")
                    if isinstance(input_metadata_path, str) and not (self.root / input_metadata_path).exists():
                        self.add_error(path, f"artifact_inputs[{index}].metadata_path does not exist: {input_metadata_path}")

            schema_inputs = doc.get("schema_inputs")
            if isinstance(schema_inputs, list):
                for index, schema_input in enumerate(schema_inputs):
                    if not isinstance(schema_input, dict):
                        continue
                    schema_input_path = schema_input.get("schema_path")
                    if isinstance(schema_input_path, str) and not (self.root / schema_input_path).exists():
                        self.add_error(path, f"schema_inputs[{index}].schema_path does not exist: {schema_input_path}")
                    template_path = schema_input.get("template_path")
                    if isinstance(template_path, str) and template_path and not (self.root / template_path).exists():
                        self.add_error(path, f"schema_inputs[{index}].template_path does not exist: {template_path}")

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    self.add_error(path, f"{location} is not allowed in public review-packet builder manifest records")

    def validate_review_packet_route_table_outputs(self) -> None:
        schema_path = self.root / "schemas" / "review-packet-route-table-output.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        forbidden_keys = {
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
            "generated_packet_output",
            "generated_public_explainer",
            "medical_record_number",
            "option_rank",
            "packet_assembly",
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
        required_output_boundaries = {
            "copied-reference routing only",
            "not a review packet",
            "not expert review",
            "not generated biomedical prose",
            "not medical advice",
            "not publication-ready",
        }
        required_clinical_boundaries = {
            "not-medical-advice",
            "not-diagnostic",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        seen_records: set[str] = set()

        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "route_table_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            record_id = doc.get("route_table_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"duplicate route_table_id: {record_id}")
                seen_records.add(record_id)

            if doc.get("tool") != "tools/review_packet_manifest_route_table.py":
                self.add_error(path, "tool must be tools/review_packet_manifest_route_table.py")

            output_boundaries = doc.get("output_boundary")
            if isinstance(output_boundaries, list):
                missing = sorted(required_output_boundaries - {value for value in output_boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"output_boundary missing required values: {', '.join(missing)}")

            status = doc.get("route_table_status")
            routes = doc.get("copied_reference_routes")
            refusals = doc.get("refusal_records")
            if status == "refused":
                if isinstance(routes, list) and routes:
                    self.add_error(path, "refused route-table outputs must not contain copied_reference_routes")
            elif status in {"route-table-ready", "route-table-ready-with-missing-inputs"}:
                if isinstance(routes, list) and not routes:
                    self.add_error(path, "ready route-table outputs must contain copied_reference_routes")
                if isinstance(refusals, list) and refusals:
                    self.add_error(path, "ready route-table outputs must not contain refusal_records")
                clinical_boundaries = doc.get("clinical_use_boundary")
                if isinstance(clinical_boundaries, list):
                    missing = sorted(
                        required_clinical_boundaries - {value for value in clinical_boundaries if isinstance(value, str)}
                    )
                    if missing:
                        self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")
                else:
                    self.add_error(path, "ready route-table outputs must include clinical_use_boundary")

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    self.add_error(path, f"{location} is not allowed in public route-table output records")

    def validate_measurement_refusal_outputs(self) -> None:
        schema_path = self.root / "schemas" / "measurement-refusal-output.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        forbidden_keys = {
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
        required_clinical_boundaries = {
            "not-medical-advice",
            "not-diagnostic",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        required_blocked_uses = {
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
        required_false_boundary_fields = {
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
        seen_records: set[str] = set()

        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "measurement_refusal_output_set_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            record_id = doc.get("measurement_refusal_output_set_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"duplicate measurement_refusal_output_set_id: {record_id}")
                seen_records.add(record_id)

            clinical_boundaries = doc.get("clinical_use_boundary")
            if isinstance(clinical_boundaries, list):
                missing = sorted(required_clinical_boundaries - {value for value in clinical_boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")
            else:
                self.add_error(path, "measurement-refusal output must include clinical_use_boundary")

            data_boundary = doc.get("data_boundary")
            if isinstance(data_boundary, dict):
                missing_false = sorted(field for field in required_false_boundary_fields if data_boundary.get(field) is not False)
                if missing_false:
                    self.add_error(path, f"data_boundary fields must be false: {', '.join(missing_false)}")
            else:
                self.add_error(path, "measurement-refusal output must include data_boundary")

            shared_blocks = doc.get("shared_blocked_downstream_uses")
            if isinstance(shared_blocks, list):
                missing_blocks = sorted(required_blocked_uses - {value for value in shared_blocks if isinstance(value, str)})
                if missing_blocks:
                    self.add_error(path, f"shared_blocked_downstream_uses missing required values: {', '.join(missing_blocks)}")

            outputs = doc.get("outputs")
            if isinstance(outputs, list):
                for index, output in enumerate(outputs):
                    if not isinstance(output, dict):
                        continue
                    if output.get("output_status") != "refused":
                        self.add_error(path, f"outputs[{index}].output_status must be refused")
                    if output.get("wrapper_state") != "assay_specimen_quality_needed":
                        self.add_error(path, f"outputs[{index}].wrapper_state must be assay_specimen_quality_needed")
                    if output.get("clinical_output_allowed") is not False:
                        self.add_error(path, f"outputs[{index}].clinical_output_allowed must be false")
                    if output.get("comparison_allowed") is not False:
                        self.add_error(path, f"outputs[{index}].comparison_allowed must be false")
                    if output.get("no_interpretive_text") is not True:
                        self.add_error(path, f"outputs[{index}].no_interpretive_text must be true")
                    output_blocks = output.get("blocked_downstream_uses")
                    if isinstance(output_blocks, list):
                        missing_blocks = sorted(required_blocked_uses - {value for value in output_blocks if isinstance(value, str)})
                        if missing_blocks:
                            self.add_error(
                                path,
                                f"outputs[{index}].blocked_downstream_uses missing required values: {', '.join(missing_blocks)}",
                            )

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    if location.startswith("$.forbidden_output_fields"):
                        continue
                    self.add_error(path, f"{location} is not allowed in public measurement-refusal output records")

    def validate_measurement_refusal_route_tables(self) -> None:
        forbidden_keys = {
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
        required_false_boundary_fields = {
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
        required_clinical_boundaries = {
            "not-medical-advice",
            "not-diagnostic",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        required_blocked_routes = {
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
        allowed_route_families = {
            "structural_validator_input",
            "model_output_boundary_refusal_surface",
            "public_navigation_index",
            "synthetic_regression_fixture",
            "private_review_blocker_notice",
        }
        seen_records: set[str] = set()

        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "measurement_refusal_route_table_id" not in doc:
                continue

            record_id = doc.get("measurement_refusal_route_table_id")
            if isinstance(record_id, str):
                if record_id in seen_records:
                    self.add_error(path, f"duplicate measurement_refusal_route_table_id: {record_id}")
                seen_records.add(record_id)

            clinical_boundaries = doc.get("clinical_use_boundary")
            if isinstance(clinical_boundaries, list):
                missing = sorted(required_clinical_boundaries - {value for value in clinical_boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")
            else:
                self.add_error(path, "measurement-refusal route table must include clinical_use_boundary")

            data_boundary = doc.get("data_boundary")
            if isinstance(data_boundary, dict):
                missing_false = sorted(field for field in required_false_boundary_fields if data_boundary.get(field) is not False)
                if missing_false:
                    self.add_error(path, f"data_boundary fields must be false: {', '.join(missing_false)}")
            else:
                self.add_error(path, "measurement-refusal route table must include data_boundary")

            allowed = doc.get("allowed_route_families")
            if isinstance(allowed, list):
                unknown = sorted({value for value in allowed if isinstance(value, str)} - allowed_route_families)
                if unknown:
                    self.add_error(path, f"allowed_route_families contains unknown values: {', '.join(unknown)}")

            manifest = doc.get("blocked_route_manifest")
            if isinstance(manifest, list):
                blocked = {
                    row.get("blocked_route")
                    for row in manifest
                    if isinstance(row, dict) and row.get("status") == "blocked" and isinstance(row.get("blocked_route"), str)
                }
                missing_blocks = sorted(required_blocked_routes - blocked)
                if missing_blocks:
                    self.add_error(path, f"blocked_route_manifest missing required values: {', '.join(missing_blocks)}")

            routes = doc.get("route_records")
            if isinstance(routes, list):
                for index, route in enumerate(routes):
                    if not isinstance(route, dict):
                        continue
                    if route.get("clinical_output_allowed") is not False:
                        self.add_error(path, f"route_records[{index}].clinical_output_allowed must be false")
                    if route.get("comparison_allowed") is not False:
                        self.add_error(path, f"route_records[{index}].comparison_allowed must be false")
                    if route.get("no_interpretive_text") is not True:
                        self.add_error(path, f"route_records[{index}].no_interpretive_text must be true")
                    if route.get("route_boundary") != "refusal-metadata-only":
                        self.add_error(path, f"route_records[{index}].route_boundary must be refusal-metadata-only")
                    route_families = route.get("allowed_route_families")
                    if isinstance(route_families, list):
                        unknown = sorted({value for value in route_families if isinstance(value, str)} - allowed_route_families)
                        if unknown:
                            self.add_error(path, f"route_records[{index}].allowed_route_families contains unknown values: {', '.join(unknown)}")
                    blocked_routes = route.get("blocked_routes")
                    if isinstance(blocked_routes, list):
                        missing_blocks = sorted(required_blocked_routes - {value for value in blocked_routes if isinstance(value, str)})
                        if missing_blocks:
                            self.add_error(path, f"route_records[{index}].blocked_routes missing required values: {', '.join(missing_blocks)}")

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    if location.startswith("$.forbidden_route_fields"):
                        continue
                    self.add_error(path, f"{location} is not allowed in public measurement-refusal route-table records")

    def validate_measurement_refusal_validator_reports(self) -> None:
        required_false_boundary_fields = {
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
        required_clinical_boundaries = {
            "not-medical-advice",
            "not-diagnostic",
            "not-treatment-recommendation",
            "not-trial-recommendation",
            "research-use-only",
        }
        required_rule_ids = {
            "mrvs_00_public_synthetic_only",
            "mrvs_01_clinical_boundary_complete",
            "mrvs_02_every_refused_output_has_one_route",
            "mrvs_03_blocked_route_manifest_complete",
            "mrvs_04_destination_contracts_present",
            "mrvs_05_routes_preserve_refusal_metadata_only",
            "mrvs_06_report_emits_no_forbidden_fields",
        }
        required_sources = {
            "examples/measurement-refusal-output-fixture-v0.json",
            "disease-programs/multiple-myeloma/measurements/measurement-refusal-output-route-table-v0.json",
        }
        required_destination_contracts = {
            "measurement-refusal-output-schema-v0",
            "myeloma-state-validator-rule-map-v0",
            "model-output-boundary-wrapper-v0",
        }
        allowed_route_families = {
            "structural_validator_input",
            "model_output_boundary_refusal_surface",
            "public_navigation_index",
            "synthetic_regression_fixture",
            "private_review_blocker_notice",
        }
        allowed_validator_decisions = {
            "accepted_refusal_metadata_only",
            "blocked_private_review_notice_only",
        }
        allowed_route_fields = {
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
        required_blocked_routes = {
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
        forbidden_keys = {
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

        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "measurement_refusal_validator_report_id" not in doc:
                continue

            if doc.get("validator_id") != "measurement-refusal-validator-skeleton-v0":
                self.add_error(path, "validator_id must be measurement-refusal-validator-skeleton-v0")
            if doc.get("report_status") != "pass":
                self.add_error(path, "report_status must be pass for the public synthetic report fixture")
            if doc.get("report_type") != "synthetic-structural-validation-only":
                self.add_error(path, "report_type must be synthetic-structural-validation-only")

            clinical_boundaries = doc.get("clinical_use_boundary")
            if isinstance(clinical_boundaries, list):
                missing = sorted(required_clinical_boundaries - {value for value in clinical_boundaries if isinstance(value, str)})
                if missing:
                    self.add_error(path, f"clinical_use_boundary missing required values: {', '.join(missing)}")
            else:
                self.add_error(path, "validator report must include clinical_use_boundary")

            data_boundary = doc.get("data_boundary")
            if isinstance(data_boundary, dict):
                missing_false = sorted(field for field in required_false_boundary_fields if data_boundary.get(field) is not False)
                if missing_false:
                    self.add_error(path, f"data_boundary fields must be false: {', '.join(missing_false)}")
            else:
                self.add_error(path, "validator report must include data_boundary")

            source_artifacts = doc.get("source_artifacts")
            if isinstance(source_artifacts, list):
                missing_sources = sorted(required_sources - {value for value in source_artifacts if isinstance(value, str)})
                if missing_sources:
                    self.add_error(path, f"source_artifacts missing required values: {', '.join(missing_sources)}")
            else:
                self.add_error(path, "validator report must include source_artifacts")

            contract = doc.get("validation_contract")
            if isinstance(contract, dict):
                if contract.get("allowed_input_state") != "public-synthetic-fixtures-only":
                    self.add_error(path, "validation_contract.allowed_input_state must be public-synthetic-fixtures-only")
                if contract.get("allowed_output_type") != "structural-validation-report":
                    self.add_error(path, "validation_contract.allowed_output_type must be structural-validation-report")
                if contract.get("route_boundary") != "refusal-metadata-only":
                    self.add_error(path, "validation_contract.route_boundary must be refusal-metadata-only")
                contract_fields = contract.get("allowed_emitted_route_fields")
                if isinstance(contract_fields, list):
                    unknown_fields = sorted({value for value in contract_fields if isinstance(value, str)} - allowed_route_fields)
                    missing_fields = sorted(allowed_route_fields - {value for value in contract_fields if isinstance(value, str)})
                    if unknown_fields:
                        self.add_error(path, f"validation_contract.allowed_emitted_route_fields has unknown values: {', '.join(unknown_fields)}")
                    if missing_fields:
                        self.add_error(path, f"validation_contract.allowed_emitted_route_fields missing values: {', '.join(missing_fields)}")
                contracts = contract.get("required_destination_contracts")
                if isinstance(contracts, list):
                    missing_contracts = sorted(required_destination_contracts - {value for value in contracts if isinstance(value, str)})
                    if missing_contracts:
                        self.add_error(path, f"validation_contract.required_destination_contracts missing values: {', '.join(missing_contracts)}")
                route_families = contract.get("allowed_route_families")
                if isinstance(route_families, list):
                    unknown_families = sorted({value for value in route_families if isinstance(value, str)} - allowed_route_families)
                    missing_families = sorted(allowed_route_families - {value for value in route_families if isinstance(value, str)})
                    if unknown_families:
                        self.add_error(path, f"validation_contract.allowed_route_families has unknown values: {', '.join(unknown_families)}")
                    if missing_families:
                        self.add_error(path, f"validation_contract.allowed_route_families missing values: {', '.join(missing_families)}")
            else:
                self.add_error(path, "validator report must include validation_contract")

            summary = doc.get("summary")
            if isinstance(summary, dict):
                if summary.get("clinical_output_allowed") is not False:
                    self.add_error(path, "summary.clinical_output_allowed must be false")
                if summary.get("comparison_allowed") is not False:
                    self.add_error(path, "summary.comparison_allowed must be false")
                if summary.get("no_interpretive_text") is not True:
                    self.add_error(path, "summary.no_interpretive_text must be true")
                if summary.get("blocked_private_review_notice_only_count") != 1:
                    self.add_error(path, "summary.blocked_private_review_notice_only_count must be 1")
            else:
                self.add_error(path, "validator report must include summary")

            rule_results = doc.get("rule_results")
            if isinstance(rule_results, list):
                rule_ids = {row.get("rule_id") for row in rule_results if isinstance(row, dict) and isinstance(row.get("rule_id"), str)}
                missing_rules = sorted(required_rule_ids - rule_ids)
                if missing_rules:
                    self.add_error(path, f"rule_results missing required rule IDs: {', '.join(missing_rules)}")
                for index, row in enumerate(rule_results):
                    if not isinstance(row, dict):
                        continue
                    if row.get("status") != "pass":
                        self.add_error(path, f"rule_results[{index}].status must be pass")
            else:
                self.add_error(path, "validator report must include rule_results")

            route_results = doc.get("route_results")
            if isinstance(route_results, list):
                if isinstance(summary, dict) and summary.get("route_count") != len(route_results):
                    self.add_error(path, "summary.route_count must equal route_results length")
                for index, route in enumerate(route_results):
                    if not isinstance(route, dict):
                        continue
                    unknown_keys = sorted(set(route) - allowed_route_fields)
                    if unknown_keys:
                        self.add_error(path, f"route_results[{index}] has unknown emitted fields: {', '.join(unknown_keys)}")
                    if route.get("clinical_output_allowed") is not False:
                        self.add_error(path, f"route_results[{index}].clinical_output_allowed must be false")
                    if route.get("comparison_allowed") is not False:
                        self.add_error(path, f"route_results[{index}].comparison_allowed must be false")
                    if route.get("no_interpretive_text") is not True:
                        self.add_error(path, f"route_results[{index}].no_interpretive_text must be true")
                    if route.get("route_boundary") != "refusal-metadata-only":
                        self.add_error(path, f"route_results[{index}].route_boundary must be refusal-metadata-only")
                    if route.get("validator_decision") not in allowed_validator_decisions:
                        self.add_error(path, f"route_results[{index}].validator_decision is not allowed")
                    blocked_routes = route.get("blocked_routes")
                    if isinstance(blocked_routes, list):
                        missing_blocks = sorted(required_blocked_routes - {value for value in blocked_routes if isinstance(value, str)})
                        if missing_blocks:
                            self.add_error(path, f"route_results[{index}].blocked_routes missing required values: {', '.join(missing_blocks)}")
                    route_families = route.get("allowed_route_families")
                    if isinstance(route_families, list):
                        unknown_families = sorted({value for value in route_families if isinstance(value, str)} - allowed_route_families)
                        if unknown_families:
                            self.add_error(path, f"route_results[{index}].allowed_route_families has unknown values: {', '.join(unknown_families)}")
                    if route.get("validator_decision") == "blocked_private_review_notice_only":
                        if route.get("public_processing_allowed") is not False:
                            self.add_error(path, f"route_results[{index}] private-review blocker must keep public_processing_allowed false")
                        if route.get("route_status") != "private_or_real_quality_review_blocked":
                            self.add_error(path, f"route_results[{index}] private-review blocker has wrong route_status")
            else:
                self.add_error(path, "validator report must include route_results")

            blocked_manifest = doc.get("blocked_output_manifest")
            if isinstance(blocked_manifest, list):
                missing_blocks = sorted(required_blocked_routes - {value for value in blocked_manifest if isinstance(value, str)})
                if missing_blocks:
                    self.add_error(path, f"blocked_output_manifest missing required values: {', '.join(missing_blocks)}")

            for key in sorted(forbidden_keys):
                for location, _value in self.find_key(doc, key):
                    if location.startswith("$.forbidden_output_fields"):
                        continue
                    self.add_error(path, f"{location} is not allowed in public measurement-refusal validator reports")

    def validate_case_to_cure_synthetic_pipelines(self) -> None:
        schema_path = self.root / "schemas" / "case-to-cure-synthetic-pipeline.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        expected_stage_ids = {f"case_{index:02d}" for index in range(15)}
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "synthetic_case_pipeline_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            notice = doc.get("synthetic_case_notice")
            if isinstance(notice, dict):
                if notice.get("uses_real_patient_data") is not False:
                    self.add_error(path, "synthetic_case_notice.uses_real_patient_data must be false")
                if notice.get("contains_phi") is not False:
                    self.add_error(path, "synthetic_case_notice.contains_phi must be false")
                if notice.get("contains_patient_specific_recommendation") is not False:
                    self.add_error(path, "synthetic_case_notice.contains_patient_specific_recommendation must be false")

            stages = doc.get("pipeline_stages")
            if isinstance(stages, list):
                seen_stage_ids: set[str] = set()
                for index, stage in enumerate(stages):
                    if not isinstance(stage, dict):
                        continue
                    stage_id = stage.get("stage_id")
                    if isinstance(stage_id, str):
                        if stage_id in seen_stage_ids:
                            self.add_error(path, f"pipeline_stages[{index}] duplicate stage_id: {stage_id}")
                        seen_stage_ids.add(stage_id)
                missing = sorted(expected_stage_ids - seen_stage_ids)
                if missing:
                    self.add_error(path, f"pipeline_stages missing required stage ids: {', '.join(missing)}")

            publication_gate = doc.get("publication_gate_result")
            if isinstance(publication_gate, dict):
                if publication_gate.get("actual_case_data_publication_allowed") is not False:
                    self.add_error(path, "publication_gate_result.actual_case_data_publication_allowed must be false")
                if publication_gate.get("patient_specific_outputs_publication_allowed") is not False:
                    self.add_error(path, "publication_gate_result.patient_specific_outputs_publication_allowed must be false")

    def validate_source_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.is_json_schema(doc):
                continue
            for location, values in self.find_key(doc, "source_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string source id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown source_id: {value}")

    def validate_taxonomy_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.is_json_schema(doc):
                continue
            for location, values in self.find_key(doc, "taxonomy_class_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string taxonomy id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown taxonomy class_id: {value}")

    def validate_mechanism_group_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.rel(path).as_posix() in SKIP_SCHEMA_VALIDATION:
                continue
            if self.is_json_schema(doc):
                continue
            for location, values in self.find_key(doc, "mechanism_group_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string mechanism id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown mechanism_id: {value}")
            for location, value in self.find_key(doc, "mechanism_group_id"):
                if not isinstance(value, str):
                    self.add_error(path, f"{location} must be a string")
                elif value not in known_ids:
                    self.add_error(path, f"{location} references unknown mechanism_id: {value}")

    def validate_extraction_record_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.rel(path).as_posix() in SKIP_SCHEMA_VALIDATION:
                continue
            if self.is_json_schema(doc):
                continue
            if isinstance(doc, dict) and "extraction_record_id" in doc:
                continue
            for location, values in self.find_key(doc, "extraction_record_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string extraction record id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown extraction_record_id: {value}")

    def validate_extraction_signal_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.rel(path).as_posix() in SKIP_SCHEMA_VALIDATION:
                continue
            if self.is_json_schema(doc):
                continue
            if isinstance(doc, dict) and "extraction_record_id" in doc:
                continue
            for location, values in self.find_key(doc, "extraction_signal_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string extraction signal id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown signal_id: {value}")

    def validate_measurement_term_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.is_json_schema(doc):
                continue
            if isinstance(doc, dict) and "glossary_id" in doc:
                continue
            for location, values in self.find_key(doc, "measurement_term_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string measurement term id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown measurement term_id: {value}")

    def validate_claim_set_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.is_json_schema(doc):
                continue
            if isinstance(doc, dict) and "claim_set_id" in doc:
                continue
            for location, values in self.find_key(doc, "claim_set_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string claim set id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown claim_set_id: {value}")

    def validate_claim_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.is_json_schema(doc):
                continue
            if isinstance(doc, dict) and "claim_set_id" in doc:
                continue
            for location, values in self.find_key(doc, "linked_claim_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string claim id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown claim_id: {value}")

    def validate_gap_register_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.is_json_schema(doc):
                continue
            if isinstance(doc, dict) and "gap_register_id" in doc:
                continue
            for location, values in self.find_key(doc, "gap_register_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string gap register id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown gap_register_id: {value}")

    def validate_gap_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.is_json_schema(doc):
                continue
            if isinstance(doc, dict) and "gap_register_id" in doc:
                continue
            for location, values in self.find_key(doc, "linked_gap_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string gap id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown gap_id: {value}")

    def validate_query_record_references(self, known_ids: set[str]) -> None:
        for path, doc in self.json_docs.items():
            if self.is_json_schema(doc):
                continue
            for location, values in self.find_key(doc, "trial_query_record_ids"):
                if not isinstance(values, list):
                    self.add_error(path, f"{location} must be an array")
                    continue
                for value in values:
                    if not isinstance(value, str):
                        self.add_error(path, f"{location} contains a non-string query record id")
                    elif value not in known_ids:
                        self.add_error(path, f"{location} references unknown query_record_id: {value}")

    def validate_query_records(self) -> None:
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "query_record_id" not in doc:
                continue
            if path.name.endswith("template-v0.json"):
                continue
            api = doc.get("api_provenance")
            if not isinstance(api, dict):
                self.add_error(path, "query record missing api_provenance object")
                continue
            if not api.get("api_version"):
                self.add_error(path, "query record missing api_provenance.api_version")
            if not api.get("data_timestamp"):
                self.add_error(path, "query record missing api_provenance.data_timestamp")
            if not isinstance(api.get("total_count"), int):
                self.add_error(path, "query record api_provenance.total_count must be an integer")
            urls = doc.get("urls")
            if not isinstance(urls, dict) or not urls.get("api_studies_url"):
                self.add_error(path, "query record missing urls.api_studies_url")

    def validate_against_schema(self, path: Path, value: Any, schema: dict[str, Any], loc: str = "$") -> None:
        expected_type = schema.get("type")
        if expected_type and not self.type_matches(value, expected_type):
            self.add_error(path, f"{loc} expected type {expected_type}, got {type(value).__name__}")
            return

        enum = schema.get("enum")
        if enum is not None and value not in enum:
            self.add_error(path, f"{loc} value {value!r} is not in enum {enum!r}")

        pattern = schema.get("pattern")
        if pattern and isinstance(value, str) and re.fullmatch(pattern, value) is None:
            self.add_error(path, f"{loc} value {value!r} does not match pattern {pattern}")

        min_length = schema.get("minLength")
        if isinstance(min_length, int) and isinstance(value, str) and len(value) < min_length:
            self.add_error(path, f"{loc} must have length >= {min_length}")

        fmt = schema.get("format")
        if fmt and isinstance(value, str):
            self.validate_format(path, value, fmt, loc)

        if isinstance(value, dict):
            required = schema.get("required", [])
            if isinstance(required, list):
                for key in required:
                    if key not in value:
                        self.add_error(path, f"{loc}.{key} is required")
            props = schema.get("properties", {})
            if isinstance(props, dict):
                for key, subschema in props.items():
                    if key in value and isinstance(subschema, dict):
                        self.validate_against_schema(path, value[key], subschema, f"{loc}.{key}")
            if schema.get("additionalProperties") is False and isinstance(props, dict):
                allowed = set(props)
                for key in value:
                    if key not in allowed:
                        self.add_error(path, f"{loc}.{key} is not an allowed property")

        if isinstance(value, list):
            min_items = schema.get("minItems")
            if isinstance(min_items, int) and len(value) < min_items:
                self.add_error(path, f"{loc} must contain at least {min_items} item(s)")
            if schema.get("uniqueItems") is True:
                seen: set[str] = set()
                for item in value:
                    marker = json.dumps(item, sort_keys=True)
                    if marker in seen:
                        self.add_error(path, f"{loc} contains duplicate item {item!r}")
                    seen.add(marker)
            item_schema = schema.get("items")
            if isinstance(item_schema, dict):
                for index, item in enumerate(value):
                    self.validate_against_schema(path, item, item_schema, f"{loc}[{index}]")

    def type_matches(self, value: Any, expected: str) -> bool:
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

    def validate_format(self, path: Path, value: str, fmt: str, loc: str) -> None:
        if fmt == "date":
            try:
                date.fromisoformat(value)
            except ValueError:
                self.add_error(path, f"{loc} is not an ISO date: {value!r}")
        elif fmt == "uri":
            parsed = urlparse(value)
            if not parsed.scheme or not parsed.netloc:
                self.add_error(path, f"{loc} is not an absolute URI: {value!r}")
        elif fmt == "uri-reference":
            if not value:
                self.add_error(path, f"{loc} is an empty URI reference")

    def find_key(self, value: Any, key: str, loc: str = "$") -> list[tuple[str, Any]]:
        matches: list[tuple[str, Any]] = []
        if isinstance(value, dict):
            for child_key, child_value in value.items():
                child_loc = f"{loc}.{child_key}"
                if child_key == key:
                    matches.append((child_loc, child_value))
                matches.extend(self.find_key(child_value, key, child_loc))
        elif isinstance(value, list):
            for index, item in enumerate(value):
                matches.extend(self.find_key(item, key, f"{loc}[{index}]"))
        return matches

    def is_json_schema(self, value: Any) -> bool:
        return isinstance(value, dict) and "$schema" in value and "properties" in value

    def is_artifact_metadata_path(self, path: Path) -> bool:
        return path.name.endswith(".metadata.json")

    def report(self) -> None:
        if self.errors:
            print("Validation failed:")
            for issue in self.errors:
                print(f"  ERROR {issue.path}: {issue.message}")
        else:
            print("Validation passed.")
        if self.warnings:
            for issue in self.warnings:
                print(f"  WARN  {issue.path}: {issue.message}")
        print(f"Checked {len(self.json_docs)} JSON file(s).")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root to validate. Defaults to the parent of tools/.",
    )
    args = parser.parse_args()
    return Validator(args.root.resolve()).run()


if __name__ == "__main__":
    sys.exit(main())
