# cerebrovascular-stroke-brain-perfusion-resilience 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cerebrovascular-stroke-brain-perfusion-resilience` |
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


本目录维护脑血管、卒中和脑灌注韧性资料。它是神经连续性的急性血流失败域。

## 目录结构

```text
cerebrovascular-stroke-brain-perfusion-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义卒中、脑灌注、再灌注窗口和长期功能恢复如何影响主体持续性。
- 本目录不保存卒中急救、诊断、溶栓、取栓、用药或康复处方。
- 资料必须区分公共健康资料、临床指南、急性治疗窗口、康复证据和个体医疗决策。

## 上下游关系

- 上游来自神经病学、卒中医学、心血管风险、急救系统、影像和康复医学。
- 下游服务神经连续性、行动能力、有效时间、照护转移和二级预防模型。
- 不替代 `cardiovascular-resilience/`；本目录聚焦脑灌注和卒中导致的神经连续性损失。

## 维护规则

- 不提供个体急救、诊断、治疗、用药或风险评分建议。
- 不把影像、血压、可穿戴或 AI 输出写成个人卒中判断。
- 新增资料必须标注卒中类型、证据阶段、适用人群、功能结局和剩余未知项。
