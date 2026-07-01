# Survivor Benefits Death Notification Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/survivor-benefits-death-notification-continuity` |
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


Survivor Benefits Death Notification Continuity 研究死亡通知、遗属福利、社保/退伍军人/雇主福利、养老金通知和停止/转移支付如何把死亡事件后的收入断点转化为可恢复资源链。

> 核心问题：死亡常常同时切断工资、照护、福利和家庭管理者；如果死亡通知和遗属福利链断裂，幸存者会在最脆弱窗口失去收入、医疗和住房稳定性。

## 研究对象

- Survivor benefits、death notification、Social Security survivor benefits、VA survivor benefits、employer benefits 和 pension notifications。
- 死亡报告、福利停止、遗属申请、超额支付、身份核验、受益人记录和跨机构通知。
- 配偶、子女、残障遗属、照护者、退伍军人家庭、低收入家庭和无数字接入人群。

## 先验链路

```text
死亡事件会让家庭收入、福利资格和照护责任发生突变
  -> 公共机构、雇主、养老金和福利系统需要被通知并重新判定遗属资格
  -> 通知失败、受益人资料错误或申请入口不可达会造成付款中断、超额支付或资源缺口
  -> 幸存者的住房、医疗、食物、照护和教育稳定性下降
  -> 家庭成员的未来选择权与行动能力被压缩
  -> 因而遗属福利和死亡通知链是死亡后资源连续性的核心接口
```

## 关键变量

- 死亡通知路径、遗属资格、申请时效、受益人记录、支付连续性和 overpayment 风险。
- SSA、VA、雇主、养老金、工会、公共福利和保险之间的通知边界。
- 儿童、残障遗属、移民家庭、无银行账户、无数字接入、语言可达和诈骗风险。

## 证据入口

- Social Security Administration survivor benefits and reporting death materials。
- USA.gov death of a loved one and benefit navigation materials。
- VA survivor benefits, employer benefit and pension public materials。

## 非目标

- 本域不判断遗属福利资格、金额、申请策略、期限、税务、移民或法律后果。
- 不代报死亡、不代填申请、不解释个人福利记录或处理 overpayment。
- 不收集 SSN、死亡证明、福利信、银行账户、家庭关系、军人记录或雇主资料。

## 上下游

- 上游：`death-certificate-registration-cause-of-death-record-continuity/`、`social-security-earnings-benefit-record-continuity/`、`retirement-pension-savings-plan-continuity/`。
- 下游：`bereavement-leave-grief-support-continuity/`、`life-insurance-beneficiary-claim-continuity/`、`estate-inventory-asset-liability-handoff-continuity/`。
