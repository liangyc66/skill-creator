# Skill: bugfix

## Trigger

Use for:
- broken behavior
- investigation before implementation
- regression repair
- root-cause-driven fixes

---

## Goal

Identify the real failure cause and apply the smallest correct fix.

---

## Inputs

- observed symptom
- expected behavior
- error output or failing path
- relevant task file

---

## Procedure

1. State the failure clearly
2. Confirm expected behavior
3. Reproduce or narrow the failing path
4. Identify root cause before editing
5. Fix only the necessary logic
6. Verify the failing path and one adjacent non-failing path
7. Record root cause and residual risk

---

## Outputs

- root cause summary
- fix summary
- files changed
- verification result
- residual risk

---

## Constraints

- do not patch symptoms without evidence
- do not widen scope during investigation
- do not claim a fix without validating the failure path
