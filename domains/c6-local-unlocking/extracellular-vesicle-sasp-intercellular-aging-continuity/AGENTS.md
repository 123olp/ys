# extracellular-vesicle-sasp-intercellular-aging-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/extracellular-vesicle-sasp-intercellular-aging-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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


`domains/c6-local-unlocking/extracellular-vesicle-sasp-intercellular-aging-continuity/` 保存细胞外囊泡、SASP 和细胞间衰老通讯研究域。

## 目录结构

```text
extracellular-vesicle-sasp-intercellular-aging-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责 EV、SASP、衰老信号传播、组织微环境和细胞间通讯风险建模。
- 本域可整理 exosome/EV 文献、SASP 传播、递送平台和测量质量边界资料。
- 本域不提供 exosome 产品、细胞培养、提取注射、检测解读、临床或商业建议。

## 维护规则

- 所有 EV/SASP 主张必须标注样本来源、分离方法、cargo 异质性、模型物种和证据阶段。
- 与 `cellular-senescence-clearance/` 和 `nanomedicine-targeted-delivery-molecular-repair/` 交叉时区分信号机制、递送平台和治疗声称。
- 新增文件或子目录时同步更新本文件。
