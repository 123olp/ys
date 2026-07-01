# emergency-medical-services-prehospital-care 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/emergency-medical-services-prehospital-care` |
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


本目录维护急救医疗服务、院前照护与时间关键响应域。它是 Human Infra 的“急性可逆窗口接入层”，负责急性事件如何被发现、调度、稳定和转运。

## 目录结构

```text
emergency-medical-services-prehospital-care/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明 EMS、院前照护、调度、响应时间、转运和质量改进如何影响主体持续性。
- 本域只做公开 EMS 系统、政策、覆盖、质量和响应资料整理。
- 不提供急救操作、医疗处置、分诊、现场指挥、医院选择、路线、法律或危险现场建议。

## 维护规则

- 新增材料必须区分院前系统能力、个人急救教育、灾害响应和急诊院内照护。
- 不把 EMS 资料写成实时医疗指令或现场操作手册。
- 涉及急性风险时，只写系统变量、证据边界和官方求助原则，不写处置步骤。
