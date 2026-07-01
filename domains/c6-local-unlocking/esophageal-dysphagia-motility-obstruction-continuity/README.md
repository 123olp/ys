# Esophageal Dysphagia Motility Obstruction Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/esophageal-dysphagia-motility-obstruction-continuity` |
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


Esophageal dysphagia motility obstruction continuity studies the passage of swallowed material through the esophagus, including obstruction, motility difficulty, reflux-related burden, and delayed transfer from swallowing to digestion.

核心问题：

> 吞下不等于进入营养链；食管通过失败会让进食变成卡顿、疼痛、反流、体重下降和诊疗延迟。

## 先验位置

```text
主体持续性最大化
  -> 外部食物必须通过入口和食管转入消化吸收系统
  -> 食管负责从咽部向胃部转运食团
  -> 狭窄、梗阻、运动障碍或反流会破坏摄食效率和安全
  -> 因而食管吞咽连续性是吞咽入口和胃肠吸收之间的通道条件
```

## 关注对象

- 吞咽后卡顿、食管运动、结构性狭窄、反流负担、进食回避、体重变化和就医延迟。
- 与 `oropharyngeal-dysphagia-swallow-safety-continuity/` 的关系：口咽域关注气道保护；本域关注食管转运。
- 与 `gastrointestinal-barrier-absorption/` 的关系：胃肠域关注吸收；本域关注到达吸收系统前的食管通道。

## Human Infra 模型链路

```text
识别 / 评估 / 诊疗路径 / 营养支持 T
  -> 改变食管通道、吞咽舒适度、进食效率和体重风险变量 X
  -> 改变营养进入、疼痛负担、回避行为和诊疗连续性状态 S
  -> 改变营养不足、脱水、急性梗阻、住院和有效时间损失风险 λ(t)
  -> 影响主体能量输入、行动能力和未来选择权
```

## 非目标

- 不提供食管疾病诊断、内镜解释、吞咽检查解释、药物、手术、饮食调整或急诊判断。
- 不根据个人卡食、疼痛、反流、体重或检查结果判断病因和风险等级。
- 不替代胃肠、耳鼻喉、营养、急诊或临床照护服务。

## Source Signals

- NIDCD dysphagia resources。
- MedlinePlus swallowing and esophageal disorder materials。
- Gastroenterology guideline literature as research context。
