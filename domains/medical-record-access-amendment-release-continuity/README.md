# Medical Record Access Amendment Release Continuity

## 定位

本域研究主体能否获得、下载、纠错、修正、释放、授权和携带医疗记录，以及病历访问、amendment、release of information 和 information blocking 如何影响照护连续性。

它不是病历索取代理、HIPAA 法律意见、医疗记录解释、纠错申请代写或隐私投诉工具。

## 先验问题

```text
医疗判断何以可复核？
  -> 主体和照护团队必须能获得关键医疗记录
  -> 错误记录必须有修正、补充或争议标记路径
  -> 授权释放和跨机构携带必须可追踪
  -> 否则转诊、第二意见、慢病管理和急救会被错误或缺失资料截断
```

## 研究对象

- HIPAA right of access、amendment、accounting / release of information。
- Patient access、USCDI、FHIR、TEFCA、information blocking 和 record portability。
- 记录错误、身份匹配、延迟、费用、格式、代理访问和第三方应用授权。

## 关键变量

- 记录请求完成时间、拒绝率、费用、格式可用性和 amendment 响应。
- 错误记录类型、重复患者、identity matching、机构间交换和可携带性。
- 授权范围、撤回、代理人、照护者、第三方应用和隐私风险。

## 证据入口

- HHS HIPAA right of access 和 amendment guidance。
- ONC patient records、information blocking、USCDI、FHIR 和 TEFCA 资料。
- 医疗记录访问、患者数据可携带和信息阻断研究。

## 非目标

- 不代写 records request、amendment request、release authorization、HIPAA complaint 或 legal letter。
- 不解释个人病历、诊断、影像、化验、医嘱、账单、编码或保险资料。
- 不收集 PHI、portal 凭证、身份证件、授权书、签名、MRN、member ID 或医疗记录副本。

## 上下游

- 上游：`patient-portal-account-message-continuity/`、`patient-data-interoperability/`。
- 下游：`specialist-referral-authorization-navigation-continuity/`、`care-transitions-discharge-continuity/`。
