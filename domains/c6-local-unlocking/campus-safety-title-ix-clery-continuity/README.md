# Campus Safety Title IX Clery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/campus-safety-title-ix-clery-continuity` |
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

`campus-safety-title-ix-clery-continuity` 研究校园安全、Title IX、sexual misconduct response、Clery Act、crime reporting、emergency notification、supportive measures 和安全数据公开如何影响学生到场、归属、恢复和权利连续。

> 核心问题：高校不是纯学习空间；如果性骚扰、性暴力、跟踪、校园犯罪、报复、报告失信和安全通知断裂，学生会失去到场能力、学习时间、信任关系和恢复路径。

## 关注对象

- Title IX discrimination and sexual misconduct response、supportive measures、grievance process、retaliation prevention 和 reporting channels。
- Clery Act campus crime statistics、timely warnings、emergency notifications、security policies 和 annual security reports。
- 校园警务、安全服务、victim advocacy、confidential resources、housing/academic adjustments 和 community referral。
- 报告障碍、创伤恢复、缺勤、转学、休学、报复、程序公平和公开数据可理解性。

## Human Infra 链路

```text
校园安全、Title IX 与 Clery 连续
  -> 伤害报告、安全通知、支持性措施和程序责任保持可见
  -> 性骚扰暴力、报复、恐惧缺勤和制度失信的长期损耗下降
  -> 到场能力、学习参与、恢复路径和权利救济保持
  -> 主体安全、校园归属和未来选择权增强
```

## 非目标

- 不提供个人报案、Title IX 投诉、法律策略、证据保存、危机处置、安全计划、校园警务或个案建议。
- 不替代 emergency services、campus safety、Title IX office、confidential advocate、counseling、medical care 或法律援助。
- 不收集或处理受害者资料、事件细节、位置、证据、身份、健康资料、纪律资料或调查记录。

## Source Signals

- U.S. Department of Education OCR Title IX resources: https://www.ed.gov/about/ed-offices/ocr
- U.S. Department of Education Campus Safety and Security data: https://ope.ed.gov/campussafety/
- ED Clery Act campus safety and security materials: https://www.ed.gov/laws-and-policy/higher-education-laws-and-policy/campus-safety-and-security
- Institutional annual security reports, Title IX policies and public safety materials.

## 下一步

- 建立 `harm/report -> supportive measures -> process -> safety notification -> continuity` 变量表。
- 区分 Title IX、Clery、campus safety、confidential advocacy、victim services、discipline 和 civil rights data。
- 与 `personal-safety-violence-prevention`、`online-safety-digital-harm-prevention`、`school-climate-bullying-violence-prevention-continuity` 和本轮高教域建立边界。
