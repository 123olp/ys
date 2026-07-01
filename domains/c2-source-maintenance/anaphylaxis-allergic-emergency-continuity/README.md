# Anaphylaxis Allergic Emergency Continuity

`anaphylaxis-allergic-emergency-continuity/` 研究过敏性休克、严重过敏、触发物识别、肾上腺素自动注射器可及、急救接入、学校/工作/公共场所计划和复发预防如何影响主体持续性。

> 核心问题：过敏性休克会在分钟级内同时影响气道、循环和意识。它不是普通过敏，而是触发物、识别、可及药物、场所准备和后续评估共同决定的急性主体中断风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖气道和循环不被免疫反应突然关闭
  -> 过敏性休克可在短时间内造成窒息、休克和死亡
  -> 结果取决于触发物管理、识别、应急药物可及、场所计划和急救转接
  -> 因此过敏急症是免疫-气道-循环交界的急性失效域
```

## 关注对象

- Anaphylaxis recognition systems, allergen exposure context, epinephrine auto-injector access, school/workplace plans, EMS handoff, biphasic risk, follow-up allergy care。
- 与 `immune-maintenance/` 的边界：该域关注免疫系统长期维护；本域关注严重过敏急性窗口。
- 与 `medical-id-allergy-critical-alert-continuity/` 的关系：关键过敏身份信息可影响本域的识别和转接。

## Human Infra 模型链路

```text
过敏急症准备系统 T
  -> 改变触发物暴露、识别延迟、药物可及、场所计划和急救转接变量 X
  -> 改变气道、循环、意识、急诊观察和复发风险状态 S
  -> 改变窒息、休克、死亡和长期活动受限风险 λ(t)
  -> 影响主体存活、活动边界和未来选择权
```

## 非目标

- 不提供过敏诊断、肾上腺素使用、剂量、急救步骤、食物/药物挑战、脱敏、学校计划或个案医疗建议。
- 不生成 anaphylaxis action plan、过敏风险评分、暴露规避、处方或现场处理工具。
- 不收集个案过敏史、药物、食物、学校/工作地点、急救事件或医疗资料。

## Source Signals

- World Allergy Organization anaphylaxis guidance: https://www.worldallergy.org/
- NIAID food allergy guideline materials: https://www.niaid.nih.gov/
- AAAAI anaphylaxis practice parameter materials: https://www.aaaai.org/

## 下一步

- 建立 Anaphylaxis Continuity Card：trigger, recognition, epinephrine access, place plan, EMS transfer, follow-up。
- 与 `immune-maintenance/`、`medical-id-allergy-critical-alert-continuity/` 和 `school-health-services-chronic-condition-continuity/` 建立接口。
