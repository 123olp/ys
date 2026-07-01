# venous-thromboembolism-pulmonary-embolism-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/venous-thromboembolism-pulmonary-embolism-continuity` |
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


本目录维护 DVT、肺栓塞、抗凝连续性和复发预防资料。它是血液凝固、循环、呼吸和移动能力交界处的急性风险域。

## 目录结构

```text
venous-thromboembolism-pulmonary-embolism-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 VTE/PE 如何改变急性死亡、氧合、右心负荷、复发和行动能力。
- 本目录只维护系统级变量、来源和边界，不保存个案影像、凝血结果、用药、癌症史、妊娠状态或住院资料。
- 资料进入本域时必须区分风险场景、诊断路径、抗凝连续性、出血权衡、复发和长期功能。

## 上下游关系

- 上游来自 ESC、CDC、NHLBI 和血栓/肺栓塞 public materials。
- 下游服务 `blood-oxygen-hemostasis/`、`respiratory-oxygenation/` 和 `transfusion-blood-management-hemorrhage-continuity/`。
- 不替代医生、急诊、血液科、心肺团队、产科或个体医疗建议。

## 维护规则

- 不写血栓诊断、影像解读、D-dimer、抗凝、溶栓、滤器、旅行、术后或妊娠建议。
- 不把系统级 VTE/PE 研究写成个人风险评分或治疗工具。
- 新增变量必须区分血栓形成、栓塞、氧合、右心、抗凝、出血和复发。
