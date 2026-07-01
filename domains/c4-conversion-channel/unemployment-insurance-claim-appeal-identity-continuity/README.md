# Unemployment Insurance Claim Appeal Identity Continuity

`unemployment-insurance-claim-appeal-identity-continuity` 研究失业保险从 claim intake、身份核验、monetary/non-monetary determination、weekly certification、overpayment、appeal、fraud control 到 payment continuity 的执行链路，以及它如何影响失业后的现金流、求职能力、住房稳定和心理恢复。

## 核心问题

失业保险的主体价值在于把短期收入冲击变成可恢复窗口。若身份核验、雇主分离信息、工资记录、每周认证、申诉或支付失败，主体会在求职、住房、食物、医疗和债务之间快速失去缓冲。

## 对象

- UI claim、initial claim、continued claim/weekly certification、monetary determination、non-monetary determination 和 separation information。
- identity verification、fraud prevention、overpayment、appeal、payment delay 和 state UI system modernization。
- 与 `unemployment-insurance-wage-record-continuity` 的分工：后者关注工资记录底座，本域关注申领、核验、申诉和支付执行。

## Human Infra 价值

- 把失业保险建模为失业冲击后的时间购买机制：用现金流保护求职、住房、医疗和家庭稳定。
- 解释身份核验和申诉摩擦如何把风险转嫁给已经失去收入的主体。
- 补齐公共福利执行链路中的“收入中断恢复”域。

## 边界

- 不提供 UI 资格判断、claim filing、weekly certification、appeal、overpayment、身份核验、雇主争议、法律、税务或个案建议。
- 不代写 claim、appeal、certification、separation statement、fraud response 或州级机构沟通材料。
- 不帮助伪造身份、虚假失业、隐瞒收入、规避 work search、绕过 ID proofing、骗领 UI 或处理欺诈风控。
- 不收集 SSN、州 UI account、工资记录、雇主信息、身份证件、银行账户、案件号或门户凭证。

## 上游与下游

- 上游：`unemployment-insurance-wage-record-continuity`、`income-payroll-employment-record-continuity`、`administrative-burden-procedural-friction`。
- 下游：`emergency-rental-assistance-arrears-continuity`、`debt-obligation-collection-relief-continuity`、`job-search-labor-market-matching-continuity`、`mental-health-care-access-continuity`。

## 初始资料线索

- U.S. Department of Labor Unemployment Insurance: https://oui.doleta.gov/unemploy/
- U.S. Department of Labor claimant resources: https://oui.doleta.gov/unemploy/claimant.asp
- U.S. Department of Labor UI modernization: https://www.dol.gov/agencies/eta/ui-modernization
