# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cytoskeleton-mechanotransduction-cellular-mechanics-continuity` |
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
cytoskeleton-mechanotransduction-cellular-mechanics-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义细胞骨架、机械转导、力感知、细胞形态和细胞内力学如何进入主体持续性模型。
- 本目录只承载研究域定位、机制、变量、证据边界和非目标。
- 本目录不提供训练、康复、设备、力学刺激、检测解释、实验或治疗建议。

## 维护规则

- 新资料必须区分细胞力学、组织力学、ECM、核结构、血管剪切应力和人体功能终点。
- 不把力学信号直接写成可操作的健康建议。
- 与 `extracellular-matrix-glycation/` 保持边界：本域关注细胞内力学和力信号转换，ECM 域关注组织外材料结构。
