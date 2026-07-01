# 学生贷款服务、还款与减免连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/student-loan-servicing-repayment-forgiveness-continuity` |
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


本域研究联邦和私人学生贷款、贷款服务商、还款计划、收入驱动还款、延期、宽限、公共服务减免、免除、违约和记录连续性如何影响主体教育资本、职业选择、现金流和未来行动空间。它关注教育融资的长期服务系统，而不是申请、还款、减免、再融资或法律建议。

## 研究对象

- 联邦学生贷款、私人学生贷款、服务商、账户记录、余额、利息、还款计划和账单。
- 标准还款、收入驱动还款、延期、宽限、合并、再认证、PSLF、discharge、forgiveness 和违约。
- 服务商转移、付款计数、身份认证、记录保全、信用报告、工资扣押和税款抵扣风险。
- 与教育访问、就业资格、信用报告、债务催收和公共福利的边界。

## 价值链路

```text
主体通过学生贷款提前获得教育资本
  -> 贷款服务、还款计划和减免规则把教育收益绑定到长期记录系统
  -> 准确计数、稳定服务和清晰选项维持职业转换与现金流弹性
  -> 服务错误、再认证失败、违约或记录断裂会压缩未来选择权
  -> 学生贷款连续性把教育投资纳入长期主体能力与债务治理
```

## 关键问题

- 还款计划、利息资本化和服务商记录如何影响长期成本？
- 收入驱动还款、PSLF、discharge 和 forgiveness 如何依赖记录连续性？
- 服务商转移、付款计数和再认证失败如何造成主体行动风险？
- 学生贷款与教育访问、职业选择和信用报告如何连接？

## 上游与下游

- 上游：`education-access-learning-continuity/`、`credit-consumer-reporting-access-continuity/`、`employment-income-continuity/`。
- 下游：`debt-obligation-collection-relief-continuity/`、`workforce-credentialing-licensing-continuity/`、`household-budget-cashflow-continuity/`、`public-assistance-benefits-continuity/`。

## 非目标

- 不提供借款、选校、还款计划选择、合并、再融资、PSLF、forgiveness、discharge、违约处理或法律建议。
- 不判断某个贷款、服务商、减免路径、还款计划或申诉是否适合个人。
- 不协助虚假学籍、收入造假、就业证明造假、伪造减免资料、逃债、规避催收、身份欺诈或贷款欺诈。

## 初始资料入口

- Federal Student Aid: Manage Loans and Repayment
- CFPB: Student loans consumer tools
- U.S. Department of Education student loan servicing materials
- CFPB and FSA complaint / servicer transfer materials
