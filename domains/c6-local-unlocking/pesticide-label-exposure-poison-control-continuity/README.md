# Pesticide Label Exposure Poison Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pesticide-label-exposure-poison-control-continuity` |
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


`pesticide-label-exposure-poison-control-continuity` 研究农药/杀虫剂标签、家庭和职业使用、误用暴露、儿童/宠物风险和毒物控制连接如何影响主体持续性。

> 核心问题：病媒和虫害治理本身也会制造风险；如果标签、储存、使用边界和中毒连接失败，控制工具会变成新的身体、家庭和环境风险源。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要控制害虫和病媒，同时不引入新的化学伤害
  -> 农药误用、误混、错误储存和过量暴露会造成中毒和室内污染
  -> 标签理解、储存、儿童/宠物保护、职业边界和毒物中心连接构成工具安全前提
  -> 若该前提失败，原本的风险控制会反向破坏健康、住房和恢复能力
```

## 关注对象

- 农药/杀虫剂标签、室内外使用、儿童、宠物、职业接触、储存、误混和中毒风险。
- 毒物中心、EPA 标签制度、NPIC、家庭 pest control、病媒控制和灾后/住房场景。
- 与 `household-cleaning-disinfection-pest-control-continuity/` 的边界：家庭卫生域是上位；本域聚焦农药标签和化学暴露控制链。

## Human Infra 链路

```text
农药标签和暴露边界可理解、可执行、可求助
  -> 误用、误混、儿童/宠物暴露和中毒风险下降
  -> 害虫治理不再反向破坏居住、健康和恢复环境
  -> 主体持续性获得更安全的环境控制工具
```

## 非目标

- 不提供农药选择、配方、施用、混合、剂量、解毒、现场清理、法律合规或职业操作建议。
- 不替代 EPA、NPIC、毒物中心、职业安全、公共卫生、害虫治理、医疗或兽医服务。
- 不鼓励标签规避、非法施药、危险混合、过量使用或化学品转移储存。

## Source Signals

- EPA Pesticide Labels: https://www.epa.gov/pesticide-labels
- EPA Safe Pest Control: https://www.epa.gov/safepestcontrol
- National Pesticide Information Center: https://npic.orst.edu/
- Poison Help: https://www.poisonhelp.org/

## 下一步

- 建立 `pest pressure -> pesticide decision -> label comprehension -> exposure event -> poison-control/medical connection` 变量表。
- 区分家庭、学校、职业、农业、灾后、宠物、儿童和多户住宅场景。
