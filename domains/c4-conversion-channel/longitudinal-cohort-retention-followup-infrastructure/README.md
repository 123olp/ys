# Longitudinal Cohort Retention Followup Infrastructure

`longitudinal-cohort-retention-followup-infrastructure/` 研究纵向队列、长期随访、参与者留存、失访、数据链接、生命历程观测和队列治理，如何支撑寿命、健康寿命和主体持续性模型。

> 核心问题：有效永生不是短期指标问题，而是生命路径问题。若没有长期队列、稳定随访和失访治理，就无法判断因素、技术和干预如何改变风险函数、生存曲线和未来选择权。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要理解生命路径随时间如何变化
  -> 生命路径需要纵向队列、重复观测、随访、数据链接和失访控制
  -> 失访、选择偏差、随访断裂和队列老化会扭曲风险估计
  -> 因此纵向队列留存与随访基础设施是寿命模型的数据脊梁
```

## 关注对象

- 纵向队列、生命历程研究、随访设计、参与者留存、失访、再联系和数据链接。
- 队列代表性、选择偏差、幸存者偏差、迁移、死亡链接、健康记录链接和长期数据治理。
- 寿命、健康寿命、功能状态、暴露变化、干预采用、社会条件和未来选择权的长期观测。
- 与 `survival-analysis-healthspan-risk-modeling/` 的边界：生存分析域关注统计模型；本域关注支撑模型的长期观察基础设施。
- 与 `data-quality-missingness-representativeness/` 的边界：数据质量域关注一般缺失和代表性；本域聚焦队列随访、留存和生命历程观测。

## Human Infra 模型链路

```text
纵向队列留存与随访基础设施 T
  -> 改变随访频率、留存率、失访机制、数据链接、事件确认和代表性变量 X
  -> 改变生命路径数据、暴露变化和结局观测的系统状态 S
  -> 改变选择偏差、幸存者偏差、失访偏差和错误风险估计 λ(t)
  -> 影响寿命模型、健康寿命模型、干预评估和未来选择权预测可信度
```

## 非目标

- 不提供重新识别参与者、绕过同意、滥用数据链接、压迫参与者留存或规避伦理审查策略。
- 不把单个队列结果写成所有人群通用结论。
- 不替代统计建模、IRB、数据治理或参与者社区参与。

## Source Signals

- UK Biobank: https://www.ukbiobank.ac.uk/
- NIH All of Us Research Program: https://www.researchallofus.org/
- Framingham Heart Study: https://www.framinghamheartstudy.org/
- CDC National Health and Nutrition Examination Survey: https://www.cdc.gov/nchs/nhanes/
- NIA Health and Retirement Study: https://hrs.isr.umich.edu/

## 下一步

- 建立队列基础设施变量表：招募、留存、随访频率、失访机制、事件确认、数据链接和代表性。
- 与 `survival-analysis-healthspan-risk-modeling/`、`causal-inference-target-trial-emulation/`、`research-participant-consent-community-engagement/` 和 `registries-real-world-data-governance/` 建立接口。
