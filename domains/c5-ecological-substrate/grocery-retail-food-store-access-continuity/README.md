# Grocery Retail Food Store Access Continuity

`grocery-retail-food-store-access-continuity` 研究 grocery store、超市、小型食品零售、农贸市场、线上下单取货/配送、营业时段、价格、交通可达和支付入口如何影响主体能否持续获得日常食物。

> 核心问题：食物系统存在不等于食物进入家庭；如果食品零售点不可达、不可负担、不可支付或不可配送，营养输入会在最后一公里断裂。

## 关注对象

- 超市、杂货店、小型食品店、农贸市场、移动市场、线上购物取货、配送覆盖和营业时段。
- 食物可得性、价格、健康食品选择、交通距离、残障可达、支付方式、库存可靠性、停电/灾害闭店和替代购物路径。
- 与 USDA ERS Food Access Research Atlas、地方食品环境、交通、价格冲击、SNAP/WIC 零售商、食品安全和消费者保护的接口。

## Human Infra 链路

```text
食品零售可达且可支付
  -> 家庭日常食物输入能够持续补给
  -> 饥饿、营养质量下降、预算挤压和时间损耗风险下降
  -> 主体可把收入、福利、交通和时间转化为真实餐食
  -> 身体维护、恢复能力和未来选择权增强
```

## 非目标

- 不提供商店推荐、购物清单、囤货策略、价格套利、偷盗、优惠券滥用、支付规避、配送平台规避或个案消费者投诉策略。
- 不替代 USDA、地方食品政策机构、零售商、支付机构、配送平台、营养师、消费者保护或社会服务机构。
- 不收集个人购物记录、支付账号、福利卡号、家庭地址、配送轨迹、库存漏洞、商店安防细节或个人营养隐私。

## Source Signals

- USDA ERS Food Access Research Atlas: https://www.ers.usda.gov/data-products/food-access-research-atlas/
- USDA ERS Food Environment Atlas: https://www.ers.usda.gov/data-products/food-environment-atlas/
- USDA FNS SNAP Retailer Locator: https://www.fns.usda.gov/snap/retailer-locator
- USDA Local Food Directories: https://www.ams.usda.gov/local-food-directories

## 下一步

- 建立 `store -> access mode -> price/payment -> food basket -> nutrition continuity` 变量表。
- 区分全服务超市、小型零售、农贸市场、线上取货配送、灾害替代零售和食品沙漠/低可达区域。
- 与 `food-security-nutrition-access`、`snap-ebt-redemption-retailer-payment-continuity`、`wic-benefit-redemption-infant-maternal-nutrition-continuity`、`transportation-access-mobility` 和 `fraud-scams-consumer-protection` 建立边界。
