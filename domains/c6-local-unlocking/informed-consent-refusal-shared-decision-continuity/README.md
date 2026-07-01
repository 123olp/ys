# Informed Consent Refusal Shared Decision Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/informed-consent-refusal-shared-decision-continuity` |
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


## 定位

本域研究 informed consent、refusal、shared decision-making、goals of care、risk/benefit communication 和 decision documentation 如何影响主体能否在医疗遭遇中持续表达选择。

它不是同意书填写、治疗选择、DNR/POLST、法律意见、医疗建议或风险承诺工具。

## 先验问题

```text
医疗行动何以代表主体选择？
  -> 主体必须获得可理解、充分、非胁迫的信息
  -> 选择、拒绝、替代方案和风险必须被记录和尊重
  -> 决策过程必须能适配语言、认知、残障和代理情境
  -> 否则治疗会从主体行动变成制度替主体行动
```

## 研究对象

- Informed consent、informed refusal、shared decision-making、decision aids。
- Risk/benefit communication、treatment alternatives、goals of care、decision documentation。
- Capacity、support person、surrogate boundary、语言理解、健康素养和非胁迫条件。

## 关键变量

- 理解度、风险沟通质量、decision aid 可用性、选择记录完整度。
- 拒绝权、替代方案说明、非胁迫性、文化语言适配和代理边界。
- 紧急例外、重复同意、电子同意和失能/能力波动场景。

## 证据入口

- AHRQ SHARE approach 和 shared decision-making 资料。
- HHS CLAS、health literacy、患者权利和 informed consent 研究。
- 医疗伦理、decision aids、risk communication 和 consent quality 文献。

## 非目标

- 不推荐治疗、检查、手术、药物、拒绝、同意、DNR/POLST/MOLST 或替代方案。
- 不代写同意书、拒绝书、advance directive、medical power of attorney 或法律文件。
- 不判断 capacity、coercion、medical necessity、standard of care 或个案风险。

## 上下游

- 上游：`health-literacy-navigation/`、`language-access-plain-communication/`。
- 下游：`advance-care-planning-medical-decision-continuity/`、`supported-decision-making-guardianship-rights/`。
