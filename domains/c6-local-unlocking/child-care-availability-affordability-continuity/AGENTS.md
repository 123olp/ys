# child-care-availability-affordability-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/child-care-availability-affordability-continuity` |
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


`child-care-availability-affordability-continuity/` 是 Human Infra 的托育供给与费用可承受性执行域，负责研究名额、费用、时段、距离和年龄覆盖如何影响家庭运行与照护者有效时间。

## 目录结构

```text
child-care-availability-affordability-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义托育供给、费用和可达性执行域的对象、链路、非目标和来源信号。
- 本域只整理公开资料、指标和结构性变量，不做个体机构推荐、价格判断、排队策略或家庭安排。
- 儿童身份、家庭收入、住址、排班、托育记录和候补名单资料不得进入本域。

## 上下游关系

- 上游：`childcare-family-continuity/`、`social-protection-benefits-delivery/`、`workforce-employment-services/`。
- 下游：`time-allocation-effective-time/`、`financial-resilience-access/`、`child-care-subsidy-ccdf-payment-continuity/`。

## 维护规则

- 新增资料必须说明它影响名额、费用、时段、距离、年龄覆盖、等待时间还是照护稳定性。
- 禁止输出托育机构选择、补贴申请、儿童适配、费用建议或家庭纠纷建议。
