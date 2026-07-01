# Caregiving Long Term Care

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/caregiving-long-term-care` |
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


`caregiving-long-term-care/` 研究当主体出现失能、慢病、认知衰退或生活支持需求时，照护和长期照护系统能否持续接住主体。

> 核心问题：主体不只是需要治疗，还需要在长期生活中被照护、协作、替代和恢复；照护系统断裂会把可活时间变成不可行动、不可恢复或不可尊严存在的时间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能经历疾病、失能、脆弱、认知退行和长期依赖
  -> 家庭、社区、机构和专业照护必须可持续
  -> 长寿才不会退化为无人照护、照护者崩溃或主体尊严丧失
```

## 关注对象

- 家庭照护、长期照护、居家和社区支持、机构照护、照护协调和照护者负担。
- ADL/IADL、失能、认知障碍、慢病管理、临终前照护和照护转移。
- 照护资源不足、照护者倦怠、经济压力、照护中断和虐待/忽视风险。
- 与康复、社会连接、医疗连续性、公共福利和住房环境的接口。

## Human Infra 模型链路

```text
照护与长期照护
  -> 失能、慢病、脆弱和认知退行被日常支持系统接住
  -> 生活活动、用药、就医、营养、卫生、沟通和安全不被中断
  -> 有效时间、尊严、恢复机会和社会参与被保留
  -> 主体持续性从单纯生存转化为可行动、可感知、可被支持的存在
```

## 非目标

- 不制定个体照护计划、护理操作、医学处理、用药或安全处置。
- 不提供保险、福利、长期照护机构、法律监护或财务规划建议。
- 不把照护技术写成替代关系、同意、尊严和专业服务的万能方案。

## Source Signals

- NIA Caregiving: https://www.nia.nih.gov/health/caregiving
- NIA Long-Term Care: https://www.nia.nih.gov/health/caregiving/long-term-care
- WHO Ageing and Health: https://www.who.int/news-room/fact-sheets/detail/ageing-and-health

## 下一步

- 建立照护连续性变量表：照护强度、照护者负担、ADL/IADL、服务可及、转移风险和照护质量。
- 整理长期照护、家庭照护、居家社区服务和照护者健康的 Source Cards。
- 明确与 `social-connection-relational-infra/`、`rehabilitation-functioning/` 和 `housing-built-environment-stability/` 的交叉边界。
