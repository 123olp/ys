# Maternal Newborn Child Development

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/maternal-newborn-child-development` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

`maternal-newborn-child-development/` 研究孕产健康、新生儿健康、儿童健康、生长标准、早期儿童发展、养育照护和家庭调查资料。

> 核心问题：主体持续性不是成年后才开始；身体、认知、免疫、学习能力、压力系统和未来选择权从孕产、新生儿和儿童早期就被基础设施塑造。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体能力的形成有早期生命窗口
  -> 孕产、新生儿、儿童健康、营养、生长、照护和安全环境会改变长期生命路径
  -> 早期生命基础设施决定未来主体的身体、认知、学习和恢复能力底座
```

## 关注对象

- 孕产健康、孕产死亡率、产前照护、新生儿死亡率、儿童健康、生长标准、早期儿童发展和 nurturing care。
- PRAMS、DHS、World Bank ECD、Healthy People pregnancy and childbirth 等调查、政策和指标。
- 与 `reproductive-fertility-continuity/` 的关系：生殖连续性域关注生育力和生殖自主性；本域关注孕产、新生儿、儿童早期健康与发展。
- 与 `childcare-family-continuity/`、`nutrition-metabolic-health/`、`learning-skill-acquisition/` 和 `social-protection-benefits-delivery/` 的接口。

## Human Infra 模型链路

```text
母婴儿童早期生命基础设施
  -> 改变孕产安全、新生儿生存、儿童健康、生长、照护和早期发展条件
  -> 改变未来主体的身体储备、认知能力、学习能力、压力恢复和社会参与底座
  -> 降低早期死亡、发育受损、营养不足、照护断裂和代际不平等风险
  -> 增强长期健康寿命、有效时间、能力形成和未来选择权
```

## 非目标

- 不提供孕产、新生儿、儿童诊断、治疗、喂养、发育评估、疫苗、药物或育儿建议。
- 不判断家庭、父母、儿童能力、风险等级、福利资格或保险筛选。
- 不把早期生命数据用于家庭监控、惩罚、排名、歧视或责任转嫁。

## Source Signals

- WHO maternal health: https://www.who.int/health-topics/maternal-health
- WHO maternal mortality: https://www.who.int/news-room/fact-sheets/detail/maternal-mortality
- WHO antenatal care recommendations: https://www.who.int/publications/i/item/9789241549912
- WHO newborn mortality: https://www.who.int/news-room/fact-sheets/detail/newborn-mortality
- WHO child health: https://www.who.int/health-topics/child-health
- WHO child growth standards: https://www.who.int/tools/child-growth-standards
- Nurturing Care Framework: https://www.who.int/publications/i/item/9789241514064
- CDC PRAMS: https://www.cdc.gov/prams/
- CDC Child Development: https://www.cdc.gov/child-development/
- World Bank Early Childhood Development: https://www.worldbank.org/en/topic/earlychildhooddevelopment

## 下一步

- 建立早期生命变量表：孕产安全、产前照护、新生儿生存、儿童健康、生长、营养、照护、早期学习、家庭环境和保护边界。
- 与 `childcare-family-continuity/` 拆分早期健康发展和托育/家庭运行边界。
- 整理 WHO maternal/newborn/child health、Nurturing Care、PRAMS、DHS 和 World Bank ECD 的 Source Cards。
