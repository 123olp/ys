# Post Flood Mold Moisture Indoor Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/post-flood-mold-moisture-indoor-recovery-continuity` |
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


`post-flood-mold-moisture-indoor-recovery-continuity/` 研究洪水、漏水、潮湿、霉菌、室内空气和建筑材料干燥失败如何影响灾后住房可返回性与健康恢复。

> 核心问题：洪水退去不等于住房恢复；湿气和霉菌会把房屋、睡眠、呼吸健康、免疫风险和长期居住稳定继续锁在不可行动状态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体恢复需要可居住室内环境、呼吸安全、睡眠和物品保存
  -> 洪水和潮湿可导致霉菌、材料损坏、空气质量下降和过敏/哮喘负担
  -> 室内恢复失败会延迟返回并加重健康风险
  -> 因此洪水后霉菌与湿气恢复是主体住房恢复连续性的环境健康域
```

## 关注对象

- CDC mold cleanup after disaster、EPA mold resources、FEMA flood recovery、室内湿气、空气质量、材料干燥和高风险人群。
- 暴露风险、健康负担、住房可返回、承包商边界、保险/修复延迟和公共沟通。
- 与 `air-quality-ventilation-exposure-control/` 的边界：该域关注日常空气质量；本域关注洪水后潮湿和霉菌恢复。

## Human Infra 模型链路

```text
洪水后湿气与霉菌恢复系统 T
  -> 改变室内湿度、霉菌暴露、空气质量、材料修复和住房可返回变量 X
  -> 改变主体灾后居住环境状态 S
  -> 改变呼吸负担、过敏哮喘、感染风险、睡眠损失和迁移风险 λ(t)
  -> 影响恢复速度、健康寿命和未来选择权
```

## 非目标

- 不提供个人清理步骤、霉菌检测解释、承包商推荐、结构安全判断、保险理赔建议或医疗诊断。
- 不收集房屋地址、照片、霉菌样本、保险单、健康状况或儿童/老人房间信息。
- 不替代 CDC、EPA、地方公共卫生、持证修复承包商、保险专业人员或医疗服务。

## Source Signals

- CDC Mold After a Disaster: https://www.cdc.gov/mold-health/about/clean-up.html
- EPA Mold Resources: https://www.epa.gov/mold
- Ready.gov Floods: https://www.ready.gov/floods
