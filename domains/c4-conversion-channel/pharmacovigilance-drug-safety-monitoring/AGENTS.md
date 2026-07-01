# pharmacovigilance-drug-safety-monitoring 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/pharmacovigilance-drug-safety-monitoring` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录维护药物警戒、上市后药品安全与不良反应监测域。它是 Human Infra 的“治疗工具现实世界安全反馈层”，负责药品在真实使用中的风险信号和反馈治理。

## 目录结构

```text
pharmacovigilance-drug-safety-monitoring/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明不良事件报告、上市后安全、风险沟通、标签更新和药物警戒如何影响主体持续性。
- 本域只做公开药品安全、监管、信号监测和风险治理资料整理。
- 不提供用药、停药、换药、剂量、个案归因、法律、索赔、药品购买或监管规避建议。

## 维护规则

- 新增材料必须区分疗效证据、可及性证据、质量问题和上市后安全信号。
- 不把不良事件数据库写成因果证明或个人用药结论。
- 涉及药品风险时，必须保留证据等级、适用人群、监管语境和不确定性。
