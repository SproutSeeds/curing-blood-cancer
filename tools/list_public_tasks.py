#!/usr/bin/env python3
"""List public contribution task queues."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_TASK_QUEUES = Path("disease-programs/multiple-myeloma/public-tasks")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def task_queues(root: Path, task_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted((root / task_dir).glob("*.json")):
        doc = load_json(path)
        if isinstance(doc, dict) and "task_queue_id" in doc:
            records.append((path.relative_to(root), doc))
    return records


def values(doc: dict[str, Any], key: str) -> list[str]:
    raw = doc.get(key)
    if not isinstance(raw, list):
        return []
    return [item for item in raw if isinstance(item, str)]


def keep_task(task: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.priority and task.get("priority") != args.priority:
        return False
    if args.status and task.get("status") != args.status:
        return False
    if args.task_type and task.get("task_type") != args.task_type:
        return False
    if args.gap_id and args.gap_id not in values(task, "linked_gap_ids"):
        return False
    return True


def print_text(records: list[tuple[Path, dict[str, Any]]], args: argparse.Namespace) -> None:
    tasks = [
        task
        for _, doc in records
        for task in doc.get("tasks", [])
        if isinstance(task, dict) and keep_task(task, args)
    ]
    print("Public task summary")
    print(f"Task queues: {len(records)}")
    print(f"Tasks: {len(tasks)}")
    print()

    for path, doc in records:
        print(f"{doc.get('title', 'Untitled')} ({doc.get('task_queue_id', '')})")
        print(f"  path: {path.as_posix()}")
        print(f"  boundary: {doc.get('clinical_use_boundary', '')}")
        print(f"  gap_registers: {', '.join(values(doc, 'gap_register_ids'))}")
        print("  tasks:")
        for task in doc.get("tasks", []):
            if not isinstance(task, dict) or not keep_task(task, args):
                continue
            print(f"    - {task.get('task_id', '')} [{task.get('priority', '')}; {task.get('status', '')}]")
            print(f"      type: {task.get('task_type', '')}")
            print(f"      issue_form: {task.get('suggested_issue_form', '')}")
            print(f"      linked_gaps: {', '.join(values(task, 'linked_gap_ids'))}")
            print(f"      issue_draft: {task.get('issue_draft_path', '')}")
            print(f"      {task.get('task_title', '')}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--task-queues", type=Path, default=DEFAULT_TASK_QUEUES)
    parser.add_argument("--priority", choices=["high", "medium", "low"], help="Only show tasks with this priority.")
    parser.add_argument(
        "--status",
        choices=["ready", "blocked", "in-progress", "done", "deferred"],
        help="Only show tasks with this status.",
    )
    parser.add_argument("--task-type", help="Only show tasks with this task_type.")
    parser.add_argument("--gap-id", help="Only show tasks linked to this gap_id.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    records = task_queues(root, args.task_queues)

    if args.json:
        print(
            json.dumps(
                {
                    "task_queues": [
                        {
                            "path": path.as_posix(),
                            "task_queue": doc,
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
