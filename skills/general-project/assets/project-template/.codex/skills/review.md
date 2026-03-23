# Skill: review

## Trigger

Use for:
- pre-merge review
- self-review after implementation
- independent validation of changed scope

---

## Goal

Evaluate the changed code for correctness, side effects, and scope discipline.

Default execution route:

- use an independent `code review` sub-agent / Code Review mode when available
- if unavailable, perform the same review procedure with a normal reviewer and record the fallback

---

## Inputs

- diff
- changed files
- task file
- expected behavior

---

## Procedure

1. Review only changed scope first
2. Check correctness against intended behavior
3. Check edge cases and failure paths
4. Check unintended side effects
5. Check whether validation/tests are sufficient
6. Check whether scope expanded unnecessarily
7. Separate blocking issues from suggestions
8. State whether the review was done by Code Review mode or by fallback reviewer flow

---

## Outputs

- blocking issues
- non-blocking suggestions
- risk summary
- review conclusion

---

## Constraints

- do not redesign the feature unless required
- do not expand into unrelated modules
- do not produce vague review comments
