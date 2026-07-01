# Occupational Electrical Shock Arc Flash Continuity

`occupational-electrical-shock-arc-flash-continuity/` 研究职业电气暴露、电击、电弧闪爆、电弧爆炸、临时用电、架空线路和带电系统任务如何影响工作者主体持续性。

核心问题：

> 当工作任务接近电能系统时，主体能否不把维修、施工、检测和操作窗口转换成电击、烧伤、心律失常、爆炸创伤或死亡。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要在施工、维修、制造和公共服务中接触电能系统
  -> 电能把任务置于电击、触电死亡、电弧闪爆、烧伤和爆炸窗口
  -> 电气事故会快速造成心脏骤停、热损伤、创伤和长期功能损失
  -> 因此职业电气安全是技术工作持续性的基础执行条件
```

## 关注对象

- Occupational electrical exposure、electric shock、electrocution、arc flash/blast、temporary power、overhead lines、energized-system boundary、task authorization。
- 风险链：电气任务 -> 接近或接触带电系统 -> 电击/闪爆/爆炸 -> 死亡、烧伤、神经/心脏损伤和长期恢复。
- 制度链：hazard identification、authorization boundary、de-energization interface、training evidence、incident reporting。

## Human Infra 模型位置

```text
职业电气任务 T
  -> 改变电击/闪爆暴露 X
  -> 改变心脏、电神经、皮肤和创伤状态 S
  -> 改变急性死亡/烧伤/失能风险 lambda(t)
  -> 改变有效工作年限、技术技能资本和未来选择权
```

## 非目标

- 不提供电气施工、布线、带电作业、故障排查、电弧闪爆计算、PPE 类别、锁定挂牌、维修、设备操作、合规或现场安全方案。
- 不替代 `residential-electrical-wiring-outlet-safety-continuity/` 的家庭用电边界，也不替代 `hazardous-energy-lockout-tagout-continuity/` 的能量隔离边界。
- 不判断个人工伤、责任、赔偿、复工、事故调查、OSHA 违规或法律策略。

## Source Signals

- OSHA Electrical: https://www.osha.gov/electrical
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Electrical Continuity Card：energized exposure、shock path、arc-flash boundary、temporary/overhead power interface、authorization evidence、EMS latency、incident reporting。
- 与 `hazardous-energy-lockout-tagout-continuity/`、`burn-injury-critical-care-rehabilitation-continuity/` 和 `cardiac-arrest-cpr-defibrillation-continuity/` 建立接口。
