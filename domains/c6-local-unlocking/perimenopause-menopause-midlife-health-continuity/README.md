# Perimenopause Menopause Midlife Health Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/perimenopause-menopause-midlife-health-continuity` |
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


`perimenopause-menopause-midlife-health-continuity/` 研究围绝经期、更年期症状、睡眠、情绪、骨骼、心血管、泌尿生殖健康、工作参与和医疗决策如何影响主体持续性。

> 核心问题：围绝经期不是单一症状事件，而是睡眠、情绪、骨骼、心血管、性健康、工作能力和长期风险重新排序的中年窗口。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖中年阶段的骨骼、睡眠、情绪、代谢、性健康和工作参与维护
  -> 围绝经期/更年期可改变症状负担、恢复能力、风险感知和医疗决策
  -> 结果取决于信息质量、非污名沟通、症状管理可及、风险评估和共享决策
  -> 因此更年期是寿命中段风险转轨和有效时间保护的关键域
```

## 关注对象

- Perimenopause、menopause symptoms、vasomotor symptoms、sleep disruption、mood, bone health, cardiovascular risk, genitourinary syndrome, workplace participation, hormone therapy decision support boundaries。
- 与 `endocrine-hormonal-regulation/` 的边界：该域关注激素调节总机制；本域关注围绝经期到中年健康的执行和决策连续性。
- 与 `osteoporosis-fracture-prevention-bone-health-continuity/` 的关系：骨量和骨折风险是更年期后长期持续性的关键分支。

## Human Infra 模型链路

```text
围绝经期与中年健康支持系统 T
  -> 改变症状识别、睡眠质量、情绪稳定、骨骼风险、泌尿生殖健康和工作支持变量 X
  -> 改变恢复能力、有效时间、关系参与、长期风险感知和医疗决策状态 S
  -> 改变失眠、抑郁、骨折、心血管风险、工作退出和生活质量损失 λ(t)
  -> 影响主体中年到老年阶段的行动能力、健康寿命和未来选择权
```

## 非目标

- 不提供个人激素治疗、补充剂、用药、检查排序、症状诊断、癌症/心血管风险判断或治疗建议。
- 不生成个人更年期评分、处方替代、工作证明、保险路径或临床分诊。
- 不收集个案月经、症状、病史、用药、癌症风险、性健康、工作或身份敏感资料。

## Source Signals

- NIA menopause: https://www.nia.nih.gov/health/menopause/what-menopause
- HHS Office on Women's Health menopause: https://www.womenshealth.gov/menopause
- NIH menopause hormone therapy information: https://www.nia.nih.gov/health/menopause/hormone-therapy-menopause

## 下一步

- 建立 Menopause Continuity Card：symptoms, sleep, mood, bone, cardiovascular, genitourinary, work participation, shared decision boundary。
- 与 `endocrine-hormonal-regulation/`、`osteoporosis-fracture-prevention-bone-health-continuity/` 和 `sleep-circadian-recovery/` 建立接口。
