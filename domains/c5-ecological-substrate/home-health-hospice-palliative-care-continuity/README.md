# Home Health Hospice Palliative Care Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-health-hospice-palliative-care-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


居家医疗、缓和医疗、安宁疗护与临终连续性域研究：当主体处于严重疾病、功能下降、长期症状或生命末期时，医疗、照护、症状控制、家庭支持和主体目标如何被连续承接。

## 对象

- 居家医疗、家庭护理、缓和医疗、安宁疗护、严重疾病照护和临终支持。
- 症状负担、疼痛、呼吸困难、营养、用药、功能支持、护理设备和照护者压力。
- 目标照护、预立照护计划、转诊时机、家庭沟通、尊严、文化偏好和服务资格边界。
- 医院、家庭、长期照护机构、社区服务和急诊之间的切换。
- 严重疾病场景对有效寿命、可承受持续性、主观时间质量和未来选择权的影响。

## Human Infra 价值

主体持续性不是只追求更长日历寿命。严重疾病阶段的关键问题是：存在是否仍可感知、可承受、可被照护、可表达目标、可维持关系和尊严。

```text
严重疾病和居家照护可连续
  -> 症状、功能、照护者负担和转诊断点被承接
  -> 延长生命不脱离可承受性、尊严和主体目标
  -> 有效时间质量和可承受持续性提高
```

## 边界

本域只整理公开居家医疗、缓和医疗、安宁疗护、严重疾病照护和照护者支持资料。

不提供：

- 个体临床判断、安宁疗护资格、停治/转治、用药、镇痛、护理、设备或急症处理建议。
- 预立指示、监护、遗嘱、保险覆盖、福利资格、账单、机构选择或法律建议。
- 协助死亡、自杀、伤害自己或他人的建议。
- 把缓和医疗或安宁疗护写成放弃治疗、缩短生命或家庭责任转嫁。

## 上游与下游

- 上游：`pain-suffering-control/`、`caregiving-long-term-care/`、`healthcare-access-continuity/`、`medicine-access-treatment-continuity/`。
- 下游：`care-transitions-discharge-continuity/`、`functioning-quality-of-life-outcomes/`、`dementia-cognitive-decline-care-continuity/`、`elder-justice-adult-protective-services/`。

## 初始资料线索

- CMS Home Health Services: https://www.cms.gov/medicare/coverage/home-health-services
- CMS Hospice: https://www.cms.gov/medicare/coverage/hospice
- NIA Palliative Care and Hospice Care public materials。
- WHO Palliative Care public materials。

## 下一步

- 建立严重疾病连续性变量表：症状负担、照护强度、家庭支持、服务资格、转诊断点、急诊使用和目标一致性。
- 整理居家医疗、缓和医疗、安宁疗护和照护者支持 Source Cards。
- 明确与疼痛控制、长期照护、出院连续性和伦理安全边界的交叉。
