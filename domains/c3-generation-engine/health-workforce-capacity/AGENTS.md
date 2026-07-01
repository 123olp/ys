# health-workforce-capacity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/health-workforce-capacity` |
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


本目录承载健康劳动力供给、分布、训练、保留、负荷和团队容量如何影响医疗可达性与主体持续性。

## 结构

```text
health-workforce-capacity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只讨论健康劳动力作为系统容量，不处理个人执照、薪资、移民、用工争议或择医排名。
- 后续新增材料应优先是劳动力数据 Source Card、短缺变量、团队模型和 AI 替代边界。

## 上下游关系

- 上游：`healthcare-access-continuity/`、`occupational-work-design/`、`labor-rights-workplace-protection/`。
- 下游：`patient-safety-organizational-learning/`、`rehabilitation-functioning/`、`caregiving-long-term-care/`。
- 相邻域：`community-health-workers-peer-support/`、`medicine-access-treatment-continuity/`、`emergency-preparedness-response/`。

## 维护规则

- 不提供个人职业、执照、招聘、薪资、移民或劳动争议建议。
- 不用劳动力短缺叙事支持降低安全、压榨工作者或取消专业责任。
- 若新增数据表、预测或地图，必须同步维护本文件和相关索引。
