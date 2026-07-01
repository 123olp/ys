# Surprise Billing Balance Bill Protection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/surprise-billing-balance-bill-protection-continuity` |
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

本域研究 No Surprises Act、balance billing、out-of-network emergency care、air ambulance、in-network facility 中的 out-of-network provider 和 cost-sharing limits 如何保护主体免受意外账单冲击。

它不是账单争议、法律维权、provider 选择或保险投诉工具。

## 先验问题

```text
不可预见医疗成本如何被限制？
  -> 急诊和特定非急诊场景中主体无法完全选择网络内 provider
  -> 法律保护必须限制 balance billing 和过高 cost-sharing
  -> 通知、consent、dispute 和 enforcement 机制必须可执行
  -> 否则不可控网络状态会转化为高额债务
```

## 研究对象

- No Surprises Act consumer protections、balance billing prohibition 和 cost-sharing limits。
- Emergency services、air ambulance、in-network facility / out-of-network provider 场景。
- Notice and consent、state law interface、complaint process 和 enforcement。

## 关键变量

- surprise bill 发生率、保护适用率、complaint 入口可达性。
- 网络状态可见性、notice/consent 清晰度、cost-sharing mismatch。
- out-of-network exposure、medical debt risk 和 patient administrative burden。

## 证据入口

- CMS No Surprises、Medical Bill Rights 和 consumer advocate toolkit。
- Federal NSA rules、state surprise billing protections 和 enforcement materials。
- KFF、Commonwealth Fund、Health Affairs surprise billing research。

## 非目标

- 不判断个人账单是否受 No Surprises Act 保护或是否合法。
- 不代写投诉、申诉、法律信、provider/payer dispute 或 collections response。
- 不提供 provider、facility、network、emergency choice、consent 策略或规避建议。

## 上下游

- 上游：`provider-directory-network-adequacy-continuity/`、`insurance-eligibility-benefits-verification-continuity/`。
- 下游：`patient-billing-payment-plan-continuity/`、`charity-care-financial-assistance-medical-debt-continuity/`。
