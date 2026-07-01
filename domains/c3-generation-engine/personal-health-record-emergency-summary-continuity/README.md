# Personal Health Record Emergency Summary Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/personal-health-record-emergency-summary-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
