# Human Digital Twin Life Course Simulation

## 定位

本域研究人类数字孪生、生命历程模拟和主体状态仿真如何把 Human Infra 的多域变量连接成可更新、可审查、可迭代的动态模型。

这里的数字孪生不是“复制一个人”，而是围绕主体状态、环境、行为、干预、风险和反馈建立的模型接口，用于比较场景、暴露链路和系统脆弱性。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体不是单变量，而是身体、认知、资源、环境和工具共同演化的系统
  -> 需要把多源数据、状态转移、风险函数和干预策略连接起来
  -> 需要生命历程级场景模拟和反馈更新
  -> human-digital-twin-life-course-simulation
```

## 关注对象

- 主体状态向量、环境状态、行为策略、技术干预和反馈观测。
- 生理、认知、资源、社会支持、环境暴露和工具系统的多层状态。
- life-course simulation、scenario analysis、multi-state model、agent-based model 和系统动力学。
- 数字孪生的模型粒度、数据来源、更新频率、可解释性和验证边界。
- 个体数据权利、同意、隐私、模型漂移和错误行动风险。

## Human Infra 模型链路

```text
多域观测数据
  -> 形成主体状态向量 X_t
  -> 状态转移模型估计 X_{t+1} 的可能分布
  -> 干预策略 A_t 改变状态转移和风险函数
  -> 场景模拟比较不同生命路径的有效时间和未来选择权
  -> 实际反馈更新模型并触发校准、审查和中止
```

## 非目标

- 不建立真实个人数字孪生服务。
- 不收集、存储或处理个人敏感健康数据。
- 不提供临床决策、诊断、治疗、保险、就业或行为控制建议。
- 不把模型仿真当成现实命运或个体承诺。

## Source Signals

- Dynamic digital twin for disease life course: https://www.jmir.org/2022/9/e35675/
- Human modeling systematic review: https://arxiv.org/abs/2302.03593
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- TRIPOD model reporting guidance: https://www.tripod-statement.org/

## 下一步

- 定义 Human Infra 的最小主体状态向量：身体、认知、资源、环境、工具、协作、恢复和风险暴露。
- 为每个研究域标注它影响的是状态变量、转移函数、观测能力、行动能力还是治理边界。
- 设计只用于展示的 toy digital twin，不接入个人数据。
