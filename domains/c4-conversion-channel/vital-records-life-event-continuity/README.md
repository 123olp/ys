# 生命事件与核心民事记录连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/vital-records-life-event-continuity` |
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


本域研究出生、死亡、婚姻、离婚等生命事件记录如何把家庭事实、身份事实和制度事实连接起来。它关注的是主体和家庭在跨机构、跨地区、跨时间的服务系统中能否被持续识别，而不是个体证件办理建议。

## 研究对象

- 出生、死亡、婚姻、离婚等 vital records。
- 认证副本、记录更正、延迟登记、跨辖区记录请求。
- 生命统计、民事登记、亲属关系和身份锚点。
- 生命事件记录与护照、学校、医疗、保险、税务、福利、继承和家庭服务的下游关系。

## 价值链路

```text
主体和家庭关系需要被制度持续识别
  -> 出生、死亡、婚姻、离婚等生命事件生成核心民事记录
  -> 这些记录被福利、学校、税务、保险、护照、继承和医疗系统复用
  -> 记录缺失、错误、不可访问或跨辖区断裂会让主体失去服务入口
  -> 生命事件记录连续性把家庭事实转化为可被制度承认的长期身份底座
```

## 关键问题

- 哪些生命事件记录是主体进入制度系统的底层锚点？
- 记录错误、姓名不一致、亲属关系缺失或无法取得认证副本时，会影响哪些下游服务？
- 生命事件记录如何与法律身份、家庭关系、福利资格、学校记录、医疗记录和遗产交接互相依赖？
- 生命统计和民事登记如何从个体记录扩展为公共健康、人口统计和资源分配基础设施？

## 上游与下游

- 上游：`legal-identity-civil-registration/`、`child-protection-family-safety/`、`maternal-newborn-child-development/`、`trust-estate-affairs-succession-continuity/`。
- 下游：`name-change-identity-record-synchronization-continuity/`、`household-composition-dependent-eligibility-continuity/`、`family-law-custody-child-support-continuity/`、`healthcare-access-continuity/`、`social-protection-benefits-delivery/`。

## 非目标

- 不提供个人出生证、死亡证、婚姻证、离婚记录申请、更正、认证、翻译、认证副本或跨州跨国文件办理建议。
- 不判断个人亲属关系、婚姻状态、继承资格、移民身份、福利资格、税务身份或法律权利。
- 不协助伪造、规避、隐藏、篡改、借用或滥用身份文件和民事记录。

## 初始资料入口

- USA.gov: Vital Records
- CDC/NCHS: Where to Write for Vital Records
- CDC/NCHS: National Vital Statistics System
- State, county, and local vital records offices
