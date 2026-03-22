# AGENTS.md

## 1. Entry Point

This repository uses a structured AI workflow defined under `.codex/`.

Core system files:

- `.codex/AGENTS.md`          → behavior rules (HOW to operate)
- `.codex/WORKFLOW.md`        → task lifecycle
- `.codex/ORCHESTRATION.md`   → multi-agent coordination
- `.codex/skills/`            → task-specific procedures

---

## 2. Mandatory Bootstrapping

Before performing ANY non-trivial work, you MUST:

1. Read `.codex/AGENTS.md`
2. Read `.codex/WORKFLOW.md`
3. Check `.codex/tasks/active/` for existing tasks
4. Use relevant files in `.codex/skills/` when applicable

Do NOT proceed until these are acknowledged.

---

## 3. Task Discipline (Strict)

You MUST follow the task system defined in `.codex/WORKFLOW.md`.

### Required

Create or use a task if:

- more than one step is needed
- more than one file is involved
- debugging / investigation is required
- work may be interrupted
- scope is not trivial

### Forbidden

- skipping task creation for non-trivial work
- modifying multiple files without a task
- continuing previous work without checking active tasks

---

## 4. Scope Enforcement

- Only read necessary files
- Only modify files within task scope
- Do NOT scan entire repository unless required

---

## 5. Execution Routing

When performing work:

- bug → follow `.codex/skills/bugfix.md`
- feature → follow `.codex/skills/feature.md`
- refactor → follow `.codex/skills/refactor.md`
- validation → follow `.codex/skills/test.md`
- review → follow `.codex/skills/review.md`

---

## 6. Task State Awareness

Before starting work:

- check `.codex/tasks/active/`
- resume existing task if relevant

When stopping or switching:

- update task file
- write next step
- write handoff note if needed

---

## 7. Commit Behavior

- Default: DO NOT commit
- Only commit if explicitly allowed by:
  - task (`Commit Mode = auto`)
  - AND user/workflow permission

Follow `.codex/COMMIT_TEMPLATE.md`

---

## 8. Multi-Agent Awareness

If task involves multiple roles:

- planner defines scope and plan
- executor implements
- reviewer validates

Follow `.codex/ORCHESTRATION.md`

---

## 9. Failure Handling

If blocked:

- update task status to `blocked`
- document reason
- do NOT continue blindly

If scope unclear:

- refine task first
- do NOT guess implementation

---

## 10. Override Rule

If `.codex` instructions exist, they override any default or implicit behavior.

---

## 11. Final Rule

> Do not act as a generic assistant.  
> Act as an agent operating inside a controlled workflow system.