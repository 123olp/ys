# SNAP EBT Redemption Retailer Payment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/snap-ebt-redemption-retailer-payment-continuity` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

`snap-ebt-redemption-retailer-payment-continuity` 研究 SNAP 资格之外的执行层：EBT 卡、PIN、余额、授权零售商、在线购买、交易失败、系统中断、替换卡和支付恢复如何影响食物福利能否真实兑换为食物。

> 核心问题：福利批准不等于食物到手；如果 EBT 支付、授权零售商或账户恢复失败，名义营养援助会停在制度记录里。

## 关注对象

- SNAP EBT 卡、PIN、余额查询、交易授权、授权零售商、在线 SNAP、替换卡、盗刷/丢失、系统中断和客户服务。
- 零售商覆盖、支付网络、账户安全、错误交易、排队摩擦、停电灾害、语言可达和残障可达。
- 与 USDA FNS SNAP、州 EBT 管理、零售商授权、消费者保护、反欺诈、数字支付和食品零售可达的接口。

## Human Infra 链路

```text
SNAP EBT 可安全兑换
  -> 营养援助从资格记录转成可购买食物
  -> 支付失败、账户失控、零售商不可用和交易摩擦风险下降
  -> 家庭在收入冲击中仍能维持基本食物输入
  -> 主体恢复能力、预算韧性和未来选择权增强
```

## 非目标

- 不提供 SNAP 资格判断、申请材料、规避规则、福利欺诈、EBT 破解、PIN 获取、盗刷、转售福利、零售商欺诈或个案申诉策略。
- 不替代 USDA FNS、州 SNAP/EBT 机构、授权零售商、支付处理方、消费者保护、法律或社会服务。
- 不收集 EBT 卡号、PIN、余额截图、交易记录、家庭身份、收入材料、地址、账户凭据或个案福利文件。

## Source Signals

- USDA FNS SNAP: https://www.fns.usda.gov/snap/supplemental-nutrition-assistance-program
- USDA FNS SNAP Retailers: https://www.fns.usda.gov/snap/retailer
- USDA FNS SNAP Online Purchasing: https://www.fns.usda.gov/snap/online-purchasing-pilot
- USDA FNS SNAP Retailer Locator: https://www.fns.usda.gov/snap/retailer-locator

## 下一步

- 建立 `benefit account -> payment credential -> retailer acceptance -> transaction outcome -> food continuity` 变量表。
- 区分资格决定、EBT 凭证、授权零售、在线购买、系统中断、盗刷恢复和灾害替代支付。
- 与 `social-protection-benefits-delivery`、`food-security-nutrition-access`、`grocery-retail-food-store-access-continuity`、`financial-inclusion-payment-systems` 和 `fraud-scams-consumer-protection` 建立边界。
