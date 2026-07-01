# Disembodied CNS 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/disembodied-cns` |
| 所属层级 | `C1` - 可能性边界改写层 |
| 父级容器 | `domains/c1-boundary-rewriting` |
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


`disembodied-cns/` 是去具身外部维持型中枢生命系统研究域。它只做高层系统建模、证据问题、风险分类和伦理边界，不提供实验操作协议。

## 目录结构

```text
disembodied-cns/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义具身半自主开放生命系统与去具身外部维持型中枢生命系统的对照、接口架构、研究对象和非目标。

## 上下游关系

- 上游依赖 `docs/explanations/human-runtime-infrastructure.md` 的 Human Infra 总模型和 `docs/reference/ethics-and-safety-boundaries.md` 的安全边界。
- 与 `memory-editing/` 共享主体连续性、可表达性、可退出性和尊严原则。
- 不依赖 `longevity-evidence/` 的数据采集脚本；两者只共享证据追溯和风险表达原则。

## 维护规则

- 新增内容必须保持非操作性、非实验步骤、非人体改造指南。
- 技术讨论必须围绕系统边界、接口、控制、反馈、故障、验证和伦理。
- 不宣称当前技术已经实现脱离身体的长期人格保存。
