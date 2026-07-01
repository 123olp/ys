# Male Factor Infertility Sperm Health Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/male-factor-infertility-sperm-health-continuity` |
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

`male-factor-infertility-sperm-health-continuity/` 研究男性因素不育、精子数量/活力/形态、内分泌、泌尿生殖、感染、环境暴露、生活方式、遗传因素和关系压力如何影响主体未来选择权。

> 核心问题：男性因素不育不是单纯“精子指标差”，而是生殖未来选择权、伴侣关系、身份压力、暴露史、内分泌和医疗可及性交叉的长期计划问题。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体的未来选择权包括是否保留生殖与亲缘路径
  -> 男性因素不育会通过精子健康、内分泌、感染、暴露、遗传和关系压力改变该路径
  -> 若评估、隐私、伴侣沟通和生育保存接口断裂，主体会损失未来选择权和关系稳定性
  -> 因此男性因素不育是生殖连续性中的独立机制域
```

## 关注对象

- Male infertility、sperm count/motility/morphology、varicocele context、hypogonadism context、infection/inflammation、gonadotoxic exposures、occupational/environmental exposures、genetic factors、fertility preservation and partner burden。
- 与 `reproductive-fertility-continuity/` 的边界：上位域关注生育未来选择权；本域关注男性因素和精子健康这一具体机制。
- 与 `fertility-preservation-gamete-embryo-cryostorage-continuity/` 的关系：精子冷冻可作为部分选择权保存接口，但不保证未来生育结果。
- 与 `occupational-exposure-industrial-hygiene/` 的关系：热、化学、辐射和职业暴露可能进入精子健康变量，但本域不做个人暴露归因。

## Human Infra 模型链路

```text
男性因素不育评估与支持系统 T
  -> 改变精子健康、内分泌状态、感染/炎症、暴露识别、隐私、伴侣沟通和保存选择变量 X
  -> 改变主体生殖未来选择权、关系压力、身份负担、医疗导航和长期计划状态 S
  -> 改变不育、诊断延迟、关系冲突、资源消耗、心理负担和未来选择受限 lambda(t)
  -> 影响主体关系路径、生殖自主和长期选择空间
```

## 非目标

- 不提供精液报告解读、男性不育诊断、用药、补剂、激素、手术、生活方式、感染处理、精子冷冻、ART、伴侣建议或个体医疗建议。
- 不把精子指标、性功能、年龄、职业暴露或生活方式写成个人归因。
- 不收集个人精液报告、性健康、伴侣、生育、基因、职业暴露、用药或心理资料。

## Source Signals

- WHO infertility fact sheet: https://www.who.int/news-room/fact-sheets/detail/infertility
- MedlinePlus male infertility: https://medlineplus.gov/maleinfertility.html
- NICHD infertility: https://www.nichd.nih.gov/health/topics/infertility

## 下一步

- 建立 Male Factor Fertility Card：sperm health, endocrine context, exposure history, infection/inflammation, privacy, partner burden, preservation interface。
- 与 `reproductive-fertility-continuity/`、`fertility-preservation-gamete-embryo-cryostorage-continuity/` 和 `occupational-exposure-industrial-hygiene/` 建立接口。
