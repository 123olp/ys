# Outpatient Laboratory Specimen Result Routing Continuity

## 定位

本域研究门诊检验医嘱、标本采集、采样点、运输、结果回传、患者查看和 follow-up routing 如何把检测能力转化为主体可用的医疗信号。

它不同于 `clinical-laboratory-diagnostic-quality/`：本域关注执行链路和结果路由，不评价具体检验质量或解释结果。

## 先验问题

```text
检测何以成为可行动信号？
  -> 医嘱必须被主体看见并完成采样
  -> 标本必须正确进入实验室和信息系统
  -> 结果必须回到患者和照护团队
  -> 异常结果必须触发下一步
  -> 否则检测能力不会转化为风险控制
```

## 研究对象

- Outpatient lab order、specimen collection、draw station、home collection 和 specimen transport。
- 结果回传、患者门户、临床 inbox、abnormal result follow-up 和 critical value routing。
- 采样准备、营业时间、地理可达、预约/ walk-in、保险覆盖和费用透明。
- 结果延迟、lost specimen、duplicate order、unviewed result 和 follow-up failure。

## 关键变量

- 医嘱完成率、采样到结果时间、结果查看率和 abnormal follow-up 闭环率。
- 标本丢失率、重采率、采样点距离、营业覆盖和门户可达性。
- critical result 通知时间、ordering clinician inbox 负担和患者理解边界。

## 证据入口

- CMS CLIA、Medicare clinical laboratory test coverage 和 AHRQ diagnostic safety 资料。
- ONC / USCDI / patient access、HL7 FHIR DiagnosticReport 和 lab data interoperability。
- 临床结果管理、critical value reporting 和 diagnostic error 研究。

## 非目标

- 不解释检验结果、推荐检测、判断异常、给出诊断、治疗或复查建议。
- 不提供采样 SOP、实验室操作、认证规避、账单争议或检测选择策略。
- 不收集检验单、结果、病历、保险、标本标签、门户账号或健康资料。

## 上下游

- 上游：`primary-care-panel-appointment-access-continuity/`、`clinical-laboratory-diagnostic-quality/`、`patient-data-interoperability/`。
- 下游：`specialist-referral-authorization-navigation-continuity/`、`medication-reconciliation-regimen-adherence-continuity/`、`measurement-feedback/`。
