# Unused Medicine Takeback Disposal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/unused-medicine-takeback-disposal-continuity` |
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

## 定位

本域研究未用药、过期药、管制药品、家庭药品储存、take-back、drop box、邮寄回收和安全处置如何降低误用、中毒、过量、儿童暴露和环境风险。

它不是家庭药品处置操作指南、管制药规避或药品获取入口。

## 先验问题

```text
药物治疗结束后何以不反向伤害主体？
  -> 未用药必须不被误用、滥用、误服或泄露
  -> 回收和处置路径必须低摩擦、可信、合规
  -> 否则治疗材料会变成家庭风险、成瘾风险和环境残留
```

## 研究对象

- DEA Take Back、authorized collectors、drug disposal boxes 和 mail-back。
- FDA disposal guidance、flush list、家庭药品安全储存和儿童误服预防。
- 管制药品、opioids、过期药、OTC 药物和家庭药柜风险。
- 药品回收可达性、隐私、环境和社区安全。

## 关键变量

- 回收点覆盖、可达时间、参与率、剩余药品数量。
- 家庭误服、中毒、过量、转售/转赠和非医疗使用风险。
- 特殊药品处置路径、隐私和环境暴露。

## 证据入口

- DEA National Prescription Drug Take Back Day 与 disposal 资料。
- FDA unused medicines disposal 和 safe medicine storage 资料。
- Poison Help、CDC overdose prevention 和社区药物安全资料。

## 非目标

- 不指导家庭自行处置某个药品、冲洗、销毁、转赠、出售或邮寄药品。
- 不提供获取管制药、规避监管、隐藏药品、处理证据或逃避执法的步骤。
- 不收集药品照片、药名剂量、处方、管制药信息、家庭地址或个人用药史。

## 上下游

- 上游：`medicine-access-treatment-continuity/`、`substance-exposure-control/`、`product-safety-recall-systems/`。
- 下游：`child-protection-family-safety/`、`chemical-safety-poison-control-toxicology/`、`waste-management-hazardous-materials-continuity/`。
