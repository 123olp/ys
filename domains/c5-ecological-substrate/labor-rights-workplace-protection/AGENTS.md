# labor-rights-workplace-protection 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/labor-rights-workplace-protection` |
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


`domains/c5-ecological-substrate/labor-rights-workplace-protection/` 是 Human Infra 的劳动权利与工作场所保护域，负责把工资工时、安全权利、反歧视、反报复、申诉和劳动组织治理建模为工作连续性的制度条件。

## 目录结构

```text
labor-rights-workplace-protection/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义劳动标准、工资工时、安全权利、反歧视、申诉入口和组织治理的对象、链路、非目标和来源信号。
- 本域只做公开资料整理、变量建模、证据边界和权利执行断点分析。
- 个案法律意见、工资计算、雇佣分类、投诉策略、劳动组织策略、谈判策略和胜诉承诺不属于本域。

## 上下游关系

- 上游：`governance-rights/`、`language-access-plain-communication/` 和 `access-to-justice-legal-aid/`。
- 下游：`occupational-work-design/`、`financial-resilience-access/`、`mental-health-affective-stability/` 和 `time-allocation-effective-time/`。

## 维护规则

- 新增资料必须说明它支持的是劳动标准、工资工时、安全权利、反歧视、反报复、申诉执行还是组织治理变量。
- 不能把劳动资料写成个案法律判断、劳动争议策略或规避程序建议。
