# File Checklist

## Purpose

Use this checklist after bootstrapping a repository with `general-project` to confirm the workflow kit is present and coherent.

## Required Root File

- `AGENTS.md`

## Required `.codex/` Core Files

- `.codex/AGENTS.md`
- `.codex/WORKFLOW.md`
- `.codex/ORCHESTRATION.md`
- `.codex/COMMIT_TEMPLATE.md`
- `.codex/PROMPTS.md`
- `.codex/TASK_TEMPLATE.md`

## Required `.codex/skills/` Files

- `.codex/skills/bugfix.md`
- `.codex/skills/feature.md`
- `.codex/skills/refactor.md`
- `.codex/skills/review.md`
- `.codex/skills/test.md`
- `.codex/skills/planning.md`
- `.codex/skills/handoff.md`
- `.codex/skills/git-commit.md`

## Required `.codex/tasks/` Directories

- `.codex/tasks/active/`
- `.codex/tasks/paused/`
- `.codex/tasks/done/`
- `.codex/tasks/dropped/`
- `.codex/tasks/blocked/`

## Post-Bootstrap Checks

1. Confirm root `AGENTS.md` points agents into `.codex/`.
2. Confirm `.codex/AGENTS.md` and `.codex/WORKFLOW.md` match the intended repository discipline.
3. Confirm every skill route mentioned in `AGENTS.md` actually exists in `.codex/skills/`.
4. Confirm the task directories exist before any non-trivial work starts.
5. Run:
   - `python skills/general-project/scripts/bootstrap_project.py check <target-repo>`
6. In a real target repository, dry-run a first task:
   - create one task file under `.codex/tasks/active/`
   - move it to `.codex/tasks/done/` after a trivial simulated completion

## Optional Customization Points

- Tighten wording in `.codex/AGENTS.md` for your team's review bar.
- Adjust `.codex/skills/` routing if your repository uses different task categories.
- Add project-specific references only after the generic workflow kit is stable.
