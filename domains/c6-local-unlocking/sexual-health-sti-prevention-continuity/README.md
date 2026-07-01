# Sexual Health STI Prevention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/sexual-health-sti-prevention-continuity` |
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


`sexual-health-sti-prevention-continuity/` 研究性健康、STI 预防、检测、治疗转介、伴侣通知、隐私保护和污名降低如何影响主体持续性。

> 核心问题：性健康不是边缘议题，而是身体完整性、关系安全、生育能力、感染风险、心理状态和医疗可及性的交汇点。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖安全、自主、可获得和可保密的性健康服务维护身体与关系连续性
  -> STI 可通过无症状感染、慢性并发症、传播链、污名和医疗回避改变长期风险
  -> 结果取决于检测可及、治疗转介、伴侣服务、预防工具、隐私和非歧视环境
  -> 因此性健康与 STI 预防是身体、关系和公共卫生之间的基础域
```

## 关注对象

- STI prevention、screening access、testing continuity、treatment referral、partner services、confidentiality、sexual health education、stigma, consent, trauma-informed care。
- 与 `chronic-infectious-disease-care-continuity/` 的边界：该域关注慢性感染照护；本域关注性健康场景下的预防、检测、转介和隐私。
- 与 `personal-safety-violence-prevention/` 的关系：性健康资料必须同时尊重同意、胁迫、暴力和保密边界。

## Human Infra 模型链路

```text
STI 预防与性健康服务系统 T
  -> 改变检测可及、预防工具、治疗转介、伴侣通知、隐私和污名变量 X
  -> 改变感染状态、生殖健康、关系安全、医疗回避和心理负荷 S
  -> 改变慢性并发症、传播风险、有效时间损失和未来选择权 λ(t)
  -> 影响主体身体完整性、关系行动、长期计划和公共卫生屏障
```

## 非目标

- 不提供个人 STI 检测解读、用药、伴侣通知脚本、暴露后处理、性行为建议、诊断、治疗或法律建议。
- 不生成个人感染风险评分、筛查周期、避孕/预防工具选择、暴露判断或临床分诊。
- 不收集个案性行为、伴侣、感染、创伤、定位、未成年人或身份敏感资料。

## Source Signals

- CDC STI treatment guidelines: https://www.cdc.gov/std/treatment-guidelines/default.htm
- CDC STI prevention: https://www.cdc.gov/sti/prevention/
- USPSTF STI recommendations: https://www.uspreventiveservicestaskforce.org/uspstf/topic_search_results?topic_status=P&category%5B%5D=15

## 下一步

- 建立 Sexual Health Continuity Card：prevention, testing, confidentiality, treatment referral, partner services, stigma, safety。
- 与 `hiv-testing-prep-prevention-continuity/`、`reproductive-fertility-continuity/` 和 `personal-safety-violence-prevention/` 建立接口。
