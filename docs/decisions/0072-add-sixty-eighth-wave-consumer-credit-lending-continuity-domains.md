# ADR 0072: Add Sixty-Eighth-Wave Consumer Credit and Lending Continuity Domains

## Status

Accepted.

## Context

Human Infra 已经覆盖银行账户、信用报告、债务义务、合同订阅账单、支付卡争议、消费者交易和市场履约。但主体日常资源连续性中还有一组更基础的跨期机制：通过信用和贷款把未来收入、住房、车辆、教育、家庭支持或购买力提前转换成当前可用资源。

这些对象不能只放进 `debt-obligation-collection-relief-continuity`、`credit-consumer-reporting-access-continuity`、`payment-card-dispute-unauthorized-charge-continuity` 或第 67 波消费者交易域。债务域关注已经形成的义务、催收和救济；信用报告域关注信用记录入口；支付争议域关注交易错误纠正；消费者交易域关注购买到可用结果。本波关注的是借款、授信、服务、披露和还款义务本身如何改变主体未来现金流、移动能力、住房稳定、教育资本和跨境家庭支持。

## Decision

新增第 68 波 8 个消费者信贷、贷款服务与跨期资源连续性域：

- `credit-card-revolving-credit-cost-continuity`
- `consumer-loan-origination-apr-disclosure-continuity`
- `mortgage-origination-servicing-foreclosure-continuity`
- `auto-loan-lease-servicing-repossession-continuity`
- `student-loan-servicing-repayment-forgiveness-continuity`
- `payday-small-dollar-title-loan-continuity`
- `buy-now-pay-later-installment-financing-continuity`
- `remittance-money-transfer-disclosure-continuity`

## Consequences

- Human Infra 能把“未来收入被提前占用或跨境转移”的机制拆成可审查域：信用卡循环信用、一般消费贷款、房贷、车贷/租赁、学生贷款、高成本小额贷款、BNPL 和汇款。
- 这些域只做公开资料整理、机制建模、证据边界和禁止用途声明；不提供贷款申请、还款、再融资、减免、止赎、收车、汇款、避税、逃债、金融规划、法律或个案争议建议。
- 后续若新增 CFPB、Federal Student Aid、FTC、HUD、FinCEN、OFAC、州金融监管机构、州 DMV 或州检察长资料，应优先进入对应细分域；只有已经进入催收、破产或债务救济的问题回到 `debt-obligation-collection-relief-continuity`，只有信用记录可及性回到 `credit-consumer-reporting-access-continuity`，只有交易错误纠正回到 `payment-card-dispute-unauthorized-charge-continuity`。
