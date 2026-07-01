# intensive-care-organ-support-delirium-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/intensive-care-organ-support-delirium-continuity` |
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


本目录维护 ICU 多器官支持、谵妄治理、恢复和 ICU 后综合征资料。它是危重病存活能否转化为有效主体持续性的研究域。

## 目录结构

```text
intensive-care-organ-support-delirium-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 ICU 支持、谵妄和恢复负担如何改变主体持续性。
- 本目录只维护系统级框架和证据边界，不保存 ICU 个案资料、设备参数、医嘱、家属记录或生命体征。
- 资料进入本域时必须保留 ICU 场景、器官支持类型、恢复结局、功能指标和禁止用途。

## 上下游关系

- 上游来自 SCCM、ICU Liberation、PADIS、危重病恢复和医院质量资料。
- 下游服务 `mechanical-ventilation-respiratory-failure-continuity/`、`ecmo-extracorporeal-life-support-continuity/`、`delirium-acute-cognitive-failure-prevention/` 和有效时间建模。
- 不替代 ICU 团队、医生、护士、呼吸治疗师、家属会议、伦理委员会或个人医疗建议。

## 维护规则

- 不写镇静、撤机、营养、感染控制、转院、预后或家属决策建议。
- 不把 ICU 质量改进资料写成个案治疗路径。
- 新增资料必须区分存活、认知恢复、身体恢复和家庭/社会恢复。
