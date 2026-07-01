# Crane Derrick Hoist Rigging Suspended Load Continuity

`crane-derrick-hoist-rigging-suspended-load-continuity/` 研究起重机、桅杆起重机、葫芦、吊装索具、悬吊载荷、指挥通信和坠落/碰撞/压伤如何影响工作者主体持续性。

核心问题：

> 当建设、制造和物流任务依赖重物提升时，主体能否不被悬吊载荷、失控吊装和沟通失败转化为压伤、创伤、死亡和长期劳动能力损失。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要通过施工、制造、维修和物料搬运获取资源
  -> 起重吊装把主体置于悬吊载荷、坠落物、碰撞、压伤和通信失效窗口
  -> 吊装失败会快速造成死亡、截肢、TBI、骨折和大出血
  -> 因此起重吊装安全是工业任务持续性的基础执行条件
```

## 关注对象

- Cranes、derricks、hoists、rigging、suspended loads、struck-by/crushed-by hazards、signal person、lift planning evidence boundary、exclusion zone。
- 风险链：提升任务 -> 载荷/索具/通信/区域控制失效 -> 坠落或摆动 -> 击打/压伤 -> 创伤、失能和停工。
- 制度链：qualified-person interface、inspection evidence、communication protocol、contractor coordination、incident reporting。

## Human Infra 模型位置

```text
起重吊装任务 T
  -> 改变悬吊载荷暴露 X
  -> 改变身体完整性和现场逃逸状态 S
  -> 改变急性死亡/压伤/击打风险 lambda(t)
  -> 改变有效工作年限、技能资本和未来选择权
```

## 非目标

- 不提供吊装方案、索具计算、载荷图使用、手势信号、设备操作、检查、认证、维修、施工、合规或现场安全方案。
- 不判断个人工伤、责任、赔偿、复工、事故调查、OSHA 违规或法律策略。
- 不帮助规避安全规则、绕开培训、隐藏事故、替代雇主安全计划或现场专业人员。

## Source Signals

- OSHA Crane, Derrick and Hoist Safety: https://www.osha.gov/cranes-derricks
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Suspended Load Continuity Card：load exposure、rigging evidence、communication boundary、exclusion zone、inspection evidence、rescue/EMS latency、incident reporting。
- 与 `occupational-exposure-industrial-hygiene/`、`human-factors-ergonomics-task-system-continuity/` 和 `trauma-system-hemorrhage-control-continuity/` 建立接口。
