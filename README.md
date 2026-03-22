# skill-creator

简体中文 | [English](docs/README_EN.md)

本仓库用于发布可复用的 Codex skills，当前包含 `skills/general-project`。

## 已包含技能

- `general-project`：先为目标仓库初始化可复用的 `.codex` 工作流，再按最小改动原则执行通用项目任务并做验证。

## 目录结构

- `skills/`：技能源码（发布主体）
- `docs/`：补充文档

## 安装（步骤化）

1. 进入本仓库根目录。
2. 创建目标目录 `~/.codex/skills/general-project`（Windows 对应 `%USERPROFILE%\.codex\skills\general-project`）。
3. 复制 `skills/general-project` 下全部文件到目标目录。
4. 在会话中显式调用 `$general-project`。

### 方式 A：PowerShell

```powershell
$dest = Join-Path $env:USERPROFILE ".codex\skills\general-project"
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item -Path ".\skills\general-project\*" -Destination $dest -Recurse -Force
```

### 方式 B：Shell (bash)

```bash
dest="$HOME/.codex/skills/general-project"
mkdir -p "$dest"
cp -R ./skills/general-project/. "$dest/"
```

## 调用示例

```text
使用 $general-project 初始化并处理当前仓库
```
