# Personal Health Record Emergency Summary Continuity

Personal Health Record Emergency Summary Continuity 研究个人健康记录、急救摘要、问题清单、用药摘要、过敏、设备、联系人和关键偏好如何在急救、转诊、灾害和跨机构照护中保持可读、可携带和可更新。

> 核心问题：完整病历太大、机构病历太分散；急救窗口真正需要的是可立即读取、可验证、足够简短的主体健康摘要。

## 研究对象

- Personal health record、emergency health summary、wallet card、medical summary 和 patient-maintained record。
- 诊断问题清单、重大手术、关键设备、过敏、用药、疫苗、联系人、医生和偏好信息。
- 纸质、数字、手机、可穿戴、门户导出、FHIR/CCD、Blue Button 和照护者副本。

## 先验链路

```text
急救和跨机构照护要求快速理解主体基本健康状态
  -> 机构病历分散、访问受限、摘要缺失或过载
  -> 主体需要可携带、可更新、低摩擦的急救健康摘要
  -> 摘要质量影响诊疗安全、转诊效率、药物风险、联系人接入和灾害安置
  -> 摘要若错误或过期，也会制造误治和隐私风险
  -> 因而个人健康急救摘要是病历权利转化为即时行动能力的执行层
```

## 关键变量

- 摘要字段、更新时间、来源、可读格式、离线可用性和授权边界。
- 与门户、FHIR、Blue Button、照护者副本和纸质卡片的同步方式。
- 错误、过期、信息过载、隐私泄露、设备锁定和语言可达风险。

## 证据入口

- MedlinePlus Personal Health Records.
- ONC patient access and health record materials.
- CMS Blue Button and patient access API materials.
- Ready.gov emergency documents and medical information materials.

## 非目标

- 本域不整理、解释、生成、翻译或验证个人病历、诊断、药物、结果或急救摘要。
- 不提供医疗建议、急救建议、病历模板填写、FHIR 导出操作、门户设置或应用推荐。
- 不收集 PHI、报告、用药清单、影像、联系方式、设备序列号或个人健康资料。

## 上下游

- 上游：`medical-record-access-amendment-release-continuity/`、`patient-data-interoperability/`、`digital-identity-security/`。
- 下游：`emergency-medical-services-prehospital-care/`、`care-transitions-discharge-continuity/`、`medical-id-allergy-critical-alert-continuity/`。
