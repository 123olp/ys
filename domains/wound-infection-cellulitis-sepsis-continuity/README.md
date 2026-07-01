# Wound Infection, Cellulitis and Sepsis Continuity

`wound-infection-cellulitis-sepsis-continuity/` 研究皮肤破口、慢性伤口、蜂窝织炎和软组织感染如何从局部边界失败发展为全身感染风险，并影响主体行动、住院和死亡风险。

> 核心问题：皮肤感染是外界进入身体系统的通道；一旦失控，它会从局部疼痛和红肿升级为全身性风险。

## 先验位置

```text
有效永生
  -> 主体必须维持外界与内部环境之间的感染边界
  -> 伤口或皮肤屏障破裂会增加微生物进入机会
  -> 局部感染可能扩大为蜂窝织炎、深部感染或脓毒症风险
  -> 因此伤口感染是皮肤边界失效进入系统性风险的过渡域
```

## 关注对象

- Wound infection, cellulitis, skin and soft tissue infection, spreading infection, sepsis risk, recurrence and care delay。
- 与 `sepsis-shock-early-recognition-resuscitation-continuity/` 的关系：后者关注全身性脓毒症抢救，本域关注皮肤/伤口入口和早期失控链路。

## Human Infra 模型链路

```text
伤口感染控制连续性 T
  -> 改变屏障破口、局部炎症、传播速度、照护延迟和抗菌治理 X
  -> 改变局部组织状态、疼痛、行动能力和全身感染负担 S
  -> 改变住院、脓毒症、器官支持和死亡风险 lambda(t)
  -> 改变有效时间、恢复窗口和未来选择权
```

## 非目标

- 不提供感染诊断、抗生素选择、急诊判断、伤口照片判断、用药剂量或个人治疗建议。
- 不输出“是否蜂窝织炎”“是否脓毒症”等个体结论。

## Source Signals

- MedlinePlus cellulitis materials.
- MedlinePlus wounds and injuries materials.
- CDC / Sepsis public health materials.
