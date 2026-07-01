# home-refrigeration-food-storage-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-refrigeration-food-storage-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录承载家庭冷藏、冷冻、食品保存和停电食品安全连续性研究域，关注食物资源如何在家庭端保持安全、可用和可恢复。

## 目录结构

```text
home-refrigeration-food-storage-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义家庭冷藏、食品储存、停电和食品安全如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 USDA FSIS、FDA、CDC 和本地公共卫生食品安全资料。
- 不写具体食物是否可吃、疾病处理、食品处置、设备购买、召回规避或囤积建议。
- 涉及温度、时间和停电时只讨论变量、风险边界、来源信号和恢复路径。
- 新增指标必须注明口径：温度暴露窗口、停电持续时间、易腐食品比例、食品浪费、召回可达性或冷藏依赖任务。
