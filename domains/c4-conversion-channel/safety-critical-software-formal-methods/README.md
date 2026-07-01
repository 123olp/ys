# Safety Critical Software Formal Methods

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/safety-critical-software-formal-methods` |
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


`safety-critical-software-formal-methods/` 研究安全关键软件、形式化方法、验证确认、运行时监控、故障隔离和高可靠系统工程，如何影响 Human Infra 的医疗、AI、交通、能源和生命支持系统可信度。

> 核心问题：Human Infra 越依赖 AI、设备、生命支持、自动化和关键基础设施，主体持续性越取决于软件是否能在高风险边界内被证明、测试、监控和安全退化。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体维护系统会越来越依赖软件、控制系统、AI 代理和自动化设备
  -> 高风险软件必须可规格化、可验证、可测试、可监控、可回滚和可失效安全
  -> 若软件错误进入生命支持、医疗设备或基础设施控制，工具增强会变成主体风险源
  -> 因此安全关键软件和形式化方法是高风险工具可信域
```

## 关注对象

- 形式化规格、模型检查、定理证明、静态分析、验证确认、运行时监控和安全壳。
- 医疗设备软件、生命支持控制、自动驾驶/交通、能源控制、AI 代理工具调用和关键服务自动化。
- 与 `model-cards-ai-audit-documentation/` 的边界：模型卡关注模型用途和限制；本域关注软件系统本身的规格、验证和失效安全。
- 与 `cybersecurity-resilience-critical-services/` 的边界：网络安全关注攻击和恢复；本域关注正确性、可靠性和安全关键行为。

## Human Infra 模型链路

```text
安全关键软件与形式化方法 T
  -> 改变规格清晰度、验证覆盖、状态空间审查、运行时监控、故障隔离和回滚变量 X
  -> 改变高风险软件系统的可信、可审计和失效安全状态 S
  -> 改变软件缺陷、自动化事故、生命支持失效和基础设施级联风险 λ(t)
  -> 影响医疗、AI、交通、能源、照护和主体持续性
```

## 非目标

- 不提供攻击、规避安全壳、绕过认证、关闭监控或篡改安全关键系统的方法。
- 不把形式化证明写成系统绝对安全。
- 不替代监管认证、独立验证确认、临床安全评估或工程审查。

## Source Signals

- NASA Formal Methods: https://shemesh.larc.nasa.gov/fm/
- NASA Formal Methods Symposium: https://shemesh.larc.nasa.gov/NFM2026/
- NIST Secure Software Development Framework: https://csrc.nist.gov/Projects/ssdf
- FDA Software as a Medical Device resources: https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd

## 下一步

- 建立安全关键软件变量表：规格、危险分析、验证方法、测试覆盖、运行时监控、故障模式、退化策略和认证状态。
- 与 `ai-agency-safety/`、`medical-device-equipment-safety-maintenance/`、`critical-infrastructure-lifeline-interdependency-resilience/` 和 `cybersecurity-resilience-critical-services/` 建立接口。
