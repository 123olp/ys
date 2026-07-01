# Provider Directory Network Adequacy Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/provider-directory-network-adequacy-continuity` |
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

本域研究 provider directory、网络充足性、network tier、可接诊状态、地理距离、语言/无障碍信息和保险网络如何决定主体能否找到真实可用的医疗服务入口。

它不是医生推荐、保险计划选择、个案转诊或申诉策略入口。

## 先验问题

```text
"有医疗覆盖"何以成为真实照护入口？
  -> 网络内 provider 必须可被发现
  -> 名录必须准确、可接诊、可预约
  -> 距离、语言、无障碍和接受新患者状态必须可信
  -> 否则覆盖只存在于目录里，不进入主体行动
```

## 研究对象

- Provider directory、Care Compare、plan directory 和 network adequacy。
- 接受新患者、网络内外、专业类型、服务地点和营业时间。
- 地理距离、交通可达、语言服务、无障碍和远程服务可用性。
- 目录错误、ghost network、网络窄化、provider 退出和更新延迟。

## 关键变量

- 目录准确率、可接诊率、电话成功率和预约转化率。
- 网络内 provider 距离、专科覆盖、语言/无障碍覆盖和新患者可接收比例。
- 名录更新延迟、错误率、拒收率、网络外账单暴露和资格错配。

## 证据入口

- CMS network adequacy、provider directory、Medicare Care Compare 和 plan compare 资料。
- Medicaid managed care 网络充足性、州保险监管和 provider directory 标准。
- AHRQ、KFF、NASEM 和卫生服务可及性研究。

## 非目标

- 不推荐医生、医院、保险计划、network tier 或转诊路径。
- 不提供申诉、network exception、账单争议、保险策略或法律建议。
- 不收集保险 ID、诊断、provider 联系记录、预约记录或个案健康资料。

## 上下游

- 上游：`healthcare-access-continuity/`、`insurance-risk-transfer/`、`digital-identity-security/`。
- 下游：`primary-care-panel-appointment-access-continuity/`、`specialist-referral-authorization-navigation-continuity/`、`appointment-availability-wait-time-continuity/`。
