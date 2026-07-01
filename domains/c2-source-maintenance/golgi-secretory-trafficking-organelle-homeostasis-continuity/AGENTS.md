# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/golgi-secretory-trafficking-organelle-homeostasis-continuity` |
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


## 目录结构

```text
golgi-secretory-trafficking-organelle-homeostasis-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义 Golgi 运输、分泌通路、糖基化、细胞器压力和细胞供应链如何进入主体持续性模型。
- 本目录只整理机制、变量、证据边界和非目标。
- 本目录不提供 Golgi 调节、糖基化调节、金属离子调节、补剂、检测或临床建议。

## 维护规则

- 新资料必须说明它支持的是 Golgi 结构、运输、分泌、ECM、疾病机制还是人体结局。
- 不把细胞器压力响应或分泌信号外推为抗衰疗法。
- 与 `extracellular-matrix-glycation/` 的关系必须保持清楚：本域关注细胞内加工和输出，ECM 域关注组织外结构材料。
