# Medical ID Allergy Critical Alert Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/medical-id-allergy-critical-alert-continuity` |
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


Medical ID Allergy Critical Alert Continuity 研究 medical ID、过敏/不良反应、关键诊断、癫痫/糖尿病/抗凝等急救提示和可穿戴/手机急救信息如何在主体无法表达时被发现、理解和正确使用。

> 核心问题：很多急救风险不需要完整病历，先需要一个醒目、可信、不过度暴露隐私的关键警报。

## 研究对象

- Medical ID、medical alert bracelet/card、手机 emergency info、可穿戴急救信息和钱包卡。
- 药物过敏、食物过敏、严重不良反应、植入设备、抗凝、糖尿病、癫痫、肾上腺危机等关键提示。
- 发现概率、可信度、更新机制、语言可读性、隐私暴露和误标风险。

## 先验链路

```text
急救现场时间有限且主体可能无法沟通
  -> 完整病历通常不可立即访问
  -> 关键过敏、设备、病情和禁忌需要被快速发现
  -> Medical ID 和 critical alert 可把少量高价值信息暴露给急救链
  -> 信息若缺失、错误、过期或不可见，会增加误治、延误和伤害风险
  -> 因而医疗 ID 与关键警报是主体无法表达时的最低健康信号层
```

## 关键变量

- 警报类型、可见性、准确性、更新频率、验证来源和读取场景。
- 隐私最小化、语言/符号、照护者联系方式、设备依赖和紧急访问方式。
- 误报、漏报、过敏混淆、过度暴露身份和平台锁定风险。

## 证据入口

- MedlinePlus personal health records and emergency information materials.
- CDC chronic condition emergency preparedness materials.
- NLM/FDA device and health information materials.
- Emergency medical services and patient safety materials.

## 非目标

- 本域不判断某人是否需要 medical ID、写什么内容、是否过敏、是否停药或急救如何处置。
- 不提供医疗、急救、设备、药物、可穿戴、手机设置、产品推荐或法律建议。
- 不收集过敏史、诊断、药物、设备序列号、联系方式、定位或 PHI。

## 上下游

- 上游：`personal-health-record-emergency-summary-continuity/`、`allergy-adverse-reaction` 相关资料、`wearables-continuous-sensing-personal-informatics/`。
- 下游：`emergency-medical-services-prehospital-care/`、`medication-list-implant-device-emergency-continuity/`、`patient-safety-organizational-learning/`。
