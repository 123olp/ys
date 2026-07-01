# Advance Care Planning Medical Decision Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/advance-care-planning-medical-decision-continuity` |
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


Advance Care Planning Medical Decision Continuity 关注预先医疗照护计划、advance directives、health care proxy、goals of care 和临床沟通如何在主体失能、意识障碍、重病或无法表达时保持医疗决策连续性。

## 对象

- 预先医疗照护计划、advance directives、living will、health care proxy 和医疗代理人。
- 主体价值、治疗目标、不可接受状态、沟通偏好、家庭照护者和临床团队之间的信息传递。
- 急性疾病、慢病恶化、意识障碍、痴呆、临终阶段和跨机构转移中的决策断点。

## Human Infra 价值

```text
主体持续性需要医疗决策保持可表达
-> 疾病或失能会让主体暂时或长期无法亲自说明偏好
-> 若缺少预先计划，医疗团队和家属只能在压力下猜测主体意愿
-> 预先医疗照护计划把价值、目标和代理人提前写入可传递结构
-> 医疗决策更可能沿着主体偏好、尊严和风险承受边界延续
```

## 边界

- 本域不提供个人医疗、法律、遗嘱、代理授权、急救、DNR/POLST/MOLST 填写或临床治疗建议。
- 不判断某个患者应接受、拒绝或中止任何治疗。
- 不替代医生、律师、医院伦理委员会、授权代理人、法院或当地法律要求。
- 只整理公开资料、制度结构、角色边界、沟通断点、证据和禁止用途。

## 上游与下游

- 上游：`patient-advocacy-shared-decision-making/`、`care-transitions-discharge-continuity/`、`disorders-of-consciousness-coma-recovery/`、`dementia-cognitive-decline-care-continuity/`。
- 下游：`home-health-hospice-palliative-care-continuity/`、`medical-interpreter-cultural-mediation/`、`health-data-privacy-governance/`、`governance-rights/`。

## 初始资料线索

- National Institute on Aging advance care planning and advance directives.
- National Institute on Aging getting your affairs in order.
- HHS and state-level patient rights / advance directive materials.
