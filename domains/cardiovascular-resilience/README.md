# Cardiovascular Resilience

Cardiovascular Resilience 负责整理心脏、血管、血压、动脉粥样硬化、血栓、卒中、心衰和循环系统韧性。

核心问题：

> 主体所有行动都依赖循环系统持续供氧、供能和清除代谢废物；心血管失效是主体持续性最常见、最关键的终止通道之一。

## 先验位置

```text
主体持续性最大化
  -> 大脑、肌肉、器官和修复系统依赖稳定循环
  -> 血压、血管弹性、斑块、血栓和心脏泵功能决定主要死亡风险
  -> 心血管事件会突然截断行动、认知和未来选择权
  -> 因此循环系统韧性是风险函数 λ(t) 的核心组成
```

## 关注对象

- 血压、血脂、动脉粥样硬化、冠心病、卒中、心衰、房颤和血栓风险。
- 心血管风险与营养、活动、睡眠、压力、空气污染、糖尿病和肾脏功能的交叉。
- 一级预防、早筛、风险评分和治疗证据的边界整理。
- 与 `measurement-feedback/` 的关系：风险评分和生物标志物必须保留适用人群、校准范围和不确定性。

## Human Infra 模型链路

```text
心血管干预 / 风险控制 T
  -> 改变血压、血脂、炎症、血栓、血管和心脏功能 X
  -> 改变循环系统状态 S
  -> 改变心梗、卒中、心衰、失能和死亡风险 λ(t)
  -> 改变健康寿命、认知连续性和有效行动时间
```

## 非目标

- 不提供诊断、用药、剂量、筛查频率、手术或治疗建议。
- 不把单项指标直接写成个体死亡风险结论。
- 不输出个体心血管事件预测日期。

## Source Signals

- WHO Cardiovascular Diseases: https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)
- WHO Hypertension: https://www.who.int/news-room/fact-sheets/detail/hypertension
