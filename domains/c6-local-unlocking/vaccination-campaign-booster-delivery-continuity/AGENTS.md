# vaccination-campaign-booster-delivery-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/vaccination-campaign-booster-delivery-continuity` |
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


`domains/c6-local-unlocking/vaccination-campaign-booster-delivery-continuity/` 是 Human Infra 的疫苗行动与加强针递送连续性域，负责把免疫技术转化为暴发期间可达、及时、公平的群体保护。

## 目录结构

```text
vaccination-campaign-booster-delivery-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义疫苗行动、加强针递送、冷链、预约、提醒、高风险覆盖和可达公平的对象、链路、非目标和来源信号。
- 本域只整理公共卫生行动资料、执行变量和边界。
- 个体接种建议、禁忌判断、医学风险解释、预约代办、证明伪造和冷链操作不属于本域。

## 上下游关系

- 上游：`immunization-public-health-surveillance/`、`pharmaceutical-quality-supply-integrity/` 和 `pharmacovigilance-drug-safety-monitoring/`。
- 下游：`school-workplace-outbreak-operations-continuity/`、`immunization-record-proof-continuity/` 和 `healthcare-surge-triage-capacity-continuity/`。

## 维护规则

- 新增资料必须说明它支持递送、覆盖、冷链、预约、提醒、信任还是公平。
- 不能输出接种医学建议、优先级规避、证明伪造、冷链操作或个体风险判断。
