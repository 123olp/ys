# Children Youth Special Health Care Needs Care Coordination Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/children-youth-special-health-care-needs-care-coordination-continuity` |
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


儿童与青少年特殊健康照护需求协调连续性，关注 CYSHCN、medical home、专科协作、护理计划、家庭照护负担、学校接口、保险授权、DME/药品供应和青年转衔如何影响长期主体持续性。

## 对象

- Children and youth with special health care needs
- Pediatric medical home and care coordination
- Specialty referral and shared care plan
- Family caregiver workload and respite interface
- School, IEP/504 and chronic condition supports
- Insurance, prior authorization, DME and medication access
- Transition to adult care boundary

## Human Infra 价值

特殊健康照护需求儿童的持续性不只取决于某项治疗，而取决于儿科、专科、学校、保险、设备、药品、家庭照护和成人转衔能否共享一个可执行护理网络。该域把复杂儿童照护建模为跨机构任务系统，而不是把负担默认交给家庭记忆和临时协调。

## 边界

- 不提供诊断、治疗、药物、设备、保险授权策略、IEP/504 建议、护理计划、转院转科、急诊或个体医疗/教育/法律建议。
- 不判断某儿童是否属于 CYSHCN、是否残障、是否需要 DME、是否有资格获得 Medicaid/SSI/IDEA 或某项学校支持。
- 不替代儿科、专科、护理协调员、学校、早期干预、社工、保险、DME 供应商、法律服务或紧急服务。

## 上游与下游

- 上游：`well-child-visit-preventive-care-continuity/`、`developmental-behavioral-screening-referral-continuity/`、`health-insurance-enrollment-renewal-continuity/`。
- 下游：`school-health-services-chronic-condition-continuity/`、`special-education-iep-504-accommodation-continuity/`、`transition-age-youth-mental-health-service-continuity/`。

## 初始资料线索

- HRSA / MCHB children and youth with special health care needs materials.
- AAP medical home and care coordination materials.
- CMS / Medicaid EPSDT and pediatric care coordination materials.
