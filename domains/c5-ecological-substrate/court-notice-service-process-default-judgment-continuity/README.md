# Court Notice Service Process Default Judgment Continuity

本域研究法律通知、送达、开庭信息、语言/无障碍可达、回应期限、缺席判决和执行后果如何影响主体是否真正拥有程序参与机会。

> 核心问题：权利常常不是在实体规则中丢失，而是在没有收到通知、看不懂程序、错过期限或缺席判决后丢失；程序通知连续性是主体避免资源、住房、收入和身份被静默剥夺的基础设施。

## 关注对象

- 法律通知、service of process、法院传票、听证通知、电子通知、邮寄失败、地址错误和语言可达。
- 回应期限、缺席判决、工资扣押、驱逐、债务执行、家庭法院命令、保护令和行政听证。
- 与 `address-residency-mail-service-continuity/`、`access-to-justice-legal-aid/`、`debt-obligation-collection-relief-continuity/` 和 `tenant-screening-rental-access-continuity/` 的接口。
- 通知质量、可理解性、无障碍、身份匹配、记录校验、复议/撤销路径和程序性排除风险。

## Human Infra 链路

```text
法院通知 / 送达 / 缺席判决风险可控
  -> 主体能够及时知道程序、理解要求并获得回应机会
  -> 资源、住房、收入、家庭权利和信用不因静默程序失败被剥夺
  -> 法律救济、复议、撤销和执行监督路径仍可进入
  -> 名义权利转化为真实可用的程序参与能力
```

## 非目标

- 不提供个人案件、送达有效性、答辩、撤销缺席判决、驱逐、债务、家庭法院、保护令或法律建议。
- 不指导躲避送达、伪造通知、隐藏地址、滥用程序、规避执行或骚扰当事人。
- 不替代律师、法院自助中心、法律援助、书记员、调解员或官方通知系统。

## Source Signals

- U.S. Courts Civil Cases: https://www.uscourts.gov/about-federal-courts/types-cases/civil-cases
- Federal Rules of Civil Procedure: https://www.uscourts.gov/rules-policies/current-rules-practice-procedure/federal-rules-civil-procedure
- National Center for State Courts Access to Justice: https://www.ncsc.org/consulting-and-research/areas-of-expertise/access-to-justice

## 下一步

- 建立程序通知变量表：送达方式、地址质量、语言、无障碍、期限、回应入口、缺席后果、执行路径和救济机制。
- 整理 U.S. Courts、FRCP、NCSC、Legal Services Corporation 和 state court self-help Source Cards。
- 与 `access-to-justice-legal-aid/` 明确分工：司法可及域关注法律服务入口，本域关注程序通知和缺席风险链。
