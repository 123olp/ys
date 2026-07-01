# public-procurement-contracting-capacity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-procurement-contracting-capacity` |
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


本目录承载 Human Infra 中“公共采购与合同能力”研究域。

## 结构

```text
public-procurement-contracting-capacity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义公共采购、合同和供应商管理如何影响主体持续性。
- 本目录只做公开资料整理、制度变量、交付链路和治理边界，不放投标策略、合同操控或采购规避内容。

## 上下游关系

- 上游：`docs/reference/research-domain-atlas.md`、`public-service-design-accessibility/`、`civic-data-open-government-transparency/`。
- 下游：医疗、应急、住房、交通、教育、数字服务、供应链、制造维修、社会保护和灾后恢复相关模型。

## 维护规则

- 公开结论必须回到官方采购、审计、发展机构、开放数据或公共治理来源。
- 不写围标、串标、利益输送、报价策略、资质规避、供应商操控或个案法律商业建议。
- 涉及具体采购项目时，只做结构性分析，不给中标或合规判断。
