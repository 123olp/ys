# Newborn Screening Result Followup Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/newborn-screening-result-followup-continuity` |
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


新生儿筛查结果与随访连续性，关注出生后早期筛查、样本采集、实验室报告、异常结果通知、诊断确认、专科转介、家庭沟通和州级项目接口如何影响可逆风险窗口。

## 对象

- Newborn screening program interface
- Specimen collection and result routing
- Abnormal result notification and follow-up
- Confirmatory testing referral boundary
- Family communication and language access
- State program, pediatric care and specialty handoff
- Privacy and genetic information boundary

## Human Infra 价值

新生儿筛查不是单次检测，而是把出生后短暂、可逆、可能高后果的代谢、内分泌、血液、免疫或其他风险接入可通知、可确认、可转诊和可随访的公共卫生系统。该域把“早期信号是否能转成及时行动”建模为下一代主体持续性的早期基础设施。

## 边界

- 不提供筛查项目选择、筛查结果解释、遗传风险解释、诊断、治疗、喂养、药物、急诊或个体儿科建议。
- 不判断某个婴儿是否异常、是否需要复查、是否需要治疗、是否遗传风险增加或家庭成员是否需要检测。
- 不替代儿科、新生儿科、遗传咨询、州 newborn screening program、公共卫生机构、实验室、保险、语言服务或紧急服务。

## 上游与下游

- 上游：`maternal-newborn-child-development/`、`postpartum-care-recovery-follow-up-continuity/`、`healthcare-access-continuity/`。
- 下游：`well-child-visit-preventive-care-continuity/`、`children-youth-special-health-care-needs-care-coordination-continuity/`、`patient-data-interoperability/`。

## 初始资料线索

- CDC newborn screening materials.
- HRSA newborn screening and follow-up resources.
- State newborn screening program public materials.
