# weatherization-insulation-air-sealing-thermal-envelope-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/weatherization-insulation-air-sealing-thermal-envelope-continuity` |
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


本目录承载天气化、保温、气密与住宅围护结构连续性研究域，关注热边界、湿气边界和空气交换如何支撑居住、睡眠、照护和恢复空间。

## 目录结构

```text
weatherization-insulation-air-sealing-thermal-envelope-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义保温、气密、围护结构、能源负担、潮湿和室内空气平衡如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 DOE/Energy Saver、Weatherization Assistance Program、EPA、地方建筑规范、能源审计和公共卫生资料。
- 不写施工教程、材料选择、补贴申请、能效审计、通风设计、霉菌清理、房屋交易或个案住房建议。
- 新增指标必须注明口径：热边界、空气渗漏、保温状态、湿气风险、通风平衡、能源负担或任务后果。
- 涉及霉菌、燃烧设备、通风不足、灾后修复或低收入天气化时，必须保留专业评估和公共安全边界。
