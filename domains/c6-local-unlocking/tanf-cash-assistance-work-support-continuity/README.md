# TANF Cash Assistance Work Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/tanf-cash-assistance-work-support-continuity` |
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


`tanf-cash-assistance-work-support-continuity` 研究 TANF 现金援助、工作参与、时间限制、制裁、case management、child support cooperation、child care/work support 和州级执行差异如何影响家庭现金流、照护安排、就业连接和儿童发展连续性。

## 核心问题

TANF 不是单纯现金项目，而是家庭、工作、托育、制裁和州级管理共同构成的任务系统。任何一个环节失败，都可能让低收入家庭在食物、住房、儿童照护、交通和就业之间失去稳定行动窗口。

## 对象

- TANF cash assistance、work participation、time limits、sanctions、case management 和 state plan variation。
- child care、transportation、work supports、child support cooperation、家庭暴力例外和 hardship 机制。
- 与 SNAP、Medicaid/CHIP、CCDF、housing、workforce services 和 child welfare 的接口。

## Human Infra 价值

- 把低收入家庭现金援助视为儿童发展、照护者工作连续性和家庭风险缓冲基础设施。
- 解释 work requirement、case management 和制裁如何改变有效时间、照护负担和未来选择权。
- 将反稀缺工程从物资获得扩展到家庭任务链路稳定。

## 边界

- 不提供 TANF 资格判断、申请、续期、工作要求合规、制裁处理、child support、托育补贴、法律、税务、移民或个案建议。
- 不代写申请、证明、case plan、good cause、sanction appeal 或机构沟通材料。
- 不帮助规避工作要求、隐瞒收入、虚构家庭组成、逃避 child support cooperation、骗领福利或操纵州级规则。
- 不收集家庭成员、收入、child support、案件号、住址、移民身份或门户凭证。

## 上游与下游

- 上游：`social-protection-benefits-delivery`、`administrative-burden-procedural-friction`、`childcare-family-continuity`。
- 下游：`child-care-subsidy-ccdf-payment-continuity`、`snap-eligibility-recertification-abawd-continuity`、`medicaid-chip-renewal-redetermination-continuity`、`workforce-development-reskilling`。

## 初始资料线索

- ACF Office of Family Assistance TANF: https://www.acf.hhs.gov/ofa/programs/tanf
- ACF TANF policy and guidance: https://www.acf.hhs.gov/ofa/policy-guidance
- ACF TANF data and reports: https://www.acf.hhs.gov/ofa/data
