# workforce-employment-services 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/workforce-employment-services` |
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


本目录承载就业服务、劳动力发展、学徒制、职业信息、再就业支持和合理便利如何进入 Human Infra 模型。

## 结构

```text
workforce-employment-services/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只处理就业服务与劳动力发展基础设施，不处理个体职业建议、法律争议、福利资格或招聘承诺。
- 后续资料必须区分学习能力、就业入口、岗位内工作设计和劳动权利保护。

## 上下游关系

- 上游：`learning-skill-acquisition/`、`digital-inclusion-connectivity/`、`public-service-design-accessibility/`。
- 下游：`financial-resilience-access/`、`occupational-work-design/`、`labor-rights-workplace-protection/`。
- 相邻域：`assistive-technology-access/`、`time-allocation-effective-time/`、`social-protection-benefits-delivery/`。

## 维护规则

- 不提供个体职业规划、简历、面试、工资、劳动争议、移民或福利建议。
- 不支持歧视性筛选、虚假招聘、培训骗局、劳动者监控或剥削性匹配。
- 若新增职业数据或服务资料，必须标注来源、地区、时效和使用边界。
