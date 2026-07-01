# head-start-early-head-start-family-support-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/head-start-early-head-start-family-support-continuity` |
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


`head-start-early-head-start-family-support-continuity/` 是 Human Infra 的 Head Start / Early Head Start 综合早期发展和家庭支持执行域，负责研究早期学习、健康、营养、家庭参与和转介如何支撑儿童与家庭连续性。

## 目录结构

```text
head-start-early-head-start-family-support-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 Head Start / Early Head Start 域的对象、链路、非目标和来源信号。
- 本域只整理综合服务模型、绩效标准和家庭支持变量，不做个体资格、申请、录取或项目推荐。
- 儿童记录、家庭收入、健康记录、教育记录、申请材料和家庭服务计划不得进入本域。

## 上下游关系

- 上游：`childcare-family-continuity/`、`maternal-newborn-child-development/`、`community-resource-navigation/`。
- 下游：`school-enrollment-attendance-continuity/`、`learning-skill-acquisition/`、`food-security-nutrition-access/`。

## 维护规则

- 新增资料必须说明它影响早期学习、健康、营养、家庭支持、父母参与、转介还是入学过渡。
- 禁止输出申请策略、项目选择、儿童诊断、教育处方、医疗建议或家庭个案评估。
