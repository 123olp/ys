# Nutrition Insecurity Screening Referral Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/nutrition-insecurity-screening-referral-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
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

该域研究营养不安全、食物不安全和健康相关社会需求如何在医疗、公共卫生、福利和社区食物系统之间被识别、记录、转介、闭环跟踪。它把“患者缺食物”从背景变量转成主体持续性问题中的观测、导航和转接接口。

## 核心问题

- 医疗系统如何识别 nutrition insecurity / food insecurity，而不把它停留在问卷勾选。
- 筛查信号如何进入 closed-loop referral、care management、社区资源、食物药房、医学定制餐或营养治疗。
- 哪些断点会让主体从“被识别有需求”滑回“无人转接、无人跟踪、无人确认是否获得食物”。
- 筛查、转介和跟踪如何处理隐私、污名、语言、交通、数字访问和资格边界。

## 对象

- HRSN screening、food insecurity screening、nutrition insecurity screening。
- 电子健康记录、社区资源目录、closed-loop referral、社会处方和 care navigation。
- 食品银行、food pharmacy、produce prescription、medically tailored meals / groceries 和 dietitian referral。
- 隐私、同意、数据共享、污名和 follow-up 状态。

## Human Infra 价值

营养不安全会削弱恢复、注意力、慢病控制、用药执行、儿童发展、照护能力和工作学习稳定性。该域关注医疗系统是否能把“缺食物”转成可行动的支持链路，防止主体在已经被系统看见后仍然因为转介失败继续失能。

## 边界

- 只整理公开政策、项目模型、变量、证据、风险和执行断点。
- 不提供个人筛查、资格判断、转介选择、福利申请、饮食处方、医疗诊断或保险建议。
- 不收集、复制、处理或要求个人健康信息、收入、住址、食品不安全问卷答案、保险号或医疗记录。

## 上游与下游

- 上游：`food-security-nutrition-access`、`healthcare-access-continuity`、`social-prescribing-community-referral-continuity`、`patient-data-interoperability`。
- 下游：`medically-tailored-meals-chronic-care-continuity`、`medically-tailored-groceries-food-benefit-continuity`、`produce-prescription-fruit-vegetable-benefit-continuity`、`food-pharmacy-clinic-pantry-integration-continuity`、`medical-nutrition-therapy-dietitian-access-continuity`。

## 初始资料线索

- HHS Office of Disease Prevention and Health Promotion: Food Is Medicine.
- HHS ASPE: Food Is Medicine current activities.
- CMS: Medicaid Section 1115 health-related social needs guidance and demonstrations.
- USDA ERS: food security and food access resources.
- NIH Common Fund: Food is Medicine research opportunities.
