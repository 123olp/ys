# Patient Advocacy Shared Decision Making

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/patient-advocacy-shared-decision-making` |
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


患者倡导与共同决策域研究：当医学证据、临床选项、主体偏好、治疗负担和风险承受能力发生冲突时，主体如何参与、表达、复核并维护自己的未来选择权。

## 对象

- 患者倡导、共同决策、决策辅助工具、知情同意、第二意见和照护伙伴。
- 主体目标、价值偏好、风险承受、治疗负担、功能目标、生活质量和不确定性沟通。
- 患者权利、问题清单、病历访问、会诊准备、照护会议和服务申诉边界。
- 医疗权力不对称、低健康素养、语言障碍、复杂病情和家庭决策冲突。
- 倡导与共同决策对医疗安全、有效时间、主体自主性和未来选择权的影响。

## Human Infra 价值

主体持续性不是只接受系统安排，而是主体能够把证据、偏好、风险和长期目标带入决策过程。患者倡导与共同决策把“被治疗的人”重新放回行动主体的位置。

```text
主体偏好和证据进入医疗决策
  -> 信息不对称、治疗负担、误解和被动同意下降
  -> 医疗路径更贴合主体目标、功能和风险承受能力
  -> 主体自主性和未来选择权提高
```

## 边界

本域只整理公开患者倡导、共同决策、决策辅助、知情同意和患者参与资料。

不提供：

- 个体治疗选择、第二意见、诊断、用药、检查、停治、转院或风险承受建议。
- 医疗投诉、诉讼、保险申诉、法律代理、病历纠纷或机构排名建议。
- 对患者、家属、医生、机构、治疗方案或临床试验的站队式动员。
- 用话术操纵患者、家属或医生，或把共同决策写成逃避专业责任。

## 上游与下游

- 上游：`health-literacy-navigation/`、`medical-interpreter-cultural-mediation/`、`governance-rights/`、`functioning-quality-of-life-outcomes/`。
- 下游：`healthcare-access-continuity/`、`clinical-trials-regulatory-science-translation/`、`home-health-hospice-palliative-care-continuity/`、`health-economics-value-assessment/`。

## 初始资料线索

- AHRQ SHARE Approach: https://www.ahrq.gov/health-literacy/professional-training/shared-decision/index.html
- AHRQ Patient and Family Engagement public materials。
- CMS person and family engagement public materials。
- Public materials on decision aids, informed consent and patient rights。

## 下一步

- 建立共同决策变量表：选项清晰度、风险理解、偏好表达、治疗负担、功能目标、决策辅助和复核能力。
- 整理患者倡导、共同决策、决策辅助和知情同意 Source Cards。
- 明确与健康素养、医疗解释、治理权利和缓和医疗的边界。
