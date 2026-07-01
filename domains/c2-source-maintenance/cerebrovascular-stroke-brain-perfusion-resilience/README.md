# Cerebrovascular Stroke Brain Perfusion Resilience

`cerebrovascular-stroke-brain-perfusion-resilience/` 研究脑血流、卒中、短暂性脑缺血、脑小血管病、再灌注窗口和卒中后恢复，如何影响 Human Infra 的神经连续性、行动能力和死亡风险。

> 核心问题：主体连续性依赖大脑持续获得血流、氧气和代谢支持。卒中不是普通心血管风险的附属变量，而是会在短时间内改变意识、语言、记忆、运动和未来选择权的脑灌注失败模式。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 大脑必须持续获得足够灌注和氧气
  -> 脑血管事件可在短窗口内造成死亡、失语、瘫痪、认知损伤和身份连续性破坏
  -> 若预防、识别、急救、再灌注、康复和二级预防失败，寿命会转化为失能时间
  -> 因此脑血管与卒中韧性是神经连续性的急性风险域
```

## 关注对象

- 缺血性卒中、出血性卒中、短暂性脑缺血发作、脑小血管病、脑灌注和再灌注窗口。
- 卒中预防、急性识别、转运、治疗窗口、康复、二级预防和长期功能恢复。
- 与 `cardiovascular-resilience/` 的边界：心血管域关注循环系统整体风险；本域关注脑灌注失败对意识、语言、运动和认知连续性的影响。
- 与 `rehabilitation-functioning/` 的边界：康复域关注功能恢复服务；本域关注卒中从急性脑损伤到长期恢复的完整风险链。

## Human Infra 模型链路

```text
脑血管与卒中韧性 T
  -> 改变血压、血管状态、凝血、房颤、急救时间、再灌注机会和康复强度变量 X
  -> 改变脑灌注、神经损伤范围、功能恢复和二级预防状态 S
  -> 改变死亡、复发、失语、瘫痪、认知损伤和长期失能风险 λ(t)
  -> 影响寿命、健康寿命、有效时间和主体连续性
```

## 非目标

- 不提供卒中急救、诊断、溶栓、取栓、用药、康复处方或个体风险判断。
- 不替代急救系统、神经科、康复医学、公共卫生或临床指南。
- 不把单项血压、影像、可穿戴信号或 AI 风险评分写成个人诊断。

## Source Signals

- CDC Stroke: https://www.cdc.gov/stroke/
- WHO Stroke fact sheet: https://www.who.int/news-room/fact-sheets/detail/stroke
- NINDS Stroke: https://www.ninds.nih.gov/health-information/disorders/stroke
- American Heart Association Stroke Guidelines: https://www.ahajournals.org/journal/str

## 下一步

- 建立卒中变量表：危险因素、预防、急救时间、治疗窗口、损伤范围、康复、复发、功能结局和照护连续性。
- 与 `cardiovascular-resilience/`、`emergency-medical-services-prehospital-care/`、`rehabilitation-functioning/` 和 `care-transitions-discharge-continuity/` 建立接口。
