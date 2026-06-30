# Synthetic Data Generation Validation Continuity

`synthetic-data-generation-validation-continuity/` 研究合成数据生成、隐私风险、效用验证、分布保真、偏差扩散和下游评估，如何决定合成数据能否作为 Human Infra 的研究与 AI 训练材料。

> 核心问题：合成数据可以降低隐私和稀缺数据约束，也可能制造虚假规律、泄露原始样本或放大偏差。它不是天然安全数据。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要更多可用数据支持研究、评测、仿真和 AI 工具训练
  -> 真实数据常受隐私、稀缺、偏差、访问和伦理约束限制
  -> 合成数据可能缓解约束，但必须验证隐私、效用、分布和下游影响
  -> 因此合成数据生成与验证是数据稀缺到可审查数据资源的转换域
```

## 关注对象

- 合成数据生成方法、隐私攻击风险、相似性、成员推断、属性泄露、效用和公平性。
- 分布保真、边界案例、下游模型性能、误差传播、标注语义和 synthetic-to-real gap。
- 合成数据说明书、生成模型版本、原始数据来源、验证报告和禁止用途。
- 与 `privacy-preserving-computation/` 的关系：隐私计算域关注安全计算机制；本域关注合成数据作为产物是否可靠。
- 与 `ai-data-provenance-contamination-drift-continuity/` 的边界：数据谱系域关注全链路来源和漂移；本域关注合成数据生成与验证。

## Human Infra 模型链路

```text
合成数据生成与验证 T
  -> 改变数据可用性、隐私风险、分布保真、偏差和下游效用变量 X
  -> 改变模型训练、仿真、评测和研究验证的数据状态 S
  -> 改变隐私泄露、虚假规律、偏差扩散和模型失效风险 λ(t)
  -> 影响研究速度、AI 工具可靠性、主体隐私和未来选择权
```

## 非目标

- 不提供重新识别、成员推断攻击、隐私攻击、规避审查或用合成数据洗白敏感数据的方法。
- 不把合成数据写成自动匿名化、自动合规或自动无偏。
- 不使用合成数据输出个体医疗、法律、金融或寿命预测。

## Source Signals

- NIST Privacy Engineering and synthetic data resources: https://www.nist.gov/privacy-framework
- UK ICO anonymisation and synthetic data guidance: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- EU AI Act information portal: https://artificialintelligenceact.eu/
- Datasheets for Datasets: https://arxiv.org/abs/1803.09010

## 下一步

- 建立 Synthetic Data Card 字段：generator, source data boundary, privacy test, utility test, distribution check, downstream mismatch, forbidden use。
- 与 `privacy-preserving-computation/`、`ai-data-provenance-contamination-drift-continuity/` 和 `data-quality-missingness-representativeness/` 建立验证接口。
