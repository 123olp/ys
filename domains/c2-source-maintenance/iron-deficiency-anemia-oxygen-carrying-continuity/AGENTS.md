# iron-deficiency-anemia-oxygen-carrying-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/iron-deficiency-anemia-oxygen-carrying-continuity` |
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


本目录维护铁缺乏、贫血、氧输送、疲劳、病因追踪和恢复可及资料。它关注贫血如何改变体力、认知速度和有效时间。

## 目录结构

```text
iron-deficiency-anemia-oxygen-carrying-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义铁缺乏贫血如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、月经、胃肠症状、妊娠、饮食、用药或保险资料。
- 资料进入本域时必须保留贫血类型、铁状态、来源路径、阶段性风险、治疗可及和禁止用途。

## 上下游关系

- 上游来自 NHLBI、NIH ODS、血液学、营养、妇科、胃肠和慢病资料。
- 下游服务 `blood-oxygen-hemostasis/`、`menstrual-health-cycle-literacy-continuity/` 和消化连续性模型。
- 不替代血液科、营养、妇科、胃肠科、产科、药学、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、化验判读、补铁剂量、输血、胃肠检查、月经处理、妊娠或饮食建议。
- 不把贫血资料写成补充剂计划或失血来源判断。
- 新增资料必须区分铁缺乏、其他贫血、氧输送、疲劳、来源追踪和功能结果。
