# Municipal 311 Service Request Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/municipal-311-service-request-continuity` |
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

`municipal-311-service-request-continuity/` 研究 311、非紧急服务请求、地方公共工程派单、状态回传和服务请求数据如何影响主体在邻里环境中的问题报告、跟踪和恢复能力。

## 先验链路

```text
主体要在社区中持续行动
  -> 邻里问题必须能从个人观察转成公共机构可处理的请求
  -> 请求需要渠道、分类、位置、编号、责任部门和状态回传
  -> 311 / Open311 / 地方服务请求系统把问题转成可派单的公共服务对象
  -> 请求失败会让路灯、坑洞、垃圾、积水、标志、噪声和通行障碍长期滞留
  -> 日常出行、照护、工作、学习、公共安全和邻里信任被持续消耗
```

## 研究对象

- 311、non-emergency service request、Open311 / GeoReport、service category、request status、department routing、SLA、closure code、公开服务请求数据和回传机制。

## 不能做

- 不提供紧急报警替代、执法规避、骚扰举报、虚假投诉、个人跟踪、位置监控、投诉代写、法律策略、政治动员或个案市政服务申诉建议。
- 不收集、复制或要求家庭地址、精确位置、照片、车牌、邻居身份、联系方式、执法记录、账号、投诉记录或其他敏感资料。

## Source Signals

- Open311 GeoReport v2: https://wiki.open311.org/GeoReport_v2/
- NYC Open Data 311 service requests: https://opendata.cityofnewyork.us/
- Code for America 311 and civic service context: https://www.codeforamerica.org/
- USA.gov local governments: https://www.usa.gov/local-governments

## 上下游关系

- 上游：`public-service-design-accessibility/`、`civic-data-open-government-transparency/`、`public-works-civil-infrastructure-asset-management/`。
- 下游：`streetlight-outage-nighttime-visibility-continuity/`、`sidewalk-curb-ramp-maintenance-access-continuity/`、`storm-drain-catch-basin-local-flooding-continuity/`。
