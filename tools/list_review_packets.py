#!/usr/bin/env python3
"""List public expert-review packets and review items."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_REVIEW_PACKETS = Path("disease-programs/multiple-myeloma/reviews")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def values(doc: dict[str, Any], key: str) -> list[str]:
    raw = doc.get(key)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, str)]


def review_packets(root: Path, review_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / review_dir).glob("*.json")):
        doc = load_json(path)
        if isinstance(doc, dict) and "review_packet_id" in doc:
            records.append((path.relative_to(root), doc))
    return records


def keep_packet(packet: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.review_status:
        review = packet.get("review")
        if not isinstance(review, dict) or review.get("review_status") != args.review_status:
            return False
    if args.claim_id:
        items = [item for item in packet.get("review_items", []) if isinstance(item, dict)]
        if not any(args.claim_id in values(item, "linked_claim_ids") for item in items):
            return False
    if args.gap_id:
        items = [item for item in packet.get("review_items", []) if isinstance(item, dict)]
        if not any(args.gap_id in values(item, "linked_gap_ids") for item in items):
            return False
    return True


def print_text(records: list[tuple[Path, dict[str, Any]]], args: argparse.Namespace) -> None:
    items = [
        item
        for _, packet in records
        for item in packet.get("review_items", [])
        if isinstance(item, dict)
        and (not args.claim_id or args.claim_id in values(item, "linked_claim_ids"))
        and (not args.gap_id or args.gap_id in values(item, "linked_gap_ids"))
    ]
    print("Review packet summary")
    print(f"Review packets: {len(records)}")
    print(f"Review items: {len(items)}")
    print()

    for path, packet in records:
        review = packet.get("review", {})
        review_status = review.get("review_status", "") if isinstance(review, dict) else ""
        print(f"{packet.get('title', 'Untitled')} ({packet.get('review_packet_id', '')})")
        print(f"  path: {path.as_posix()}")
        print(f"  boundary: {packet.get('clinical_use_boundary', '')}")
        print(f"  review_status: {review_status}")
        print(f"  claim_sets: {', '.join(values(packet, 'claim_set_ids'))}")
        print(f"  gap_registers: {', '.join(values(packet, 'gap_register_ids'))}")
        print("  review_items:")
        for item in packet.get("review_items", []):
            if not isinstance(item, dict):
                continue
            if args.claim_id and args.claim_id not in values(item, "linked_claim_ids"):
                continue
            if args.gap_id and args.gap_id not in values(item, "linked_gap_ids"):
                continue
            print(
                f"    - {item.get('review_item_id', '')} "
                f"[{item.get('review_focus', '')}; {item.get('current_public_status', '')}]"
            )
            print(f"      linked_claims: {', '.join(values(item, 'linked_claim_ids'))}")
            print(f"      linked_gaps: {', '.join(values(item, 'linked_gap_ids'))}")
            print(f"      action: {item.get('reviewer_action_needed', '')}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--review-packets", type=Path, default=DEFAULT_REVIEW_PACKETS)
    parser.add_argument(
        "--review-status",
        choices=["draft", "source-checked", "expert-review-needed", "expert-reviewed", "deprecated"],
        help="Only show packets with this review status.",
    )
    parser.add_argument("--claim-id", help="Only show review items linked to this claim_id.")
    parser.add_argument("--gap-id", help="Only show review items linked to this gap_id.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    records = [(path, packet) for path, packet in review_packets(root, args.review_packets) if keep_packet(packet, args)]

    if args.json:
        print(
            json.dumps(
                {
                    "review_packets": [
                        {
                            "path": path.as_posix(),
                            "review_packet": packet,
                        }
                        for path, packet in records
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
