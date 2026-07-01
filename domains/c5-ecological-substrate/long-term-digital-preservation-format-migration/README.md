# Long Term Digital Preservation Format Migration

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/long-term-digital-preservation-format-migration` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

`long-term-digital-preservation-format-migration/` 研究长期数字保存、格式迁移、校验和、元数据、可读性、媒介退化和档案治理，如何影响 Human Infra 的知识、身份、作品和研究证据连续性。

> 核心问题：主体持续性依赖跨时间可恢复的资料。数据存在不等于未来可读，未来可读也不等于语境、权限、完整性和解释链仍然存在。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 记忆、作品、研究证据、授权记录和项目上下文必须跨很长时间保存
  -> 长期保存依赖格式、元数据、校验、备份、迁移、权限和可读性治理
  -> 若格式腐烂、媒介退化或语境丢失，数字连续性会变成不可解释碎片
  -> 因此长期数字保存和格式迁移是外部记忆连续性的档案域
```

## 关注对象

- OAIS、数字保存工作流、文件格式、校验和、fixity、元数据、备份、迁移、仿真和长期访问。
- 个人档案、科研数据、医疗记录、授权文件、作品、代码、模型、Source Card 和 Web 作品保存。
- 与 `life-logging-personal-archives-continuity/` 的边界：生命日志域关注个人资料采集和组织；本域关注长期保存、格式迁移和可读性治理。
- 与 `digital-legacy-data-succession/` 的边界：数字遗产域关注权限交接；本域关注资料本身能否长期保持完整可读。

## Human Infra 模型链路

```text
长期数字保存与格式迁移 T
  -> 改变格式稳定性、元数据、校验、备份、迁移、权限和可读性变量 X
  -> 改变个人档案、研究证据、作品和授权记录的长期可恢复状态 S
  -> 改变资料丢失、语境断裂、身份解释失败和长期项目重启成本 λ(t)
  -> 影响外部记忆、知识复利、研究复现和主体持续性
```

## 非目标

- 不提供绕过访问控制、破解加密、盗取档案或规避版权的方法。
- 不把数字档案、聊天记录或作品保存写成主体连续性证明。
- 不替代法律遗嘱、数据受托、机构档案政策或隐私合规。

## Source Signals

- Library of Congress Digital Preservation: https://www.loc.gov/preservation/digital/
- Library of Congress Sustainability of Digital Formats: https://www.loc.gov/preservation/digital/formats/
- NDSA Levels of Digital Preservation: https://ndsa.org/publications/levels-of-digital-preservation/
- Digital Preservation Coalition Handbook: https://www.dpconline.org/handbook

## 下一步

- 建立长期保存变量表：格式、媒介、校验、元数据、复制数、地理分布、迁移计划、权限和语境说明。
- 与 `life-logging-personal-archives-continuity/`、`digital-legacy-data-succession/`、`personal-knowledge-management-cognitive-offloading/` 和 `post-quantum-cryptography-long-term-data-security/` 建立接口。
