# mitochondrial-bioenergetics 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/mitochondrial-bioenergetics` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


`domains/c2-source-maintenance/mitochondrial-bioenergetics/` 保存线粒体生物能量学研究域。它关注细胞能源、氧化还原和线粒体质量控制如何支撑行动与恢复。

## 目录结构

```text
mitochondrial-bioenergetics/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责线粒体功能、ATP、氧化应激、线粒体 DNA、线粒体自噬和质量控制。
- 本域可整理机制文献、指标边界、疾病交叉和模型变量。
- 本域不提供补剂、药物、运动、禁食、检测解释或治疗建议。

## 维护规则

- 任何线粒体主张必须区分机制、替代指标、功能终点和安全性。
- 与肌肉、神经、心血管、免疫、睡眠和代谢交叉时必须标注主拥有域。
- 新增文件或子目录时，同步更新本文件。
