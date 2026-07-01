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
