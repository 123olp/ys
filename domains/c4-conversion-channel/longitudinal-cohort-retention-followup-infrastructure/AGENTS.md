# longitudinal-cohort-retention-followup-infrastructure 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/longitudinal-cohort-retention-followup-infrastructure` |
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


本目录维护纵向队列、长期随访、参与者留存和生命历程数据基础设施。它是寿命、健康寿命和有效时间模型的长期观测层。

## 目录结构

```text
longitudinal-cohort-retention-followup-infrastructure/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义队列留存、随访、失访、事件确认和数据链接如何支撑 Human Infra 定量模型。
- 本目录不保存参与者数据、队列微数据、联系信息或可识别记录。
- 所有队列材料必须保留样本范围、随访时间、结局定义、失访情况和人群适用边界。

## 上下游关系

- 上游来自参与者同意、数据治理、队列方法和公共队列资料。
- 下游服务生存分析、因果推断、数字孪生、健康寿命预测和真实世界证据。
- 不替代 `data-quality-missingness-representativeness/`；本目录关注队列运行和随访基础设施。

## 维护规则

- 不提供重新识别、越权链接、诱导留存或规避同意策略。
- 不把队列相关性写成干预因果结论。
- 若新增队列证据，必须记录样本、随访、结局、失访、偏差和适用边界。
