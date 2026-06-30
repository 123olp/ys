# Insurance Eligibility Benefits Verification Continuity

## 定位

本域研究保险资格、coverage active 状态、benefits verification、cost-sharing、deductible、out-of-pocket maximum、network status 和 coverage limitations 如何在服务发生前被核验。

它不是保险权益解释、个案费用预测、provider 选择或保险争议建议入口。

## 先验问题

```text
医疗服务可支付何以成立？
  -> 覆盖状态必须可核验
  -> 权益、网络、费用分担和限制必须可被服务方与主体理解
  -> 保险信息必须在预约、检查、治疗和账单系统之间一致
  -> 否则服务会在资格核验或费用分担处失败
```

## 研究对象

- Eligibility and benefits verification、coverage active status、subscriber/dependent relationship。
- Deductible、copay、coinsurance、out-of-pocket maximum、benefit limits 和 exclusions。
- In-network / out-of-network status、payer-provider contract、real-time eligibility 和 clearinghouse。

## 关键变量

- 资格核验准确率、信息延迟、网络状态错误率和 coverage mismatch。
- 费用分担可理解度、benefit limit 触发率、eligibility denial。
- 服务发生前后保险信息一致性和人工纠错负担。

## 证据入口

- CMS 和 payer interoperability / eligibility 相关资料。
- CAQH CORE eligibility and benefits standards。
- CMS care compare、plan documents、summary of benefits and coverage 资料。

## 非目标

- 不解释个人 benefits、deductible、network、coverage、claim 或 bill。
- 不推荐 insurance plan、network、provider、facility 或服务路径。
- 不收集保险卡、member ID、病历、诊断、claim、账单或个人财务资料。

## 上下游

- 上游：`health-insurance-enrollment-renewal-continuity/`、`provider-directory-network-adequacy-continuity/`。
- 下游：`medical-service-prior-authorization-utilization-management-continuity/`、`claims-adjudication-eob-denial-continuity/`。
