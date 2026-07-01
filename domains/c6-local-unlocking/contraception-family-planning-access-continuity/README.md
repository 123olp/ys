# Contraception Family Planning Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/contraception-family-planning-access-continuity` |
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


`contraception-family-planning-access-continuity/` 研究避孕可及、选择自主、医学适用性、费用覆盖、供应连续、咨询质量和生育计划如何影响主体持续性。

> 核心问题：生育时间、身体风险、照护责任、教育、工作和长期资源路径都受到避孕与家庭计划可及性的影响。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖身体自主、时间窗口、照护负担、资源计划和关系安全
  -> 避孕与家庭计划决定生育事件是否可被主体纳入长期项目和健康风险管理
  -> 结果取决于选择范围、医学适用性、咨询质量、费用覆盖、供应连续和隐私保护
  -> 因此避孕与家庭计划是时间、身体、资源和未来选择权之间的基础域
```

## 关注对象

- Contraceptive access、family planning、informed choice、medical eligibility, method continuation, side effect counseling, cost coverage, pharmacy access, privacy, reproductive coercion safeguards。
- 与 `reproductive-fertility-continuity/` 的边界：该域关注生殖能力和生育连续性总机制；本域关注避孕与生育计划的可及和选择自主。
- 与 `pregnancy-parental-work-continuity/` 的关系：本域影响孕产前的时间窗口和资源路径。

## Human Infra 模型链路

```text
避孕与家庭计划可及系统 T
  -> 改变方法选择、医学适用性、咨询质量、费用覆盖、供应连续和隐私变量 X
  -> 改变生育时间、身体风险、照护责任、教育/工作连续性和资源计划 S
  -> 改变有效时间损失、健康风险、经济压力和未来选择权 λ(t)
  -> 影响主体长期行动路径、关系自主和代际资源配置
```

## 非目标

- 不提供个人避孕方法选择、医学适用性判断、用药、器械、紧急避孕、流产、妊娠处理、法律或保险建议。
- 不生成个人生育计划、风险评分、咨询替代、禁忌判定或临床分诊。
- 不收集个案性行为、妊娠、伴侣、病史、药物、位置、未成年人或身份敏感资料。

## Source Signals

- CDC U.S. Medical Eligibility Criteria for Contraceptive Use: https://www.cdc.gov/contraception/hcp/usmec/
- CDC U.S. Selected Practice Recommendations for Contraceptive Use: https://www.cdc.gov/contraception/hcp/usspr/
- HHS Office on Women's Health birth control: https://www.womenshealth.gov/a-z-topics/birth-control-methods

## 下一步

- 建立 Family Planning Continuity Card：choice, eligibility, counseling, cost, supply, privacy, coercion safeguards, follow-up。
- 与 `reproductive-fertility-continuity/`、`pregnancy-parental-work-continuity/` 和 `health-insurance-enrollment-renewal-continuity/` 建立接口。
