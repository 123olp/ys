# Asylum Refugee Protection Status Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/asylum-refugee-protection-status-continuity` |
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


本域研究庇护、难民身份、临时保护、人道保护、家庭团聚、安置和保护状态转换如何影响主体在迫害、战争、灾害或制度断裂后的持续存在与恢复。

> 核心问题：当主体无法安全依赖原国家或原制度时，保护身份本身成为生存基础设施；若申请、等待、认定、安置或身份转换断裂，安全、医疗、教育、工作和家庭都会被长期悬置。

## 关注对象

- 庇护、难民、临时保护、人道假释、补充保护、无遣返原则、重新安置和家庭团聚。
- 申请等待、身份文件、工作许可、住所、医疗、教育、语言、法律援助、创伤支持和数据敏感性。
- 保护状态与 `migration-displacement-humanitarian-continuity/`、`legal-identity-civil-registration/`、`healthcare-access-continuity/` 和 `access-to-justice-legal-aid/` 的接口。
- 与一般移民身份域的边界：本域关注保护逻辑、迫害/危险背景和人道安置，不关注普通居留管理。

## Human Infra 链路

```text
庇护 / 难民 / 保护状态连续
  -> 原制度失效或危险时，主体仍能进入替代保护框架
  -> 安全、住所、医疗、教育、工作、家庭团聚和法律救济逐步恢复
  -> 被遣返、无证、失学、失医、剥削和长期等待风险下降
  -> 主体在极端制度断裂后保留恢复路径和未来选择权
```

## 非目标

- 不提供庇护、难民、保护身份、面谈、证据、上诉、搬迁、边境、旅行、工作许可或法律建议。
- 不判断个人是否符合庇护、难民、临时保护、人道假释或家庭团聚资格。
- 不提供边境穿越路线、规避执法、伪造材料、危险旅行、藏匿、绕过程序或削弱保护对象隐私的方法。

## Source Signals

- UNHCR Protection: https://www.unhcr.org/what-we-do/protect-human-rights
- UNHCR Refugee Data Finder: https://www.unhcr.org/refugee-statistics/
- USCIS Asylum: https://www.uscis.gov/humanitarian/refugees-and-asylum/asylum
- USCIS Refugees: https://www.uscis.gov/humanitarian/refugees-and-asylum/refugees

## 下一步

- 建立保护状态变量表：安全风险、身份文件、等待时间、工作许可、家庭团聚、医疗教育接入、法律援助和数据保护。
- 整理 UNHCR、USCIS、EOIR、IOM、OCHA、IDMC 和 WHO Refugee and Migrant Health Source Cards。
- 与 `migration-displacement-humanitarian-continuity/` 明确分工：迁移域研究整体人道服务连续性，本域研究保护身份和身份转换链。
