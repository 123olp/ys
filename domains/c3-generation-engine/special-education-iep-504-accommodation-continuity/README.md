# Special Education IEP 504 Accommodation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/special-education-iep-504-accommodation-continuity` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

`special-education-iep-504-accommodation-continuity` 研究 IDEA、IEP、Section 504、合理便利、相关服务、评估、转学交接和程序保障如何决定残障学生能否持续学习、参与和获得支持。

> 核心问题：残障支持不是附加服务，而是让学生在学校任务系统中保持可参与、可学习、可沟通和可恢复的基础设施。

## 关注对象

- IDEA 资格、评估、IEP、相关服务、转衔计划和 procedural safeguards。
- Section 504 计划、合理便利、无障碍、辅助技术、考试和课堂参与支持。
- 转学、升学、毕业、再评估、服务中断、人员短缺和家庭沟通断点。
- 残障支持与出勤、纪律、校医服务、心理健康、交通、语言可达和家庭照护的交叉。

## Human Infra 链路

```text
IEP/504 与学校便利连续
  -> 学生功能限制被转化为可执行支持、服务和环境适配
  -> 学习参与、沟通、移动、行为支持和健康安全更稳定
  -> 排除、惩罚化误读、家庭负担和长期能力损耗下降
  -> 主体学习能力、未来教育路径和社会参与资格增强
```

## 非目标

- 不提供个人 IEP、504、评估申请、申诉、due process、安置、残障诊断、治疗、教育法律或医疗建议。
- 不替代家长、学生、学校团队、教育律师、医生、治疗师、州保护与倡导机构或教育部门。
- 不收集或解释个人残障、教育、心理、行为、纪律或医疗记录。

## Source Signals

- U.S. Department of Education IDEA portal and Office of Special Education Programs resources.
- Office for Civil Rights disability discrimination and Section 504 resources.
- State education agency special education and accommodation guidance.
- National technical assistance centers for IDEA implementation and transition support.

## 下一步

- 建立 `functional need -> service/accommodation -> participation -> learning continuity` 变量表。
- 区分 IDEA、Section 504、ADA 无障碍、辅助技术、校医支持和行为支持。
- 与 `assistive-technology-access`、`disability-services-independent-living`、`school-discipline-exclusion-restraint-continuity` 和 `school-transportation-safe-routes-continuity` 建立边界。
