# Clinical Trials Regulatory Science Translation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/clinical-trials-regulatory-science-translation` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

`clinical-trials-regulatory-science-translation/` 研究临床试验、监管科学、真实世界证据、伦理审查、终点选择、安全监测和批准路径如何把生物医学发现转化为可验证、可治理、可获得的干预。

> 核心问题：一个技术“可能有用”不等于能进入人体、通过试验、被监管接受并安全扩散。有效永生需要的不只是发现，还需要把发现穿过临床证据和监管科学的转化通道。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要医学和生物技术干预真正可用
  -> 可用干预必须经过人体试验、伦理审查、安全监测、终点评价和监管决策
  -> 试验设计失败、终点错配、安全信号遗漏和监管证据不足会阻断技术转化
  -> 因此临床试验与监管科学是未来医学收益进入主体系统的转化域
```

## 关注对象

- 临床试验注册、研究设计、随机化、对照、终点、样本、随访、安全监测、伦理审查和数据透明。
- 监管科学、真实世界证据、上市后监测、适应证、标签、风险收益和患者代表性。
- 长寿、再生医学、细胞重编程、癌症、AI 医疗、药物和设备进入人体研究的证据路径。
- 与 `longevity-evidence/` 的边界：长寿证据域汇总干预证据；本域关注临床证据如何被设计、生成、监管和转化。
- 与 `research-infrastructure-open-science-translation/` 的边界：科研基础设施域关注发现生态；本域关注人体研究和监管证据链。

## Human Infra 模型链路

```text
临床试验与监管科学 T
  -> 改变研究设计、终点、代表性、安全监测、真实世界证据和监管决策变量 X
  -> 改变干预能否被验证、批准、监测、标签化和扩散的系统状态 S
  -> 改变无效干预、迟滞转化、安全遗漏、证据错配和不可及风险 λ(t)
  -> 影响医学技术窗口、健康寿命、恢复能力和未来选择权
```

## 非目标

- 不提供入组建议、试验选择、用药、停药、治疗方案、监管规避或个体医疗建议。
- 不把临床试验注册、早期结果、新闻稿或监管申请写成疗效已经成立。
- 不支持绕过伦理审查、知情同意、安全监测、试验注册或监管要求。

## Source Signals

- ClinicalTrials.gov: https://clinicaltrials.gov/
- WHO International Clinical Trials Registry Platform: https://www.who.int/clinical-trials-registry-platform
- FDA Regulatory Science: https://www.fda.gov/science-research/science-and-research-special-topics/regulatory-science
- FDA Real-World Evidence: https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence
- NIH Office of Clinical Research: https://ocr.od.nih.gov/

## 下一步

- 建立临床转化变量表：试验阶段、终点、样本代表性、安全监测、监管路径、真实世界证据和上市后风险。
- 与 `longevity-evidence/`、`cellular-reprogramming/`、`regenerative-medicine/`、`cancer-control/` 和 `patient-safety-organizational-learning/` 建立接口。
