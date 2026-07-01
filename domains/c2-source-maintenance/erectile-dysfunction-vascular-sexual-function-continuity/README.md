# Erectile Dysfunction Vascular Sexual Function Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/erectile-dysfunction-vascular-sexual-function-continuity` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

`erectile-dysfunction-vascular-sexual-function-continuity/` 研究勃起功能障碍作为血管、代谢、神经、内分泌、药物、心理、关系和性功能接口，如何影响主体持续性、尊严、关系和长期风险识别。

> 核心问题：ED 不只是性功能问题，它可能是血管代谢风险、药物副作用、心理负担和关系压力的可见信号，也会通过尊严、亲密关系和医疗回避影响主体行动质量。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要身体完整性、关系参与、尊严和长期风险识别能力
  -> ED 可能连接血管、代谢、神经、内分泌、药物、心理和关系变量
  -> 若污名或商业化误导阻断评估，主体会损失风险发现窗口、关系质量和身体自主
  -> 因此 ED 是性功能、血管代谢信号和尊严连续性的交叉域
```

## 关注对象

- Erectile dysfunction、vascular risk signal、diabetes/cardiovascular context、neurologic/endocrine context、medication side effects、psychological stress、relationship burden、privacy and stigma。
- 与 `urogenital-continuity/` 的边界：上位域关注泌尿生殖尊严；本域关注 ED 作为性功能、血管代谢和关系接口。
- 与 `cardiovascular-resilience/` 的关系：ED 可能与血管健康和代谢风险相关，但本域不做个人心血管风险判读。
- 与 `sexual-health-sti-prevention-continuity/` 的边界：STI 域关注感染预防和公共卫生；本域关注性功能与风险信号。

## Human Infra 模型链路

```text
ED 风险识别与支持系统 T
  -> 改变血管代谢信号、神经/内分泌背景、药物副作用、心理压力、关系安全、隐私和污名变量 X
  -> 改变主体身体自主、尊严、亲密关系、医疗信任、风险识别和有效时间状态 S
  -> 改变心血管/糖尿病风险漏检、关系冲突、心理负担、商业误导和医疗回避 lambda(t)
  -> 影响主体长期健康风险治理、关系连续性和生活质量
```

## 非目标

- 不提供 ED 诊断、药物、补剂、器械、激素、心理治疗、性行为建议、心血管风险判读、伴侣建议或个体医疗建议。
- 不比较产品、平台、诊所、处方、设备或商业服务。
- 不收集个人性功能、伴侣、药物、心血管、糖尿病、心理健康或身份敏感资料。

## Source Signals

- NIDDK erectile dysfunction: https://www.niddk.nih.gov/health-information/urologic-diseases/erectile-dysfunction
- MedlinePlus erectile dysfunction: https://medlineplus.gov/erectiledysfunction.html
- NIDDK diabetes, sexual and urologic problems: https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/sexual-urologic-problems

## 下一步

- 建立 ED Continuity Card：vascular/metabolic signal, medication context, psychologic load, privacy, relationship burden, misinformation risk。
- 与 `urogenital-continuity/`、`cardiovascular-resilience/`、`diabetes-insulin-glucose-monitoring-supplies-continuity/` 和 `mental-health-affective-stability/` 建立接口。
