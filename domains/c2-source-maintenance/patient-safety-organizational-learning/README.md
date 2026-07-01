# Patient Safety Organizational Learning

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/patient-safety-organizational-learning` |
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


`patient-safety-organizational-learning/` 研究患者安全、团队沟通、事件报告、根因分析、CUSP、TeamSTEPPS、高可靠组织和伤害预防。

> 核心问题：医疗和照护中的错误不能只归因于个人；组织是否能报告、学习、修复和重设流程，决定可避免伤害是否会持续截断主体。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要医疗、照护和组织系统支持
  -> 复杂组织会制造交接、沟通、疲劳、设备、流程和文化风险
  -> 事件学习和系统安全决定错误能否转化为改进，而不是重复伤害
```

## 关注对象

- 患者安全、医疗伤害、事件报告、团队沟通、交接、CUSP、TeamSTEPPS、RCA2、安全文化和高可靠组织。
- 医疗组织如何降低错误、疲劳、流程断裂、沟通失败、药物错误、感染和可避免伤害。
- 与 `risk-engineering/` 的关系：风险工程域关注通用风险；本域关注医疗与照护组织中的患者安全和学习机制。
- 与 `healthcare-access-continuity/`、`medicine-access-treatment-continuity/`、`occupational-work-design/` 和 `measurement-feedback/` 的接口。

## Human Infra 模型链路

```text
患者安全与组织学习基础设施
  -> 改变事件报告、团队沟通、根因分析、流程改进和安全文化
  -> 改变医疗照护系统中错误被发现、学习、纠正和防止复发的能力
  -> 降低可避免伤害、沟通失败、照护交接断裂和重复事故风险
  -> 增强医疗可信度、恢复机会、健康寿命和主体持续性
```

## 非目标

- 不提供医疗事故法律意见、索赔策略、个案责任判断、机构排名或临床处置建议。
- 不把安全文化测量写成惩罚员工、压制报告、甩锅患者或规避责任的工具。
- 不提供医疗流程操作、急救、药物、设备、感染控制或机构管理替代方案。

## Source Signals

- WHO Global Patient Safety Action Plan 2021-2030: https://www.who.int/publications/i/item/9789240032705
- AHRQ TeamSTEPPS: https://www.ahrq.gov/teamstepps-program/index.html
- AHRQ CUSP: https://www.ahrq.gov/hai/cusp/index.html
- AHRQ Surveys on Patient Safety Culture: https://www.ahrq.gov/sops/index.html
- IHI RCA2: https://www.ihi.org/resources/tools/rca2-improving-root-cause-analyses-and-actions-prevent-harm

## 下一步

- 建立患者安全变量表：事件报告、近失误、交接、沟通、团队训练、根因分析、行动闭环、安全文化和学习速度。
- 与 `risk-engineering/` 拆分通用风险工程和医疗组织学习边界。
- 整理 WHO Patient Safety、AHRQ TeamSTEPPS、CUSP、SOPS 和 IHI RCA2 的 Source Cards。
