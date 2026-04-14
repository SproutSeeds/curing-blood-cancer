#!/usr/bin/env python3
"""List public mechanism extraction records by mechanism bucket."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


DEFAULT_MAP = Path("disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-map-v0.json")
DEFAULT_EXTRACTIONS = Path("disease-programs/multiple-myeloma/mechanisms/extractions")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def mechanism_labels(root: Path, map_path: Path) -> dict[str, str]:
    doc = load_json(root / map_path)
    labels: dict[str, str] = {}
    for group in doc.get("mechanism_groups", []):
        if isinstance(group, dict):
            mechanism_id = group.get("mechanism_id")
            label = group.get("label")
            if isinstance(mechanism_id, str) and isinstance(label, str):
                labels[mechanism_id] = label
    return labels


def extraction_records(root: Path, extractions_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / extractions_dir).glob("*.json")):
        doc = load_json(path)
        if isinstance(doc, dict) and "extraction_record_id" in doc:
            records.append((path.relative_to(root), doc))
    return records


def build_summary(
    records: list[tuple[Path, dict[str, Any]]],
) -> dict[str, list[dict[str, str | list[str]]]]:
    grouped: dict[str, list[dict[str, str | list[str]]]] = defaultdict(list)
    for path, record in records:
        record_id = str(record.get("extraction_record_id", ""))
        source_ids = [str(item) for item in record.get("source_ids", [])]
        for signal in record.get("extracted_signals", []):
            if not isinstance(signal, dict):
                continue
            mechanism_id = signal.get("mechanism_group_id")
            if not isinstance(mechanism_id, str):
                continue
            grouped[mechanism_id].append(
                {
                    "record_id": record_id,
                    "path": path.as_posix(),
                    "signal_id": str(signal.get("signal_id", "")),
                    "summary": str(signal.get("signal_summary", "")),
                    "evidence_level": str(signal.get("evidence_level", "")),
                    "source_ids": source_ids,
                }
            )
    return dict(grouped)


def print_text(labels: dict[str, str], grouped: dict[str, list[dict[str, str | list[str]]]]) -> None:
    signal_count = sum(len(items) for items in grouped.values())
    record_ids = {
        str(item["record_id"])
        for items in grouped.values()
        for item in items
        if item.get("record_id")
    }
    print("Mechanism extraction summary")
    print(f"Records: {len(record_ids)}")
    print(f"Signals: {signal_count}")
    print()

    for mechanism_id in sorted(grouped):
        label = labels.get(mechanism_id, "unknown mechanism")
        print(f"{mechanism_id} - {label}")
        for item in grouped[mechanism_id]:
            sources = ", ".join(item.get("source_ids", []))
            print(f"  - {item['signal_id']} [{item['evidence_level']}]")
            print(f"    record: {item['record_id']}")
            print(f"    source_ids: {sources}")
            print(f"    {item['summary']}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--map", type=Path, default=DEFAULT_MAP)
    parser.add_argument("--extractions", type=Path, default=DEFAULT_EXTRACTIONS)
    parser.add_argument("--mechanism-id", help="Only show one mechanism bucket.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    labels = mechanism_labels(root, args.map)
    records = extraction_records(root, args.extractions)
    grouped = build_summary(records)

    if args.mechanism_id:
        grouped = {args.mechanism_id: grouped.get(args.mechanism_id, [])}

    if args.json:
        print(json.dumps({"mechanisms": labels, "groups": grouped}, indent=2, sort_keys=True))
    else:
        print_text(labels, grouped)
    return 0


if __name__ == "__main__":
    sys.exit(main())

