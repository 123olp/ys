# Surgical Wound, Dehiscence and Surgical Site Infection Continuity

`surgical-wound-dehiscence-ssi-continuity/` 研究手术切口闭合、裂开、手术部位感染、出院后监测、护理交接和复诊延迟如何影响主体恢复、再入院和行动连续性。

> 核心问题：手术把身体打开后再关闭；切口闭合和感染治理决定治疗是否真正完成。

## 先验位置

```text
有效永生
  -> 主体可能依赖手术修复或替代身体功能
  -> 手术切口必须稳定闭合并避免感染失控
  -> 切口裂开或手术部位感染会把修复路径转化为新风险
  -> 因此手术伤口连续性是外科干预能否净增主体持续性的门槛域
```

## 关注对象

- Surgical wound, incision, dehiscence, surgical site infection, discharge instructions, follow-up, readmission and care transition。
- 与 `surgical-anesthesia-perioperative-safety/` 的关系：后者关注围手术期安全总域，本域关注切口、闭合、SSI 和出院后连续性。

## Human Infra 模型链路

```text
手术切口连续性 T
  -> 改变切口闭合、污染暴露、SSI 风险、出院交接和复诊延迟 X
  -> 改变恢复速度、疼痛、活动限制和再入院状态 S
  -> 改变感染、再手术、住院和死亡风险 lambda(t)
  -> 改变医学干预的净收益和有效恢复时间
```

## 非目标

- 不提供切口诊断、裂开判断、抗生素、换药、拆线、复诊策略、急诊判断或个体术后建议。
- 不解释个人手术记录、照片、引流、发热或实验室结果。

## Source Signals

- CDC / NHSN surgical site infection materials.
- CDC healthcare-associated infection materials.
- AHRQ surgical safety and discharge communication materials.
