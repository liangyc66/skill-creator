# AGENTS.md

## 1. Authority

- Product docs define WHAT to build
- AGENTS.md defines HOW all agents operate
- WORKFLOW.md defines task lifecycle
- ORCHESTRATION.md defines multi-agent collaboration
- skills/ define task-specific procedures

If rules conflict, priority is:

1. User instruction
2. Safety rules
3. AGENTS.md
4. WORKFLOW.md
5. ORCHESTRATION.md
6. Relevant skill file

---

## 2. Core Principles

- Correctness > speed
- Clarity > cleverness
- Minimal change > broad rewrite
- Explicit reasoning > hidden assumptions
- Reuse > rebuild

---

## 3. Scope Control (Hard Rule)

Read only what is necessary.

### File reading priority

1. User-specified files
2. Current task file
3. Entry point / directly changed files
4. Direct imports / callers / callees
5. Related tests
6. Relevant docs only if needed

Do NOT scan the whole repository unless explicitly required.

---

## 4. Change Policy

All changes must be:

- Small
- Localized
- Traceable
- Reversible where possible

Avoid:

- Unrelated refactors
- Style-only mass edits
- Speculative cleanup
- New abstractions without clear benefit

---

## 5. Before Coding

Must identify:

- Goal
- Scope
- Constraints
- Dependencies
- Risks
- Verification approach

For non-trivial work, this must be recorded in a task file.

---

## 6. During Coding

- Follow existing conventions
- Reuse existing code paths where possible
- Prefer direct fixes over architectural expansion
- Keep logic explicit
- Do not silently alter behavior beyond scope

---

## 7. After Coding

Always provide:

- What changed
- Why it changed
- Files modified
- Verification performed
- Remaining risks
- Suggested next step

If task-based workflow is active, update the task file first.

---

## 8. Testing & Verification

Default rule:

- Run the minimum verification necessary to justify the change

When modifying core logic:

- Add or update targeted tests when practical
- Verify affected code path explicitly

Do NOT run full repo build/test unless:

- User asks for it
- Change is high risk
- Localized verification is insufficient

---

## 9. Task Discipline

Non-trivial work MUST use WORKFLOW.md.

Non-trivial means any of:

- More than one logical step
- More than one file
- Bug investigation
- Cross-module impact
- Refactor
- Interruptible work
- Work requiring handoff

---

## 10. Git Discipline

- Never commit, amend, rebase, or push unless allowed by workflow and user authorization
- Commit behavior is governed by WORKFLOW.md and skills/git-commit.md
- If authorization is unclear, assume manual mode

---

## 11. Multi-Agent Discipline

When multiple agents are involved:

- One planner / coordinator defines the task boundary
- One executor changes code at a time unless explicitly partitioned
- Reviewer does not expand scope beyond changed area
- Handoff must be written, not implicit

See ORCHESTRATION.md.

---

## 12. Safety Rules

Never:

- Expose or modify secrets without reason
- Change infra / env / credentials casually
- Introduce breaking change silently
- Edit unrelated modules
- Fabricate verification results
- Claim a task is done if unresolved blockers remain

---

## 13. Final Principle

> Make the smallest correct change with the clearest justification and the lowest collateral impact.