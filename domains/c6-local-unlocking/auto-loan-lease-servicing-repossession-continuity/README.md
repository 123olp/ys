# 车贷、租赁、服务与收车连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/auto-loan-lease-servicing-repossession-continuity` |
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


本域研究车贷、汽车租赁、经销商融资、APR、附加产品、贷款服务、付款、逾期、收车和留置权如何影响主体通勤、工作、照护、医疗和日常移动能力。它关注车辆融资如何把移动资格转化为长期偿付义务，而不是购车推荐、贷款谈判、收车规避或法律建议。

## 研究对象

- 车贷、汽车租赁、经销商融资、银行/信用社/金融公司放款和线上汽车融资。
- APR、首付、期限、月供、附加产品、服务合同、GAP、保险、标题留置权和费用。
- 账单、自动扣款、服务商转移、逾期、违约、收车、拍卖差额和信用报告。
- 与车辆登记、保险、维修、通勤、债务催收和信用报告的边界。

## 价值链路

```text
主体通过车贷或租赁获得车辆移动能力
  -> 融资条款、附加费用和服务关系把移动入口绑定到未来付款
  -> 准确披露、稳定服务和可追踪付款维持通勤、工作和照护连续性
  -> 逾期、收车、差额债务或留置权错误会直接切断日常行动链
  -> 车贷连续性把车辆移动从资产问题转化为跨期服务和债务问题
```

## 关键问题

- APR、期限、附加产品和车辆价值如何影响真实拥有成本？
- 车贷服务错误、自动扣款失败和服务商转移如何触发移动中断？
- 收车、拍卖差额和信用报告如何形成二级债务风险？
- 车贷与车辆登记、保险、维修和通勤连续性如何相互影响？

## 上游与下游

- 上游：`driver-license-vehicle-registration-continuity/`、`transportation-access-mobility/`、`credit-consumer-reporting-access-continuity/`。
- 下游：`debt-obligation-collection-relief-continuity/`、`vehicle-maintenance-repair-continuity/`、`commute-work-location-continuity/`、`insurance-coverage-claims-continuity/`。

## 非目标

- 不提供购车、租车、贷款、再融资、保险、维修、收车应对、债务谈判或法律建议。
- 不判断某辆车、贷款、租赁、经销商、附加产品或收车行动是否适合个人。
- 不协助虚假贷款申请、收入造假、里程/车况欺诈、隐藏车辆、规避收车、逃债、洗钱、产权欺诈或伪造文件。

## 初始资料入口

- CFPB: Auto loans consumer tools
- FTC: Buying new or used cars consumer materials
- CFPB and FTC auto finance / add-on product materials
- State DMV and attorney general consumer auto finance materials
