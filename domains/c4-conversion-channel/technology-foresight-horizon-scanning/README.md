# Technology Foresight Horizon Scanning

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/technology-foresight-horizon-scanning` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
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

## 定位

本域研究技术预见、地平线扫描、早期信号、情景分析和弱信号监测，如何帮助 Human Infra 系统性发现可能改变主体持续性边界的新技术、新风险和新制度窗口。

Human Infra 的终极问题不是只管理今天已经成熟的技术，还要理解哪些未来技术可能改变寿命、有效时间、主观时间、相对时间和未来选择权。若没有地平线扫描，项目会被新闻热度牵引；若没有边界，技术预见又会变成炒作和投资叙事。本域负责把“未来可能性”转为可审查的研究候选队列。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要等待、识别、采用和整合未来技术窗口
  -> 技术窗口出现前通常只有弱信号、临床前结果、专利、资金、政策和原型
  -> 需要技术预见和地平线扫描把弱信号转成候选研究域和审查任务
  -> technology-foresight-horizon-scanning
```

## 关注对象

- Horizon scanning、strategic foresight、weak signals、scenario planning 和 early warning。
- 科研论文、临床试验、专利、监管公告、资金流、公司披露、标准化活动和政策信号。
- 技术成熟度、证据成熟度、社会可及性、成本曲线和风险曲线。
- 未来技术如何进入 Human Infra 的 radar、Source Card、Scenario Card 和 ADR。
- 技术预见如何服务“等待-采用-升级”的主体持续性飞轮。

## Human Infra 模型链路

```text
弱信号和新技术线索
  -> 地平线扫描与技术预见
  -> 形成候选研究域、证据队列和场景假设
  -> 进入 Research Domain Radar 或正式 domains/*
  -> 支撑未来窗口识别、等待策略和研究组合治理
```

## 非目标

- 不提供投资建议、交易策略、公司评级、市场时机判断或财务预测。
- 不把新闻、融资、专利或公司公告写成疗效、可行性或时间表证明。
- 不制造“必然到来”的技术决定论叙事。
- 不替代正式证据审查、监管审查、伦理审查或模型评估。

## Source Signals

- OECD Strategic Foresight: https://www.oecd.org/strategic-foresight/
- WHO Health Technology Assessment and horizon scanning: https://www.who.int/teams/health-products-policy-and-standards/assistive-and-medical-technology/health-technology-assessment
- EUnetHTA: https://www.eunethta.eu/
- FDA Emerging Sciences and Technologies: https://www.fda.gov/science-research/science-and-research-special-topics/emerging-science-and-technology
- OECD Science, Technology and Innovation Outlook: https://www.oecd.org/sti/oecd-science-technology-and-innovation-outlook-25186167.htm

## 下一步

- 建立 Horizon Signal Card：signal type、source、mechanism、maturity、evidence gap、risk、trigger、watch cadence。
- 把 `docs/reference/research-domain-radar.md` 从静态列表升级为带信号来源、触发条件和复核周期的候选域队列。
- 与 `research-portfolio-prioritization-funding-governance/` 对接，把弱信号转成研究组合优先级，而不是单点追热点。
