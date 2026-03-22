---
name: general-project
description: Bootstrap and execute general software project work across unfamiliar or established repositories. Use when Codex needs to initialize a reusable `.codex` workflow kit, inspect project context, clarify scope, plan the smallest correct change, implement features or fixes, validate behavior, review risks, or prepare concise delivery notes for almost any codebase.
---

# General Project

## Overview

Use this skill for two things:

- bootstrap a repository with the bundled `.codex` workflow kit
- execute normal project work with tight scope and proportionate verification

Read [template-map.md](references/template-map.md) for the generated layout. Read [file-checklist.md](references/file-checklist.md) when validating a bootstrapped repository.

## Default Invocation Rule

When invoked for a repository, default to this sequence unless the user explicitly says not to:

1. Check whether the repository already has the full workflow kit:
   - root `AGENTS.md`
   - `.codex/AGENTS.md`
   - `.codex/WORKFLOW.md`
   - `.codex/ORCHESTRATION.md`
   - `.codex/COMMIT_TEMPLATE.md`
   - `.codex/PROMPTS.md`
   - `.codex/TASK_TEMPLATE.md`
   - `.codex/skills/*.md`
   - `.codex/tasks/{active,paused,done,dropped,blocked}`
2. If the kit is missing or incomplete, run `bootstrap_project.py init <target-repo>`.
3. Then run `bootstrap_project.py check <target-repo>`.
4. Only continue with the actual project task after `check` succeeds.

If the repository already has a complete and valid workflow kit, skip bootstrap unless the user asks to refresh, repair, or re-bootstrap it.

If the repository already has a root `AGENTS.md` but it does not point into `.codex/`, do not skip bootstrap. `init` should preserve the existing file and inject the managed `.codex` entry block.

## Bootstrapping

Default command flow:

```bash
python scripts/bootstrap_project.py init <target-repo>
python scripts/bootstrap_project.py check <target-repo>
```

If the user does not want the root `AGENTS.md` touched at all, use:

```bash
python scripts/bootstrap_project.py init <target-repo> --skip-root-agents
```

Use `--force` only when replacing conflicting workflow files is intentional.

If acting inside the target repository, run bootstrap as the default setup step when needed. Do not ask the user to remember these commands first.

## Execution Workflow

### 1. Frame the task

Identify:

- the concrete goal
- the expected output
- the task type: question, bug, feature, refactor, review, documentation, or validation
- explicit constraints from the user, repository rules, and environment

If the request is broad, narrow it to the smallest useful deliverable.

### 2. Build only necessary context

Read in this order unless the repository defines a stricter process:

1. user-specified files
2. project instructions and active task files
3. directly affected code and nearby tests
4. only the imports, callers, callees, or docs needed to remove uncertainty

Avoid broad repository scans.

### 3. Define boundaries

Before editing, make these explicit:

- what is in scope
- what must not change
- what dependencies or assumptions matter
- what verification is sufficient
- what risks remain

Use the repository task system for any non-trivial work.

### 4. Choose the smallest correct change

Prefer:

- existing code paths over new abstractions
- local fixes over wide rewrites
- explicit logic over hidden indirection
- incremental edits over speculative expansion

### 5. Verify proportionally

Use the minimum verification that credibly supports the change:

- targeted tests when practical
- focused manual or command-line checks for affected behavior
- lint or type checks only when they meaningfully cover the changed path

Do not claim verification that was not performed.

### 6. Deliver clearly

Report:

- what changed
- why it changed
- what was verified
- what remains risky or unverified
- the next useful step, if any

## Heuristics

- If requirements are ambiguous, choose a reasonable default only when it is low-risk and reversible; otherwise surface the ambiguity.
- If the repository already has stronger local process rules, follow them.
- Start from the bundled template rather than hand-writing workflow files.
- If tests or scripts are unavailable, use direct inspection and narrow runtime checks, then state the validation gap.
- If scope begins to grow, split the work into the smallest independently useful increment.
