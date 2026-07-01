# Pediatric Lead Screening Environmental Followup Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pediatric-lead-screening-environmental-followup-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


儿童铅筛查与环境随访连续性，关注血铅检测入口、结果通知、公共卫生随访、住房/水源环境调查、家庭沟通、学校托育接口和长期发育支持如何影响儿童能力形成。

## 对象

- Pediatric blood lead screening interface
- Result notification and public-health follow-up
- Housing, paint, dust, soil and water exposure pathways
- Environmental investigation and remediation handoff
- Nutrition, developmental and educational support boundary
- Language, rental housing and code enforcement barriers
- Privacy, stigma and family-data boundary

## Human Infra 价值

儿童铅暴露不是单一毒物问题，而是住房、饮水、租赁、公共卫生、儿科、学校和家庭资源之间的连续性问题。该域把儿童血铅信号是否能转化为环境修复、服务支持和长期发育保护，纳入主体持续性的早期风险治理。

## 边界

- 不提供检测结果解释、治疗、营养处方、chelation、环境采样教程、施工修复、法律策略、租赁争议、学校安置或个体医疗建议。
- 不判断某个儿童是否中毒、是否需要治疗、某住所是否安全、某房东/机构是否违规或某家庭是否有责任。
- 不替代儿科、公共卫生、环境卫生、住房 code enforcement、EPA/CDC/州项目、法律服务、学校或紧急服务。

## 上游与下游

- 上游：`well-child-visit-preventive-care-continuity/`、`lead-heavy-metal-exposure-control/`、`housing-habitability-inspection-code-enforcement-continuity/`。
- 下游：`developmental-behavioral-screening-referral-continuity/`、`school-health-services-chronic-condition-continuity/`、`early-intervention-idea-part-c-developmental-services-continuity/`。

## 初始资料线索

- CDC Childhood Lead Poisoning Prevention materials.
- EPA lead and housing hazard materials.
- Medicaid / public health lead screening materials.
