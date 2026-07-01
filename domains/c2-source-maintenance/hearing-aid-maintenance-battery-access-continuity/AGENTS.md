# hearing-aid-maintenance-battery-access-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/hearing-aid-maintenance-battery-access-continuity` |
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


本目录承载助听设备维护、电池/充电、配件、维修替换和使用训练连续性研究域，关注听觉增强设备如何保持长期可用。

## 目录结构

```text
hearing-aid-maintenance-battery-access-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义助听设备运行、维护、供电和维修如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 NIDCD、FDA、Medicare、听力康复、辅助技术和可访问沟通资料。
- 不写听力诊断、验配、参数调整、设备购买、维修教程、医保覆盖判断或品牌比较。
- 涉及儿童、认知衰退、灾害警报和公共服务时，必须保留替代沟通和可达性边界。
- 新增指标必须注明口径：供电可用性、维护可得性、配件适配、维修等待、训练负担或沟通失败后果。
