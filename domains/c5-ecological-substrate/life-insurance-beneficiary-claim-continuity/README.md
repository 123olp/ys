# Life Insurance Beneficiary Claim Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/life-insurance-beneficiary-claim-continuity` |
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


Life Insurance Beneficiary Claim Continuity 研究寿险保单、受益人指定、保单定位、死亡理赔、未领取权益和争议边界如何把死亡风险池转化为幸存者可获得资源。

> 核心问题：寿险的价值不在保单存在，而在死亡后受益人能否知道、证明、申请并实际获得给付；保单失联会把风险转移工具变成沉没文件。

## 研究对象

- Life insurance policy、beneficiary designation、claim、policy locator、unclaimed benefits 和 group life insurance。
- 受益人记录更新、保单查找、死亡证明、理赔文件、雇主团体寿险和州监管/未领取财产。
- 受益人冲突、离婚/再婚、未成年受益人、信托受益人、诈骗和身份核验。

## 先验链路

```text
主体生前可能通过寿险把死亡风险转移给保险池
  -> 死亡后受益人必须知道保单存在并完成身份、死亡和受益权证明
  -> 保单、受益人或理赔入口若失联，风险转移无法兑现
  -> 幸存者失去偿债、丧葬、住房、教育和恢复所需资源
  -> 家庭未来选择权和财务韧性下降
  -> 因而寿险受益人与理赔链是死亡后风险转移兑现层
```

## 关键变量

- 保单可发现性、受益人记录准确性、理赔入口、证明材料、理赔延迟和未领取权益。
- 个人寿险、团体寿险、雇主福利、州保单定位器、未领取财产和监管投诉路径。
- 受益人争议、未成年/失能受益人、家庭暴力、诈骗、身份盗用和隐私风险。

## 证据入口

- NAIC Life Insurance Policy Locator and consumer materials。
- State insurance department consumer materials。
- Employer group life and unclaimed property public materials。

## 非目标

- 本域不推荐寿险、计算保额、解释保单、判断受益人、代写理赔或争议材料。
- 不提供法律、税务、保险、投资、遗产规划或个案财务建议。
- 不收集保单号、死亡证明、受益人信息、身份证件、银行账户或理赔资料。

## 上下游

- 上游：`death-certificate-registration-cause-of-death-record-continuity/`、`insurance-risk-transfer/`、`retirement-pension-savings-plan-continuity/`。
- 下游：`survivor-benefits-death-notification-continuity/`、`estate-inventory-asset-liability-handoff-continuity/`、`financial-resilience-access/`。
