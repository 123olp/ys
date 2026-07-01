# Kidney Transplant, Immunosuppression and Graft Continuity

`kidney-transplant-immunosuppression-graft-continuity/` 研究肾移植、移植物功能、免疫抑制、感染风险、排斥、药物供应、随访和保险中断如何影响主体持续性。

> 核心问题：肾移植把清除能力重新内置到身体中，但它依赖长期免疫抑制、随访、药物供应和感染/排斥风险治理。

## 先验位置

```text
有效永生
  -> 外部替代清除可以被器官替代重建
  -> 移植后的清除能力依赖免疫与药物系统长期稳定
  -> 因此肾移植是清除能力重建后的长期治理域
```

## 关注对象

- Kidney transplant, graft function, rejection, immunosuppression, infection, medication adherence, drug supply, follow-up, insurance and transition of care。
- 与 `xenotransplantation-bioengineered-organ-replacement/` 的关系：后者关注远期器官替代平台，本域关注当前肾移植连续性。

## Human Infra 模型链路

```text
移植随访与免疫抑制连续性 T
  -> 改变排斥、感染、药物供应、毒性、随访和保险中断 X
  -> 改变移植物功能、清除能力、免疫状态和生活稳定性 S
  -> 改变死亡、移植物失败、住院和重返透析风险 lambda(t)
  -> 改变健康寿命、资源负担和未来选择权
```

## 非目标

- 不提供移植资格、配型、免疫抑制用药、剂量、实验室解释、感染处理、保险策略或个体建议。
- 不输出个人移植物风险、排斥判断、用药调整、供体判断或机构选择。

## Source Signals

- NIDDK kidney transplant materials.
- National Kidney Foundation kidney transplant and anti-rejection medicine materials.
- UNOS / OPTN public transplant system materials.
