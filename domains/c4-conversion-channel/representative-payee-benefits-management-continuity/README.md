# Representative Payee Benefits Management Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/representative-payee-benefits-management-continuity` |
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


Representative Payee Benefits Management Continuity 关注 Social Security representative payee、VA fiduciary、公共福利代收代管、记录责任和防滥用机制如何在主体无法管理福利时保持收入和基本生活连续性。

## 对象

- Representative payee、VA fiduciary、benefits management、收入支付、账单、住房、食物、医疗和照护费用。
- 主体无法管理福利、认知下降、严重疾病、儿童、残障、无家可归或机构照护中的收入断点。
- 报告义务、资金用途、记录保存、滥用、监督、变更代理和受益人保护。

## Human Infra 价值

```text
主体持续性需要公共收入在能力下降时仍用于主体本身
-> 福利支付常常承担住房、食物、药物和照护的底线输入
-> 若主体无法管理资金，收入可能被浪费、挪用、断供或被他人控制
-> 代表收款人和受托项目把代管、用途限制、报告和监督纳入制度
-> 福利更可能稳定转化为主体基本生活和照护连续性
```

## 边界

- 本域不提供福利申请、代表收款人申请、资格判断、支付金额、申诉、账户设置、资金使用或个案举报建议。
- 不判断某人是否需要代表收款人、某代理是否合格或某支出是否合规。
- 不替代 SSA、VA、福利机构、律师、保护服务、法院或个案管理人员。
- 只整理公开资料、角色义务、监督结构、风险边界和禁止用途。

## 上游与下游

- 上游：`social-protection-benefits-delivery/`、`financial-inclusion-payment-systems/`、`disability-services-independent-living/`、`homelessness-unsheltered-health-continuity/`。
- 下游：`financial-fiduciary-power-of-attorney-continuity/`、`elder-justice-adult-protective-services/`、`community-resource-navigation/`。

## 初始资料线索

- Social Security Administration Representative Payee Program.
- Social Security Administration Advance Designation.
- VA Fiduciary Program public materials.
