# Foster Care Aging Out Independent Living Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/foster-care-aging-out-independent-living-continuity` |
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


本目录承载寄养出离、独立生活服务、extended foster care 和成年转接资料。它不替代既有寄养/收养域，而是下钻到“保护系统结束后的持续性缺口”。

## 目录结构

```text
foster-care-aging-out-independent-living-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 Chafee、independent living、extended foster care、教育培训券、住房、医保、身份记录和永久支持关系。
- 关注青年从机构照护转向成年自主时的多系统断裂。
- 不提供个案资格、安置、福利、住房、法院、监护、教育资助、医疗或法律建议。

## 维护规则

- 新增资料必须优先引用 ACF Children's Bureau、Youth.gov、Medicaid、教育或住房公开资料。
- 必须区分政策入口、项目模型、结果评估和个案故事。
- 所有材料都要保留儿童福利、隐私、创伤知情和青年自主边界。
