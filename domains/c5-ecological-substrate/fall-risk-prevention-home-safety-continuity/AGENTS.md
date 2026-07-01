# fall-risk-prevention-home-safety-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/fall-risk-prevention-home-safety-continuity` |
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


本目录维护跌倒风险筛查、家居安全、药物/视力/平衡/肌力接口、跌倒后复盘和恐惧回避资料。它是主体在骨折、TBI、机构化和行动半径收缩之前的日常安全执行域。

## 目录结构

```text
fall-risk-prevention-home-safety-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义跌倒风险识别、家居安全、药物审查、平衡接口和跌倒后恢复如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案居住平面、跌倒史、药物、影像、视频、位置或诊疗资料。
- 资料进入本域时必须保留环境层级、身体接口、隐私风险、伤害结局和禁止用途。

## 上下游关系

- 上游来自 CDC STEADI、CDC falls、NIA 和跌倒预防资料。
- 下游服务 `musculoskeletal-integrity/`、`vestibular-balance-spatial-orientation/`、`osteoporosis-fracture-prevention-bone-health-continuity/` 和居家安全建模。
- 不替代医生、物理治疗、职业治疗、急诊、家居改造、保险或法律服务。

## 维护规则

- 不写跌倒风险判断、训练动作、药物调整、辅具选择、家居改造、活动许可、急救或康复建议。
- 不生成监控布置、责任判断、保险、法律或个案安全方案。
- 新增变量必须区分风险筛查、环境、身体接口、跌倒后复盘、恐惧回避和长期行动能力。
