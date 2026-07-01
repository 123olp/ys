# Diabetic Foot Ulcer and Amputation Prevention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/diabetic-foot-ulcer-amputation-prevention-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
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


`diabetic-foot-ulcer-amputation-prevention-continuity/` 研究糖尿病相关神经病变、血流不足、足部伤口、感染、鞋袜/足部保护、筛查和照护延迟如何影响行动能力、截肢风险和主体持续性。

> 核心问题：糖尿病足把代谢、神经、血管、皮肤、感染和行动系统压缩在同一个末端失效点上。

## 先验位置

```text
有效永生
  -> 主体必须维持行动底盘和远端组织完整性
  -> 糖尿病可同时影响感觉、血流、免疫和伤口愈合
  -> 足部伤口和感染会放大截肢、失能和死亡风险
  -> 因此糖尿病足是代谢病影响主体行动连续性的关键执行域
```

## 关注对象

- Diabetic foot, neuropathy, peripheral artery disease, foot ulcer, infection, amputation prevention, footwear, screening and follow-up。
- 与 `peripheral-neuropathy-somatosensory-continuity/` 的关系：后者关注感觉输入，本域关注感觉缺失进入足部伤口和截肢链路。

## Human Infra 模型链路

```text
糖尿病足预防连续性 T
  -> 改变感觉反馈、足部压力、血流、感染入口、筛查和照护延迟 X
  -> 改变足部组织完整性、行动能力和截肢风险状态 S
  -> 改变住院、截肢、失能和死亡风险 lambda(t)
  -> 改变主体移动自由、有效时间和长期照护需求
```

## 非目标

- 不提供足部检查结论、伤口照片判断、鞋垫/鞋类推荐、抗生素、清创、手术或个体治疗建议。
- 不替代糖尿病管理、外周神经、血管、感染和康复域。

## Source Signals

- NIDDK diabetes foot problems materials.
- CDC diabetes and your feet materials.
- MedlinePlus diabetic foot and wound materials.
