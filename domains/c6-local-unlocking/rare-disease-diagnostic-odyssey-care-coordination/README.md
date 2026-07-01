# Rare Disease Diagnostic Odyssey Care Coordination

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/rare-disease-diagnostic-odyssey-care-coordination` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

罕见病诊断漫游与照护协调域研究：当疾病低患病率、症状异质、证据稀薄、专科分散时，主体如何从误诊、延误、重复检查和服务碎片化中被持续接住。

## 对象

- 罕见病、未确诊疾病、遗传病、复杂表型、孤儿药、患者登记和专家网络。
- 诊断漫游、转诊路径、基因检测、临床实验室质量、跨专科会诊和研究招募。
- 症状管理、功能支持、学校/工作合理便利、社会服务、患者组织和家庭照护负担。
- 诊断不确定性、误诊风险、数据可携带、病历摘要、自然史研究和治疗窗口。
- 罕见病对健康寿命、有效时间、家庭资源、未来选择权和主体身份理解的影响。

## Human Infra 价值

罕见病的关键断点通常不是单一治疗，而是“找不到正确问题”。这个域把罕见病纳入主体持续性基础设施：尽早识别信号、组织资料、连接专家、减少重复损耗，并把研究机会和照护支持转化为可行动路径。

```text
罕见病路径被识别和协调
  -> 误诊、延误、重复检查和服务碎片化下降
  -> 主体更早进入合适诊断、支持、研究和治疗窗口
  -> 健康寿命、有效时间和未来选择权提高
```

## 边界

本域只整理公开罕见病、未确诊疾病、诊断路径、照护协调、孤儿药和患者支持资料。

不提供：

- 个体诊断、鉴别诊断、基因检测解读、用药、手术、临床试验报名或治疗建议。
- 遗传咨询、产前/生殖选择、家族风险判断、保险和就业披露建议。
- 对疾病、患者组织、医生、实验室、药物或试验项目的背书。
- 把罕见病资料写成确定个人预后、寿命预测、资格判断或医疗承诺。

## 上游与下游

- 上游：`clinical-laboratory-diagnostic-quality/`、`genomic-stability-dna-repair/`、`patient-data-interoperability/`、`research-infrastructure-open-science-translation/`。
- 下游：`clinical-trials-regulatory-science-translation/`、`medicine-access-treatment-continuity/`、`functioning-quality-of-life-outcomes/`、`caregiving-long-term-care/`。

## 初始资料线索

- NIH Genetic and Rare Diseases Information Center: https://rarediseases.info.nih.gov/
- FDA Rare Diseases at FDA: https://www.fda.gov/industry/medical-products-rare-diseases-and-conditions
- NIH Undiagnosed Diseases Network public materials。
- Orphan drug, natural history and patient registry public materials。

## 下一步

- 建立诊断漫游变量表：首症状时间、转诊次数、误诊次数、检测可及、专家密度、资料完整性和家庭负担。
- 整理罕见病 Source Cards：诊断、自然史、患者登记、孤儿药、患者组织和不确定性边界。
- 区分“诊断协调基础设施”与“个体诊疗建议”，避免越界。
