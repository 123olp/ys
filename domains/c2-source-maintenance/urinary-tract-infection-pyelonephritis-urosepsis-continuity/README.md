# Urinary Tract Infection, Pyelonephritis and Urosepsis Continuity

`urinary-tract-infection-pyelonephritis-urosepsis-continuity/` 研究尿路感染、上行感染、肾盂肾炎、尿源性脓毒症、复发负担和服务延迟如何影响主体持续性。

> 核心问题：尿路感染不是单纯不适，它可能通过疼痛、发热、谵妄、肾脏受累、脓毒症和反复用药负担，把排泄出口变成急性风险和长期恢复成本。

## 先验位置

```text
有效永生
  -> 主体必须稳定排出代谢废物并避免感染扩散
  -> 尿路上行感染会把排泄系统变成全身炎症入口
  -> 因此 UTI、肾盂肾炎和尿源性脓毒症是排泄出口安全域
```

## 关注对象

- Urinary tract infection, recurrent UTI, pyelonephritis, urosepsis, fever, delirium, antimicrobial exposure, care delay, hydration and access boundaries。
- 与 `urogenital-continuity/` 的关系：该域负责泌尿生殖总框架，本域聚焦感染从局部症状到全身风险的路径。

## Human Infra 模型链路

```text
感染识别与服务可及 T
  -> 改变感染扩散、疼痛、发热、谵妄、抗菌药暴露和复发 X
  -> 改变排泄安全、肾脏负担、睡眠、行动和恢复状态 S
  -> 改变急性恶化、住院、脓毒症和长期衰弱风险 lambda(t)
  -> 改变有效时间、恢复成本和未来选择权
```

## 非目标

- 不提供个人 UTI 诊断、尿检解释、抗生素选择、补液方案、复发预防、急诊判断或医疗机构选择。
- 不输出个人感染风险、脓毒症概率、用药建议、怀孕/儿童/老年个案建议或护理操作。

## Source Signals

- NIDDK urinary tract infection materials.
- CDC urinary tract infection basics.
- MedlinePlus urinary tract infection public materials.
