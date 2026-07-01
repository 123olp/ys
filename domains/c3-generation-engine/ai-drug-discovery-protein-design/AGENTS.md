# ai-drug-discovery-protein-design 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-drug-discovery-protein-design` |
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


本目录维护 AI 药物发现、蛋白设计和实验闭环证据。它是未来医学技术窗口加速域，不是药物疗效库。

## 目录结构

```text
ai-drug-discovery-protein-design/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AI 生成候选、蛋白设计、结构预测和实验验证如何影响 Human Infra 的未来技术窗口。
- 本目录不保存可执行生物设计协议、受限靶点设计、病原增强、毒素设计或规避审查材料。
- 资料必须区分计算预测、体外验证、动物实验、临床候选和获批疗法。

## 上下游关系

- 上游来自结构生物学、计算化学、机器学习、自动化实验和数据资源。
- 下游服务新药供给、蛋白疗法、再生医学、癌症控制、临床转化和技术预见。
- 不替代 `clinical-trials-regulatory-science-translation/`；本目录聚焦发现和设计阶段。

## 维护规则

- 不把模型分数、结构预测或生成候选写成临床疗效。
- 不提供双重用途设计细节、实验操作协议或监管规避路径。
- 新增案例必须标注模型任务、验证层级、数据边界、失败模式和转化阶段。
