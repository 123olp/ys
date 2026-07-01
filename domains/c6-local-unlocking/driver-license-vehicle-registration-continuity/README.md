# 驾照、车辆登记与个人移动资格连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/driver-license-vehicle-registration-continuity` |
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


本域研究驾驶资格、车辆登记、车牌、title、保险证明和 REAL ID 等移动凭证如何支撑主体跨地点行动。它关注的是移动资格和车辆记录的制度连续性，而不是驾驶、车辆购买、维修、保险或 DMV 办理建议。

## 研究对象

- 驾驶证、州 ID、REAL ID、车辆 title、车辆登记、车牌和地址同步。
- 驾驶资格、暂停/吊销、医学限制、保险证明、车辆检查和排放要求。
- 车辆记录与工作、医疗、照护、教育、灾害撤离、投票和身份核验的关系。
- 车辆召回、事故记录、欠费、罚单和跨州迁移造成的移动资格断点。

## 价值链路

```text
主体需要跨地点到达资源和任务现场
  -> 驾照、车辆登记和移动凭证把个人行动权、车辆资产和道路系统连接起来
  -> 地址同步、title、保险、检查和资格状态决定车辆能否合法持续使用
  -> 记录错误、吊销、跨州迁移、费用负担或车辆记录断裂会压缩行动半径
  -> 移动资格连续性把交通能力从物理可行转化为制度可承认的行动能力
```

## 关键问题

- 驾驶资格和车辆记录如何影响工作、医疗、照护、教育、家庭和应急撤离？
- 车辆 title、登记、保险证明、地址和姓名变更之间有哪些同步断点？
- 移动凭证丢失、吊销、跨州迁移或费用负担如何改变主体机会空间？
- 驾驶资格如何与道路安全、残障便利、老龄化、医学条件和公共交通替代方案互动？

## 上游与下游

- 上游：`transportation-access-mobility/`、`road-traffic-injury-prevention-safe-mobility/`、`digital-identity-security/`、`address-residency-mail-service-continuity/`。
- 下游：`workforce-employment-services/`、`healthcare-access-continuity/`、`disaster-recovery-relief-continuity/`、`road-traffic-injury-prevention-safe-mobility/`、`product-safety-recall-systems/`。

## 非目标

- 不提供 DMV 办理、驾驶、路线、车辆购买、车辆维修、保险、事故责任、罚单、吊销恢复、REAL ID 或法律建议。
- 不判断个人是否可以驾驶、是否需要报备疾病、是否应买车、是否可跨州登记或是否可逃避罚单。
- 不协助伪造证件、规避身份核验、规避吊销、规避保险、规避检查、危险驾驶或跟踪车辆。

## 初始资料入口

- USA.gov: Driver's licenses and vehicle registration
- Department of Homeland Security: REAL ID
- State DMV / motor vehicle agency official materials
- NHTSA: Vehicle recalls and safety data
- AAMVA official standards and reference materials
