# Data Breach Notification Identity Recovery Continuity 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/data-breach-notification-identity-recovery-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录承载数据泄露通知与身份恢复研究。它不保存真实泄露资料，不提供攻击、账号接管、索赔、冻结解冻或身份恢复代办。

## 目录结构

```text
data-breach-notification-identity-recovery-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须围绕通知变量、暴露数据类型、恢复入口和长期风险，不写个案处置。
- 禁止加入泄露数据库、暗网搜索、撞库、社工、身份盗用或账号接管内容。
- 与 `digital-identity-security/`、`fraud-scams-consumer-protection/` 和 `credit-consumer-reporting-access-continuity/` 保持边界。
