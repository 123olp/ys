# Healthcare Language Interpreter Effective Communication Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/healthcare-language-interpreter-effective-communication-continuity` |
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

## 定位

本域研究医疗语言服务、interpreter access、translated materials、effective communication、CLAS 和 LEP 场景如何影响主体能否理解、表达和执行医疗任务。

它不是翻译认证、医疗解释、法律意见、个案口译安排或临床沟通代写工具。

## 先验问题

```text
医疗理解何以成立？
  -> 医疗信息必须以主体能理解的语言和形式到达
  -> 口译、翻译和有效沟通必须覆盖预约、同意、结果、账单和出院
  -> 家属临时翻译不能替代系统性语言服务
  -> 否则主体无法可靠表达症状、理解风险、执行计划或保护权利
```

## 研究对象

- Healthcare interpreter services、language assistance、translated notices、CLAS standards。
- LEP、Deaf/Hard of Hearing、auxiliary aids、plain language、teach-back 和 culturally appropriate communication。
- 预约、急诊、住院、同意、结果、药物、出院、账单和投诉中的语言断点。

## 关键变量

- 语言需求识别率、口译等待时间、材料翻译覆盖率和沟通错误率。
- 口译模式、质量、隐私、术语负担、健康素养和文化适配。
- 语言服务费用、责任方、远程口译、紧急场景和投诉路径。

## 证据入口

- HHS National CLAS Standards、LEP.gov 和 HHS OCR language access 资料。
- ADA effective communication、CDC health literacy 和 plain language 资料。
- 医疗口译、语言可及、沟通错误和 patient safety 文献。

## 非目标

- 不提供医学翻译、诊断解释、治疗解释、口译替代、法律建议或认证翻译。
- 不安排 interpreter、投诉、预约、授权、账单沟通或语言服务请求。
- 不收集医疗记录、语言身份、移民状态、PHI、联系方式或音视频资料。

## 上下游

- 上游：`language-access-plain-communication/`、`health-literacy-navigation/`。
- 下游：`informed-consent-refusal-shared-decision-continuity/`、`clinical-results-notification-followup-continuity/`。
