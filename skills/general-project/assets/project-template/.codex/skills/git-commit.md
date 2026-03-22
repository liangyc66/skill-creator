# Skill: git-commit

## Trigger

Use for:
- logical checkpoint
- completed task segment
- handoff boundary
- verified bug fix / feature slice

---

## Goal

Create small, meaningful, reviewable commits.

---

## Preconditions

Commit only when allowed by:
- user authorization
- AGENTS.md
- WORKFLOW.md
- task Commit Mode

---

## Procedure

1. Confirm scope of change
2. Exclude unrelated files
3. Group only one logical unit
4. Write precise commit message
5. Commit at checkpoint boundary only

---

## Commit Message Format

<type>: <summary>

Recommended types:
- fix
- feat
- refactor
- test
- docs
- chore

Examples:
- fix: prevent null crash in login state mapping
- feat: add retry action for network timeout card
- refactor: simplify session validation branch
- test: cover empty response fallback

---

## Constraints

- never commit secrets
- never combine unrelated changes
- never use vague messages
- never commit automatically without explicit permission