# sexual-assault-forensic-exam-advocacy-continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/sexual-assault-forensic-exam-advocacy-continuity` |
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

`sexual-assault-forensic-exam-advocacy-continuity` 研究性暴力发生后，医疗照护、forensic exam、SANE/SAFE 服务、advocacy、证据保存边界、匿名/限制报告选项、创伤支持和权利告知如何影响主体身体恢复、心理恢复、法律参与和未来选择权。

## Scope

- Sexual assault、rape crisis response、medical forensic examination、SANE/SAFE、advocacy、crisis counseling 和 victim rights information。
- 医疗照护、药物预防、证据采集流程说明、报告选项、保密、语言可达、残障可达和未成年人边界。
- 与校园、军队、拘押、医疗机构、移民和家庭暴力交叉的公开制度资料。

## Continuity Logic

```text
性暴力事件
-> 身体伤害、感染风险、创伤反应、证据时效和制度参与压力同时出现
-> 医疗 forensic exam、advocacy、保密选项和权利告知成为恢复接口
-> 接口缺失会增加健康风险、二次伤害、法律退出和长期创伤负荷
```

## Source Spine

- DOJ Office on Violence Against Women sexual assault materials.
- Office for Victims of Crime sexual assault and victim services materials.
- CDC sexual violence prevention resources.
- HHS Office on Women's Health sexual assault resources.
- SAFEta / national protocol materials where used as public professional guidance.

## Evidence Boundary

本域只整理公开性暴力响应、医疗 forensic exam、受害者 advocacy、报告选项和创伤支持资料。

Do not include:

- 个案医疗建议、证据采集建议、报警策略、诉讼策略、校园投诉策略、移民策略或安全计划。
- 可用于制造、隐藏、伪造、污染、破坏或操控证据的信息。
- 识别受害者、加害者、医疗人员、服务点或未成年人的信息。

## Upstream / Downstream

- Upstream: `personal-safety-violence-prevention/`, `healthcare-access-continuity/`, `healthcare-civil-rights-nondiscrimination-continuity/`.
- Downstream: `victim-witness-rights-notification-continuity/`, `crime-victim-compensation-restitution-continuity/`, `campus-safety-title-ix-clery-continuity/`, `mental-health-affective-stability/`.
