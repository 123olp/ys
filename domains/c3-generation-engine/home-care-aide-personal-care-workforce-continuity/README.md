# Home Care Aide Personal Care Workforce Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/home-care-aide-personal-care-workforce-continuity` |
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

`home-care-aide-personal-care-workforce-continuity/` 研究 home care aide、personal care attendant、direct care workforce、排班、人员稳定、培训、工资条件和上门服务中断如何影响居家生活、失能支持和家庭照护负担。

> 核心问题：主体能否留在家中，不只取决于是否有家，还取决于是否有人能够按时、安全、可持续地提供日常生活协助。上门个人照护劳动力是长期照护能否从制度承诺变成实际支持的关键接口。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 失能主体需要 ADL/IADL、转移、卫生、餐食、陪同和风险观察支持
  -> 这些支持依赖稳定、可训练、可排班、可留任的直接照护劳动力
  -> 居家持续性因此受 home care workforce 供给、条件和中断风险约束
```

## 关注对象

- Home care aide、personal care aide、direct support professional、personal attendant 和 consumer-directed care。
- 排班、缺勤、人员流动、工资条件、训练要求、背景审查、语言文化匹配和安全。
- ADL/IADL 支持、居家服务授权、服务小时缺口、家庭照护补位和服务中断。
- 与 `disability-services-independent-living/`、`caregiving-long-term-care/`、`home-health-hospice-palliative-care-continuity/` 的边界。

## Human Infra 模型链路

```text
居家个人照护劳动力
  -> 改变服务小时、人员稳定、技能匹配、信任和到访可靠性
  -> 改变主体 ADL/IADL、卫生、营养、移动、就医和安全状态
  -> 降低无人照护、家庭照护者过载、跌倒/感染未发现和机构化风险
  -> 增加居家持续性、尊严、有效时间和家庭系统稳定
```

## 非目标

- 不推荐雇佣、解雇、工资、合同、背景审查或具体 home care agency。
- 不提供护理操作、转移技巧、药物管理、伤口护理、急救或个人安全方案。
- 不判断 Medicaid、HCBS、waiver、个人护理服务、工时授权或福利资格。
- 不收集照护人员、雇主、家庭地址、排班、健康或支付资料。

## Source Signals

- Medicaid Home & Community Based Services: https://www.medicaid.gov/medicaid/home-community-based-services/index.html
- Medicaid Long-Term Services and Supports: https://www.medicaid.gov/medicaid/long-term-services-supports/index.html
- NIA Long-Term Care: https://www.nia.nih.gov/health/caregiving/long-term-care
- ACL Direct Care Workforce resources: https://acl.gov/

## 下一步

- 建立居家照护劳动力变量表：服务小时、人员流动、缺勤、技能匹配、训练、工资条件、语言文化匹配和服务中断。
- 整理 HCBS、personal care services、direct care workforce 和 consumer-directed care Source Cards。
