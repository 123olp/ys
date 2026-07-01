# disorders-of-consciousness-coma-recovery 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/disorders-of-consciousness-coma-recovery` |
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


本目录维护意识障碍、昏迷和恢复边界资料。它是主体连续性判定的医学与伦理边界域。

## 目录结构

```text
disorders-of-consciousness-coma-recovery/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义昏迷、无反应觉醒、最低意识状态、评估和恢复如何影响主体持续性。
- 本目录不保存个案评估、预后判断、撤治建议、生命支持决策或伦理裁决。
- 资料必须区分意识状态分类、评估工具、康复证据、代理决策和伦理边界。

## 上下游关系

- 上游来自神经病学、神经康复、ICU、伦理学、神经影像、脑电和长期照护。
- 下游服务主体连续性理论、去具身中枢、脑保存、治理权利和严重疾病照护。
- 不替代 `governance-rights/`；本目录聚焦意识状态不确定时的主体连续性医学边界。

## 维护规则

- 不提供个体意识判断、预后、撤治、生命支持或照护决策建议。
- 不把单次反应、影像、脑电或模型输出写成意识存在证明。
- 新增资料必须标注状态定义、评估工具、误诊风险、伦理边界和适用对象。
