# Patent Invention Disclosure Maintenance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/patent-invention-disclosure-maintenance-continuity` |
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

`patent-invention-disclosure-maintenance-continuity` 研究专利、发明披露、优先权、公开、转让、维护费、技术许可和 prior art 记录如何影响科研成果、工程发明、创业资产、技术转移和未来技术可及性。

> 核心问题：发明如果不能被记录、公开、归属、维护和转化，就会在论文、实验室、公司和供应链之间断裂，无法进入主体可用技术窗口。

## 关注对象

- Patent application、publication、grant、assignment、maintenance fees、priority、inventorship 和 public patent records。
- 发明披露、实验记录、资助来源、技术转移、许可、exclusive/non-exclusive arrangements 和公共资助成果。
- Prior art、patent landscape、freedom-to-operate 作为研究资料边界，而不是个案法律结论。
- Human Infra 中未来技术从发现、披露、保护、公开到可获得服务的制度路径。

## Human Infra 链路

```text
发明和技术原型出现
  -> 披露、专利、公开、转让和维护记录决定技术资产形态
  -> 技术能否被生产、许可、扩散和持续维护发生变化
  -> 未来技术窗口的可采用概率和可及性发生变化
  -> 主体获得新工具、治疗、材料和服务的机会改变
```

## 非目标

- 不提供专利申请、权利要求撰写、prior art 检索意见、侵权分析、FTO、维护费策略、许可谈判或法律意见。
- 不判断具体专利有效性、新颖性、创造性、侵权风险、商业价值或投资价值。
- 不提供规避专利、绕开许可、商业秘密获取、专利抢注、专利布局或诉讼策略。
- 不收集未公开发明披露、实验记录、资助合同、商业秘密、许可合同或法律通信。

## Source Signals

- USPTO Patents: https://www.uspto.gov/patents
- WIPO Patents: https://www.wipo.int/patents/en/
- Google Patents as discovery interface: https://patents.google.com/
- NIST Bayh-Dole resources: https://www.nist.gov/tpo/bayh-dole

## 下一步

- 建立 `invention -> disclosure -> patent/publication -> assignment/license -> access/maintenance -> continuity` 变量表。
- 区分专利作为公开记录、技术转移制度、市场排他权和主体可及性门槛。
- 与 `intellectual-property-technology-transfer-access`、`research-portfolio-prioritization-funding-governance`、`clinical-trials-regulatory-science-translation` 和 `technology-foresight-horizon-scanning` 建立边界。
