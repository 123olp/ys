# Shellfish Biotoxin Harmful Algal Bloom Food Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/shellfish-biotoxin-harmful-algal-bloom-food-continuity` |
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


`shellfish-biotoxin-harmful-algal-bloom-food-continuity` 研究贝类毒素、有害藻华、海产品供应、采捕关闭和食物连续性的关系。

> 核心问题：贝类毒素把海洋生态变化、食品监管、地方生计、餐饮供应和急性神经/胃肠风险连接在一起，是水生食物系统里的高不确定性节点。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖安全、多样和可获得的水生食物系统
  -> 有害藻华产生的贝类毒素会进入采捕、市场、餐饮和家庭食用链
  -> 监测、关闭、召回、供应替代和风险沟通构成食物安全前提
  -> 若该前提失败，海产品可及、地方收入、旅游餐饮和急性中毒风险都会被重定价
```

## 关注对象

- Shellfish biotoxins、red tide、有害藻华、贝类采捕关闭、海产品检测、召回和食品风险沟通。
- 食品监管、渔业生计、餐饮供应、旅游经济和消费者信息。
- 与 `fisheries-aquatic-food-systems-continuity/` 的边界：上位域关注水生食物系统；本域关注贝类毒素和 HAB 食物链节点。

## Human Infra 链路

```text
贝类毒素监测和食品公告有效运行
  -> 急性中毒、召回混乱和供应不确定性下降
  -> 海产品供应、餐饮、渔业收入和消费者信任更稳定
  -> 营养可及、经济连续性和行动选择权被保护
```

## 非目标

- 不提供个体食用许可、采捕建议、检测解释、烹饪安全、中毒治疗、餐馆选择、供应链合规或贸易建议。
- 不替代 FDA、NOAA、州贝类管制、食品监管、医疗、毒物中心或渔业管理机构。
- 不把海域地图、关闭公告、检测值、气味外观或 AI 输出写成个人食品安全结论。

## Source Signals

- FDA National Shellfish Sanitation Program: https://www.fda.gov/food/federalstate-food-programs/national-shellfish-sanitation-program-nssp
- NOAA Harmful Algal Blooms: https://oceanservice.noaa.gov/hazards/hab/
- CDC Harmful Algal Blooms: https://www.cdc.gov/harmful-algal-blooms/

## 下一步

- 建立 `HAB -> shellfish biotoxin -> harvest closure / recall -> food access and poisoning risk` 变量表。
- 区分商业采捕、休闲采捕、餐饮、旅游、地方渔业生计和食品召回场景。
