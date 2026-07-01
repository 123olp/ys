# Workforce Employment Services

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/workforce-employment-services` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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


`workforce-employment-services/` 研究就业服务、劳动力发展、学徒制、职业信息、再就业支持、岗位匹配和合理便利如何让主体把能力转化为收入、角色和长期任务窗口。

> 核心问题：主体不仅需要学习能力，还需要进入可持续工作的制度通道；就业服务失败会让能力、时间和健康无法转化为资源与社会参与。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须长期维持收入、技能更新、社会角色和任务入口
  -> 技能需要通过就业服务、劳动力发展、学徒制、职业信息和合理便利转化为工作机会
  -> 失业、转型失败、岗位错配和便利缺失会压缩资源、身份、行动和未来选择权
  -> 因此劳动力与就业服务是主体持续性的能力转化域
```

## 关注对象

- 就业服务、CareerOneStop、WIOA、学徒制、O*NET、My Next Move、劳动力市场信息和合理便利。
- 再就业、技能转型、岗位匹配、残障就业、工作适配、收入恢复和职业路径导航。
- 与 `learning-skill-acquisition/` 的边界：学习域关注能力形成；本域关注能力进入劳动市场和服务系统。
- 与 `occupational-work-design/` 的边界：工作设计关注岗位内健康和组织；本域关注就业入口、转型和服务。

## Human Infra 模型链路

```text
就业服务与劳动力发展 T
  -> 改变职业信息、技能转型、岗位匹配、学徒制、合理便利和再就业支持变量 X
  -> 改变主体收入、角色、技能使用和社会参与状态 S
  -> 改变长期失业、收入断裂、技能过期、职业错配、健康恶化和机会损失风险 λ(t)
  -> 影响财务韧性、身份连续、有效时间和未来选择权
```

## 非目标

- 不提供个体职业规划、简历、面试、就业承诺、工资判断、移民、福利、法律或劳动争议建议。
- 不支持歧视性筛选、剥削性招聘、监控劳动者、虚假岗位、培训骗局或资格规避。
- 不把就业服务写成让人无限服从劳动力市场的工具；主体健康、尊严和退出权优先。

## Source Signals

- CareerOneStop: https://www.careeronestop.org/
- U.S. Department of Labor Employment and Training Administration: https://www.dol.gov/agencies/eta
- WIOA: https://www.dol.gov/agencies/eta/wioa
- Apprenticeship.gov: https://www.apprenticeship.gov/
- O*NET: https://www.onetonline.org/
- My Next Move: https://www.mynextmove.org/
- Job Accommodation Network: https://askjan.org/

## 下一步

- 建立变量表：就业入口、技能转型、岗位匹配、合理便利、再就业支持、收入恢复和职业信息质量。
- 与 `learning-skill-acquisition/`、`occupational-work-design/`、`labor-rights-workplace-protection/` 和 `financial-resilience-access/` 建立边界。
