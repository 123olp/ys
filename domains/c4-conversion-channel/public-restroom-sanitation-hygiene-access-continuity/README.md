# Public Restroom Sanitation Hygiene Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-restroom-sanitation-hygiene-access-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


`public-restroom-sanitation-hygiene-access-continuity` 研究公共厕所、洗手设施、卫生维护、开放时段、无障碍如厕、经期卫生和照护者辅助空间如何影响主体在离家后能否持续工作、学习、出行、照护、就医和参加公共生活。

> 核心问题：公共空间中的身体需求不是附属小事；如厕和卫生接入断裂，会把行动半径、停留时间、尊严、安全和公共参与同时压缩。

## 关注对象

- 公共厕所、洗手设施、卫生用品、经期卫生、家庭/无障碍厕所、婴幼儿换尿布台和照护辅助空间。
- 开放时段、维护频率、清洁质量、导视、排队、费用、关闭策略、损坏修复和极端天气/灾害期间的替代设施。
- 与 WASH、公共卫生、无障碍设计、城市治理、公共交通、旅游、露宿者服务、学校和灾害响应的接口。

## Human Infra 链路

```text
公共如厕和卫生接入稳定
  -> 主体离家停留时间和行动半径增加
  -> 感染、脱水、憋尿、尊严损失和公共空间排除风险下降
  -> 工作、学习、照护、就医、交通换乘和社区参与更可持续
  -> 主体有效时间、行动自由和未来选择权增强
```

## 非目标

- 不提供厕所定位跟踪、规避管理、破坏设施、占用空间、偷拍骚扰、非法进入、露宿规避执法或个案投诉策略。
- 不替代地方政府、公共卫生部门、设施运营方、无障碍专业人员、法律服务或社会服务机构。
- 不收集个人如厕记录、位置轨迹、健康隐私、未成年人信息、设施安防细节或实时人流数据。

## Source Signals

- CDC WASH: https://www.cdc.gov/healthywater/global/wash.html
- CDC Handwashing: https://www.cdc.gov/handwashing/
- ADA.gov Public Accommodations: https://www.ada.gov/topics/title-iii/
- OSHA Sanitation guidance: https://www.osha.gov/restrooms-sanitation

## 下一步

- 建立 `facility -> access window -> hygiene function -> dignity/safety impact -> task continuity` 变量表。
- 区分公共厕所、交通枢纽厕所、学校厕所、工作场所厕所、灾害临时厕所和无障碍/家庭厕所。
- 与 `water-sanitation-hygiene-continuity`、`housing-built-environment-stability`、`public-service-design-accessibility`、`transportation-access-mobility` 和 `emergency-preparedness-response` 建立边界。
