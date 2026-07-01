# scientific-instrumentation-sensor-calibration-maintenance 目录说明

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
