# skill-creator

## 中文说明

本仓库用于发布可复用的 Codex skills，当前包含 `skills/general-project`。

### 已包含技能

- `general-project`：先为目标仓库初始化可复用的 `.codex` 工作流，再按最小改动原则执行通用项目任务并做验证。

### 目录结构

- `skills/`：技能源码（发布主体）
- `docs/`：补充文档

### 安装示例（PowerShell）

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills\general-project"
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Path ".\skills\general-project\*" -Destination $dest -Recurse -Force
```

安装后可在会话中显式调用：

```text
使用 $general-project 初始化并处理当前仓库
```

## English

This repository publishes reusable Codex skills, currently including `skills/general-project`.

### Included Skill

- `general-project`: bootstrap a reusable `.codex` workflow for the target repo, then execute general project tasks with minimal-scope changes and proportional verification.

### Repository Layout

- `skills/`: published skill sources
- `docs/`: supporting documentation

### Installation Example (PowerShell)

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills\general-project"
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Path ".\skills\general-project\*" -Destination $dest -Recurse -Force
```

After installation, explicitly invoke it in a session:

```text
Use $general-project to bootstrap and handle the current repository
```
