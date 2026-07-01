# Infant Formula Baby Food Supply Safety Continuity

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
