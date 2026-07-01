# Intellectual Property Technology Transfer Access

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/intellectual-property-technology-transfer-access` |
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

本域研究知识产权、专利、许可、技术转移、大学和公共研究成果商业化、药物和医疗技术可及性，如何决定未来技术是否真的能被主体使用，而不是停留在论文、专利、公司资产或少数人可及的产品中。

Human Infra 关注未来技术窗口，但技术成熟并不等于主体可及。专利池、独占许可、生产权、定价、地域授权、监管数据、商业秘密和公共资助条款都会影响新技术能否进入人的生命路径。本域是“技术产生”到“技术可及”的制度转换层。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 未来技术必须从实验室进入可获得、可负担、可持续的实际服务
  -> 知识产权、许可、技术转移和市场准入会决定技术扩散路径
  -> 需要审查技术所有权、转化机制和可及性边界
  -> intellectual-property-technology-transfer-access
```

## 关注对象

- 专利、许可、商业秘密、数据权利、公共资助成果和技术转移机制。
- 大学、政府实验室、公司、基金会和公共机构之间的成果转化路径。
- Bayh-Dole、march-in rights、全球健康可及性、药品和医疗技术扩散。
- 独占授权、平台锁定、价格、生产能力、供应链、地域差异和公平可及性。
- Human Infra 中未来技术的“是否存在”与“主体是否能用上”的差异。

## Human Infra 模型链路

```text
科研发现和技术原型
  -> 知识产权、许可和技术转移安排
  -> 决定生产、定价、地域扩散、服务交付和可及性
  -> 影响主体采用概率、未来选择权和技术窗口真实价值
  -> 把技术成熟度转化为主体可获得性的治理问题
```

## 非目标

- 不提供法律意见、专利申请策略、规避侵权、绕开许可、商业秘密获取或谈判指导。
- 不判断具体专利有效性、侵权风险、自由实施空间或商业估值。
- 不把知识产权简单写成创新之敌或创新保证；只审查它如何影响主体可及性。
- 不替代 `medicine-access-treatment-continuity/`；本域关注技术扩散制度，药品日常可及由药品连续性域负责。

## Source Signals

- WIPO Technology Transfer: https://www.wipo.int/technology-transfer/en/
- NIH Technology Transfer: https://www.techtransfer.nih.gov/
- NIST Bayh-Dole: https://www.nist.gov/tpo/bayh-dole
- AUTM: https://autm.net/
- WHO intellectual property and public health: https://www.who.int/health-topics/medicines/intellectual-property
- WHO Global Strategy and Plan of Action on Public Health, Innovation and Intellectual Property: https://www.who.int/publications/i/item/9789241503117

## 下一步

- 建立 Technology Access Card：technology、owner、public funding、license model、manufacturing path、price/access risk、geographic constraints、equity concern。
- 与 `clinical-trials-regulatory-science-translation/` 对接，区分临床证据成熟、监管许可和实际可及。
- 与 `research-portfolio-prioritization-funding-governance/` 对接，把可及性作为研究组合优先级变量。
