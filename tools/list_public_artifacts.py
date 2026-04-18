#!/usr/bin/env python3
"""List public artifact metadata records."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import sys
from pathlib import Path
from typing import Any


METADATA_SUFFIX = ".metadata.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def values(doc: dict[str, Any], key: str) -> list[str]:
    raw = doc.get(key)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, str)]


def list_count(doc: dict[str, Any], key: str) -> int:
    raw = doc.get(key)
    return len(raw) if isinstance(raw, list) else 0


def artifact_path(root: Path, metadata_path: Path) -> Path:
    relative = metadata_path.relative_to(root).as_posix()
    if relative.endswith(METADATA_SUFFIX):
        stem = relative[: -len(METADATA_SUFFIX)]
    else:
        return metadata_path.relative_to(root)

    for suffix in (".md", ".json", ".py", ".html"):
        candidate = root / f"{stem}{suffix}"
        if candidate.exists():
            return candidate.relative_to(root)
    return metadata_path.relative_to(root)


def artifacts(root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(root.rglob(f"*{METADATA_SUFFIX}")):
        if ".git" in path.parts:
            continue
        doc = load_json(path)
        if not isinstance(doc, dict):
            continue
        records.append(
            {
                "artifact_id": doc.get("artifact_id", ""),
                "title": doc.get("title", "Untitled"),
                "artifact_class": doc.get("artifact_class", ""),
                "claim_level": doc.get("claim_level", ""),
                "blood_cancer_scope": values(doc, "blood_cancer_scope"),
                "path": artifact_path(root, path).as_posix(),
                "metadata_path": path.relative_to(root).as_posix(),
                "source_count": list_count(doc, "sources"),
                "limitation_count": list_count(doc, "limitations"),
            }
        )
    return sorted(records, key=lambda item: (item["artifact_class"], item["title"], item["artifact_id"]))


def keep_record(record: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.artifact_class and record.get("artifact_class") != args.artifact_class:
        return False
    if args.claim_level and record.get("claim_level") != args.claim_level:
        return False
    if args.scope:
        scope = " ".join(record.get("blood_cancer_scope", [])).lower()
        if args.scope.lower() not in scope:
            return False
    return True


def print_text(records: list[dict[str, Any]]) -> None:
    counts = Counter(record.get("artifact_class", "") for record in records)

    print("Public artifact summary")
    print(f"Artifacts: {len(records)}")
    print("Classes:")
    for artifact_class, count in sorted(counts.items()):
        print(f"  {artifact_class or 'unspecified'}: {count}")
    print()

    for record in records:
        print(f"{record.get('title', 'Untitled')} ({record.get('artifact_id', '')})")
        print(f"  class: {record.get('artifact_class', '')}")
        print(f"  claim_level: {record.get('claim_level', '')}")
        print(f"  scope: {', '.join(record.get('blood_cancer_scope', []))}")
        print(f"  path: {record.get('path', '')}")
        print(f"  metadata: {record.get('metadata_path', '')}")
        print(f"  sources: {record.get('source_count', 0)}")
        print(f"  limitations: {record.get('limitation_count', 0)}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--artifact-class", help="Only show artifacts with this artifact_class.")
    parser.add_argument("--claim-level", help="Only show artifacts with this claim_level.")
    parser.add_argument("--scope", help="Only show artifacts whose blood_cancer_scope contains this text.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    records = [record for record in artifacts(root) if keep_record(record, args)]

    if args.json:
        print(json.dumps({"artifacts": records}, indent=2, sort_keys=True))
    else:
        print_text(records)
    return 0


if __name__ == "__main__":
    sys.exit(main())
