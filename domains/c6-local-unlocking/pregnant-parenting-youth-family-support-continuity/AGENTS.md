# Pregnant Parenting Youth Family Support Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pregnant-parenting-youth-family-support-continuity` |
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


本目录承载怀孕与育儿青年学校连续、健康转接、托育、住房、营养、亲职支持和隐私边界资料。它处理基础设施和服务连续性，不处理个体医疗或家庭决策。

## 目录结构

```text
pregnant-parenting-youth-family-support-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 pregnant and parenting youth、学校连续、医疗转接、托育、营养福利、住房、亲职支持和隐私授权。
- 关注青年主体和下一代照护系统如何同时保持连续。
- 不提供怀孕、分娩、育儿、托育、福利、学校权利、医疗、心理、法律或家庭冲突建议。

## 维护规则

- 新增资料必须优先引用 Youth.gov、HHS/ACF、ED、CDC、WIC/Head Start 或公开教育/公共卫生资料。
- 涉及未成年人、怀孕、育儿、家庭关系和儿童安全时必须保留高敏感边界。
- 不把服务资料转化为个体资格判断或家庭决策建议。
