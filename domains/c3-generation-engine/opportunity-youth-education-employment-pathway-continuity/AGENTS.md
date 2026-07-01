# Opportunity Youth Education Employment Pathway Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/opportunity-youth-education-employment-pathway-continuity` |
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


本目录承载机会青年、断线青年、替代教育、职业训练、学徒前路径和就业入口连续性资料。它连接教育、就业和基本需求支持，不提供个案职业建议。

## 目录结构

```text
opportunity-youth-education-employment-pathway-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 opportunity youth、high-school equivalency、alternative education、Job Corps、YouthBuild、职业训练、支持服务和证书转接。
- 关注青年重新进入学习和工作路径所需的交通、托育、住房、身份和支持接口。
- 不提供项目申请、就业匹配、简历、资格判断、职业规划、贷款、福利或法律建议。

## 维护规则

- 新增资料必须优先引用 Youth.gov、DOL、ED、地方劳动力系统或公开评估资料。
- 必须区分项目入口、资格规则、服务模型、结果研究和宣传材料。
- 不把就业率或工资数据转化为个人承诺。
