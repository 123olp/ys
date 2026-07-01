# home-care-task-coordination-care-plan-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-care-task-coordination-care-plan-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
| 路径真相源 | `domains/_possibility-space-control/classification.tsv` |
| 复核状态 | `heuristic-v0.1` |

### 文件职责

- `README.md` 面向读者，说明研究对象、Human Infra 价值链路、证据边界、非目标和下一步资料入口。
- `AGENTS.md` 面向维护者和代理，说明目录结构、上下游依赖、禁止事项、更新规则和验证要求。

### 更新规则

- 修改本域对象、边界或上下游关系时，必须同步检查 README、AGENTS 和分类表中的 `physical_path`。
- 新增资料优先沉淀为 Source Signals、Source Cards、Claim-Evidence Matrix 或明确的证据段落，不把未经核验的摘要写成稳定结论。
- 若发现当前层级不符合“可能性空间控制力”标尺，先修改 `_possibility-space-control/rubric.md` 或 `classification.tsv`，再移动目录。

### 禁止事项

- 不把研究域写成个体行动处方、临床建议、法律建议、投资建议、工程操作手册或规避规则指南。
- 不在本目录保存无来源、无边界、无证据等级的断言。
- 不绕过父级 C1-C6 物理目录直接在 `domains/` 根目录新增正式研究域。
<!-- domain-agent-contract:end -->


本目录维护家庭照护任务协调、care plan、责任分工、提醒、交接和异常升级连续性资料。它关注任务系统，不生成个人照护计划。

## 目录结构

```text
home-care-task-coordination-care-plan-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明家庭照护任务协调如何降低遗漏、重复、责任漂移、认知负荷和服务断点。
- 本目录只整理公开资料、机制链路、工具边界和隐私风险。
- 不保存个人健康数据、家庭日历、照护计划、药物表、家庭分工、门户账号或设备资料。

## 维护规则

- 新增资料必须区分 care coordination、care plan、family task management、patient portal proxy access 和临床医嘱。
- 不生成个人任务清单、用药表、预约计划、护理操作、监控方案或家庭纠纷裁决。
- 涉及共享工具时，必须保留同意、代理访问、最小数据和撤回边界。
