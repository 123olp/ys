# science-communication-evidence-translation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/science-communication-evidence-translation-continuity` |
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


本目录负责科学传播、风险沟通和证据转译连续性。

## 结构

```text
science-communication-evidence-translation-continuity/
├── AGENTS.md
└── README.md
```

## 边界

- 只维护科学传播、公众理解、风险沟通、不确定性表达和传播边界。
- 上游：`domains/c4-conversion-channel/trustworthy-scientific-communication-peer-review/`、`domains/c3-generation-engine/media-information-literacy-public-libraries/`。
- 下游：README、Web 论文页、推文材料、社区传播和模型解释。
- 不提供宣传操控、恐慌传播、微定向说服、伪科学包装、疗效承诺或政策游说。

## 维护规则

使用 National Academies、WHO、NIH 和 CDC clear communication 资料作为锚点。传播材料必须保留主张边界、不确定性、适用对象和行动边界。
