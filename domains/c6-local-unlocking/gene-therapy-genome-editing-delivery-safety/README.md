# Gene Therapy Genome Editing Delivery Safety

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/gene-therapy-genome-editing-delivery-safety` |
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

`gene-therapy-genome-editing-delivery-safety/` 研究基因治疗、体内/体外基因编辑、递送载体、表达控制、长期随访和遗传安全如何影响主体持续性。

> 核心问题：如果未来能够直接改写或补偿致病基因、调节表达程序或增强修复能力，那么真正的约束不是“能不能编辑”，而是“能否安全、可控、可验证、可停止并长期随访”。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要降低遗传病、癌症易感、退行性损伤和组织失败风险
  -> 基因治疗和基因编辑可能改变底层状态变量
  -> 递送、脱靶、插入突变、免疫反应、表达失控和长期随访失败会反过来制造新风险
  -> 因此基因治疗、编辑与递送安全是身体可维护性的高杠杆研究域
```

## 关注对象

- AAV、慢病毒、脂质纳米颗粒、mRNA、ex vivo 细胞编辑和 in vivo 递送。
- CRISPR、base editing、prime editing、表观遗传编辑和转基因表达控制。
- 脱靶、on-target 大片段改变、插入突变、免疫原性、剂量、组织靶向和长期随访。
- 与 `cellular-reprogramming/` 的边界：重编程域关注细胞身份与年龄状态；本域关注基因层编辑、递送和长期安全。
- 与 `clinical-trials-regulatory-science-translation/` 的边界：临床转化域关注试验与监管流程；本域关注平台机制和风险变量。

## Human Infra 模型链路

```text
基因治疗 / 基因编辑 T
  -> 改变致病变异、表达程序、细胞功能和修复能力 X
  -> 改变疾病状态、组织状态和长期风险暴露 S
  -> 改变死亡风险、失能风险、癌症风险和恢复能力 λ(t)
  -> 影响健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供载体构建、编辑设计、靶点选择、剂量、给药、实验流程或人体应用建议。
- 不把机制可行性、动物结果、早期安全性试验或公司公告写成稳定人体疗效。
- 不提供胚胎编辑、生殖系编辑、增强性编辑、监管规避或 DIY 生物实验建议。
- 不把基因编辑写成通用延寿工具；必须绑定具体疾病、组织、递送和证据层级。

## Source Signals

- FDA Cellular & Gene Therapy Products: https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products
- FDA human gene therapy with genome editing guidance: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/human-gene-therapy-products-incorporating-human-genome-editing
- FDA long-term follow-up after human gene therapy products: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/long-term-follow-after-administration-human-gene-therapy-products
- NIH / NHGRI genome editing policy issues: https://www.genome.gov/about-genomics/policy-issues/Genome-Editing
- NCBI Gene Therapy overview: https://www.ncbi.nlm.nih.gov/books/NBK22254/

## 下一步

1. 建立变量表：递送方式、编辑方式、靶组织、表达持续时间、脱靶、安全监测和长期随访。
2. 与 `cancer-control/`、`regenerative-medicine/`、`immune-maintenance/`、`clinical-trials-regulatory-science-translation/` 建立交叉引用。
3. 将代表性论文转成 Source Cards，区分机制、动物、人体验证和上市后安全。
