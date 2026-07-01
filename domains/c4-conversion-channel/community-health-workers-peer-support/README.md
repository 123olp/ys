# Community Health Workers Peer Support

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/community-health-workers-peer-support` |
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


`community-health-workers-peer-support/` 研究社区健康工作者、同伴支持者、导航员和可信社区中介如何把医疗、公共卫生、社会服务和恢复支持连接到主体日常生活。

> 核心问题：服务存在不等于主体会信任、理解和持续使用；社区健康工作者与同伴支持把专业系统翻译为关系、陪伴、导航、反馈和低门槛支持。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须把医疗和社会服务嵌入日常生活
  -> 单靠机构入口、网页和临床建议不足以解决信任、语言、交通、文化、创伤和坚持问题
  -> 社区中介和同伴支持能降低服务导航成本并增强恢复关系
  -> 因此社区健康工作者与同伴支持是服务转化为实际行动的关系接口域
```

## 关注对象

- 社区健康工作者、peer support、patient navigator、promotoras、community link workers 和社会处方接口。
- 信任、文化/语言适配、健康教育、转介、随访、慢病支持、行为健康恢复和服务闭环。
- 培训、监督、边界、报酬、角色清晰度、数据隐私和非专业替代风险。
- 与 `community-resource-navigation/` 的边界：本域关注人际中介角色；资源导航域关注目录、筛查、转介和闭环系统。
- 与 `health-workforce-capacity/` 的边界：本域关注社区和同伴角色；健康劳动力容量域关注整体卫生人力系统。

## Human Infra 模型链路

```text
社区健康工作者与同伴支持 T
  -> 改变信任、语言适配、服务导航、持续陪伴、转介闭环和恢复支持变量 X
  -> 改变主体理解、进入、坚持和反馈医疗/社会服务的状态 S
  -> 改变服务脱落、慢病管理失败、复发、孤立、误解和恢复中断风险 λ(t)
  -> 影响健康寿命、行动能力、社会连接和未来选择权
```

## 非目标

- 不把社区健康工作者或同伴支持者写成医生、心理治疗师、急救人员、法律顾问或危机干预替代。
- 不提供诊断、治疗、用药、心理咨询、危机处理、个案转介或资格建议。
- 不支持无偿化、低薪化、过度任务转移、隐私越权或用社区关系替代制度责任。

## Source Signals

- WHO Community Health Workers guideline: https://www.who.int/publications/i/item/9789241550369
- CDC Community Health Workers: https://www.cdc.gov/community-health-workers/
- HRSA Community Health Worker Training Program: https://www.hrsa.gov/grants/find-funding/HRSA-22-124
- SAMHSA Peer Support Workers: https://www.samhsa.gov/brss-tacs/recovery-support-tools/peers
- CDC Health Equity: https://www.cdc.gov/health-equity/

## 下一步

- 建立社区中介变量表：信任、语言、文化适配、导航、随访、闭环、监督、培训、报酬和边界。
- 与 `healthcare-access-continuity/`、`community-resource-navigation/`、`mental-health-affective-stability/` 和 `social-connection-relational-infra/` 建立接口。
