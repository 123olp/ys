# Trauma System Hemorrhage Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/trauma-system-hemorrhage-control-continuity` |
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


`trauma-system-hemorrhage-control-continuity/` 研究创伤系统、院前分诊、止血、创伤中心、影像/手术窗口、出血控制和康复转接如何降低事故导致的突然死亡与失能。

> 核心问题：创伤不是单个伤口，而是时间、出血、转运、手术、血液供应和康复共同组成的救援系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能被事故、暴力、跌落和灾害造成的创伤突然终止
  -> 生存依赖院前响应、止血、分诊、创伤中心、手术和输血协同
  -> 创伤系统失效会把可救治损伤变成死亡或长期残障
  -> 因此创伤系统与出血控制是外部事故风险的急性修复域
```

## 关注对象

- Trauma system、prehospital triage、hemorrhage control、tourniquet access、trauma center level、massive transfusion, time-to-definitive care、rehabilitation handoff。
- 与 `road-traffic-injury-prevention-safe-mobility/` 的边界：道路安全关注预防；本域关注事故发生后的救援系统。
- 与 `transfusion-blood-management-hemorrhage-continuity/` 的关系：严重创伤常依赖血液可得、止血和大量输血。

## Human Infra 模型链路

```text
创伤系统与出血控制 T
  -> 改变院前响应、止血、分诊、转运、创伤中心和输血变量 X
  -> 改变失血、手术窗口、器官灌注、残障和康复状态 S
  -> 改变事故死亡、失能和长期功能损失风险 λ(t)
  -> 影响主体身体连续性、有效时间和行动能力
```

## 非目标

- 不提供止血、急救、战术医疗、武器伤处理、现场处置、手术或转运建议。
- 不生成创伤中心选择、急诊策略、保险策略、法律责任、事故处置或个体医疗建议。
- 不收集事故现场、伤情照片、身份、定位、病历、暴力证据或敏感救援资料。

## Source Signals

- National Academies trauma care system report: https://nap.nationalacademies.org/catalog/23511/a-national-trauma-care-system-integrating-military-and-civilian-trauma
- American College of Surgeons Trauma Programs: https://www.facs.org/quality-programs/trauma/
- WHO Emergency and Trauma Care: https://www.who.int/health-topics/emergency-care

## 下一步

- 建立 Trauma Rescue Card：mechanism, hemorrhage, triage, trauma center access, definitive control, transfusion, rehab handoff。
- 与 `emergency-medical-services-prehospital-care/`、`surgical-anesthesia-perioperative-safety/` 和 `transfusion-blood-management-hemorrhage-continuity/` 建立接口。
