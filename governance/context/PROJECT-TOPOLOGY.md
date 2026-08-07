---
id: GOV-PROJECT-TOPOLOGY
type: index
status: current
owner: engineering
created: 2026-08-06
last_reviewed: 2026-08-06
review_cycle: P90D
---

# Project Topology

## 项目结构

| 路径 | 职责 | 禁止事项 | 主要验证 |
|---|---|---|---|
| `governance/` | 项目工程治理包、上下文路由、标准、门禁和证据记录 | 不覆盖项目原有 README、AGENTS、CI 或模块文档 | `validate_governance_package.py --strict` |
| `governance/tasks/` | 任务树、任务包和执行状态 | 不把任务临时状态直接当成长期标准 | `validate_tasks_tree.py` |
| 源代码目录 | 项目业务实现与测试 | 不绕过既有模块边界和公共接口 | 使用项目实际 test/lint/typecheck 命令 |

## 依赖方向

治理包只提供项目记忆和执行护栏；源代码目录保持业务实现职责；任务容器记录执行过程，长期有效经验再晋升到 standards、processes、architecture-gates 或 evidence。
