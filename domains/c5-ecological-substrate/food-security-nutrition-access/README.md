# Food Security Nutrition Access

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/food-security-nutrition-access` |
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


`food-security-nutrition-access/` 研究食物是否稳定、可负担、安全、营养充分且可获得，从而支撑主体长期能量、健康、恢复和行动能力。

> 核心问题：营养代谢是身体内部过程，食物安全是外部供给条件；如果食物不可得、不可负担、不安全或质量不足，主体持续性会在进入身体之前被截断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要长期稳定的能量、蛋白、微量营养素和安全食物
  -> 食物系统必须可得、可负担、安全、营养充分且抗冲击
  -> 身体维护、认知表现、免疫、防病和恢复才有现实输入
```

## 关注对象

- 食物安全、饥饿、营养不足、食物负担、食物荒漠和食物系统冲击。
- 食品安全、供应稳定、粮价波动、收入冲击、灾害下食物连续性。
- 与营养代谢、供应链、公共福利、照护、儿童发展和灾害响应的接口。

## Human Infra 模型链路

```text
食物安全与营养可及
  -> 稳定、安全、可负担的食物进入生活系统
  -> 能量、营养材料、免疫和恢复输入不被中断
  -> 饥饿、营养不良、慢病风险、认知负担和家庭压力下降
  -> 健康寿命、有效时间和主体行动能力提高
```

## 非目标

- 不提供个体饮食处方、减重方案、补剂、疾病饮食、食品安全处置或医学建议。
- 不提供粮食囤积、黑市采购、非法获取、规避监管或恐慌性准备建议。
- 不把食物安全问题简化为个人选择，忽视收入、价格、供应链、社区和政策条件。

## Source Signals

- FAO SOFI: https://www.fao.org/publications/sofi
- World Bank Food Security: https://www.worldbank.org/en/topic/agriculture/brief/food-security-update
- WHO Healthy Diet: https://www.who.int/news-room/fact-sheets/detail/healthy-diet

## 下一步

- 建立食物安全变量表：可得性、可负担性、安全性、营养质量、供应稳定、价格冲击和家庭压力。
- 整理 FAO SOFI、World Bank food security、WHO diet、食品安全和食物援助资料卡片。
- 与 `nutrition-metabolic-health/` 明确分工：本域研究外部食物可及，后者研究进入身体后的代谢状态。
