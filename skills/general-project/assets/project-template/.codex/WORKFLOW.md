# WORKFLOW.md

## 1. Purpose

This file defines task creation, task progression, task interruption, verification checkpoints, and completion rules.

---

## 2. Task Levels

### L0 — trivial
Examples:
- typo fix
- one-line rename
- tiny formatting adjustment

Rule:
- no task file required

### L1 — bounded implementation
Examples:
- small feature in one module
- isolated bug fix
- small test update

Rule:
- task file recommended

### L2 — multi-step / cross-file
Examples:
- bug investigation
- multi-file feature
- non-trivial refactor

Rule:
- task file required

### L3 — design / risky / multi-agent
Examples:
- architecture change
- broad behavior adjustment
- work that needs planner / reviewer / handoff

Rule:
- task file required
- explicit plan required
- handoff required if interrupted

---

## 3. Task Directory Layout

.codex/tasks/
- active/
- paused/
- done/
- dropped/

Optional:
- blocked/

---

## 4. One Task Per File

Each non-trivial task must use exactly one task file.

Filename format:

YYYYMMDD-HHMM-<short-kebab-title>.md

Example:

20260321-1430-login-null-crash.md

---

## 5. Task Lifecycle

Allowed transitions:

- active -> paused
- paused -> active
- active -> done
- active -> dropped
- active -> blocked
- blocked -> active
- blocked -> dropped

Do not leave work in an undefined state.

---

## 6. Task Template

```md
# Task: <short title>

## Goal
What must be achieved

## Level
L1 | L2 | L3

## Status
active | paused | blocked | done | dropped

## Owner
planner | executor | reviewer | single-agent

## Commit Mode
manual | auto

## Scope
Files / modules / behavior in scope

## Out of Scope
What must not be changed

## Context
Relevant background

## Findings
Important observations

## Files Checked
- path/file1
- path/file2

## Plan
1. ...
2. ...
3. ...

## Decisions
Key decisions already made

## Verification
What has been verified / how

## Risks
Known risks / possible side effects

## Open Questions
Unresolved issues

## Next Step
Immediate next action

## Handoff Note
Only needed when switching owner or pausing work
````

---

## 7. Create Task Rule

Create a task file immediately when any of the following is true:

* work is not L0
* work may be interrupted
* work spans multiple files
* diagnosis is required before coding
* another agent may continue the work

---

## 8. Update Task Rule

Task file must be updated when:

* scope changes
* new root-cause finding appears
* plan changes
* files changed materially
* verification completed
* task status changes
* ownership changes
* before ending the session

---

## 9. Execution Loop

For each active task, follow this loop:

1. Read current task file
2. Confirm scope
3. Read minimal relevant files
4. Update findings / plan
5. Implement one logical chunk
6. Verify minimally
7. Update task file
8. Decide:

   * continue
   * commit checkpoint
   * pause
   * handoff
   * finish

---

## 10. Verification Rule

Default:

* code-level verification
* targeted path verification
* updated tests where justified

Escalate verification when:

* behavior change is user-visible
* bug is high-impact
* refactor touches shared utility
* failure mode is expensive

Avoid full build/test unless clearly necessary.

---

## 11. Commit Rule

### Default

Commit Mode = manual

### Auto commit is allowed only if BOTH are true:

1. task file says `Commit Mode = auto`
2. user/workflow explicitly allows commit behavior

### Valid checkpoint moments

* one logical unit completed
* bug fix verified
* before risky refactor
* before task handoff
* before task switch
* before session end if useful

---

## 12. Pause Rule

Pause a task when:

* switching to another task
* waiting for user input or external dependency
* context window is getting crowded
* another agent will continue

When pausing:

* update status
* write next step
* write handoff note if needed
* move file to paused/ or blocked/

---

## 13. Done Rule

A task can be marked `done` only if:

* goal is satisfied within scope
* verification is recorded
* remaining risks are documented
* next step is either none or optional follow-up

---

## 14. Dropped Rule

Mark `dropped` if:

* task is invalid
* duplicate of another task
* no longer relevant
* blocked permanently with no planned follow-up

---
