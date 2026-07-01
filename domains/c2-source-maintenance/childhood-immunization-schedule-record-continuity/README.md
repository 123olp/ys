# Childhood Immunization Schedule Record Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/childhood-immunization-schedule-record-continuity` |
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


儿童常规免疫排程与记录连续性，关注官方免疫排程、接种记录、学校/托育证明、漏种追踪、供应与预约、家庭沟通、豁免和公共卫生记录接口如何影响儿童群体保护。

## 对象

- Childhood immunization schedule interface
- Immunization information systems and records
- School / childcare proof and documentation
- Reminder, recall and missed-dose follow-up
- Vaccine access, appointment and supply barriers
- Family communication and language access
- Exemption, consent and privacy boundary

## Human Infra 价值

儿童免疫不是单个家庭选择，而是把儿童个体保护、群体屏障、学校托育准入、公共卫生记录和照护连续性连接起来的基础设施。该域关注记录、预约、提醒、可及性和证明链路如何让官方免疫信息转化为真实保护，而不是讨论个体是否应接种。

## 边界

- 不提供疫苗医学建议、排程解释、补种方案、禁忌判断、不良反应判断、豁免策略、学校入学策略或个体医疗建议。
- 不判断某个儿童是否应接种、是否可延迟、是否有禁忌、是否免疫充分或是否需要急诊。
- 不替代儿科、公共卫生机构、免疫信息系统、学校/托育机构、保险、法律服务或紧急服务。

## 上游与下游

- 上游：`well-child-visit-preventive-care-continuity/`、`immunization-public-health-surveillance/`、`immunization-record-proof-continuity/`。
- 下游：`school-enrollment-attendance-continuity/`、`child-care-licensing-health-safety-continuity/`、`outbreak-case-investigation-contact-tracing-continuity/`。

## 初始资料线索

- CDC child and adolescent immunization schedule materials.
- CDC immunization information systems materials.
- State school and childcare immunization record materials.
