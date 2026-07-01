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
