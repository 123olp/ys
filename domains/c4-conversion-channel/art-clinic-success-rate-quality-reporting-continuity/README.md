# ART Clinic Success Rate Quality Reporting Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/art-clinic-success-rate-quality-reporting-continuity` |
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

ART 诊所成功率、质量报告与数据可解释连续性，关注 fertility clinic reporting、CDC ART success rates、NASS、数据校验、报告口径、患者构成、分母定义和可解释边界如何影响主体选择和信任。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要把复杂技术服务转化为可比较、可审查、可行动的选择
  -> ART 成功率高度依赖年龄、卵源、周期类型、分母和诊所报告口径
  -> 如果数据不可解释，主体会在高成本、高情绪负担服务中失去判断能力
  -> 因此 ART 质量报告是生殖技术选择权的观测与治理接口
```

## 关注对象

- CDC ART Success Rates、National ART Surveillance System、clinic-specific reports、national summary 和 state-specific surveillance。
- 成功率分母、患者年龄、own eggs / donor eggs、intended retrieval、actual retrieval、transfer、live birth、multiple birth 和数据延迟。
- 数据校验、discrepancy rate、非报告诊所、隐私保护、患者构成差异和误读风险。
- 与 `assisted-reproductive-technology-ivf-cycle-continuity/` 的边界：IVF 域关注周期执行；本域关注周期结果如何被报告、比较和解释。

## Human Infra 模型链路

```text
ART 质量报告 T
  -> 改变成功率口径、诊所可见性、数据质量、风险透明度和选择信息变量 X
  -> 改变主体对服务路径、费用风险、时间窗口和预期管理状态 S
  -> 改变误选、过度承诺、机会成本、资源耗尽和信任崩溃风险 lambda(t)
  -> 影响未来选择权、资源持续性和高成本生殖技术的可审查性
```

## 非目标

- 不提供诊所排名、诊所推荐、成功率个体解释、治疗选择、保险支付或法律建议。
- 不把 clinic-specific ART success rates 写成个人生育概率。
- 不使用报告数据进行个人价值判断、群体污名化或商业营销。

## Source Signals

- CDC ART Success Rates: https://www.cdc.gov/art/success-rates/index.html
- CDC National ART Surveillance System: https://www.cdc.gov/art/php/nass/index.html
- CDC NASS Data Validation: https://www.cdc.gov/art/php/nass/data-validation.html
- CDC Accessing NASS Data: https://www.cdc.gov/art/php/data-access/index.html

## 下一步

1. 建立 ART reporting card：reporting unit、denominator、outcome、lag、validation、privacy 和 interpretation boundary。
2. 与 `assisted-reproductive-technology-ivf-cycle-continuity/`、`uncertainty-quantification-model-calibration/` 和 `data-quality-missingness-representativeness/` 建立接口。
