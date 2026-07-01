# Patient Grievance Complaint Ombuds Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/patient-grievance-complaint-ombuds-continuity` |
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


## 定位

本域研究 patient grievance、complaint、ombudsman、state survey agency、quality complaint、civil rights complaint 和 feedback loop 如何影响主体在医疗系统中纠错和获得回应。

它不是投诉代写、医疗纠纷、法律策略、保险申诉、监管举报或机构施压工具。

## 先验问题

```text
医疗制度何以可纠错？
  -> 主体必须知道问题可以向哪里反馈
  -> 投诉、grievance、ombuds 和监管入口必须可达、可追踪、可保护隐私
  -> 反馈必须能进入质量改进、权利保护或个案回应路径
  -> 否则错误、歧视、延误和沟通失败无法形成修正回路
```

## 研究对象

- Patient grievance、hospital complaint、quality complaint、state survey agency、ombudsman。
- Medicare beneficiary rights、health plan grievance、civil rights complaint 和 patient relations。
- 投诉入口、时限、保护、反馈、分流、质量改进和 retaliation 风险。

## 关键变量

- 投诉入口可见性、受理率、响应时间、分流准确性和问题闭环率。
- 匿名性、隐私、retaliation fear、语言无障碍和数字/线下入口。
- 质量投诉、民权投诉、账单投诉、保险 grievance 和法律纠纷边界。

## 证据入口

- CMS hospital complaints、State Survey Agency、Medicare Ombudsman 和 beneficiary rights 资料。
- HHS OCR complaint、AHRQ CANDOR 和 patient safety reporting 资料。
- Patient grievance、complaint management、ombuds 和 healthcare accountability 文献。

## 非目标

- 不代写 complaint、grievance、appeal、demand letter、lawsuit、OCR complaint 或 regulator report。
- 不判断医疗事故、过失、歧视、账单合法性、保险决定、赔偿或胜诉概率。
- 不提供投诉策略、施压策略、舆论策略、取证策略、录音录像、跟踪或报复对抗方法。

## 上下游

- 上游：`patient-safety-organizational-learning/`、`healthcare-civil-rights-nondiscrimination-continuity/`。
- 下游：`governance-rights/`、`access-to-justice-legal-aid/`。
