# Administrative Burden Procedural Friction

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/administrative-burden-procedural-friction` |
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


`administrative-burden-procedural-friction/` 研究申请、证明、等待、续期、申诉、表单、账户、资格和合规流程如何消耗主体时间、注意力、执行功能和资源。

> 核心问题：权利、服务和资源存在不等于主体能够获得；学习成本、心理成本和合规成本会把制度支持变成有效时间损耗、申请放弃、服务断线和未来选择权收缩。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须把制度资源转化为真实支持
  -> 转化过程依赖理解规则、提交证明、等待审核、维护资格和处理错误
  -> 行政负担会消耗注意力、时间、执行功能、交通、费用和心理承受力
  -> 因此行政负担与程序摩擦是资源能否抵达主体的中间变量域
```

## 关注对象

- 学习成本、心理成本、合规成本、证明负担、等待、续期、申诉、表单复杂度和状态反馈。
- 福利、医疗、住房、灾后救济、法律援助、移民、教育、税务和就业服务中的跨域程序摩擦。
- 行政负担如何作用于时间贫困、健康恶化、服务放弃、错误惩罚和制度不信任。
- 与 `public-service-design-accessibility/` 的边界：本域关注负担机制；公共服务设计域关注入口和流程如何设计。
- 与 `time-allocation-effective-time/` 的边界：本域是制度程序摩擦的专门层；时间域处理更广泛时间分配。

## Human Infra 模型链路

```text
行政负担 T
  -> 改变学习成本、证明成本、等待成本、心理成本、合规成本和错误恢复变量 X
  -> 改变主体完成制度任务、保持资格和获得资源的状态 S
  -> 改变申请放弃、资格断线、服务延误、时间贫困、心理耗竭和资源不可达风险 λ(t)
  -> 影响有效时间、资源可及、恢复能力和未来选择权
```

## 非目标

- 不提供个体申请、规避审核、虚假证明、福利策略、法律意见、税务建议或案件处理指导。
- 不把行政负担研究用于提高拒付率、筛除脆弱人群、增加门槛或优化排除。
- 不把效率压缩写成取消申诉、人工帮助、语言可达、隐私和正当程序的理由。

## Source Signals

- Moynihan, Herd, Harvey administrative burden article: https://doi.org/10.1111/puar.12375
- Performance.gov Customer Experience: https://www.performance.gov/cx/
- Digital.gov: https://digital.gov/
- OMB Customer Experience resources: https://www.whitehouse.gov/omb/management/ofcio/customer-experience/
- PlainLanguage.gov: https://www.plainlanguage.gov/

## 下一步

- 建立行政负担变量表：学习、心理、合规、证明、等待、续期、申诉、错误恢复和人工帮助。
- 与 `social-protection-benefits-delivery/`、`public-service-design-accessibility/`、`access-to-justice-legal-aid/` 和 `time-allocation-effective-time/` 建立接口。
