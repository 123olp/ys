# Machine Guarding Amputation Prevention Continuity

`machine-guarding-amputation-prevention-continuity/` 研究机器防护、夹点、切割点、旋转部件、传动部件、amputation risk、维护绕行和生产压力如何影响主体持续性。

核心问题：

> 机器把人的力量放大，也会把人的身体暴露给更高能量密度；防护失效会把工作技能直接转化为截肢和长期功能损失。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体通过机器放大生产和行动能力
  -> 机器存在切割、夹卷、剪切、冲压、旋转和传动危险点
  -> 防护被移除、失效或绕过时，身体完整性变成系统薄弱点
  -> 因此机器防护是工作能力不被设备反噬的基础条件
```

## 关注对象

- Machine guarding、point of operation、nip point、rotating parts、amputation hazards、interlocks、maintenance bypass、production pressure。
- 风险链：机器任务 -> 防护缺失/绕行 -> 接触危险点 -> 截肢/挤压/撕裂 -> 长期功能和收入损失。
- 制度链：guard design、maintenance、training、lockout interface、incident learning、production incentive。

## Human Infra 模型位置

```text
机器任务 T
  -> 改变危险点暴露 X
  -> 改变身体完整性和技能执行状态 S
  -> 改变急性创伤/截肢风险 lambda(t)
  -> 改变行动能力、劳动收入和未来选择权
```

## 非目标

- 不提供机器防护设计、改装、维修、绕行、interlock、设备调试、合规检查或现场安全方案。
- 不判断事故责任、工伤、复工、赔偿、OSHA 违规或法律策略。
- 不帮助提高产能而降低防护、移除 guard、规避停机或隐藏 near miss。

## Source Signals

- OSHA Machine Guarding: https://www.osha.gov/machine-guarding
- OSHA Control of Hazardous Energy: https://www.osha.gov/control-hazardous-energy

## 下一步

- 建立 Machine Guarding Continuity Card：machine type、point-of-operation exposure、guard/interlock boundary、maintenance bypass、training、incident pathway。
- 与 `hazardous-energy-lockout-tagout-continuity/`、`occupational-exposure-industrial-hygiene/` 和 `rehabilitation-functioning/` 建立接口。
