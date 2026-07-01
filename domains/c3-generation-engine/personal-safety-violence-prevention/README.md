# Personal Safety Violence Prevention

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/personal-safety-violence-prevention` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`personal-safety-violence-prevention/` 研究人身安全、暴力预防、受害者支持和创伤后服务能否防止主体被伤害、胁迫、孤立和长期失能。

> 核心问题：暴力和胁迫会直接截断主体持续性，也会通过恐惧、创伤、资源损失和关系控制长期侵蚀行动能力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能暴露于亲密伴侣暴力、性暴力、跟踪、社区暴力、犯罪伤害和胁迫控制
  -> 预防、求助入口、受害者服务、法律保护、医疗创伤支持和安全转介必须可达
  -> 人身伤害和控制关系才不会把主体的生命、尊严、资源和未来选择权击穿
```

## 关注对象

- 亲密伴侣暴力、性暴力、跟踪、儿童/老年/残障虐待、社区暴力、犯罪伤害和胁迫控制。
- 暴力预防、风险识别、求助入口、热线/转介、受害者服务、保护令、补偿、创伤支持和恢复路径。
- 安全、隐私、保密、数字滥用、语言可达、残障可达和服务连续性。
- 与司法可及、住房、医疗、心理健康、数字身份安全、社会连接和应急响应的接口。

## Human Infra 模型链路

```text
人身安全与暴力预防
  -> 暴力暴露、胁迫控制和犯罪伤害被预防、识别和转介
  -> 医疗、心理、法律、住房、经济和受害者服务形成支持链
  -> 死亡、伤害、创伤、资源剥夺和行动控制风险下降
  -> 主体持续性获得安全、尊严和恢复层的支撑
```

## 非目标

- 不提供自卫战术、武器、报复、跟踪、监控、定位、骚扰、逃避执法或危险对抗建议。
- 不替代热线、警方、医疗、受害者服务、法律援助、庇护所或专业安全规划。
- 不输出可让施害者扩大控制、定位受害者、绕过安全措施或破坏求助路径的信息。

## Source Signals

- CDC Violence Prevention: https://www.cdc.gov/violence-prevention/
- DOJ Office for Victims of Crime: https://ovc.ojp.gov/
- DOJ Office on Violence Against Women: https://www.justice.gov/ovw
- VictimConnect Resource Center: https://victimconnect.org/

## 下一步

- 建立人身安全变量表：暴力类型、求助入口、隐私、转介、医疗创伤支持、法律保护、住房安全和恢复连续性。
- 整理 CDC、OVC、OVW、VictimConnect、WHO 暴力预防和家庭暴力服务 Source Cards。
- 与 `risk-engineering/` 明确分工：本域研究人与人之间的伤害、胁迫和受害者支持，风险工程研究更上位的风险模型。
