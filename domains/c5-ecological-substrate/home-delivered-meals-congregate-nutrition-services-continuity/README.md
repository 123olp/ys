# Home Delivered Meals Congregate Nutrition Services Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-delivered-meals-congregate-nutrition-services-continuity` |
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


`home-delivered-meals-congregate-nutrition-services-continuity` 研究老年人、残障者和行动受限主体的 home-delivered meals、congregate meals、营养筛查、社交接触和送餐中断如何影响持续摄食、独立生活和照护负担。

> 核心问题：能吃饭不只是有食物，还要能获得、准备、进食并被定期看见；送餐和集体餐食是营养、社交和安全检查的复合基础设施。

## 关注对象

- Home-delivered meals、congregate meals、Older Americans Act nutrition services、Meals on Wheels 类服务、营养筛查和送餐安全检查。
- 资格、等待名单、配送可靠性、特殊饮食、社交接触、恶劣天气、志愿者能力、照护者负担、独立生活和转介服务。
- 与 ACL、AAA、老年服务、残障服务、长期照护、慢病管理、社会连接和灾害供餐的接口。

## Human Infra 链路

```text
送餐和集体营养服务可持续
  -> 行动受限主体仍可获得餐食、社交接触和安全观察
  -> 营养不良、孤立、照护负担、住院和机构化风险下降
  -> 主体更能在家中维持独立生活和日常恢复
  -> 健康寿命、有效时间和未来选择权增强
```

## 非目标

- 不提供个人资格判断、服务申请材料、餐食处方、疾病饮食建议、照护安排、医疗处置、志愿者调度或个案申诉策略。
- 不替代 ACL、Area Agencies on Aging、Meals on Wheels、营养师、医疗机构、长期照护、残障服务或社会服务。
- 不收集个人地址、健康信息、配送路线、餐食记录、家庭风险、志愿者身份、服务名单或照护者隐私。

## Source Signals

- ACL Nutrition Services: https://acl.gov/programs/health-wellness/nutrition-services
- ACL Older Americans Act: https://acl.gov/about-acl/authorizing-statutes/older-americans-act
- Meals on Wheels America Research: https://www.mealsonwheelsamerica.org/learn-more/research
- USDA Nutrition Programs: https://www.fns.usda.gov/programs

## 下一步

- 建立 `nutrition service -> delivery/congregate mode -> social check -> functional status -> independence continuity` 变量表。
- 区分送餐、集体餐、营养筛查、社交接触、安全观察、特殊饮食和灾害中断恢复。
- 与 `caregiving-long-term-care`、`social-connection-relational-infra`、`food-security-nutrition-access`、`disability-services-independent-living` 和 `emergency-food-disaster-feeding-continuity` 建立边界。
