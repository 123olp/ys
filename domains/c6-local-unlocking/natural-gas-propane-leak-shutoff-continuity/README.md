# Natural Gas Propane Leak Shutoff Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/natural-gas-propane-leak-shutoff-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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


`natural-gas-propane-leak-shutoff-continuity` 研究天然气、丙烷、燃料管线、泄漏识别、报警、撤离、关断责任和恢复检查如何影响家庭安全、供暖、烹饪和居住连续性。

> 核心问题：燃气是高能量家庭基础设施；它能支撑供暖和烹饪，也会在泄漏、误操作或恢复失败时迅速转化为爆炸、火灾和中毒风险。

## 关注对象

- 天然气、丙烷、燃气表、阀门、软管、炉具、供暖设备、泄漏气味、报警、撤离和恢复检查。
- 施工破坏、设备老化、灾后返家、租房责任、燃料中断、燃气恢复和公共通知。
- 与供暖、烹饪、CO 风险、消防、应急通信、管线安全和维修专业人员的接口。

## Human Infra 链路

```text
燃气与丙烷泄漏关断连续
  -> 高能量燃料使用保持可识别、可撤离、可专业恢复
  -> 泄漏、爆炸、火灾、CO 和灾后返家风险下降
  -> 供暖、烹饪和居住任务不被不可见燃料风险切断
  -> 主体家庭安全边界和恢复能力提高
```

## 非目标

- 不提供关阀操作教程、泄漏判断、设备维修、燃气恢复、管线施工、燃气表操作或现场安全许可。
- 不替代燃气公司、丙烷供应商、消防部门、911、持证 plumber/HVAC、管线安全机构或房东维修义务。
- 不把燃气可用性和安全性混为一谈；本域只研究燃料接口的识别、响应、专业恢复和任务连续性。

## Source Signals

- PHMSA Pipeline Leak Recognition and What to Do: https://www.phmsa.dot.gov/safety-awareness/pipeline/pipeline-leak-recognition-and-what-do
- USFA Home Heating Fire Safety: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/
- CDC Carbon Monoxide Poisoning Basics: https://www.cdc.gov/carbon-monoxide/about/index.html

## 下一步

- 建立 `fuel gas interface -> leak signal -> response boundary -> restoration state -> continuity outcome` 变量表。
- 区分天然气、丙烷、供暖、烹饪、灾后返家、施工破坏、租房责任和燃气恢复。
- 与 `carbon-monoxide-alarm-combustion-appliance-safety-continuity`、`fuel-thermal-energy-service-continuity` 和 `home-heating-equipment-chimney-vent-maintenance-continuity` 建立边界。
