# Mycotoxin Food Crop Storage Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/mycotoxin-food-crop-storage-safety-continuity` |
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


`mycotoxin-food-crop-storage-safety-continuity` 研究霉菌毒素、作物储存、食品供应、动物饲料和慢性暴露如何影响主体持续性。

> 核心问题：霉菌毒素不是单次食物中毒；它把农业、储存、气候湿度、贸易检测、儿童营养和慢性健康风险连接成食品系统的隐性约束。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖长期安全、营养稳定和可负担的食物系统
  -> 霉菌毒素会在作物、储存、饲料和加工链中形成慢性暴露风险
  -> 检测、标准、储存控制、供应链追踪和风险沟通构成食品安全前提
  -> 若该前提失败，营养、肝肾风险、儿童发育、动物产品和贸易可用性都会受损
```

## 关注对象

- Aflatoxin、ochratoxin、fumonisin 等霉菌毒素，谷物、坚果、饲料、储存湿度和食品检测。
- 农业生产、食品监管、贸易、儿童营养、动物饲料和气候变化下的污染风险。
- 与 `food-safety-contamination-control/` 的边界：上位域关注食品污染总论；本域关注霉菌毒素这类慢性/供应链型自然毒素。

## Human Infra 链路

```text
霉菌毒素风险被检测和控制
  -> 慢性毒素暴露、食品召回和营养不确定性下降
  -> 食物供应、儿童营养、饲料和贸易系统更稳定
  -> 健康寿命、资源可及和未来选择权被保护
```

## 非目标

- 不提供食品检测解释、食用判断、储存处置、农业操作、补贴/贸易、产品购买、诊断或治疗建议。
- 不替代 FDA、USDA、食品监管、农业推广、实验室、医疗或兽医服务。
- 不把检测值、批次信息、气味外观或 AI 输出写成个体食用许可或供应链合规结论。

## Source Signals

- FDA Natural Toxins in Food: https://www.fda.gov/food/chemical-contaminants-pesticides/natural-toxins-food
- FDA Bad Bug Book: https://www.fda.gov/food/foodborne-pathogens/bad-bug-book-second-edition
- USDA ARS Mycotoxin Prevention and Applied Microbiology Research: https://www.ars.usda.gov/midwest-area/peoria-il/national-center-for-agricultural-utilization-research/mycotoxin-prevention-and-applied-microbiology-research/

## 下一步

- 建立 `crop storage -> fungal growth -> mycotoxin exposure -> food/feed safety -> continuity cost` 变量表。
- 区分家庭储存、学校/援助食品、粮食贸易、动物饲料、气候湿度和儿童营养场景。
