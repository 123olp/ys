# Dialysis Access, Vascular and Peritoneal Continuity

`dialysis-access-vascular-peritoneal-continuity/` 研究血管通路、腹膜透析通路、感染、血栓、成熟失败、通路维护和治疗中断如何影响主体持续性。

> 核心问题：透析不是只有机器，真正的入口是通路；通路失败会把可替代的清除能力变成感染、血栓、住院和治疗不可达。

## 先验位置

```text
有效永生
  -> 清除系统失败时需要外部替代清除
  -> 外部清除依赖可用、可维护、低感染风险的通路
  -> 因此透析通路是肾脏替代治疗的接口域
```

## 关注对象

- Vascular access, fistula, graft, catheter context, peritoneal dialysis catheter, access maturation, infection, thrombosis, maintenance and continuity of treatment。
- 与 `acute-kidney-injury-renal-replacement-continuity/` 的关系：AKI/RRT 域关注急性支持，本域关注透析入口作为长期/反复治疗接口。

## Human Infra 模型链路

```text
透析通路规划与维护 T
  -> 改变通路成熟、感染、血栓、治疗中断和住院 X
  -> 改变清除能力、液体电解质稳态、行动半径和照护状态 S
  -> 改变死亡风险、感染风险、心血管负担和有效时间损失 lambda(t)
  -> 改变健康寿命和未来选择权
```

## 非目标

- 不提供透析通路选择、穿刺、护理、感染处理、抗凝、手术、透析参数或个体肾病建议。
- 不输出个人通路风险、透析方案、血流量判断、腹膜炎判断或医疗机构选择。

## Source Signals

- National Kidney Foundation dialysis access materials.
- NIDDK hemodialysis and peritoneal dialysis materials.
- KDOQI vascular access guideline context.
