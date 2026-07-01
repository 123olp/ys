# 亲属照护、寄养、收养与儿童安置连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/kinship-foster-adoption-care-continuity` |
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

本域研究儿童无法由原照护安排稳定支持时，亲属照护、寄养、收养和其他儿童安置路径如何维持安全、身份、教育、医疗、关系和长期发展连续性。它关注儿童福利系统的研究边界，不提供个人收养、寄养或监护操作建议。

## 研究对象

- Kinship care、foster care、adoption、guardianship-like placements 和 permanency planning。
- 儿童身份记录、学校转接、医疗授权、保险覆盖、兄弟姐妹关系、文化和家庭联系。
- 寄养家庭、亲属照护者、个案计划、法院监督、服务转介和成年过渡。
- 安置稳定性、创伤知情照护、儿童声音、家庭支持和制度伤害风险。

## 价值链路

```text
儿童主体持续性需要稳定、安全且可恢复的照护环境
  -> 当原家庭照护失稳时，亲属照护、寄养、收养和安置系统接管部分照护责任
  -> 安置路径必须同时维持身份、关系、教育、医疗、文化和未来发展连续性
  -> 安置断裂、频繁转移、记录丢失或服务失败会把保护过程转化为新的创伤
  -> 儿童安置连续性把保护、归属和长期能力形成纳入 Human Infra
```

## 关键问题

- kinship、foster care 和 adoption 如何分别改变儿童身份、关系、服务和长期资源路径？
- 儿童福利记录如何影响学校、医疗、保险、法院、福利和成年过渡？
- 安置稳定性、创伤知情服务和家庭联系如何影响儿童未来主体能力形成？
- 如何防止本域被误用为收养中介、寄养申请、规避审核或儿童控制工具？

## 上游与下游

- 上游：`child-protection-family-safety/`、`family-law-custody-child-support-continuity/`、`vital-records-life-event-continuity/`、`maternal-newborn-child-development/`。
- 下游：`household-composition-dependent-eligibility-continuity/`、`education-access-lifelong-learning/`、`healthcare-access-continuity/`、`mental-health-affective-stability/`、`digital-legacy-data-succession/`。

## 非目标

- 不提供个人寄养、收养、亲属照护、监护、儿童福利案件、法院命令、资格审核或跨州/跨国收养建议。
- 不判断儿童安置、父母权利、照护者资格、补助资格、移民身份或个案安全。
- 不协助规避背景审查、绕过儿童保护程序、隐藏儿童位置、操控儿童证言、非法安置或儿童剥削。

## 初始资料入口

- Child Welfare Information Gateway: Kinship Care
- Child Welfare Information Gateway: Foster Care
- Child Welfare Information Gateway: Adoption
- HHS Administration for Children and Families, Children's Bureau
