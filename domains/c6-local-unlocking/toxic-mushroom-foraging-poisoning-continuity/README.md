# Toxic Mushroom Foraging Poisoning Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/toxic-mushroom-foraging-poisoning-continuity` |
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


`toxic-mushroom-foraging-poisoning-continuity` 研究野生蘑菇误食、采食文化、食物获取、毒物中心连接和急性中毒风险如何影响主体持续性。

> 核心问题：野生蘑菇风险不是“食材知识不足”；它是食物探索、文化实践、户外活动、儿童误食和急性肝肾毒性之间的高后果边界。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可靠区分可食资源和有毒暴露
  -> 野生蘑菇误食会把食物探索转化为急性中毒和医疗危机
  -> 教育、标签、毒物中心、急诊连接和食品安全边界构成行动前提
  -> 若该前提失败，户外采食、儿童安全、家庭饮食和医疗容量都会被高后果事件重定价
```

## 关注对象

- 野生蘑菇、误食、采食、儿童误食、急性中毒、肝肾风险、毒物中心和急诊连接。
- 食品安全教育、市场/餐饮边界、文化实践、语言可及和风险沟通。
- 与 `food-safety-contamination-control/` 的边界：上位域关注食品污染控制；本域关注野生蘑菇识别失败和毒物连接。

## Human Infra 链路

```text
野生蘑菇误食风险被识别和连接
  -> 高后果中毒、诊疗延误和家庭恐慌下降
  -> 食物探索、户外活动和家庭饮食边界更清楚
  -> 生命风险、医疗负担和有效时间损失下降
```

## 非目标

- 不提供蘑菇鉴定、可食性判断、采食建议、烹饪安全、治疗、解毒、急诊分诊或市场合规建议。
- 不替代 FDA、Poison Help、医疗机构、毒物中心、地方公共卫生、食品监管或专家鉴定。
- 不把照片、AI 识别、民间经验、地理位置或颜色气味写成食用许可。

## Source Signals

- CDC MMWR Poisonous Mushroom Ingestions: https://www.cdc.gov/mmwr/volumes/70/wr/mm7010a1.htm
- FDA Bad Bug Book: https://www.fda.gov/food/foodborne-pathogens/bad-bug-book-second-edition
- Poison Help: https://www.poisonhelp.org/

## 下一步

- 建立 `foraging exposure -> identification uncertainty -> ingestion risk -> poison center / ED connection -> continuity cost` 变量表。
- 区分儿童误食、成人采食、市场/餐饮、移民语言可及、社交媒体误导和户外教育场景。
