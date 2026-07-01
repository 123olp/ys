# Public Library Community Anchor Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-library-community-anchor-access-continuity` |
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

`public-library-community-anchor-access-continuity` 研究公共图书馆和社区锚点机构如何提供互联网、学习空间、公共电脑、打印扫描、信息导航、避暑/取暖、就业服务和灾害恢复中的可信公共接入。

> 核心问题：图书馆不是书架，而是低门槛公共基础设施；它把信息、学习、申请、通信、冷暖空间和社区支持交给没有私人资源的人。

## 关注对象

- 公共图书馆、社区中心、公共电脑、Wi-Fi、打印扫描、数字技能培训、就业/福利申请协助和可信信息导航。
- 开放时段、交通可达、语言服务、无障碍、隐私、未成年人保护、灾害期间服务连续性和与学校/社服/应急系统的协作。
- 与 IMLS、FCC E-Rate、数字包容、公共服务设计、教育、就业、社会服务、灾害恢复和社区韧性的接口。

## Human Infra 链路

```text
图书馆和社区锚点可达
  -> 信息、网络、设备、学习空间和公共服务导航低门槛接入
  -> 数字排除、申请失败、信息失明、孤立和灾害恢复断点下降
  -> 学习、求职、福利、医疗门户、法律信息和社区协作更可执行
  -> 主体认知资源、任务完成能力和长期选择权增强
```

## 非目标

- 不提供图书馆系统绕过、账号滥用、设备规避、盗版、骚扰馆员/用户、隐私侵犯、未成年人风险内容或个案福利/法律策略。
- 不替代图书馆、学校、社工、就业服务、法律服务、医疗门户或应急管理机构。
- 不收集借阅记录、公共电脑登录、未成年人信息、精确到访轨迹、馆内安防细节或个人申请材料。

## Source Signals

- IMLS Public Libraries: https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey
- FCC E-Rate: https://www.fcc.gov/general/e-rate-schools-libraries-usf-program
- IMLS Library Search and Compare: https://www.imls.gov/search-compare
- Digital.gov: https://digital.gov/

## 下一步

- 建立 `anchor institution -> access service -> task support -> exclusion reduction -> capability continuity` 变量表。
- 区分图书馆日常服务、数字技能、公共电脑、就业/福利导航、灾害韧性和社区学习空间。
- 与 `digital-inclusion-connectivity`、`public-service-design-accessibility`、`education-access-lifelong-learning`、`employment-job-quality-income-security` 和 `community-resilience-hub-shelter-center-continuity` 建立边界。
