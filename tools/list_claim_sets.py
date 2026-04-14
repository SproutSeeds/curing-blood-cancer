#!/usr/bin/env python3
"""List public claim sets with source, extraction, and measurement links."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_CLAIM_SETS = Path("disease-programs/multiple-myeloma/evidence-claims")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_measurement_terms(root: Path) -> dict[str, str]:
    labels: dict[str, str] = {}
    for path in sorted(root.rglob("*.json")):
        if ".git" in path.parts:
            continue
        doc = load_json(path)
        if not isinstance(doc, dict) or "glossary_id" not in doc:
            continue
        terms = doc.get("terms")
        if not isinstance(terms, list):
            continue
        for term in terms:
            if not isinstance(term, dict):
                continue
            term_id = term.get("term_id")
            label = term.get("label")
            if isinstance(term_id, str) and isinstance(label, str):
                labels[term_id] = label
    return labels


def claim_sets(root: Path, claim_set_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / claim_set_dir).glob("*.json")):
        doc = load_json(path)
        if isinstance(doc, dict) and "claim_set_id" in doc:
            records.append((path.relative_to(root), doc))
    return records


def values(doc: dict[str, Any], key: str) -> list[str]:
    raw = doc.get(key)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, str)]


def keep_record(doc: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.claim_set_id and doc.get("claim_set_id") != args.claim_set_id:
        return False
    if args.measurement_term_id and args.measurement_term_id not in values(doc, "measurement_term_ids"):
        claims = [item for item in doc.get("claims", []) if isinstance(item, dict)]
        if not any(args.measurement_term_id in values(claim, "measurement_term_ids") for claim in claims):
            return False
    if args.source_id and args.source_id not in values(doc, "source_ids"):
        claims = [item for item in doc.get("claims", []) if isinstance(item, dict)]
        if not any(args.source_id in values(claim, "source_ids") for claim in claims):
            return False
    return True


def format_terms(term_ids: list[str], labels: dict[str, str]) -> str:
    if not term_ids:
        return "none"
    return ", ".join(f"{term_id} ({labels.get(term_id, 'unknown term')})" for term_id in term_ids)


def print_text(records: list[tuple[Path, dict[str, Any]]], term_labels: dict[str, str]) -> None:
    claim_count = sum(len([item for item in doc.get("claims", []) if isinstance(item, dict)]) for _, doc in records)
    print("Claim set summary")
    print(f"Claim sets: {len(records)}")
    print(f"Claims: {claim_count}")
    print()

    for path, doc in records:
        print(f"{doc.get('claim_set_title', 'Untitled')} ({doc.get('claim_set_id', '')})")
        print(f"  path: {path.as_posix()}")
        print(f"  boundary: {doc.get('clinical_use_boundary', '')}")
        print(f"  source_ids: {', '.join(values(doc, 'source_ids'))}")
        print(f"  measurement_terms: {format_terms(values(doc, 'measurement_term_ids'), term_labels)}")
        print("  claims:")
        for claim in doc.get("claims", []):
            if not isinstance(claim, dict):
                continue
            print(
                f"    - {claim.get('claim_id', '')} "
                f"[{claim.get('evidence_level', '')}; {claim.get('claim_status', '')}]"
            )
            print(f"      measurement_terms: {format_terms(values(claim, 'measurement_term_ids'), term_labels)}")
            print(f"      extraction_records: {', '.join(values(claim, 'extraction_record_ids'))}")
            print(f"      {claim.get('claim_text', '')}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--claim-sets", type=Path, default=DEFAULT_CLAIM_SETS)
    parser.add_argument("--claim-set-id", help="Only show one claim set.")
    parser.add_argument("--measurement-term-id", help="Only show claim sets linked to a measurement term.")
    parser.add_argument("--source-id", help="Only show claim sets linked to a source id.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    term_labels = collect_measurement_terms(root)
    records = [(path, doc) for path, doc in claim_sets(root, args.claim_sets) if keep_record(doc, args)]

    if args.json:
        print(
            json.dumps(
                {
                    "measurement_terms": term_labels,
                    "claim_sets": [
                        {
                            "path": path.as_posix(),
                            "claim_set": doc,
                        }
                        for path, doc in records
                    ],
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print_text(records, term_labels)
    return 0


if __name__ == "__main__":
    sys.exit(main())
