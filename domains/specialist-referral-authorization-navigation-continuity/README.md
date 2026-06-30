# Specialist Referral Authorization Navigation Continuity

## 定位

本域研究专科转诊、referral order、保险授权、network routing、资料转交、预约闭环和反馈回传如何决定主体能否进入合适专科窗口。

它不是专科推荐、病情判断、授权申诉代写或转诊捷径入口。

## 先验问题

```text
复杂问题何以进入正确专家系统？
  -> 初级照护或服务入口必须识别需要转诊
  -> 保险和网络规则必须允许服务发生
  -> 资料必须到达专科并形成预约
  -> 专科反馈必须回到主体和原照护团队
  -> 否则转诊会变成丢失的任务
```

## 研究对象

- Specialist referral、consult order、authorization、network routing 和 referral management。
- 资料转交、影像/检验附件、病历摘要、预约确认和闭环回传。
- prior authorization、utilization management、network exception 和 out-of-network risk。
- 罕见病、复杂病、多专科协作和转诊延误。

## 关键变量

- 转诊完成率、预约成功率、授权通过时间和资料缺失率。
- referral leakage、no-show、specialist feedback 回传率和重复转诊率。
- 网络内专科供给、地理距离、语言/无障碍、等待时间和取消率。

## 证据入口

- AHRQ care coordination、referral management 和 patient safety 资料。
- CMS prior authorization、network adequacy 和 Medicare/Medicaid managed care 资料。
- IOM/NASEM、NCQA、HL7 FHIR referral / e-consult 相关资料。

## 非目标

- 不判断是否需要专科、选择哪位专家、如何加急、如何申诉或如何规避授权。
- 不代写 referral、prior authorization、medical necessity letter 或病情摘要。
- 不收集诊断、病历、影像、保险、授权号、专科预约或家庭资料。

## 上下游

- 上游：`primary-care-panel-appointment-access-continuity/`、`provider-directory-network-adequacy-continuity/`、`insurance-risk-transfer/`。
- 下游：`appointment-availability-wait-time-continuity/`、`diagnostic-imaging-order-scheduling-report-continuity/`、`rare-disease-diagnostic-odyssey-care-coordination/`。
