# emergency-alerts-communications 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/emergency-alerts-communications` |
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


本目录承载公共预警、应急通信、911/NG911、天气广播和第一响应通信如何进入主体持续性模型。

## 结构

```text
emergency-alerts-communications/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只做非操作性资料整理和变量建模，不提供现场应急、调度、通信或警报发布指导。
- 后续资料必须区分官方系统说明、标准、统计、案例和传播性解释。

## 上下游关系

- 上游：`risk-engineering/`、`digital-inclusion-connectivity/`、`language-access-plain-communication/`。
- 下游：`emergency-preparedness-response/`、`disaster-recovery-relief-continuity/`、`personal-safety-violence-prevention/`。
- 相邻域：`public-service-design-accessibility/`、`transportation-access-mobility/`、`social-connection-relational-infra/`。

## 维护规则

- 不提供实时应急建议、路线、急救、无线电或警报发布操作。
- 不输出可用于伪造、干扰、冒充或滥用公共通信系统的信息。
- 若新增案例或指标，必须保留来源、时间、地区和适用边界。
