# COMMIT_TEMPLATE.md

## 1. Purpose

Standardize commit messages and checkpoint summaries to ensure:

- clarity
- traceability
- automation compatibility

---

## 2. Commit Message Format

```

<type>: <short summary>

````

### Types

- fix       → bug 修复
- feat      → 新功能
- refactor  → 重构（无行为变化）
- test      → 测试相关
- docs      → 文档
- chore     → 杂项

---

## 3. Commit Message Body Template

```md
Why:
- 为什么要做这次修改

What:
- 修改了什么（关键点）

Scope:
- 影响范围（模块 / 文件）

Verification:
- 如何验证
- 验证结果

Risks:
- 潜在风险 / 未覆盖情况
````

---

## 4. Example

```text
fix: prevent null crash in login state mapping

Why:
- 登录状态映射在空值情况下触发崩溃

What:
- 增加 null 判断
- 添加 fallback 分支

Scope:
- login module
- session mapper

Verification:
- 手动验证崩溃路径
- 正常登录流程未受影响

Risks:
- fallback 逻辑未覆盖极端异常数据
```

---

## 5. Checkpoint Summary Template

用于阶段性总结（不一定提交代码）

```md
## Checkpoint Summary

### Completed
- 已完成内容

### Files Changed
- path/file1
- path/file2

### Key Decisions
- ...

### Verification
- 做了哪些验证
- 结果如何

### Risks
- 当前已知风险

### Next Step
- 下一步计划
```

---

## 6. Commit Rules

* one commit = one logical unit
* 不混入无关修改
* 信息必须可读、可追溯
* 禁止使用模糊描述（如“update code”）

---

## 7. Auto Commit Safety

自动提交必须满足：

1. Commit Mode = auto
2. 用户允许
3. 当前为完整逻辑单元

---

## 8. Anti-Patterns

禁止：

* fix bug
* update code
* improve logic
* minor changes

必须说明：

* 改什么
* 为什么
* 影响范围

---

## 9. Final Principle

> A commit should explain the change without reading the diff.

---
