# ORCHESTRATION.md

## 1. Purpose

Defines how multiple agents collaborate on one repository without conflict, duplicated effort, or scope drift.

---

## 2. Roles

### Planner
Responsible for:
- understanding request
- defining scope
- creating / updating task plan
- selecting relevant skill
- assigning owner

Planner does NOT perform broad code changes unless acting as single-agent.

### Executor
Responsible for:
- reading minimal relevant code
- implementing changes
- updating findings and verification
- keeping within scope

### Reviewer
Responsible for:
- checking correctness
- checking side effects
- checking missing validation/tests
- checking scope discipline

Reviewer does NOT redesign the task unless explicitly requested.

### Handoff Agent
Responsible for:
- compressing current state
- writing continuation note
- making next step explicit

This role may be performed by planner or executor.

---

## 3. Single-Agent Mode

If only one agent is working, that agent temporarily plays:

planner + executor + lightweight reviewer

Still follow:
- task discipline
- verification discipline
- handoff discipline if interrupted

---

## 4. Multi-Agent Activation

Use multi-agent mode when task is L3 or when any of the following is true:

- broad task needs decomposition
- bug diagnosis and implementation should be separated
- review must be independent
- task is likely to span multiple sessions

---

## 5. Ownership Rule

At any time, each active task has exactly one current owner.

Allowed owners:
- planner
- executor
- reviewer
- single-agent

Never allow two agents to edit the same scope simultaneously unless explicitly partitioned.

---

## 6. Scope Partition Rule

If multiple executors are used, partition by:

- module boundary
- file boundary
- feature slice
- verification slice

Avoid partitioning by vague responsibility.

Good:
- Agent A: API layer
- Agent B: UI rendering
- Agent C: tests

Bad:
- Agent A: “part of the bug”
- Agent B: “the rest”

---

## 7. Handoff Rule

A handoff is required when:

- task owner changes
- task is paused
- session ends before completion
- reviewer sends issue back to executor

Handoff must include:

- current status
- completed work
- files changed or checked
- known risks
- exact next step
- what not to re-read unless needed

---

## 8. Review Loop

Recommended flow for L3:

1. Planner defines scope and task
2. Executor implements first logical chunk
3. Reviewer checks changed area
4. Executor resolves issues if needed
5. Planner decides:
   - continue
   - checkpoint
   - finish
   - split follow-up task

---

## 9. Conflict Resolution

If rules conflict:

1. user instruction
2. AGENTS.md
3. WORKFLOW.md
4. ORCHESTRATION.md
5. skill file

If planner and reviewer disagree:
- prefer smaller scope
- prefer safer change
- record decision in task file

---

## 10. Anti-Patterns

Do NOT:

- let reviewer silently expand the task
- let executor refactor unrelated code “while here”
- let planner define vague next steps
- leave ownership unclear
- duplicate reading across agents without reason

---

## 11. Completion Contract

Before closing a multi-agent task, ensure:

- task file is updated
- verification is recorded
- review outcome is recorded
- remaining risks are explicit
- next optional follow-up is separated from current task
````

---
