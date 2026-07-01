# Xerostomia Salivary Function Oral Medication Continuity

`xerostomia-salivary-function-oral-medication-continuity/` 负责整理口干、唾液功能、药物相关口腔风险和摄食沟通连续性。

核心问题：

> 唾液是口腔系统的维护液；口干会把药物、放疗、免疫和年龄相关风险转化为龋病、感染、吞咽、说话和睡眠摩擦。

## 先验位置

```text
主体持续性最大化
  -> 主体必须维持口腔湿润、吞咽、说话、味觉、牙体保护和黏膜防御
  -> 药物、放疗、免疫疾病、年龄和脱水可影响唾液功能
  -> 口干会增加龋病、口腔感染、吞咽困难、睡眠中断和社交退缩
  -> 因此唾液功能是口腔维护、药物负担和长期照护的接口条件
```

## 关注对象

- 口干、唾液减少、药物负担、放疗后口腔风险、Sjögren 相关口腔问题和黏膜不适。
- 龋病、口腔感染、吞咽、言语、味觉、睡眠、营养和生活质量。
- 多病共存、老年人、癌症治疗后人群和长期用药场景。
- 与 `medication-access-continuity/` 的关系：本域关注口腔副作用；药物域关注供给和依从性。

## Human Infra 模型链路

```text
唾液功能维护 / 口干风险治理 T
  -> 改变口腔湿润、药物负担、龋病、感染、吞咽、言语和睡眠变量 X
  -> 改变主体口腔防御和生活功能状态 S
  -> 改变进食困难、沟通退缩、疼痛感染和长期照护负担风险
  -> 增加有效时间、舒适度和行动连续性
```

## 非目标

- 不提供药物停换、剂量调整、唾液替代品、漱口产品或治疗建议。
- 不诊断 Sjögren、药物副作用、放疗后并发症或口腔感染。
- 不替代牙医、医生、药师、风湿免疫、肿瘤或言语吞咽专业评估。

## Source Signals

- NIDCR Dry Mouth: https://www.nidcr.nih.gov/health-info/dry-mouth
- NIDCR Sjogren's Disease: https://www.nidcr.nih.gov/health-info/sjogrens-disease
- WHO Oral Health: https://www.who.int/news-room/fact-sheets/detail/oral-health

## 下一步

- 建立口干 Source Card，区分药物、放疗、免疫疾病、老年照护和口腔功能后果。
- 对接老年口腔、癌症幸存者、吞咽、语言沟通和药物连续性域。
