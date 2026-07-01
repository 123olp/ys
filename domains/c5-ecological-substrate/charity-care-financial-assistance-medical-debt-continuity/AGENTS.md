# charity-care-financial-assistance-medical-debt-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/charity-care-financial-assistance-medical-debt-continuity` |
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


## 职责

本目录承载 hospital financial assistance policy、charity care、limitation on charges、billing and collections、medical debt 和 extraordinary collection actions 连续性资料。

## 边界

- 只研究经济援助、医疗债务、收费限制、催收边界和公开制度。
- 不提供 charity care 申请、债务谈判、信用修复、法律、税务或个案财务建议。
- 不保存账单、收入、资产、税表、保险、信用报告、地址或催收资料。

## 结构

```text
charity-care-financial-assistance-medical-debt-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 charity care、FAP、payment plan、medical debt、collections 和 credit reporting。
- 涉及个体经济援助、催收或信用争议的内容必须转回医院、regulator、legal aid、consumer protection 和专业人员。
