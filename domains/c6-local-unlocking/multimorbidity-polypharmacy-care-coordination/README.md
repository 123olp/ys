# Multimorbidity Polypharmacy Care Coordination

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/multimorbidity-polypharmacy-care-coordination` |
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

多病共存、多重用药与照护协调域研究：当主体同时承载多个慢病、多个专科、多个处方和多个照护目标时，系统如何避免冲突医嘱、药物相互作用、治疗负担和功能下降。

## 对象

- 多病共存、慢病组合、老年综合征、虚弱、复杂病例和跨专科照护。
- 多重用药、药物相互作用、用药重整、处方级联、停药/减药框架和药师协作。
- 治疗负担、冲突指南、共同照护计划、目标优先级、家庭照护和随访协调。
- 急性住院、门诊、长期照护、居家服务和社区药房之间的信息断点。
- 多病共存对死亡风险、健康寿命、功能状态、有效时间和未来选择权的影响。

## Human Infra 价值

多病共存不是把多个疾病指南相加。主体持续性取决于能否把身体状态、药物、功能目标、照护负担和主体偏好统一到一个可执行计划里。

```text
多病共存和多重用药被统一协调
  -> 冲突医嘱、药物相互作用、治疗负担和照护碎片化下降
  -> 主体风险函数、功能状态和有效时间更稳定
  -> 长期行动能力和未来选择权提高
```

## 边界

本域只整理公开多病共存、多重用药、药物安全、照护协调和治疗负担资料。

不提供：

- 个体用药增减、停药、替换、剂量、相互作用判断或处方建议。
- 个体诊断、治疗优先级、转诊、检查、急诊判断或临床路径。
- 对医生、药师、药物、指南、保险计划或机构的背书。
- 把群体证据写成确定个人疗效、风险或寿命预测。

## 上游与下游

- 上游：`medicine-access-treatment-continuity/`、`pharmacovigilance-drug-safety-monitoring/`、`healthcare-access-continuity/`、`patient-data-interoperability/`。
- 下游：`patient-safety-organizational-learning/`、`functioning-quality-of-life-outcomes/`、`caregiving-long-term-care/`、`dementia-cognitive-decline-care-continuity/`。

## 初始资料线索

- HHS Multiple Chronic Conditions public materials。
- WHO Medication Without Harm: https://www.who.int/initiatives/medication-without-harm
- AHRQ Care Coordination: https://www.ahrq.gov/ncepcr/care/coordination.html
- Public materials on medication reconciliation, deprescribing and treatment burden。

## 下一步

- 建立复杂照护变量表：疾病数量、药物数量、处方者数量、治疗负担、功能目标、用药重整和冲突风险。
- 整理多病共存与多重用药 Source Cards。
- 明确与药物警戒、患者安全、照护长期服务和共同决策的边界。
