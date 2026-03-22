#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


REQUIRED_FILES = [
    "AGENTS.md",
    ".codex/AGENTS.md",
    ".codex/WORKFLOW.md",
    ".codex/ORCHESTRATION.md",
    ".codex/COMMIT_TEMPLATE.md",
    ".codex/PROMPTS.md",
    ".codex/TASK_TEMPLATE.md",
    ".codex/skills/bugfix.md",
    ".codex/skills/feature.md",
    ".codex/skills/git-commit.md",
    ".codex/skills/handoff.md",
    ".codex/skills/planning.md",
    ".codex/skills/refactor.md",
    ".codex/skills/review.md",
    ".codex/skills/test.md",
]

REQUIRED_DIRS = [
    ".codex/tasks/active",
    ".codex/tasks/paused",
    ".codex/tasks/done",
    ".codex/tasks/dropped",
    ".codex/tasks/blocked",
]

ROOT_AGENTS_MARKER_START = "<!-- general-project bootstrap start -->"
ROOT_AGENTS_MARKER_END = "<!-- general-project bootstrap end -->"
ROOT_AGENTS_INTEGRATION_BLOCK = """<!-- general-project bootstrap start -->

## Codex Workflow Entry

This repository also uses a structured AI workflow defined under `.codex/`.

Core system files:

- `.codex/AGENTS.md`          → behavior rules (HOW to operate)
- `.codex/WORKFLOW.md`        → task lifecycle
- `.codex/ORCHESTRATION.md`   → multi-agent coordination
- `.codex/skills/`            → task-specific procedures

Before performing any non-trivial work:

1. Read `.codex/AGENTS.md`
2. Read `.codex/WORKFLOW.md`
3. Check `.codex/tasks/active/` for existing tasks
4. Use relevant files in `.codex/skills/` when applicable

Treat the `.codex/` workflow rules as higher priority than implicit default behavior for repository execution.

<!-- general-project bootstrap end -->
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap a general Codex workflow kit into a target project."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize the workflow kit.")
    init_parser.add_argument("target", help="Target project directory.")
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files that conflict with the template.",
    )
    init_parser.add_argument(
        "--skip-root-agents",
        action="store_true",
        help="Do not create or overwrite the repository root AGENTS.md.",
    )

    check_parser = subparsers.add_parser("check", help="Verify the workflow kit layout.")
    check_parser.add_argument("target", help="Target project directory.")

    return parser.parse_args()


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def template_root() -> Path:
    return skill_root() / "assets" / "project-template"


def copy_file(source: Path, destination: Path, force: bool) -> None:
    if destination.exists() and not force:
        raise FileExistsError(
            f"Refusing to overwrite existing file without --force: {destination}"
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def root_agents_has_codex_entry(content: str) -> bool:
    required_signals = [
        ".codex/AGENTS.md",
        ".codex/WORKFLOW.md",
        ".codex/tasks/active/",
    ]
    return all(signal in content for signal in required_signals)


def ensure_root_agents(target_dir: Path, source_root: Path, force: bool) -> None:
    source = source_root / "AGENTS.md"
    destination = target_dir / "AGENTS.md"

    if not destination.exists():
        copy_file(source, destination, force=force)
        return

    current = destination.read_text(encoding="utf-8")
    if root_agents_has_codex_entry(current):
        return

    if ROOT_AGENTS_MARKER_START in current and ROOT_AGENTS_MARKER_END in current:
        return

    merged = current.rstrip() + "\n\n" + ROOT_AGENTS_INTEGRATION_BLOCK + "\n"
    destination.write_text(merged, encoding="utf-8")


def collect_missing_paths(target_dir: Path) -> list[str]:
    missing: list[str] = []
    for relative_file in REQUIRED_FILES:
        if not (target_dir / relative_file).is_file():
            missing.append(relative_file)
    for relative_dir in REQUIRED_DIRS:
        if not (target_dir / relative_dir).is_dir():
            missing.append(relative_dir)
    return missing


def init_project(target_dir: Path, force: bool, skip_root_agents: bool) -> int:
    source_root = template_root()
    if not source_root.exists():
        print(f"[ERROR] Template directory not found: {source_root}")
        return 1

    target_dir.mkdir(parents=True, exist_ok=True)

    if not skip_root_agents:
        ensure_root_agents(target_dir=target_dir, source_root=source_root, force=force)

    files_to_copy = [path for path in source_root.rglob("*") if path.is_file()]
    for source in files_to_copy:
        relative_path = source.relative_to(source_root)
        if relative_path.as_posix() == "AGENTS.md":
            continue
        copy_file(source, target_dir / relative_path, force=force)

    for relative_dir in REQUIRED_DIRS:
        (target_dir / relative_dir).mkdir(parents=True, exist_ok=True)

    missing = collect_missing_paths(target_dir)
    if missing:
        print("[ERROR] Bootstrap completed with missing paths:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print(f"[OK] Bootstrapped workflow kit into: {target_dir}")
    return 0


def check_project(target_dir: Path) -> int:
    missing = collect_missing_paths(target_dir)
    if missing:
        print("[ERROR] Missing required workflow paths:")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("[OK] Workflow kit structure looks complete.")
    return 0


def main() -> int:
    args = parse_args()
    target_dir = Path(args.target).resolve()

    if args.command == "init":
        return init_project(
            target_dir=target_dir,
            force=args.force,
            skip_root_agents=args.skip_root_agents,
        )

    if args.command == "check":
        return check_project(target_dir=target_dir)

    print(f"[ERROR] Unsupported command: {args.command}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
