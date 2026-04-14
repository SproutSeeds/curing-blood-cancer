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
        taxonomy_ids = self.collect_taxonomy_ids()
        query_record_ids = self.collect_query_record_ids()
        mechanism_group_ids = self.collect_mechanism_group_ids()
        extraction_record_ids = self.collect_extraction_record_ids()

        self.validate_claim_sets()
        self.validate_evidence_claims()
        self.validate_mechanism_extractions()
        self.validate_mechanism_maps()
        self.validate_opportunity_maps()
        self.validate_source_references(source_ids)
        self.validate_taxonomy_references(taxonomy_ids)
        self.validate_mechanism_group_references(mechanism_group_ids)
        self.validate_extraction_record_references(extraction_record_ids)
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

    def validate_claim_sets(self) -> None:
        schema_path = self.root / "schemas" / "claim-set.schema.json"
        schema = self.json_docs.get(schema_path)
        if not isinstance(schema, dict):
            return

        seen_sets: set[str] = set()
        for path, doc in self.json_docs.items():
            if not isinstance(doc, dict) or "claim_set_id" not in doc:
                continue
            self.validate_against_schema(path, doc, schema)

            claim_set_id = doc.get("claim_set_id")
            if isinstance(claim_set_id, str):
                if claim_set_id in seen_sets:
                    self.add_error(path, f"duplicate claim_set_id: {claim_set_id}")
                seen_sets.add(claim_set_id)
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
