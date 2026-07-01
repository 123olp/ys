# Medication List Implant Device Emergency Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/medication-list-implant-device-emergency-continuity` |
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


Medication List Implant Device Emergency Continuity 研究急救和跨机构照护中，当前药物清单、抗凝/胰岛素/免疫抑制等高风险药物、植入物、设备和维护依赖如何被识别、携带和转交。

> 核心问题：药物和植入设备是主体身体里的外部技术系统；急救时不知道它们，可能比不知道诊断更危险。

## 研究对象

- 当前药物清单、剂量、给药频率、处方方、OTC、补充剂和高风险药物标记。
- 植入设备、起搏器、泵、支架、关节、神经刺激器、设备卡和 UDI/型号资料。
- 药物停用/延误、设备 MRI/手术/急救限制、维护耗材和跨机构转交。

## 先验链路

```text
主体持续性依赖药物和植入设备长期协同身体运行
  -> 急救、住院、转诊和灾害会打断原用药和设备维护语境
  -> 医疗团队若无法获知药物和设备信息，可能发生相互作用、禁忌、重复、停药或设备风险
  -> 可携带清单和设备记录让急救系统更快恢复主体真实技术状态
  -> 记录错误、过期或不可访问会反向制造伤害
  -> 因而药物清单与植入设备急救转交是身体-技术连续性的关键接口
```

## 关键变量

- 清单完整性、更新时间、来源、处方/非处方区分、停药历史和高风险标记。
- 设备类型、型号、制造商、植入日期、限制、维护、召回和照护者可得性。
- 隐私、设备安全、供应中断、药物短缺、语言可读和 EHR/PHR 同步风险。

## 证据入口

- AHRQ medication reconciliation materials.
- FDA UDI / AccessGUDID and medical device materials.
- MedlinePlus medicines and personal health record materials.
- CDC medication safety and emergency preparedness materials.

## 非目标

- 本域不解释药物、调整剂量、判断相互作用、判断设备风险、推荐设备或提供急救处置。
- 不代写药物清单、设备卡、病历摘要、授权材料或机构沟通。
- 不收集用药、设备序列号、病历、处方、照片、账号、PHI 或定位资料。

## 上下游

- 上游：`medication-reconciliation-regimen-adherence-continuity/`、`medical-device-equipment-safety-maintenance/`、`retail-pharmacy-prescription-dispensing-continuity/`。
- 下游：`emergency-medical-services-prehospital-care/`、`care-transitions-discharge-continuity/`、`medical-record-access-amendment-release-continuity/`。
