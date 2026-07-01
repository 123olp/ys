# Retinal Detachment Urgent Referral Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/retinal-detachment-urgent-referral-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


`retinal-detachment-urgent-referral-continuity/` 负责整理视网膜脱离、症状识别、急诊转诊、手术窗口和急性中央/周边视觉保护连续性。

核心问题：

> 视网膜脱离是时间敏感型视觉连续性事件；从症状信号到眼科急诊转诊的延迟，会直接改变视觉功能保留和主体长期行动能力。

## 先验位置

```text
主体持续性最大化
  -> 主体必须保护视网膜作为视觉信号输入层
  -> 视网膜脱离可快速破坏光感受和视觉通路
  -> 症状识别、转诊速度和手术窗口决定可挽回视觉范围
  -> 因此视网膜脱离急转连续性是视觉输入急性救援路径
```

## 关注对象

- 视网膜脱离、闪光、飞蚊、视野遮挡、急性视力变化和高风险人群资料。
- 急诊识别、初级接触点、眼科转诊、手术可及性、术后随访和功能恢复。
- 驾驶、工作、阅读、跌倒、心理压力和照护依赖。
- 与 `emergency-preparedness-response/` 的关系：本域聚焦眼科急转机制；应急域负责通用急救系统。

## Human Infra 模型链路

```text
症状识别 / 急转通道 / 眼科手术窗口 T
  -> 改变转诊延迟、视网膜状态、黄斑受累、治疗窗口和随访变量 X
  -> 改变主体视觉保留、移动、阅读、工作和心理状态 S
  -> 改变不可逆视损、失能、照护依赖和未来选择权丧失风险
  -> 保护急性视觉连续性、行动能力和长期功能窗口
```

## 非目标

- 不提供症状分诊、急救步骤、是否急诊判断、影像判读、手术建议、体位建议或个体预后。
- 不根据飞蚊、闪光、照片或描述判断个人是否视网膜脱离。
- 不替代眼科急诊、急诊科、验光、手术团队或术后随访。

## Source Signals

- National Eye Institute Retinal Detachment: https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/retinal-detachment
- CDC Vision Health: https://www.cdc.gov/vision-health/
- American Academy of Ophthalmology Retinal Detachment: https://www.aao.org/eye-health/diseases/what-is-retinal-detachment

## 下一步

- 建立视网膜脱离 Source Card，区分症状信号、急转通道、手术窗口和功能后果。
- 对接急诊转诊、交通移动、低视力康复和患者权益沟通域。
