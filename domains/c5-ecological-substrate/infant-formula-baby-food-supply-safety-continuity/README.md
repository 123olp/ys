# Infant Formula Baby Food Supply Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/infant-formula-baby-food-supply-safety-continuity` |
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

`infant-formula-baby-food-supply-safety-continuity` 研究婴儿配方奶粉、婴幼儿食品、特殊医学配方、召回、短缺、WIC 替代、制造质量和安全沟通如何影响早期生命营养连续性。

> 核心问题：婴儿食物没有宽容失败窗口；短缺、污染、召回或替代失败会迅速转化为发育、照护和家庭风险。

## 关注对象

- 婴儿配方、特殊医学配方、婴幼儿食品、召回、短缺、进口替代、制造质量、标签、WIC 替代和安全沟通。
- 供应集中度、库存、污染风险、过敏/特殊需求、医疗配方依赖、价格、家庭寻找成本和监管响应。
- 与 FDA infant formula、USDA WIC、儿科、食品安全、制造质量、供应链韧性和母婴健康的接口。

## Human Infra 链路

```text
婴儿配方和婴幼儿食品供应安全
  -> 早期生命营养输入保持连续且可信
  -> 短缺、污染、召回、错误替代和照护恐慌风险下降
  -> 家庭可以稳定支持发育、睡眠、照护和医疗需求
  -> 主体早期发育基础和未来选择权增强
```

## 非目标

- 不提供婴儿喂养医疗建议、配方替代建议、配方自制、囤积、转售、进口规避、召回规避、医疗配方获取策略或个案护理建议。
- 不替代 FDA、儿科医生、营养师、WIC、制造商、公共卫生、食品安全或医疗机构。
- 不收集儿童身份、健康状况、喂养记录、家庭地址、购买记录、医疗处方、WIC 资料或召回个案材料。

## Source Signals

- FDA Infant Formula: https://www.fda.gov/food/people-risk-foodborne-illness/infant-formula
- FDA Recalls: https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts
- USDA FNS WIC Infant Formula: https://www.fns.usda.gov/wic/infant-formula
- CDC Infant and Toddler Nutrition: https://www.cdc.gov/infant-toddler-nutrition/

## 下一步

- 建立 `formula/product -> supply status -> safety signal -> substitution constraint -> development continuity` 变量表。
- 区分普通配方、特殊医学配方、婴幼儿食品、召回、短缺、WIC 替代和监管响应。
- 与 `wic-benefit-redemption-infant-maternal-nutrition-continuity`、`maternal-newborn-child-development`、`food-safety-contamination-control`、`pharmaceutical-quality-supply-integrity` 和 `supply-chain-continuity` 建立边界。
