# HIV Testing PrEP Prevention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/hiv-testing-prep-prevention-continuity` |
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

`hiv-testing-prep-prevention-continuity/` 研究 HIV 检测、PrEP 可及、PEP 转介、持续护理、病毒抑制、污名和隐私如何影响主体持续性。

> 核心问题：HIV 领域已经从单纯死亡风险转向“预防、早检、持续治疗和传播阻断”的长期连续性问题；断点常来自可及性、污名、费用、隐私和随访。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖可获得、可保密、可持续的 HIV 预防和照护入口
  -> HIV 风险和感染状态会通过免疫、慢病管理、心理负荷、关系和制度污名改变长期路径
  -> 结果取决于检测、PrEP/PEP 转介、ART 连续性、病毒抑制和反歧视保护
  -> 因此 HIV 预防与持续照护是感染风险治理和权利保护的交叉域
```

## 关注对象

- HIV testing、PrEP access、PEP referral、ART linkage, retention in care, viral suppression, U=U communication, stigma, confidentiality, insurance and pharmacy access。
- 与 `sexual-health-sti-prevention-continuity/` 的边界：该域覆盖性健康总入口；本域聚焦 HIV 的检测、预防和持续照护链。
- 与 `chronic-infectious-disease-care-continuity/` 的关系：HIV 是慢性感染连续照护的核心例子之一。

## Human Infra 模型链路

```text
HIV 检测、PrEP 与持续照护系统 T
  -> 改变检测覆盖、预防可及、治疗连接、病毒抑制、污名和隐私变量 X
  -> 改变感染风险、免疫状态、医疗连续性、关系安全和制度暴露 S
  -> 改变死亡风险、机会性感染、慢病负担、传播风险和有效时间 λ(t)
  -> 影响主体身体持续性、关系选择、工作和未来计划
```

## 非目标

- 不提供个人 HIV 风险评分、检测解释、PrEP/PEP/ART 用药、暴露后处理、伴侣建议、诊断或治疗建议。
- 不生成个人检测周期、药物选择、保险方案、药房路径或法律建议。
- 不收集个案性行为、伴侣、HIV 状态、用药、定位、身份或敏感健康资料。

## Source Signals

- CDC HIV testing: https://www.cdc.gov/hiv/testing/
- CDC PrEP clinical guidance: https://www.cdc.gov/hivnexus/hcp/prep/
- USPSTF HIV screening: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/human-immunodeficiency-virus-hiv-infection-screening
- USPSTF PrEP: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/prevention-of-human-immunodeficiency-virus-hiv-infection-pre-exposure-prophylaxis

## 下一步

- 建立 HIV Continuity Card：testing, PrEP/PEP access, linkage, retention, viral suppression, confidentiality, stigma, cost。
- 与 `sexual-health-sti-prevention-continuity/`、`chronic-infectious-disease-care-continuity/` 和 `pharmacy-benefit-formulary-prior-authorization-continuity/` 建立接口。
