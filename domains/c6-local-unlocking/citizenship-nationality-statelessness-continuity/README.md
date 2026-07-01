# Citizenship Nationality Statelessness Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/citizenship-nationality-statelessness-continuity` |
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


本域研究公民身份、国籍、自然化、双重/多重国籍、国籍丧失风险和无国籍状态如何影响主体被国家承认、保护和接入权利的连续性。

> 核心问题：主体不仅需要身份文件，还需要一个可被国家和国际系统承认的成员资格；当国籍、自然化或无国籍状态断裂时，旅行、居留、工作、保护、投票、福利、继承和领事救助都会被连带影响。

## 关注对象

- 公民身份、国籍、自然化、出生公民权、血统国籍、国籍证明和领事保护。
- 无国籍、国籍争议、文件缺失、跨境家庭、儿童登记、国籍丧失和身份恢复。
- 国籍状态与护照、投票、公共福利、工作资格、教育、医疗、税务和人道保护的接口。
- 与 `legal-identity-civil-registration/` 的边界：法律身份域关注制度识别；本域关注国家成员资格和无国籍风险。

## Human Infra 链路

```text
公民身份 / 国籍连续性
  -> 主体被某个国家或国际保护框架承认为成员或受保护对象
  -> 旅行、居留、投票、领事保护、福利、家庭团聚和法律救济入口打开
  -> 无国籍、身份争议和跨境排除风险下降
  -> 主体获得跨生命周期和跨地域的制度承认底座
```

## 非目标

- 不提供个人公民身份、自然化、国籍保留、无国籍认定、护照、签证、税务或法律建议。
- 不判断个人是否具备某国国籍、公民权、双重国籍资格或无国籍状态。
- 不协助伪造、隐藏、规避、买卖、滥用或操控国籍、身份、护照、移民或投票文件。

## Source Signals

- USCIS Citizenship and Naturalization: https://www.uscis.gov/citizenship
- U.S. Department of State Nationality: https://travel.state.gov/content/travel/en/legal/travel-legal-considerations/us-citizenship.html
- UNHCR Statelessness: https://www.unhcr.org/statelessness

## 下一步

- 建立国籍连续性变量表：取得路径、证明文件、丧失风险、无国籍风险、儿童登记、跨境家庭和恢复机制。
- 整理 USCIS、State Department、UNHCR、UN Legal Identity Agenda 和 UNICEF birth registration Source Cards。
- 与 `passport-travel-document-mobility-continuity/` 明确分工：本域研究国家成员资格，护照域研究旅行证件和跨境移动资格。
