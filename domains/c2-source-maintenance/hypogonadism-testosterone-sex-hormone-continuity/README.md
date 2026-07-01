# Hypogonadism Testosterone Sex Hormone Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/hypogonadism-testosterone-sex-hormone-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

`hypogonadism-testosterone-sex-hormone-continuity/` 研究性腺功能低下、睾酮/性激素不足、青春期/成人阶段差异、骨骼肌肉、情绪、性功能、生育力和长期监测边界如何影响主体持续性。

> 核心问题：性激素不只是性功能变量，也参与骨密度、肌肉、能量、情绪、红细胞、生殖窗口和身份体验；误读或商业化过度会同时制造漏诊和过度治疗风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要性腺轴在发育、成人和衰老阶段维持骨骼、肌肉、情绪、性功能和生育相关能力
  -> 性腺功能低下会改变睾酮/雌激素、精子生成、骨密度、肌力、疲劳、情绪和性功能变量
  -> 结果取决于病因识别、年龄/阶段语境、化验边界、治疗风险、商业夸大和长期监测
  -> 因此性腺功能低下是性激素轴、身体能力和未来选择权的关键域
```

## 关注对象

- Hypogonadism、low testosterone context、hypogonadotropic hypogonadism context、puberty/adult stage context、bone/muscle effects、sexual function、fertility and sperm production, monitoring boundary。
- 与 `male-factor-infertility-sperm-health-continuity/` 的关系：本域聚焦性腺激素轴；男性因素不育域聚焦精子健康和生殖规划负担。
- 与 `erectile-dysfunction-vascular-sexual-function-continuity/` 的关系：ED 是性功能和血管信号接口，不等于睾酮不足。

## Human Infra 模型链路

```text
性腺功能低下识别与监测 T
  -> 改变睾酮/性激素、骨密度、肌肉、疲劳、情绪、性功能和生育变量 X
  -> 改变体力、训练适应、关系参与、生殖规划、身份体验和长期治疗状态 S
  -> 改变骨折、肌少、贫血/红细胞异常、性功能困扰、生育窗口损耗和过度治疗风险 λ(t)
  -> 影响主体行动能力、未来选择权和长期健康寿命
```

## 非目标

- 不提供个人诊断、睾酮/LH/FSH/雌激素/精液化验判读、青春期判断、用药、激素、剂量、补剂、健身、性功能、生育、停药、风险评分或个体医疗建议。
- 不生成 testosterone therapy 方案、药品/诊所/产品推荐、健身增肌方案、伴侣沟通、保险申诉、实验室重测策略或身份/性功能判断。
- 不收集个案化验、精液报告、处方、身体照片、青春期资料、性生活资料、伴侣信息、生育计划或保险资料。

## Source Signals

- MedlinePlus hypogonadism: https://medlineplus.gov/ency/article/001195.htm
- MedlinePlus hypogonadotropic hypogonadism: https://medlineplus.gov/ency/article/000390.htm
- MedlinePlus testosterone levels test: https://medlineplus.gov/lab-tests/testosterone-levels-test/

## 下一步

- 建立 Sex Hormone Axis Card：stage, gonadal vs central context, bone/muscle/energy effects, fertility interface, overmedicalization boundary。
- 与 `endocrine-hormonal-regulation/`、`male-factor-infertility-sperm-health-continuity/`、`erectile-dysfunction-vascular-sexual-function-continuity/` 和 `musculoskeletal-integrity/` 建立接口。
