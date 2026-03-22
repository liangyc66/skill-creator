# Skill: review

## Trigger

Use for:
- pre-merge review
- self-review after implementation
- independent validation of changed scope

---

## Goal

Evaluate the changed code for correctness, side effects, and scope discipline.

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