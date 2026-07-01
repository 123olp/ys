# air-quality-ventilation-exposure-control 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/air-quality-ventilation-exposure-control` |
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


本目录维护空气质量、通风与暴露控制域。它是 Human Infra 的“可呼吸环境层”，负责空气暴露如何影响呼吸、心血管、认知、工作学习和公共空间连续性。

## 目录结构

```text
air-quality-ventilation-exposure-control/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明室内外空气质量、通风、过滤、气溶胶、烟雾和监测如何支撑主体持续性。
- 本域只做公开空气质量、通风标准、暴露治理和风险沟通资料整理。
- 不提供个体医疗、HVAC 设计施工、设备采购、危险环境处置或实时灾害指挥建议。

## 维护规则

- 新增材料必须区分室外污染、室内空气、感染性气溶胶、职业/学校/照护场所和灾害烟雾。
- 不把设备评测、滤材广告、施工方案或传感器读数写成个体安全承诺。
- 涉及危险暴露时，只写公共治理和证据边界，不写现场操作步骤。
