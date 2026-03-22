# Template Map

## Intent

This skill packages the workflow shape used in the current repository into a reusable project bootstrap kit.

## Template Layout

```text
project-root/
├── AGENTS.md
└── .codex/
    ├── AGENTS.md
    ├── WORKFLOW.md
    ├── ORCHESTRATION.md
    ├── COMMIT_TEMPLATE.md
    ├── PROMPTS.md
    ├── TASK_TEMPLATE.md
    ├── skills/
    │   ├── bugfix.md
    │   ├── feature.md
    │   ├── git-commit.md
    │   ├── handoff.md
    │   ├── planning.md
    │   ├── refactor.md
    │   ├── review.md
    │   └── test.md
    └── tasks/
        ├── active/
        ├── blocked/
        ├── done/
        ├── dropped/
        └── paused/
```

## How To Use The Template

1. Run `bootstrap_project.py init <target-repo>`.
2. Inspect the generated root `AGENTS.md` and `.codex/*.md`.
3. Adjust repository-specific wording only after the generic layout is in place.
4. Run `bootstrap_project.py check <target-repo>`.
5. Use the bootstrapped repository normally through the task workflow.

## What Is Intentionally Generic

- Task levels and lifecycle
- Planner / executor / reviewer orchestration
- Commit discipline
- Feature / bugfix / refactor / validation / review routing

## What Should Be Customized Per Repository

- Product-specific rules
- Domain terms
- Additional specialized skills
- Repository-specific verification commands
