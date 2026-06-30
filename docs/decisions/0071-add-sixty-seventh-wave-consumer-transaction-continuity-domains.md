# ADR 0071: Add Sixty-Seventh-Wave Consumer Transaction Continuity Domains

## Status

Accepted.

## Context

Human Infra 已经覆盖金融包容、银行账户、合同订阅账单、产品安全召回、邮政包裹、个人设备维修、家用电器维修、诈骗消费者保护和旅行中断退款。但主体日常生活中还有一组更基础的“购买到可用结果”的转换链：下单、履约、退换、保修维修、维修权、支付争议、储值余额、费用披露和评价信任。

这些对象不能只放进 `contract-subscription-billing-consent-continuity`、`product-safety-recall-systems`、`postal-parcel-delivery-pickup-continuity` 或 `fraud-scams-consumer-protection`。合同域关注持续同意和账单关系；产品安全关注缺陷和召回；邮政包裹关注物流交付；诈骗域关注欺诈识别和恢复。本波关注的是普通消费者交易如何把金钱、时间、信任和权利转换成实际可用的物品、维修、退款和市场选择。

## Decision

新增第 67 波 8 个消费者交易、履约与市场信任连续性域：

- `online-retail-order-shipping-fulfillment-continuity`
- `consumer-return-refund-dispute-resolution-continuity`
- `consumer-warranty-service-contract-repair-continuity`
- `right-to-repair-parts-manuals-access-continuity`
- `payment-card-dispute-unauthorized-charge-continuity`
- `gift-card-prepaid-stored-value-continuity`
- `price-fee-disclosure-junk-fee-continuity`
- `consumer-reviews-endorsements-marketplace-trust-continuity`

## Consequences

- Human Infra 能把消费者交易连续性拆成可审查域：订单履约、交易失败恢复、保修维修、维修接入、支付纠错、储值余额、价格透明和市场信任。
- 这些域只做公开资料整理、机制建模、证据边界和禁止用途声明；不提供购物推荐、退款脚本、chargeback 策略、维修操作、礼品卡交易、费用规避、营销刷评、个案金融、法律或消费者争议建议。
- 后续若新增 FTC、CFPB、USA.gov、U.S. DOT、州消费者保护机构、平台透明度或维修权资料，应优先进入对应细分域；只有持续订阅和合同同意回到 `contract-subscription-billing-consent-continuity`，只有缺陷召回回到 `product-safety-recall-systems`，只有诈骗身份盗用回到 `fraud-scams-consumer-protection`。
