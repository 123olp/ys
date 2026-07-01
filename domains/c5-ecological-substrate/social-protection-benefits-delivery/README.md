# Social Protection Benefits Delivery

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/social-protection-benefits-delivery` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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


`social-protection-benefits-delivery/` 研究公共福利、社会保护和服务递送能否在收入、食物、住房、医疗、能源、失业、残障和灾害冲击中接住主体。

> 核心问题：社会保护不是慈善附属品，而是把系统性风险从个体身上分摊出去的基础设施；如果资格、申请、续期、证明和申诉失败，名义权利无法转化为真实支持。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体会遭遇疾病、失业、残障、照护、贫困、灾害和家庭冲击
  -> 社会保护必须可理解、可申请、可续期、可申诉且及时支付
  -> 风险冲击才不会把健康、住房、食物、能源、教育和未来选择权一并击穿
```

## 关注对象

- 社会保护、公共福利、现金/食物/住房/能源/医疗支持、资格、申请、续期、申诉和行政负担。
- 服务递送、数字公共服务、人工帮助、排除错误、等待时间、证明负担和福利悬崖。
- 与法律身份、健康素养、财务韧性、食物安全、住房、能源和灾害恢复的接口。

## Human Infra 模型链路

```text
社会保护与福利递送
  -> 风险冲击被公共制度分摊和缓冲
  -> 资格、申请、续期、支付、申诉和人工帮助形成可用路径
  -> 食物、住房、医疗、能源、照护和收入断裂概率下降
  -> 主体持续性和未来选择权获得制度性缓冲
```

## 非目标

- 不提供个体福利申请、资格判断、材料准备、申诉、法律、税务、移民或财务建议。
- 不提供规避制度、虚假材料、欺诈、身份冒用或套利方法。
- 不把社会保护写成替代劳动权利、医疗可及、住房政策或照护系统的单一方案。

## Source Signals

- ILO Social Protection Platform: https://www.social-protection.org/
- World Bank Social Protection: https://www.worldbank.org/en/topic/socialprotection
- USA.gov Benefit Finder: https://www.usa.gov/benefit-finder

## 下一步

- 建立福利递送变量表：资格、申请、证明、续期、等待、支付、申诉、数字可达、人工帮助和行政负担。
- 整理 ILO、World Bank、USA.gov Benefit Finder、行政负担和服务设计 Source Cards。
- 与 `financial-resilience-access/` 明确分工：本域研究公共制度缓冲，后者研究个体/家庭财务韧性。
