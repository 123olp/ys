# Technology Foresight Horizon Scanning 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/technology-foresight-horizon-scanning` |
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


## 目录结构

```text
technology-foresight-horizon-scanning/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义技术预见、地平线扫描、弱信号和情景分析在 Human Infra 中的职责边界。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载未来技术候选队列、弱信号审查和情景分析。它不承载投资建议、公司评级、市场预测、疗效断言或技术必然性叙事。

## 维护规则

- 每个未来技术信号必须区分事实、披露、推断、假设和缺失证据。
- 不允许把融资、专利、新闻稿或演示原型写成技术成熟。
- 不允许输出投资、交易或市场时机建议。
- 候选域晋升必须回到 Research Domain Atlas 的独立机制、证据体系、失败模式和伦理边界契约。
