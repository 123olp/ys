# cognitive-augmentation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/cognitive-augmentation` |
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


`domains/c3-generation-engine/cognitive-augmentation/` 保存认知增强研究域。它关注 AI、工具、外部记忆、学习系统和脑机接口如何放大主体行动能力。

## 目录结构

```text
cognitive-augmentation/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责认知与工具增强的机制、变量和风险。
- 本域可整理 AI 协作、知识管理、外部记忆、学习增强和 BCI 高层资料。
- 本域不提供侵入式神经操作、药物增强、人体实验或个体治疗建议。

## 维护规则

- 任何增强主张必须同时审查自主性、依赖、权利、可解释性和失败模式。
- 不把工具表现直接等同于主体能力；必须说明主体是否仍能理解、选择和退出。
- 新增文件或子目录时，同步更新本文件。
