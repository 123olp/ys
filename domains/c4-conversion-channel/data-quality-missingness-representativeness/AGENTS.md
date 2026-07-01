# Data Quality Missingness Representativeness 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/data-quality-missingness-representativeness` |
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


## 目录结构

```text
data-quality-missingness-representativeness/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义数据质量、缺失机制、代表性、测量误差和数据入口门禁。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载数据入口审查、偏差识别和代表性治理。它不承载个人数据处理、数据再识别、隐私规避、数据爬取、数据买卖、伪造清洗或统计操控。

## 维护规则

- 所有数据源必须声明来源、覆盖对象、采集机制、缺失机制、测量误差和适用边界。
- 不允许用代表性不足的数据推导普遍化结论。
- 不允许把 imputation 后的数据写成真实观测。
- 涉及隐私、同意、授权或数据权利时必须转向 `health-data-privacy-governance/`。
