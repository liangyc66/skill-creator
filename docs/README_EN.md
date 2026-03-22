# skill-creator

[简体中文](../README.md) | English

This repository publishes reusable Codex skills, currently including `skills/general-project`.

## Included Skill

- `general-project`: bootstrap a reusable `.codex` workflow for the target repo, then execute general project tasks with minimal-scope changes and proportional verification.

## Repository Layout

- `skills/`: published skill sources
- `docs/`: supporting documentation

## Installation (Step-by-Step)

1. Go to this repository root.
2. Create target directory `~/.codex/skills/general-project`.
3. Copy all files from `skills/general-project` into that directory.
4. Explicitly invoke `$general-project` in your session.

### Method A: PowerShell

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills\general-project"
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Path ".\skills\general-project\*" -Destination $dest -Recurse -Force
```

### Method B: Shell (bash)

```bash
dest="$HOME/.codex/skills/general-project"
mkdir -p "$dest"
cp -R ./skills/general-project/. "$dest/"
```

## Invocation Example

```text
Use $general-project to bootstrap and handle the current repository
```
