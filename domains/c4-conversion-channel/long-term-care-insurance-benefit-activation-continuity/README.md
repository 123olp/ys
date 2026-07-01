# 长期照护保险与福利启动连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/long-term-care-insurance-benefit-activation-continuity` |
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

本域研究 long-term care insurance、hybrid life/LTC、activities of daily living、cognitive impairment trigger、elimination period、benefit period、care setting、premium increase、claim 和 care plan 如何影响主体失能后的照护资金和家庭照护负担。它关注私营长期照护风险转移，而不是照护机构选择、保险购买、理赔代办或法律建议。

## 研究对象

- 长期照护保险、hybrid life/LTC、home care、assisted living、nursing home、adult day care 和 care coordination。
- ADL trigger、cognitive impairment trigger、elimination period、daily/monthly benefit、benefit period、inflation protection 和 premium increase。
- claim、assessment、plan of care、provider invoice、reimbursement / indemnity、policy lapse 和 appeals。
- 与长期照护服务、家庭照护、Medicaid HCBS、残障服务和寿险理赔的边界。

## 价值链路

```text
主体进入长期照护或认知/功能衰退状态
  -> 长期照护保险把高成本照护需求转化为保单触发和福利支付问题
  -> 清晰 ADL/认知触发、照护计划和发票记录维持居家或机构照护资金
  -> 等待期、保费上涨、失效或 claim 争议会把照护需求转嫁给家庭现金流
  -> 长期照护保险连续性把失能照护成本纳入可审查的风险转移执行层
```

## 关键问题

- 长期照护保险与健康保险、Medicare、Medicaid HCBS 和寿险如何分界？
- ADL、认知 impairment 和 elimination period 如何决定 benefit activation？
- premium increase、lapse 和 inflation protection 如何影响长期可持续性？
- care setting、provider invoice 和 plan of care 如何连接家庭照护执行？

## 上游与下游

- 上游：`caregiving-long-term-care/`、`dementia-cognitive-decline-care-continuity/`、`disability-services-independent-living/`。
- 下游：`family-caregiver-respite-work-continuity/`、`trust-estate-affairs-succession-continuity/`、`life-insurance-beneficiary-claim-continuity/`、`public-assistance-benefits-continuity/`。

## 非目标

- 不提供长期照护保险购买、保额选择、claim 填写、照护机构选择、Medicaid 规划、遗产规划、法律或税务建议。
- 不判断某人是否触发 ADL/认知条件、某照护服务是否应覆盖或某保费上涨是否合理。
- 不协助伪造照护记录、虚开发票、夸大 ADL 限制、隐瞒保单信息、保险欺诈、规避 Medicaid 规则或骗取照护福利。

## 初始资料入口

- NAIC: Long-term care insurance consumer materials
- State insurance department long-term care and complaint materials
- ACL / Medicare / Medicaid public long-term services context materials
- Official elder care and consumer protection materials
