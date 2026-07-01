# Lactation Breastfeeding Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/lactation-breastfeeding-support-continuity` |
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


哺乳、泵奶与喂养支持连续性，关注 lactation support、breastfeeding counseling、泵奶空间和时间、奶量/疼痛转介、婴儿喂养信息、WIC/医疗转介、工作学校环境和家庭支持如何影响母婴营养与主体恢复。

## 对象

- Lactation support and breastfeeding counseling
- Pumping time, space and equipment interface
- WIC and community breastfeeding support
- Work, school and public accommodation boundary
- Feeding difficulty referral boundary
- Infant nutrition information access
- Privacy, stigma and family support

## Human Infra 价值

哺乳和泵奶会占用身体、时间、睡眠、工作空间、学校空间和家庭支持。该域把“母婴营养输入是否可持续”建模为医疗、福利、工作学校、设备、空间和社会支持共同维护的执行系统。

## 边界

- 不提供喂养方案、奶量判断、疼痛处理、婴儿体重解释、配方替代、药物、泵奶参数、断奶、复工泵奶安排或个体医疗建议。
- 不判断个人是否应母乳喂养、是否需要配方、是否存在疾病、是否需要某类设备或是否有法律资格。
- 不替代 lactation consultant、儿科、OB/GYN、WIC、雇主、学校、法律援助或医疗服务。

## 上游与下游

- 上游：`postpartum-care-recovery-follow-up-continuity/`、`wic-benefit-redemption-infant-maternal-nutrition-continuity/`、`pregnancy-parental-work-continuity/`。
- 下游：`infant-formula-baby-food-supply-safety-continuity/`、`infant-safe-sleep-suid-risk-reduction-continuity/`、`maternal-newborn-child-development/`。

## 初始资料线索

- CDC breastfeeding materials.
- WIC breastfeeding support materials.
- U.S. Department of Labor PUMP at Work materials.
