# anaphylaxis-allergic-emergency-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/anaphylaxis-allergic-emergency-continuity` |
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


本目录维护过敏性休克、严重过敏、场所准备和急救转接资料。它是免疫反应突然关闭气道和循环的分钟级风险域。

## 目录结构

```text
anaphylaxis-allergic-emergency-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义过敏急症如何改变窒息、休克、死亡、活动边界和恢复连续性。
- 本目录只维护系统级变量、来源和边界，不保存个案过敏史、食物/药物、学校、工作地点、急救或医疗资料。
- 资料进入本域时必须区分触发物、识别、药物可及、场所计划、EMS 转接和过敏专科随访。

## 上下游关系

- 上游来自 WAO、NIAID、AAAAI 和公共卫生过敏资料。
- 下游服务 `immune-maintenance/`、`medical-id-allergy-critical-alert-continuity/` 和学校/工作场所连续性建模。
- 不替代医生、急诊、过敏专科、学校护士、雇主、EMS 或个体医疗建议。

## 维护规则

- 不写肾上腺素使用、剂量、急救步骤、过敏诊断、暴露挑战、脱敏或处方建议。
- 不把系统级过敏急症研究写成个人 action plan 或现场处理工具。
- 新增变量必须区分触发物、识别、药物可及、场所准备、转接和复发预防。
