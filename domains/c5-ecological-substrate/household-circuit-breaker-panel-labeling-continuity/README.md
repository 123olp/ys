# Household Circuit Breaker Panel Labeling Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-circuit-breaker-panel-labeling-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


`household-circuit-breaker-panel-labeling-continuity` 研究住宅断路器面板目录、回路标签、负载认知、维修交接和电力故障资料如何影响家庭用电任务、火灾风险响应和专业服务连续性。

> 核心问题：家庭电力依赖大量具体回路；当标签缺失、错误或只有某个人知道时，停电排查、维修交接、医疗设备供电、冰箱冷链、网络设备和灾后恢复都会被信息不透明放大摩擦。

## 关注对象

- 断路器面板目录、回路标签、重要负载、医疗/通信/冷藏设备依赖、旧标签漂移和维修记录。
- 租房、老旧住房、多成员家庭、居家医疗设备、家庭办公、灾后临时用电和维修预约场景。
- 面板信息如何帮助专业人员、房东/物业、照护者和家庭成员理解电力依赖关系。
- 与住宅电气安全、备用电源、家电维护、线缆风险和家庭运行地图的接口。

## Human Infra 链路

```text
家庭回路标签与负载信息可读
  -> 用电任务、关键设备和故障范围更容易被定位和沟通
  -> 专业维修、灾后恢复、照护交接和设备优先级判断摩擦下降
  -> 停电、误关、过载、冷链中断和医疗设备供电中断风险降低
  -> 家庭电力从黑箱系统转化为可维护的任务底座
```

## 非目标

- 不提供断路器操作、电气维修、接线、配电箱开盖、负载计算、GFCI/AFCI 安装、故障诊断或现场电气安全建议。
- 不替代持证电工、消防部门、本地电气规范、房东维修义务、物业、电力公司或保险检查。
- 不收集家庭面板照片、回路细节、住址、设备清单、安防系统信息或其他可被滥用的设施资料。

## Source Signals

- USFA Appliance and Electrical Fire Safety: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/appliance-and-electrical/
- Ready.gov Power Outages: https://www.ready.gov/power-outages
- NFPA Electrical Safety: https://www.nfpa.org/education-and-research/home-fire-safety/electrical

## 下一步

- 建立 `circuit label state -> critical load visibility -> repair/emergency handoff -> continuity outcome` 变量表。
- 区分标签缺失、标签错误、设备迁移、旧房改造、医疗设备依赖和租赁责任。
- 与 `residential-electrical-wiring-outlet-safety-continuity`、`backup-power-battery-generator-safety-continuity` 和 `home-utility-shutoff-location-labeling-continuity` 建立边界。
