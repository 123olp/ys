# Health Workforce Capacity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/health-workforce-capacity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`health-workforce-capacity/` 研究医生、护士、公共卫生人员、社区健康工作者、照护人员和辅助专业人员的供给、分布、训练、保留和负荷如何限制医疗系统可达性。

> 核心问题：医学技术存在不等于主体能获得照护；如果健康劳动力不足、分布不均、流失严重或负荷过高，诊断、治疗、康复、公共卫生和长期照护都会变成排队、延误和质量风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须持续获得诊断、治疗、预防、康复和照护
  -> 这些服务依赖足够数量、技能、地域分布和可持续工作的健康劳动力
  -> 劳动力短缺、错配、倦怠和培训瓶颈会把可修复风险变成不可及风险
  -> 因此健康劳动力容量是医学收益转化为主体持续性的系统约束域
```

## 关注对象

- 医生、护士、公共卫生人员、药师、康复人员、行为健康人员、社区健康工作者和长期照护劳动力。
- 劳动力供给、地理分布、短缺区域、培训管线、保留、倦怠、技能组合和任务转移。
- 卫生人力数据、预测、职业分类、服务可达性和质量之间的关系。
- 与 `healthcare-access-continuity/` 的边界：本域关注提供服务的人力容量；医疗可及域关注服务入口、连续性、费用和质量整体。
- 与 `occupational-work-design/` 的边界：本域聚焦健康服务劳动力；工作设计域处理更广泛职业环境。

## Human Infra 模型链路

```text
健康劳动力容量 T
  -> 改变供给、分布、技能组合、负荷、保留、培训和团队协作变量 X
  -> 改变主体获得诊断、治疗、预防、康复和照护的系统状态 S
  -> 改变等待、延误、误诊、护理失败、公共卫生响应不足和照护断点风险 λ(t)
  -> 影响可修复风险、健康寿命、恢复能力和未来选择权
```

## 非目标

- 不提供个体择医、职业规划、薪资谈判、移民资格、执照认证、劳动争议或机构排名建议。
- 不支持用劳动力短缺合理化压榨、过度监控、降低安全标准或削弱专业边界。
- 不把 AI、自动化或任务转移写成可以无条件替代临床责任和人类照护关系。

## Source Signals

- WHO Health Workforce: https://www.who.int/health-topics/health-workforce
- WHO Global Strategy on Human Resources for Health: https://www.who.int/publications/i/item/9789241511131
- HRSA Health Workforce: https://bhw.hrsa.gov/
- HRSA Health Workforce Data: https://data.hrsa.gov/topics/health-workforce
- BLS Healthcare Occupations: https://www.bls.gov/ooh/healthcare/

## 下一步

- 建立健康劳动力变量表：供给、分布、短缺、技能组合、培训、保留、倦怠、任务转移和服务质量。
- 与 `healthcare-access-continuity/`、`patient-safety-organizational-learning/`、`rehabilitation-functioning/` 和 `caregiving-long-term-care/` 建立接口。
