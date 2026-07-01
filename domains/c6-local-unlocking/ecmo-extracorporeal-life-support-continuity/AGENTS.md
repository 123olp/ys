# ecmo-extracorporeal-life-support-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/ecmo-extracorporeal-life-support-continuity` |
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


本目录维护 ECMO/ECLS、体外生命支持和极端心肺衰竭桥接资料。它是短期保留主体未来选择权的高风险器官支持域。

## 目录结构

```text
ecmo-extracorporeal-life-support-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 ECMO 如何改变极端心肺衰竭中的存活窗口、并发症和退出条件。
- 本目录只维护来源、变量和安全边界，不保存个案参数、抗凝数据、病历、转运资料或费用资料。
- 资料进入本域时必须保留支持模式、中心能力、桥接目标、并发症、退出路径和禁止用途。

## 上下游关系

- 上游来自 ELSO、NIH、ICU、呼吸衰竭、循环支持和移植资料。
- 下游服务 `mechanical-ventilation-respiratory-failure-continuity/`、`intensive-care-organ-support-delirium-continuity/` 和高风险等待窗口建模。
- 不替代 ECMO 团队、ICU、心外/胸外/呼吸/麻醉团队、伦理委员会、转运中心或个人医疗建议。

## 维护规则

- 不写适应证、抗凝、泵机、转运、撤机、预后或中心选择建议。
- 不把 ECMO 描述成通用延寿或未来等待技术。
- 新增资料必须同时记录收益窗口和并发症/退出门槛。
