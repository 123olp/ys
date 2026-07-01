# Medical Service Prior Authorization Utilization Management Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medical-service-prior-authorization-utilization-management-continuity` |
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

本域研究非处方药医疗服务的 prior authorization、utilization management、medical necessity、coverage criteria、peer review 和授权续期如何影响检查、影像、手术、设备和治疗是否能执行。

它不是授权申请、医学必要性论证、申诉材料或规避保险管理规则的工具。

## 先验问题

```text
医学方案执行何以成立？
  -> 服务必须被 payer 认定为可覆盖或需授权
  -> 授权标准、资料、时限和责任方必须清楚
  -> 拒绝、补件、续期和修改必须可追踪
  -> 否则医学方案会在 utilization management 层被延迟或截断
```

## 研究对象

- Prior authorization、precertification、medical necessity review、utilization management。
- Imaging、procedure、surgery、DME、home health、therapy、specialty service 等非药品服务。
- Peer-to-peer review、denial、appeal、expedited review、reauthorization 和 administrative burden。

## 关键变量

- 授权需求率、授权通过率、等待时间、补件率和拒绝率。
- 服务延迟、取消率、改道率、clinician burden 和患者 administrative burden。
- 自动化授权、电子 prior authorization、标准化 criteria 和可追踪性。

## 证据入口

- CMS Interoperability and Prior Authorization Final Rule 资料。
- AMA、AHA、CAQH、KFF、Health Affairs 等 utilization management 研究。
- Medicare Advantage prior authorization 和 utilization management 公开资料。

## 非目标

- 不代写 prior authorization、medical necessity、peer-to-peer、appeal 或 clinical letter。
- 不提供诊断、检查、手术、治疗、编码、billing code、规避 payer criteria 或加急策略。
- 不收集病历、诊断、影像、处方、保险、授权号或医生资料。

## 上下游

- 上游：`insurance-eligibility-benefits-verification-continuity/`、`specialist-referral-authorization-navigation-continuity/`。
- 下游：`claims-adjudication-eob-denial-continuity/`、`ambulatory-procedure-surgery-center-continuity/`。
