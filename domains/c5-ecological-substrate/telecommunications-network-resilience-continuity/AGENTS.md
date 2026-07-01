# telecommunications-network-resilience-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/telecommunications-network-resilience-continuity` |
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


本目录维护电信网络韧性与通信连续性域。它是 Human Infra 的“主体外部连接不断线”层，负责通信网络、应急通信、冗余、备电和恢复时间如何支撑公共服务、求助和协作。

## 目录结构

```text
telecommunications-network-resilience-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明通信网络韧性、公共安全通信和应急通信如何进入主体持续性模型。
- 本域只做公开架构、韧性指标、服务连续性和非操作性资料整理。
- 不提供入侵、干扰、阻断、监听、伪基站、通信规避、网络破坏或具体敏感设施信息。

## 维护规则

- 新增资料必须区分公开政策框架、运营韧性指标、应急通信入口和敏感网络细节。
- 涉及关键通信设施时，避免可操作定位、攻击、规避或破坏信息。
- 不把通信韧性资料写成个人通信规避或攻击指南。
