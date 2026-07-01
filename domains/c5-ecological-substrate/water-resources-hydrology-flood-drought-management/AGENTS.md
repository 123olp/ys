# Water Resources Hydrology Flood Drought Management

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/water-resources-hydrology-flood-drought-management` |
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


本目录承载水资源、水文、洪水和干旱管理研究，关注 WASH 之前的水底座。

## 目录结构

```text
water-resources-hydrology-flood-drought-management/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究水文观测、流域、地下水、水库、洪水、干旱、水资源管理和水安全。
- 上游连接天气气候和土地系统；下游连接饮水卫生、农业、能源、住房、交通和灾害恢复。
- 不提供实时应急、工程调度、水权、取水许可、保险或农业投资建议。

## 维护规则

- 水文资料必须标明时空尺度、观测来源和官方预警边界。
- 洪水和干旱信息不得替代实时官方预警、撤离或工程决策。
- 涉及水权、跨境水、工程设计和许可时，只保留公共研究材料，不做个案判断。
