# WIC Benefit Redemption Infant Maternal Nutrition Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/wic-benefit-redemption-infant-maternal-nutrition-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

`wic-benefit-redemption-infant-maternal-nutrition-continuity` 研究 WIC 食物包、eWIC、授权商店、婴儿配方、母婴营养、转介服务和兑换失败如何影响孕产妇、婴幼儿和儿童的营养连续性。

> 核心问题：WIC 的价值不只在资格，而在被及时兑换为母婴可用食物、配方、营养支持和转介服务。

## 关注对象

- WIC 食物包、eWIC 卡、授权商店、approved foods、婴儿配方、母乳喂养支持、营养教育和健康/社会服务转介。
- 余额、购物限制、库存、替代品、语言服务、门店距离、配方短缺、预约/续期、身份隐私和儿童照护负担。
- 与 USDA FNS WIC、州 WIC、食品零售、婴儿配方安全、母婴健康、公共卫生和社会服务的接口。

## Human Infra 链路

```text
WIC 福利可兑换且适配母婴需求
  -> 孕产妇、婴幼儿和儿童获得稳定营养输入
  -> 配方短缺、兑换失败、门店不可达和营养支持中断风险下降
  -> 早期生命发育、照护负担和家庭预算更可维持
  -> 主体早期基础能力和未来选择权增强
```

## 非目标

- 不提供 WIC 资格判断、申请材料、规避规则、福利欺诈、eWIC 破解、配方囤积转售、婴儿喂养医疗建议或个案申诉策略。
- 不替代 USDA FNS、州 WIC、儿科医生、营养师、哺乳顾问、零售商、社会服务或法律服务。
- 不收集 eWIC 卡号、儿童身份、孕产健康信息、喂养记录、家庭收入、地址、预约资料或个案福利文件。

## Source Signals

- USDA FNS WIC: https://www.fns.usda.gov/wic
- USDA FNS WIC Food Packages: https://www.fns.usda.gov/wic/food-packages
- USDA FNS WIC EBT: https://www.fns.usda.gov/wic/wic-ebt
- FDA Infant Formula: https://www.fda.gov/food/people-risk-foodborne-illness/infant-formula

## 下一步

- 建立 `wic package -> eWIC credential -> authorized retailer -> infant/maternal nutrition input -> development continuity` 变量表。
- 区分 WIC 资格、eWIC 支付、授权食品、配方可得、母乳支持、营养教育和转介服务。
- 与 `maternal-newborn-child-development`、`food-security-nutrition-access`、`infant-formula-baby-food-supply-safety-continuity`、`grocery-retail-food-store-access-continuity` 和 `social-protection-benefits-delivery` 建立边界。
