# Ambulatory Procedure Surgery Center Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/ambulatory-procedure-surgery-center-continuity` |
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

本域研究 ambulatory surgery center、门诊内镜、输注、透析外的门诊操作、术前准备、陪同/接送、麻醉风险筛查、感染控制、恢复观察和 follow-up 如何决定低住院化治疗能否安全发生。

它不是手术建议、术前准备指导、麻醉评估或机构推荐入口。

## 先验问题

```text
门诊操作何以成为安全修复通道？
  -> 操作地点和团队必须可用
  -> 准备、陪同、交通、麻醉筛查和感染控制必须闭合
  -> 操作后恢复和并发症回路必须存在
  -> 否则低住院化会把风险转移给家庭和主体
```

## 研究对象

- Ambulatory surgery center、outpatient procedure、endoscopy、infusion center 和 minor procedure clinic。
- Scheduling、pre-op clearance、patient instructions、escort/transport、NPO、medication hold 和 consent workflow。
- 麻醉支持、感染控制、设备可用、转院协议、恢复观察和 post-procedure follow-up。
- 取消、延期、无陪同、准备失败、授权失败和并发症回路。

## 关键变量

- 预约到操作时间、取消率、准备失败率、无陪同取消率和授权失败率。
- 术后电话/门户 follow-up、非计划急诊/住院、感染事件和转院事件。
- 语言/无障碍支持、交通约束、照护者可用性和说明理解。

## 证据入口

- CMS Ambulatory Surgical Center Quality Reporting、Medicare ASC coverage 和 infection control 资料。
- CDC outpatient settings infection prevention、AHRQ patient safety 和 perioperative safety 资料。
- Joint Commission / AAAHC / ASCA 等门诊操作安全资料。

## 非目标

- 不推荐操作、机构、麻醉、检查、输注、内镜、手术或术前术后处理。
- 不提供 NPO、用药暂停、陪同安排、并发症判断、感染处置或加急建议。
- 不收集病历、操作单、麻醉资料、保险、预约、交通、照护者或健康资料。

## 上下游

- 上游：`appointment-availability-wait-time-continuity/`、`specialist-referral-authorization-navigation-continuity/`、`surgical-anesthesia-perioperative-safety/`。
- 下游：`care-transitions-discharge-continuity/`、`home-health-hospice-palliative-care-continuity/`、`patient-safety-organizational-learning/`。
