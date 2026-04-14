#!/usr/bin/env python3
"""List public evidence gap registers."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_GAP_REGISTERS = Path("disease-programs/multiple-myeloma/evidence-gaps")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def gap_registers(root: Path, gap_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / gap_dir).glob("*.json")):
        doc = load_json(path)
        if isinstance(doc, dict) and "gap_register_id" in doc:
            records.append((path.relative_to(root), doc))
    return records


def values(doc: dict[str, Any], key: str) -> list[str]:
    raw = doc.get(key)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, str)]


def keep_record(doc: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.gap_register_id and doc.get("gap_register_id") != args.gap_register_id:
        return False

    gaps = [item for item in doc.get("gaps", []) if isinstance(item, dict)]
    if args.priority and not any(gap.get("priority") == args.priority for gap in gaps):
        return False
    if args.gap_type and not any(gap.get("gap_type") == args.gap_type for gap in gaps):
        return False
    if args.claim_id and not any(args.claim_id in values(gap, "linked_claim_ids") for gap in gaps):
        return False
    return True


def print_text(records: list[tuple[Path, dict[str, Any]]], args: argparse.Namespace) -> None:
    gaps = [
        gap
        for _, doc in records
        for gap in doc.get("gaps", [])
        if isinstance(gap, dict)
        and (not args.priority or gap.get("priority") == args.priority)
        and (not args.gap_type or gap.get("gap_type") == args.gap_type)
        and (not args.claim_id or args.claim_id in values(gap, "linked_claim_ids"))
    ]
    print("Evidence gap summary")
    print(f"Gap registers: {len(records)}")
    print(f"Gaps: {len(gaps)}")
    print()

    for path, doc in records:
        print(f"{doc.get('title', 'Untitled')} ({doc.get('gap_register_id', '')})")
        print(f"  path: {path.as_posix()}")
        print(f"  boundary: {doc.get('clinical_use_boundary', '')}")
        print(f"  claim_sets: {', '.join(values(doc, 'claim_set_ids'))}")
        print("  gaps:")
        for gap in doc.get("gaps", []):
            if not isinstance(gap, dict):
                continue
            if args.priority and gap.get("priority") != args.priority:
                continue
            if args.gap_type and gap.get("gap_type") != args.gap_type:
                continue
            if args.claim_id and args.claim_id not in values(gap, "linked_claim_ids"):
                continue
            print(f"    - {gap.get('gap_id', '')} [{gap.get('priority', '')}; {gap.get('gap_type', '')}]")
            print(f"      linked_claims: {', '.join(values(gap, 'linked_claim_ids'))}")
            print(f"      measurement_terms: {', '.join(values(gap, 'measurement_term_ids'))}")
            print(f"      {gap.get('gap_statement', '')}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--gap-registers", type=Path, default=DEFAULT_GAP_REGISTERS)
    parser.add_argument("--gap-register-id", help="Only show one gap register.")
    parser.add_argument("--priority", choices=["high", "medium", "low"], help="Only show gaps with this priority.")
    parser.add_argument("--gap-type", help="Only show gaps with this gap_type.")
    parser.add_argument("--claim-id", help="Only show gaps linked to this claim_id.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    records = [(path, doc) for path, doc in gap_registers(root, args.gap_registers) if keep_record(doc, args)]

    if args.json:
        print(
            json.dumps(
                {
                    "gap_registers": [
                        {
                            "path": path.as_posix(),
                            "gap_register": doc,
                        }
                        for path, doc in records
                    ],
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print_text(records, args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
