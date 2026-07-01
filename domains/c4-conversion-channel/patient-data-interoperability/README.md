# Patient Data Interoperability

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/patient-data-interoperability` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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
