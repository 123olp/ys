# Patient Data Interoperability

`patient-data-interoperability/` 研究患者健康记录访问、数据可携带、互操作标准、授权应用和跨机构数据连续性。

> 核心问题：医疗、保险和照护系统只有在主体本人和授权照护者能够获取、核对、携带和授权使用关键健康数据时，才可能形成连续照护。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体状态必须跨机构、跨时间、跨服务保持可见
  -> 健康记录、药物清单、检查结果、理赔和转诊信息必须可访问、可核对、可携带
  -> 数据连续性决定照护连续性、错误减少和未来决策质量
```

## 关注对象

- 患者访问权、电子健康记录、保险数据、互操作标准、授权应用和数据可携带。
- USCDI、TEFCA、FHIR、SMART App Launch、Blue Button、患者门户和跨机构交换。
- 数据锁定、记录缺失、重复检查、药物清单断裂、转诊资料丢失和照护者授权。
- 与 `digital-identity-security/`、`healthcare-access-continuity/`、`measurement-feedback/` 和 `governance-rights/` 的接口。

## Human Infra 模型链路

```text
患者数据互操作基础设施
  -> 改变记录访问、数据携带、授权共享和跨机构交换能力
  -> 改变医疗决策、照护交接、风险识别和患者复核状态
  -> 降低信息断裂、重复检查、用药错误、转诊失败和照护碎片化风险
  -> 增强医疗连续性、主体自主性和未来选择权
```

## 非目标

- 不解释个人病历、检查结果、理赔记录或医学风险。
- 不提供绕过授权、破解门户、爬取数据、隐私规避或第三方应用背书。
- 不把互操作标准写成个体法律权利、保险权益或数据即时可得性的承诺。

## Source Signals

- ONC health record access: https://www.healthit.gov/how-to-get-your-health-record/
- ONC USCDI: https://www.healthit.gov/isp/united-states-core-data-interoperability-uscdi
- ONC TEFCA: https://www.healthit.gov/topic/interoperability/policy/trusted-exchange-framework-and-common-agreement-tefca
- CMS Blue Button: https://bluebutton.cms.gov/
- HL7 FHIR: https://hl7.org/fhir/
- SMART App Launch: https://hl7.org/fhir/smart-app-launch/

## 下一步

- 建立患者数据连续性变量表：访问、核对、携带、授权、交换、语义一致性、数据质量和撤销。
- 与 `digital-identity-security/` 拆分认证/身份恢复边界，与 `measurement-feedback/` 拆分指标解释边界。
- 整理 USCDI、TEFCA、FHIR、Blue Button 和 SMART App Launch 的 Source Cards。
