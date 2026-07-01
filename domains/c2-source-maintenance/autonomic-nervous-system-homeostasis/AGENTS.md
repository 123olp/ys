# autonomic-nervous-system-homeostasis 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/autonomic-nervous-system-homeostasis` |
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


本目录维护自主神经系统和身体自动调节资料。它是内环境、恢复和行动耐受的神经调控域。

## 目录结构

```text
autonomic-nervous-system-homeostasis/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义自主神经、交感/副交感调节、体位耐受和恢复能力如何影响主体持续性。
- 本目录不保存诊断、补液用盐、药物、运动处方或可穿戴读数解释。
- 资料必须区分机制资料、临床指南、可穿戴指标、研究假设和个体医疗判断。

## 上下游关系

- 上游来自神经病学、心脏科、内分泌、康复、睡眠、长 COVID 和生理监测。
- 下游服务行动耐受、疲劳恢复、跌倒风险、有效时间和长期照护模型。
- 不替代 `cardiovascular-resilience/`；本目录聚焦神经调控下的动态稳态。

## 维护规则

- 不提供个体诊断、用药、补液、用盐、运动或设备建议。
- 不把 HRV、心率、血压或可穿戴信号写成个人自主神经判断。
- 新增资料必须标注测量方式、适用人群、证据阶段、混杂因素和禁止用途。
