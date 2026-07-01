# endocrine-hormonal-regulation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/endocrine-hormonal-regulation` |
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


`domains/c2-source-maintenance/endocrine-hormonal-regulation/` 保存内分泌与激素调节研究域。它关注跨器官激素信号如何维持主体稳态、恢复和长期行动能力。

## 目录结构

```text
endocrine-hormonal-regulation/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责激素轴、反馈环、代谢信号、压力反应、生殖、骨骼和跨器官稳态。
- 本域可整理公开内分泌资料、疾病分类、机制和模型变量。
- 本域不提供检测解释、激素补充、处方、剂量、周期管理、停药或治疗建议。

## 维护规则

- 任何激素主张必须说明轴、变量、反馈机制、适用边界和证据等级。
- 涉及检测、药物或补充时只写证据边界，不写个体方案。
- 新增文件或子目录时，同步更新本文件。
