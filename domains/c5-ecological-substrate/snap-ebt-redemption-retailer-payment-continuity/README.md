# SNAP EBT Redemption Retailer Payment Continuity

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
