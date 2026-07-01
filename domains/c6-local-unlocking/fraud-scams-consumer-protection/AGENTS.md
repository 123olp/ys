# fraud-scams-consumer-protection 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/fraud-scams-consumer-protection` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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


本目录维护诈骗、欺诈与消费者保护域。它是 Human Infra 的“资源、身份和服务入口不被欺诈夺走”层，负责诈骗风险、举报恢复和消费者保护如何影响主体持续性。

## 目录结构

```text
fraud-scams-consumer-protection/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明诈骗、钓鱼、身份盗用、金融欺诈、投诉举报、身份恢复和消费者保护如何影响主体持续性。
- 本域只做公开消费者保护、诈骗防护、身份恢复和举报系统资料整理。
- 不提供追款、法律、投资、银行、平台申诉、诈骗脚本、钓鱼、账户接管、洗钱或反侦测建议。

## 维护规则

- 新增材料必须区分诈骗类型、消费者保护、身份恢复、平台治理、金融入口和风险沟通。
- 不把受害者责任化，不提供可复制诈骗或规避检测的内容。
- 涉及金融和法律时，只写公共资料和边界，不写个案策略。
