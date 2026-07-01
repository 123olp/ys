# scientific-instrumentation-sensor-calibration-maintenance 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/scientific-instrumentation-sensor-calibration-maintenance` |
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


本目录维护科研仪器、传感器、校准、漂移和维护。它是测量反馈系统的硬件可信层。

## 目录结构

```text
scientific-instrumentation-sensor-calibration-maintenance/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义仪器校准、维护、漂移和测量不确定性如何影响 Human Infra 模型输入。
- 本目录不保存设备原始数据、个人测量数据、认证报告或可执行设备改装方案。
- 资料必须区分计量标准、实验室实践、医疗器械要求和消费级传感器声明。

## 上下游关系

- 上游来自标准计量、实验室质量、设备安全和传感器科学。
- 下游服务测量反馈、生物标志物验证、可穿戴连续感知、环境暴露和模型校准。
- 不替代 `standards-metrology-quality-infrastructure/`；本目录聚焦具体仪器和传感器运行状态。

## 维护规则

- 不提供伪造校准、规避认证、篡改设备或医疗器械改装策略。
- 不把仪器读数写成个人诊断、用药、急救或寿命预测。
- 若新增测量案例，必须记录设备类型、校准状态、测量范围、不确定性和适用边界。
