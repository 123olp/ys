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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
