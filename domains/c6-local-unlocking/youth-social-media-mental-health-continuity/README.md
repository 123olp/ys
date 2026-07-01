# Youth Social Media Mental Health Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/youth-social-media-mental-health-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

`youth-social-media-mental-health-continuity` 研究社交媒体、推荐流、同伴反馈、比较压力、身体形象、睡眠扰动、注意力负荷和心理健康风险如何影响儿童青少年的主体持续性、学习能力、关系安全和未来选择权。

> 核心问题：线上社交如果持续消耗睡眠、注意力、归属感和情绪恢复，就会把发展窗口转化为慢性心理负荷。

## 对象

- 青少年社交媒体使用、推荐系统、通知、短视频流、同伴反馈、社交比较和身体形象压力。
- 睡眠、注意力、焦虑、抑郁、孤独、归属感、求助路径和家庭/学校支持接口。
- 平台透明度、年龄适配、风险提示、危机资源、研究数据访问和未成年人隐私。

## Human Infra 价值

```text
青少年线上社交环境可审查
  -> 注意力、睡眠、情绪恢复和关系安全更少被平台机制侵蚀
  -> 学习轮次、心理稳定、求助能力和家庭学校支持增强
  -> 主体发展窗口和未来选择权更少被早期数字环境消耗
```

## 边界

- 不提供个人心理诊断、危机干预、平台使用处方、屏幕时间计划、家庭冲突处理、学校投诉或治疗建议。
- 不判断某个儿童是否成瘾、抑郁、焦虑、自伤风险、适合某平台或应被限制使用。
- 不收集、推断或暴露未成年人账号、社交关系、心理状态、浏览记录、位置、学校、家庭冲突或健康资料。
- 不产出监控儿童、规避平台年龄规则、操纵推荐、舆论攻击、羞辱身体形象或强化污名的内容。

## 上游与下游

- 上游：`online-safety-digital-harm-prevention/`、`children-teen-data-privacy-consent-continuity/`、`mental-health-affective-stability/`。
- 下游：`school-mental-health-counseling-support-continuity/`、`sleep-circadian-recovery/`、`attention-executive-control/`、`family-caregiver-respite-work-continuity/`。

## 初始资料线索

- U.S. Surgeon General advisory on social media and youth mental health.
- HHS / NTIA Kids Online Health and Safety Task Force materials.
- AAP family media and youth media use public resources.
- CDC and SAMHSA youth mental health public materials.
