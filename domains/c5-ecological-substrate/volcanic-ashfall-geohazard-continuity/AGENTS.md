# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/volcanic-ashfall-geohazard-continuity` |
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


## 职责

本目录维护火山喷发、火山灰和相关地质灾害对主体持续性的影响。重点是空气、水、交通、农业、建筑、设备和公共服务连续性。

## 文件

```text
volcanic-ashfall-geohazard-continuity/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c3-generation-engine/air-quality-ventilation-exposure-control/`
- `domains/c5-ecological-substrate/food-security-nutrition-access/`
- `domains/c5-ecological-substrate/water-sanitation-hygiene-continuity/`
- `domains/c5-ecological-substrate/emergency-preparedness-response/`

## 下游

- 呼吸暴露、食物水资源、交通恢复、社区韧性和基础设施维护。

## 边界

- 不输出喷发预测、避难命令、清灰操作或个人防护处方。
- 不替代 USGS、气象、公共卫生或地方应急机构。
- 只整理公开来源、机制链和研究边界。
