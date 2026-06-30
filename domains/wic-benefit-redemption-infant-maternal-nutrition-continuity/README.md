# WIC Benefit Redemption Infant Maternal Nutrition Continuity

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
