# Intellectual Property Technology Transfer Access

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/intellectual-property-technology-transfer-access` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
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


## 定位

本域研究知识产权、专利、许可、技术转移、大学和公共研究成果商业化、药物和医疗技术可及性，如何决定未来技术是否真的能被主体使用，而不是停留在论文、专利、公司资产或少数人可及的产品中。

Human Infra 关注未来技术窗口，但技术成熟并不等于主体可及。专利池、独占许可、生产权、定价、地域授权、监管数据、商业秘密和公共资助条款都会影响新技术能否进入人的生命路径。本域是“技术产生”到“技术可及”的制度转换层。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 未来技术必须从实验室进入可获得、可负担、可持续的实际服务
  -> 知识产权、许可、技术转移和市场准入会决定技术扩散路径
  -> 需要审查技术所有权、转化机制和可及性边界
  -> intellectual-property-technology-transfer-access
```

## 关注对象

- 专利、许可、商业秘密、数据权利、公共资助成果和技术转移机制。
- 大学、政府实验室、公司、基金会和公共机构之间的成果转化路径。
- Bayh-Dole、march-in rights、全球健康可及性、药品和医疗技术扩散。
- 独占授权、平台锁定、价格、生产能力、供应链、地域差异和公平可及性。
- Human Infra 中未来技术的“是否存在”与“主体是否能用上”的差异。

## Human Infra 模型链路

```text
科研发现和技术原型
  -> 知识产权、许可和技术转移安排
  -> 决定生产、定价、地域扩散、服务交付和可及性
  -> 影响主体采用概率、未来选择权和技术窗口真实价值
  -> 把技术成熟度转化为主体可获得性的治理问题
```

## 非目标

- 不提供法律意见、专利申请策略、规避侵权、绕开许可、商业秘密获取或谈判指导。
- 不判断具体专利有效性、侵权风险、自由实施空间或商业估值。
- 不把知识产权简单写成创新之敌或创新保证；只审查它如何影响主体可及性。
- 不替代 `medicine-access-treatment-continuity/`；本域关注技术扩散制度，药品日常可及由药品连续性域负责。

## Source Signals

- WIPO Technology Transfer: https://www.wipo.int/technology-transfer/en/
- NIH Technology Transfer: https://www.techtransfer.nih.gov/
- NIST Bayh-Dole: https://www.nist.gov/tpo/bayh-dole
- AUTM: https://autm.net/
- WHO intellectual property and public health: https://www.who.int/health-topics/medicines/intellectual-property
- WHO Global Strategy and Plan of Action on Public Health, Innovation and Intellectual Property: https://www.who.int/publications/i/item/9789241503117

## 下一步

- 建立 Technology Access Card：technology、owner、public funding、license model、manufacturing path、price/access risk、geographic constraints、equity concern。
- 与 `clinical-trials-regulatory-science-translation/` 对接，区分临床证据成熟、监管许可和实际可及。
- 与 `research-portfolio-prioritization-funding-governance/` 对接，把可及性作为研究组合优先级变量。
