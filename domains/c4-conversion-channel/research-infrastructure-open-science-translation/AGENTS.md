# research-infrastructure-open-science-translation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-infrastructure-open-science-translation` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录承载科研基础设施、开放科学、可复现性、转化科学和知识扩散如何生成未来技术窗口。

## 结构

```text
research-infrastructure-open-science-translation/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只讨论科研生态和知识转化，不处理论文代写、学术操控、数据造假或机构伦理替代判断。
- 后续新增材料应优先是开放科学 Source Card、转化变量、复现性风险和技术窗口模型。

## 上下游关系

- 上游：`standards-metrology-quality-infrastructure/`、`civic-data-open-government-transparency/`、`education-access-lifelong-learning/`。
- 下游：`clinical-trials-regulatory-science-translation/`、`longevity-evidence/`、`cellular-reprogramming/`。
- 相邻域：`measurement-feedback/`、`health-data-privacy-governance/`、`synthetic-biology-biosecurity/`。

## 维护规则

- 不提供学术不端、同行评审规避、刷引用、署名操控或数据造假策略。
- 不把未经验证的预印本、新闻稿或商业叙事写成事实结论。
- 若新增研究流程、证据表或转化模型，必须同步维护本文件和相关索引。
