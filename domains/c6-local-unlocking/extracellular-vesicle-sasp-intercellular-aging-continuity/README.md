# Extracellular Vesicle SASP Intercellular Aging Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/extracellular-vesicle-sasp-intercellular-aging-continuity` |
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

Extracellular Vesicle SASP Intercellular Aging Continuity 负责整理细胞外囊泡、SASP、细胞间通讯、衰老信号扩散、组织微环境和远期递送平台边界。

核心问题：

> 衰老不是只发生在单个细胞内部；细胞外囊泡和 SASP 等通讯机制可能把局部损伤、炎症和衰老状态传播到邻近或远端组织。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 组织功能取决于细胞之间的通信、协调和反馈
  -> 衰老细胞、受损细胞和免疫细胞会通过 SASP 与细胞外囊泡改变微环境
  -> 通讯失衡可能扩散炎症、纤维化、免疫扰动和再生失败
  -> 若通讯机制可被观测或调节，可能改变组织级风险函数
  -> 因此细胞间衰老通讯是从细胞机制走向组织系统模型的关键域
```

## 关注对象

- extracellular vesicles、exosomes、microvesicles、SASP、intercellular communication、senescence spreading。
- EV cargo、miRNA/protein/lipid 信号、组织微环境、炎症扩散、递送平台和污染/纯化/测量边界。
- 与 `cellular-senescence-clearance/` 的关系：衰老细胞域关注细胞状态和 SASP 来源，本域关注信号传播和细胞间通讯。
- 与 `nanomedicine-targeted-delivery-molecular-repair/` 的关系：本域可作为天然递送与信号平台资料来源，但不等同于治疗方案。

## Human Infra 模型链路

```text
细胞间通讯观测 / 调节 T
  -> 改变 EV cargo、SASP 信号、炎症扩散和组织微环境 X
  -> 改变细胞群协同与组织维护状态 S
  -> 改变再生、纤维化、炎症、免疫扰动和功能衰退风险
  -> 改变健康寿命、恢复能力和有效时间
```

## 非目标

- 不提供 exosome 产品、注射、提取、培养、递送、检测解读或临床建议。
- 不把 EV/SASP 相关性写成确定治疗靶点。
- 不忽略样本污染、分离方法、cargo 异质性和组织来源不确定性。

## Source Signals

- Hallmarks of Aging: https://pubmed.ncbi.nlm.nih.gov/36599349/
- Emerging roles of extracellular vesicles in cellular senescence and aging: https://pmc.ncbi.nlm.nih.gov/articles/PMC5847882/
- Extracellular vesicles as communicators of senescence: https://pmc.ncbi.nlm.nih.gov/articles/PMC9664547/
