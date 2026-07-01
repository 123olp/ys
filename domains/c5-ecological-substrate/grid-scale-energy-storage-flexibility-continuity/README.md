# Grid Scale Energy Storage Flexibility Continuity

`grid-scale-energy-storage-flexibility-continuity/` 研究电网级储能、长时储能、需求响应、灵活负荷、备用容量和调度机制如何支撑高比例可再生能源、AI 负载和关键服务连续性。

> 核心问题：电力系统不仅需要发电，还需要时间上的可调度性。储能和灵活性不足会让能源充足性在关键时刻变成服务中断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要医疗、通信、AI、冷却、居住和交通系统持续供电
  -> 高波动负载和可再生能源需要储能、灵活性和调度缓冲
  -> 缓冲不足会导致价格尖峰、停电、负载削减和关键服务降级
  -> 因此电网级储能与灵活性是能源连续性的时间缓冲域
```

## 关注对象

- Battery storage、long-duration energy storage、pumped hydro、thermal storage、demand response、virtual power plant、reserve margin 和 grid services。
- 容量、持续时长、循环寿命、安全、并网、调度、退化、供应链、回收和关键负载保障。
- 与 `energy-access-resilience/` 的边界：能源可及域关注用户能否获得能源；本域关注电网尺度时间缓冲和灵活性。
- 与 `large-load-grid-interconnection-transmission-continuity/` 的关系：并网域关注接入；本域关注接入后的可调度性。

## Human Infra 模型链路

```text
电网储能与灵活性 T
  -> 改变备用容量、持续时长、负荷转移、频率服务和停电恢复变量 X
  -> 改变医疗、通信、数据中心、住房和交通供能状态 S
  -> 改变停电、价格尖峰、关键服务削减和恢复失败风险 λ(t)
  -> 影响主体安全、工具可用性、环境控制和长期行动能力
```

## 非目标

- 不提供储能系统安装、消防处置、项目投资、交易套利或采购建议。
- 不把储能写成无风险、无资源约束或万能替代输电的方案。
- 不替代电网可靠性、能源可及、消防安全或关键材料域。

## Source Signals

- DOE Office of Electricity Energy Storage: https://www.energy.gov/oe/energy-storage
- NREL Energy Storage: https://www.nrel.gov/grid/energy-storage.html
- IEA Energy Storage: https://www.iea.org/energy-system/electricity/grid-scale-storage
- Sandia Energy Storage: https://www.sandia.gov/ess-ssl/

## 下一步

- 建立 Storage Flexibility Card：storage class, duration, dispatch role, safety boundary, degradation, supply dependency, critical-service coupling。
