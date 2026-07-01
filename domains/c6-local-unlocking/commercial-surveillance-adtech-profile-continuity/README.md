# Commercial Surveillance Adtech Profile Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/commercial-surveillance-adtech-profile-continuity` |
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

Commercial Surveillance Adtech Profile Continuity 关注商业监控、广告技术、跨站追踪、real-time bidding、profiling、lookalike audience 和预测画像如何改变主体被定位、定价、影响、排除和暴露的风险。

## 对象

- Commercial surveillance、adtech、tracking、cookies、pixels、mobile ad IDs、profile enrichment 和 audience segments。
- 广告竞价、跨站/跨应用追踪、数据共享、推断兴趣、敏感类别画像和价格/机会差异。
- 画像进入诈骗、歧视、操控、敏感位置暴露、健康/金融/住房/就业广告和脆弱人群 targeting 的路径。

## Human Infra 价值

```text
主体持续性需要注意力和机会入口不被不可见画像操控
-> 商业监控把行为、位置、设备和兴趣转化为广告与影响基础设施
-> 错误或敏感画像会改变主体看到的信息、价格、机会、诈骗暴露和社会评价
-> 追踪透明度、数据最小化、退出机制和执法边界降低画像外溢风险
-> 主体更能保留注意力、选择权、隐私和公平接入
```

## 边界

- 本域不提供广告投放策略、画像构建、微定向、规避平台政策、追踪部署、数据购买或影响操控方法。
- 不判断某广告技术、数据共享或 campaign 是否违法。
- 不提供绕过 cookie、设备指纹、广告拦截检测、反爬或平台限制的方法。
- 只整理公开资料、风险变量、权利边界、source signals 和禁止用途。

## 上下游

- 上游：`opt-out-preference-signal-consent-revocation-continuity/`、`data-broker-registry-opt-out-deletion-continuity/`、`digital-identity-security/`。
- 下游：`fraud-scams-consumer-protection/`、`online-safety-digital-harm-prevention/`、`consumer-reviews-endorsements-marketplace-trust-continuity/`。

## Source Signals

- Federal Trade Commission commercial surveillance, dark pattern and adtech enforcement materials.
- NIST Privacy Framework.
- CPPA cross-context behavioral advertising and opt-out materials.
