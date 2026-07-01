# Endocrine Hormonal Regulation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/endocrine-hormonal-regulation` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


Endocrine Hormonal Regulation 负责整理内分泌系统、激素轴、代谢信号、压力反应、生长、生殖、骨骼和情绪调节如何支撑主体持续性。

核心问题：

> 主体不是一堆独立器官，而是被激素信号长期协调的动态系统；激素失衡会把代谢、睡眠、情绪、骨骼、免疫和生殖同时推入风险状态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须长期维持跨器官协调
  -> 激素系统调度能量、压力、生长、修复、生殖、骨骼和昼夜节律
  -> 内分泌失衡会改变代谢状态、认知情绪、组织维护和疾病风险
  -> 因此内分泌激素调节是跨系统稳态域
```

## 关注对象

- 甲状腺、胰岛、肾上腺、性腺、垂体、下丘脑和骨代谢相关激素轴。
- 胰岛素、皮质醇、甲状腺激素、性激素、生长激素、维生素 D / PTH 等状态变量。
- 糖尿病、甲状腺疾病、肾上腺异常、骨质疏松、生殖衰退、压力轴紊乱。
- 激素系统与代谢、睡眠、心理、免疫、肌骨、心血管和衰老机制的交叉。

## Human Infra 模型链路

```text
内分泌状态或干预 T
  -> 改变激素水平、受体敏感性、反馈环和跨器官信号 X
  -> 改变代谢、修复、情绪、睡眠、骨骼和免疫状态 S
  -> 改变慢病、失能、认知情绪崩塌和死亡风险 λ(t)
  -> 影响有效时间、恢复能力和长期行动窗口
```

## 非目标

- 不提供激素检测解释、补充、处方、剂量、停药、周期管理或治疗建议。
- 不把单个激素指标写成寿命预测或主体能力判断。
- 不替代 `nutrition-metabolic-health/`、`sleep-circadian-recovery/`、`mental-health-affective-stability/` 或 `musculoskeletal-integrity/`。

## Source Signals

- NIDDK endocrine diseases: https://www.niddk.nih.gov/health-information/endocrine-diseases
- NIDDK diabetes overview: https://www.niddk.nih.gov/health-information/diabetes
- Endocrine Society hormone health resources: https://www.endocrine.org/patient-engagement/endocrine-library

## 下一步

1. 建立激素轴变量表：轴、信号、反馈、目标器官、失败模式和证据类型。
2. 与 `nutrition-metabolic-health/`、`sleep-circadian-recovery/`、`mental-health-affective-stability/` 和 `musculoskeletal-integrity/` 建立边界。
