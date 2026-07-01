# Skin Care Supplies, Dressings and Barrier Products Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/skin-care-supplies-dressings-barrier-products-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


`skin-care-supplies-dressings-barrier-products-continuity/` 研究敷料、屏障产品、清洁用品、失禁用品、皮肤保护材料、DME/供应链、支付覆盖和库存中断如何影响伤口、皮肤屏障和照护连续性。

> 核心问题：皮肤保护不是只有医学知识；它还依赖材料、支付、库存、物流、照护者和正确使用边界。

## 先验位置

```text
有效永生
  -> 主体边界维护需要持续可用的材料和照护执行
  -> 敷料、屏障用品、清洁用品和失禁用品中断会放大伤口与感染风险
  -> 供应链和支付失败会把可护理问题转化为失能风险
  -> 因此皮肤护理用品是伤口和屏障连续性的资源底座
```

## 关注对象

- Dressings, barrier products, cleansers, incontinence supplies, skin protection supplies, DME, coverage, inventory and caregiver use。
- 与 `durable-medical-equipment-supplier-repair-continuity/` 的关系：后者关注广义 DME，本域关注皮肤/伤口用品和屏障产品连续性。

## Human Infra 模型链路

```text
皮肤护理用品供应连续性 T
  -> 改变敷料、屏障产品、清洁用品、失禁用品、支付和库存 X
  -> 改变伤口保护、潮湿控制、感染入口和照护执行 S
  -> 改变慢性伤口、压力损伤、感染和住院风险 lambda(t)
  -> 改变照护负担、有效时间和恢复质量
```

## 非目标

- 不推荐具体品牌、型号、敷料选择、用品替代、保险策略、护理步骤或个体采购建议。
- 不处理个人伤口、皮肤照片、处方、供应商、账单或报销资料。

## Source Signals

- FDA wound dressing and medical device public materials.
- CMS DME and supply coverage materials as policy context.
- MedlinePlus wound care and pressure injury materials.
