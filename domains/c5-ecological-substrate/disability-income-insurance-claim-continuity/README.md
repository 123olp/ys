# 残障收入保险与理赔连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disability-income-insurance-claim-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


本域研究 private disability insurance、employer group disability、short-term disability、long-term disability、elimination period、own occupation / any occupation、medical evidence、claim、appeal 和 termination 如何影响主体疾病伤残后的收入连续性。它关注保险合同型收入替代，而不是公共残障福利、医疗判断、claim 策略或法律建议。

## 研究对象

- 短期残障保险、长期残障保险、雇主团体残障、个人残障收入保险和 rider。
- elimination period、benefit amount、benefit duration、own occupation、any occupation、pre-existing condition 和 offset。
- 医疗证明、功能限制、claim、appeal、independent medical review、termination、surveillance 和复工影响。
- 与公共残障福利、工伤、病假、合理便利和工作能力评估的边界。

## 价值链路

```text
主体因疾病或伤残失去劳动收入
  -> 残障收入保险把工作能力冲击转移为合同型现金流替代
  -> 清晰定义、医学证据和 appeal 入口维持治疗恢复期间的收入连续性
  -> 拒赔、终止、offset 或定义争议会把健康事件扩散为财务危机
  -> 残障收入保险连续性把身体功能变化纳入可审查的收入风险转移
```

## 关键问题

- 私人残障保险与 Social Security disability、工伤和带薪病假如何分界？
- own occupation / any occupation、elimination period 和 offset 如何影响真实保障？
- 医疗证据、功能限制和复工记录如何影响 claim 连续性？
- claim 终止或 appeal 失败如何改变主体治疗、住房和家庭照护路径？

## 上游与下游

- 上游：`workplace-accommodation-return-to-work-continuity/`、`disability-income-work-capacity-benefit-continuity/`、`healthcare-access-continuity/`。
- 下游：`household-budget-cashflow-continuity/`、`paid-sick-family-leave-wage-replacement-continuity/`、`workers-compensation-occupational-injury-benefit-continuity/`、`debt-obligation-collection-relief-continuity/`。

## 非目标

- 不提供残障保险购买、保额选择、claim 填写、医学证明、复工安排、appeal、诉讼、福利申请或法律建议。
- 不判断某人是否残障、是否符合定义、是否应停工、是否应复工或某个 claim 是否应批准。
- 不协助伪造医疗记录、夸大功能限制、隐瞒工作收入、保险欺诈、规避 surveillance、骚扰雇主/保险人或骗取福利。

## 初始资料入口

- NAIC: Disability insurance consumer materials
- State insurance department disability insurance and complaint materials
- DOL / EEOC / SSA public disability context materials
- Official employer benefits and ERISA context materials
