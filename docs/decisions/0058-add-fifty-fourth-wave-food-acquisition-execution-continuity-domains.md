# 0058 Add Fifty Fourth Wave Food Acquisition Execution Continuity Domains

Date: 2026-06-30

Status: Accepted

## Context

Human Infra 已经有 `food-security-nutrition-access`、`food-safety-contamination-control`、`school-meals-nutrition-access-continuity`、家庭冷藏、家庭烹饪、公共饮水和农业/渔业上游系统。但这些域仍不能完整覆盖“食物如何在最后执行层被主体真实获得并转化为餐食”的问题。

主体持续性依赖稳定营养输入。营养输入不仅由生产、供应和营养知识决定，也由 grocery 可达、SNAP/EBT 兑换、WIC 兑换、食品银行、灾害供餐、送餐/集体餐、婴儿配方供应和外部熟食安全这些执行接口共同决定。

## Decision

新增第 54 波 8 个食物获得执行连续性研究域：

- `domains/c5-ecological-substrate/grocery-retail-food-store-access-continuity/`
- `domains/c5-ecological-substrate/snap-ebt-redemption-retailer-payment-continuity/`
- `domains/c2-source-maintenance/wic-benefit-redemption-infant-maternal-nutrition-continuity/`
- `domains/c5-ecological-substrate/food-bank-pantry-community-food-distribution-continuity/`
- `domains/c5-ecological-substrate/emergency-food-disaster-feeding-continuity/`
- `domains/c5-ecological-substrate/home-delivered-meals-congregate-nutrition-services-continuity/`
- `domains/c5-ecological-substrate/infant-formula-baby-food-supply-safety-continuity/`
- `domains/c5-ecological-substrate/prepared-food-restaurant-cafeteria-safety-access-continuity/`

这些域分别承载 grocery/食品零售、SNAP EBT 兑换、WIC 母婴营养兑换、食品银行/pantry、灾害供餐、送餐/集体营养服务、婴儿配方/婴幼儿食品供应安全和餐馆/cafeteria 熟食安全可达连续性。

## Boundary

这些域不能简单并入 `food-security-nutrition-access`、`food-safety-contamination-control`、`social-protection-benefits-delivery`、`school-meals-nutrition-access-continuity`、`cooking-meal-preparation-kitchen-safety-continuity`、`grocery` 类消费指南或 `emergency-preparedness-response`，因为它们关注的是食物在最后执行层如何通过商店、福利凭证、社区发放、灾害供餐、送餐服务、婴儿配方供应和外部熟食场景真实到达主体。

禁止用途包括：

- 福利资格规避、EBT/eWIC 破解、PIN 获取、盗刷、福利转售、零售商欺诈。
- 食品发放重复领取、物资骗领、库存操纵、囤积套利、灾害发放点实时跟踪。
- 婴儿喂养医疗建议、配方自制、召回规避、进口规避、特殊医学配方获取策略。
- 餐馆推荐、饮食处方、过敏医疗建议、卫生评分攻击、外卖平台规避或个案投诉策略。
- 收集福利卡号、PIN、儿童身份、购买记录、家庭收入、配送路线、受灾者身份或个人医疗/福利材料。

## Source Signals

优先使用 USDA ERS Food Access Research Atlas / Food Environment Atlas、USDA FNS SNAP、SNAP Retailer、SNAP Online Purchasing、WIC、WIC Food Packages、WIC EBT、TEFAP、Food Distribution Programs、Disaster Assistance、D-SNAP、FDA Infant Formula、FDA Recalls、CDC Infant and Toddler Nutrition、ACL Nutrition Services、Older Americans Act、FDA Food Code、CDC Food Safety、FDA Food Allergies、地方公共卫生和食品服务公开资料。

## Consequences

- `domains/` 增加 8 个新子域，每个子域必须有独立 `README.md` 与 `AGENTS.md`。
- 根 `README.md`、根 `AGENTS.md`、`docs/`、`domains/`、reference 索引和 `tools/check_repository.py` 必须同步补齐。
- 后续研究应把这些域建模为营养输入的执行接口，而不是个体购物建议、福利申请服务、营养处方、餐馆推荐、食品制备教程或个案法律/医疗/福利策略。
