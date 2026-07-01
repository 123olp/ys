# student-financial-aid-grant-scholarship-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/student-financial-aid-grant-scholarship-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


本目录承载学生资助、奖助学金和高等教育现金流连续性研究域，关注学习机会如何被学费、生活费、资助资格和债务风险约束。

## 目录结构

```text
student-financial-aid-grant-scholarship-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 FAFSA、Title IV、奖助学金、资助发放、SAP 和债务风险如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料必须优先回到 Federal Student Aid、FSA Partner Connect、College Scorecard、NCES/IPEDS、州资助机构和高校公开政策。
- 不写 FAFSA 填报、贷款选择、奖学金申请、还款、债务、税务、学校选择或个体资格建议。
- 涉及财务资料时，只讨论公开制度变量和风险链，不处理个人财务、税务、账号、银行或身份资料。
- 新增指标必须注明口径：cost of attendance、net price、aid offer、disbursement、SAP、debt、default 或 completion。
