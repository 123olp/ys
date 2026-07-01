# Chemical Release Shelter Evacuation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chemical-release-shelter-evacuation-continuity` |
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

`chemical-release-shelter-evacuation-continuity/` 研究化学释放事故中就地避险、撤离、警报理解、交通转移、家庭/学校/工作场所接续和恢复入口如何保护主体持续性。

> 核心问题：化学释放不是单点暴露事件；如果人不知道何时避险、何时撤离、如何接上医疗、交通、照护和住宿，事故会把可控暴露变成大范围生活断裂。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体长期行动依赖可呼吸、可居住、可撤离的环境
  -> 化学释放使空气、水、道路、学校、工作和家庭照护同时进入不确定状态
  -> 就地避险与撤离连续性把危险信号转化为可执行、可恢复、可转介的行动链
```

## 关注对象

- 化学事故警报、就地避险、撤离、公共沟通、交通断点、临时安置和恢复入口。
- 家庭、学校、工作场所、长期照护机构和残障功能需求人群在化学释放中的连续性。
- 与 `chemical-safety-poison-control-toxicology/` 的关系：化学安全域关注毒理和暴露治理；本域关注事故发生后的避险/撤离执行链。

## Human Infra 模型链路

```text
化学释放避险与撤离连续性
  -> 改变暴露时长、错误行动、交通断点、照护断点和恢复入口
  -> 改变急性伤害、长期健康损害、居住中断和工作学习中断风险
  -> 增强主体生存、恢复、行动和未来选择权
```

## 非目标

- 不提供具体化学品处置、防护搭建、去污、撤离路线、现场判断或实时指挥。
- 不提供中毒处理、解毒、医疗分诊、法律索赔、保险、企业合规或责任判断。
- 不提供规避警报、规避监管、隐藏释放源、制造恐慌或破坏设施的信息。

## Source Signals

- Ready.gov chemical emergencies: https://www.ready.gov/chemical
- CDC chemical emergencies: https://www.cdc.gov/chemical-emergencies/
- FEMA protective actions and emergency management resources: https://www.fema.gov/emergency-managers
- EPA chemical emergency preparedness and prevention: https://www.epa.gov/chemical-emergency-preparedness-and-prevention

## 下一步

- 建立 Chemical Release Continuity Card：release signal, protective action, evacuation/shelter, transport, care dependency, re-entry, recovery referral。
- 与 `emergency-alerts-communications/`、`household-emergency-preparedness-resilience/`、`transportation-access-mobility/` 和 `disaster-recovery-relief-continuity/` 建立接口。
