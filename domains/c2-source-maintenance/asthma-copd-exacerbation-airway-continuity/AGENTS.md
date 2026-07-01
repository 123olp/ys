# asthma-copd-exacerbation-airway-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/asthma-copd-exacerbation-airway-continuity` |
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


本目录维护哮喘急性发作、COPD 急性加重和气道连续性资料。它是日常呼吸管理和机械通气之间的时间关键研究域。

## 目录结构

```text
asthma-copd-exacerbation-airway-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义气道急性加重如何改变缺氧、住院、呼吸支持、再入院和有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、氧饱和度、肺功能、用药、设备或位置数据。
- 资料进入本域时必须区分触发物、药物可及、急诊接入、住院支持、呼吸支持和恢复交接。

## 上下游关系

- 上游来自 GINA、GOLD、NHLBI 和呼吸系统 public materials。
- 下游服务 `respiratory-oxygenation/`、`home-oxygen-respiratory-equipment-supply-continuity/` 和 `mechanical-ventilation-respiratory-failure-continuity/`。
- 不替代医生、急诊、呼吸科、药师、EMS 或个体医疗建议。

## 维护规则

- 不写吸入药、氧疗、雾化、激素、抗生素、峰流速、急诊分诊、设备设置或家庭处理建议。
- 不把系统级气道连续性研究写成个人哮喘/COPD action plan。
- 新增变量必须区分哮喘、COPD、触发物、药物可及、氧合、通气和康复。
