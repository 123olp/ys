# Menstrual Health Cycle Literacy Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/menstrual-health-cycle-literacy-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`menstrual-health-cycle-literacy-continuity/` 研究月经健康、周期素养、异常信号识别、卫生用品可及、疼痛/出血负担、学校/工作支持和医疗转介如何影响主体持续性。

> 核心问题：月经健康影响有效时间、学习工作参与、贫血风险、疼痛负担、生殖健康识别和身体自主，不能只被当作私人小问题。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要能理解、管理和求助自身周期性身体信号
  -> 月经异常、疼痛、重度出血、贫困和污名会持续消耗学习、工作、运动和关系行动
  -> 结果取决于周期素养、用品可及、学校/工作支持、异常转介和非污名环境
  -> 因此月经健康是身体信号、有效时间和制度可及之间的基础域
```

## 关注对象

- Menstrual health literacy、cycle tracking as education not surveillance、period poverty、dysmenorrhea burden、heavy menstrual bleeding, school/work accommodations, referral pathways, stigma reduction。
- 与 `reproductive-fertility-continuity/` 的边界：该域关注生殖能力和生育连续性；本域关注月经作为日常功能、信号和资源可及问题。
- 与 `pain-suffering-control/` 的关系：月经痛和相关慢性痛会持续消耗有效时间。

## Human Infra 模型链路

```text
月经健康与周期素养支持系统 T
  -> 改变周期理解、用品可及、疼痛/出血负担、异常识别、支持环境和转介变量 X
  -> 改变贫血风险、学校/工作参与、身体自主、医疗可及和心理负荷 S
  -> 改变有效时间损失、诊断延迟、资源消耗和未来选择权 λ(t)
  -> 影响主体学习、劳动、运动、关系和长期健康路径
```

## 非目标

- 不提供个人周期判读、妊娠判断、疼痛用药、激素治疗、检查排序、诊断、卫生用品选择或医疗建议。
- 不生成个人生殖健康风险评分、周期预测、监控、学校/工作证明或法律建议。
- 不收集个案月经、性行为、妊娠、未成年人、位置、学校、工作或身份敏感资料。

## Source Signals

- NICHD menstruation and menstrual problems: https://www.nichd.nih.gov/health/topics/menstruation
- HHS Office on Women's Health menstrual cycle: https://www.womenshealth.gov/menstrual-cycle
- ACOG menstrual cycle as a vital sign: https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2015/12/menstruation-in-girls-and-adolescents-using-the-menstrual-cycle-as-a-vital-sign

## 下一步

- 建立 Menstrual Health Continuity Card：literacy, supplies, pain, bleeding, participation, referral, privacy, stigma。
- 与 `reproductive-fertility-continuity/`、`pain-suffering-control/` 和 `school-health-services-chronic-condition-continuity/` 建立接口。
