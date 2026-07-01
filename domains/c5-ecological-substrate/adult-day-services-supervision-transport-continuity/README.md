# Adult Day Services Supervision Transport Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/adult-day-services-supervision-transport-continuity` |
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


`adult-day-services-supervision-transport-continuity/` 研究 adult day services、日间照护、监督、活动、健康观察、餐食和往返交通如何影响失能、认知衰退、孤立或照护者过载场景中的主体持续性。

> 核心问题：长期照护不只发生在家庭或机构。日间服务可以把白天监督、活动、餐食、社交、照护者喘息和交通组织成中间层，防止主体被困在“独自在家”和“机构化”之间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能在部分失能、认知衰退或孤立状态中仍能参与社区
  -> 白天监督、活动、营养、交通和照护者喘息必须可连续
  -> adult day services 成为居家生活与机构照护之间的执行缓冲层
```

## 关注对象

- Adult day services、adult day health care、社会活动、监督、安全观察和日间结构。
- 往返交通、接送时间、活动参与、餐食、药物提醒边界和照护者工作时间。
- 痴呆、残障、老年脆弱、社交孤立和家庭照护过载场景。
- 与 `caregiving-long-term-care/`、`family-caregiver-respite-work-continuity/`、`home-delivered-meals-congregate-nutrition-services-continuity/` 的接口。

## Human Infra 模型链路

```text
成人日间服务基础设施
  -> 改变监督、活动、餐食、交通和照护者喘息变量
  -> 改变主体白天安全、社交参与和家庭照护负担状态
  -> 降低孤立、跌倒未发现、照护者退出和过早机构化风险
  -> 增加有效时间、关系参与和居家持续性
```

## 非目标

- 不推荐具体 adult day center、交通服务、项目质量或个人照护安排。
- 不判断资格、保险覆盖、Medicaid/HCBS、长期照护保险或费用责任。
- 不制定个人日间照护计划、活动计划、交通路线、药物提醒或安全监督方案。
- 不收集个人健康、认知、行为、照护者、住址、交通或支付资料。

## Source Signals

- Eldercare Locator: https://eldercare.acl.gov/
- ACL National Family Caregiver Support Program: https://acl.gov/programs/support-caregivers/national-family-caregiver-support-program
- Medicaid Home & Community Based Services: https://www.medicaid.gov/medicaid/home-community-based-services/index.html
- NIA Caregiving: https://www.nia.nih.gov/health/caregiving

## 下一步

- 建立 adult day services 变量表：监督时间、交通接续、活动参与、餐食、照护者喘息、服务中断和过早机构化风险。
- 整理 adult day、HCBS、respite 和 caregiver support 的 Source Cards。
