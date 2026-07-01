# epilepsy-seizure-network-stability 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/epilepsy-seizure-network-stability` |
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


本目录维护癫痫、发作和脑网络稳定性资料。它是意识和行动窗口的反复中断风险域。

## 目录结构

```text
epilepsy-seizure-network-stability/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义癫痫、发作频率、治疗连续性和发作相关伤害如何影响主体持续性。
- 本目录不保存诊断、用药、急救、驾驶许可、设备选择或手术建议。
- 资料必须区分公共健康信息、临床指南、监测工具、社会支持和个体医疗判断。

## 上下游关系

- 上游来自神经病学、脑网络科学、睡眠医学、可穿戴监测、残障服务和公共健康。
- 下游服务意识稳定、行动安全、学习/工作参与、生活质量和未来选择权模型。
- 不替代 `neuro-continuity/`；本目录聚焦发作导致的意识与行动窗口中断。

## 维护规则

- 不提供个体诊断、药物、急救、设备、驾驶或手术建议。
- 不把 EEG、可穿戴信号或发作描述写成个人风险结论。
- 新增资料必须标注发作类型、证据阶段、适用人群、伤害风险和禁止用途。
