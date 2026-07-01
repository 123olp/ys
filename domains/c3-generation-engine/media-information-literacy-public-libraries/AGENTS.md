# media-information-literacy-public-libraries 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/media-information-literacy-public-libraries` |
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


本目录承载媒体与信息素养、公共图书馆、可信知识入口和社区学习空间如何支撑主体判断与任务完成。

## 结构

```text
media-information-literacy-public-libraries/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只讨论信息判断能力与公共知识基础设施，不提供宣传、操控或平台规避方法。
- 后续新增材料应优先是媒体素养 Source Card、公共图书馆数据来源、服务变量和误导风险边界。

## 上下游关系

- 上游：`information-integrity-trust/`、`digital-inclusion-connectivity/`、`language-access-plain-communication/`。
- 下游：`learning-skill-acquisition/`、`public-service-design-accessibility/`、`civic-participation-election-access/`。
- 相邻域：`health-literacy-navigation/`、`community-resource-navigation/`、`ai-agency-safety/`。

## 维护规则

- 不提供操纵传播、虚假内容、微定向、信息战或平台规避策略。
- 不把公共图书馆写成专业医疗、法律、福利或危机服务的替代。
- 若新增数据、图表或服务地图，必须同步维护本文件和相关索引。
