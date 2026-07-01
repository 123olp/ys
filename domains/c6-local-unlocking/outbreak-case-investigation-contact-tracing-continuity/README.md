# Outbreak Case Investigation Contact Tracing Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/outbreak-case-investigation-contact-tracing-continuity` |
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

`outbreak-case-investigation-contact-tracing-continuity/` 研究暴发中的病例调查、接触者追踪、暴露通知、隐私保护和服务转介如何维持主体持续性。

> 核心问题：传染病暴发不是单个病例事件；如果暴露关系不能被及时、可信、隐私保护地转化为行动信号，学习、工作、照护和医疗系统会被连锁中断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体长期行动依赖可持续的群体接触环境
  -> 暴发使日常接触网络变成传播网络
  -> 病例调查和接触追踪把不可见传播链转化为可通知、可转介、可隔离、可恢复的执行信号
```

## 关注对象

- 病例调查、接触者追踪、暴露通知、数字工具、公共卫生访谈、服务转介和隐私保护。
- 传播链识别、延迟、覆盖率、信任、语言可达、弱势群体保护和污名风险。
- 与 `immunization-public-health-surveillance/` 的关系：上位域关注监测系统；本域关注暴发后从病例到接触者的执行链。

## Human Infra 模型链路

```text
病例调查与接触追踪
  -> 改变暴露关系发现、通知、隔离支持和服务转介能力
  -> 改变传播链继续扩展的概率和被暴露主体的行动选择
  -> 降低暴发扩散、工作学校关闭、照护中断和医疗挤兑风险
  -> 增强健康寿命、有效时间、社会信任和主体持续性
```

## 非目标

- 不提供个体诊断、检测解释、隔离命令、法律建议或接触者名单识别。
- 不提供追踪规避、隐私侵害、定位、人肉搜索、污名化或暴露信息公开策略。
- 不把公共卫生调查工具写成监控、惩罚或社会控制方案。

## Source Signals

- CDC case investigation and contact tracing: https://www.cdc.gov/covid/php/contact-tracing/index.html
- CDC contact tracing resources: https://www.cdc.gov/contact-tracing/
- WHO contact tracing: https://www.who.int/news-room/questions-and-answers/item/contact-tracing
- WHO outbreak response and risk communication: https://www.who.int/emergencies

## 下一步

- 建立变量表：病例发现延迟、接触者覆盖率、通知时滞、隔离支持、隐私保护、污名风险和服务转介。
- 与 `isolation-quarantine-work-school-continuity/`、`community-testing-screening-access-continuity/` 和 `health-data-privacy-governance/` 建立接口。
