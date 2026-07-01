# wearables-continuous-sensing-personal-informatics 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/wearables-continuous-sensing-personal-informatics` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


本目录维护可穿戴、连续感知与个人信息学域。它是 Human Infra 的“主体状态连续观测”层，负责传感器、自我追踪和反馈闭环如何影响风险预警、行为调整和长期建模。

## 目录结构

```text
wearables-continuous-sensing-personal-informatics/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明可穿戴、连续监测、个人信息学、远程数据采集和传感器质量如何进入主体持续性模型。
- 本域只做公开资料整理和证据边界维护。
- 不提供诊断、治疗、用药调整、急诊判断、设备选购、算法解释或个人健康预测建议。

## 维护规则

- 新增资料必须区分消费级反馈、研究级测量、临床级监测和监管级证据。
- 涉及传感器数据时，必须记录准确性、校准、缺失、偏差、用户负担和隐私风险。
- 不把连续数据写成确定预后，不把传感器趋势直接转成医疗行动建议。
