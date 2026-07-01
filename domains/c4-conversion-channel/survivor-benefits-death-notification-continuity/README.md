# Survivor Benefits Death Notification Continuity

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
