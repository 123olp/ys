# Plasma Proteome Systemic Aging Signal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/plasma-proteome-systemic-aging-signal-continuity` |
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

Plasma Proteome Systemic Aging Signal Continuity 负责整理血浆蛋白组、循环因子、系统性衰老信号、异时共生线索、血浆置换假设和抗衰误用边界。

核心问题：

> 血液循环携带来自器官、免疫、代谢和组织损伤的系统性信号；血浆蛋白组可能反映并参与衰老状态，但不能被简化成“年轻血浆能抗衰”的消费叙事。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要跨器官信号维持协调、修复和风险反馈
  -> 血浆蛋白组和循环因子反映免疫、代谢、组织损伤和器官状态
  -> 系统性信号可能改变再生、炎症、神经、代谢和血管风险
  -> 若能被可靠测量或安全调节，可能成为生命路径模型变量
  -> 但证据边界失败会把血浆信号误读为未经证实的抗衰治疗
```

## 关注对象

- plasma proteome、circulating factors、heterochronic parabiosis、therapeutic plasma exchange hypotheses。
- 血浆蛋白年龄钟、器官来源信号、炎症/凝血/代谢因子、测量偏差和干预安全边界。
- 与 `blood-oxygen-hemostasis/` 的关系：血液域关注氧运与止血；本域关注循环信号与系统性衰老信息。
- 与 `biological-age-clocks-biomarker-validation/` 的关系：本域提供候选 biomarker 和干预信号，但需要独立验证。

## Human Infra 模型链路

```text
血浆蛋白组测量 / 循环因子干预 T
  -> 改变或观测系统性衰老信号 X
  -> 改变跨器官协调、炎症、凝血、代谢和修复状态 S
  -> 改变疾病风险、恢复能力、健康寿命和治疗窗口判断
  -> 改变主体未来选择权
```

## 非目标

- 不提供年轻血浆、血浆置换、输血、血液制品、检测解读或抗衰治疗建议。
- 不把异时共生、动物实验或蛋白组相关性写成人体疗效。
- 不推广未经批准或证据不足的抗衰血浆产品。

## Source Signals

- FDA young donor plasma warning: https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/update-important-information-about-young-donor-plasma-infusions-offered-profit
- Looking to Young Blood to Treat the Diseases of Aging: https://pmc.ncbi.nlm.nih.gov/articles/PMC6764071/
