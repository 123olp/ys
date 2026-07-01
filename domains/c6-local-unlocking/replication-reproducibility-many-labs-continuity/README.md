# Replication Reproducibility Many Labs Continuity

`replication-reproducibility-many-labs-continuity/` 研究复制研究、复现实验、多实验室协作、再分析和结果稳健性如何影响 Human Infra 证据可靠性。

> 核心问题：单一研究即使发表也可能不可复制；主体持续性模型需要知道结论是否能在不同数据、实验室、方法和人群中重复出现。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要把技术和干预放入长期决策模型
  -> 单次研究结果可能来自偶然、偏倚、过拟合或情境依赖
  -> 复制、复现、多实验室验证和再分析决定结果稳健性
  -> 因此复制/复现/多实验室连续性是证据从信号变成可靠输入的门槛
```

## 关注对象

- Replication、reproducibility、robustness、multisite study、Many Labs、reanalysis、registered replication report 和 computational reproducibility。
- 直接复制、概念复制、独立数据再分析、跨实验室异质性和失败复制解释。
- 与 `research-software-capsule-reproducibility-continuity/` 的边界：软件胶囊域关注计算环境；本域关注研究结论跨团队和情境是否稳健。
- 与 `meta-analysis-effect-size-heterogeneity-continuity/` 的边界：Meta 域量化多研究效应；本域关注复制设计和失败解释。

## Human Infra 模型链路

```text
复制复现与多实验室验证 T
  -> 改变 replication_status、reproducibility_status、cross_site_heterogeneity、robustness 变量 X
  -> 改变效应估计、证据确定性和模型输入可信状态 S
  -> 改变不可复制结论、过拟合、场景外推和技术采用误判风险 λ(t)
  -> 影响长期研究组合、模型校准和主体持续性路径判断
```

## 非目标

- 不提供数据伪造、复现实验操控、显著性追逐、论文代写、实验规避或对作者的不端指控。
- 不把失败复制自动解释为原研究错误；必须记录情境、方法和样本差异。
- 不提供湿实验、人体实验或临床操作协议。

## Source Signals

- National Academies, Reproducibility and Replicability in Science: https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science
- Center for Open Science: https://www.cos.io/
- Many Labs projects, Center for Open Science: https://www.cos.io/initiatives
- Registered Reports, Center for Open Science: https://www.cos.io/initiatives/registered-reports
- OSF Registries: https://osf.io/registries

## 下一步

- 给 Source Card 增加 `replication_status`、`reproducibility_package`、`multisite_signal`、`failed_replication_context` 和 `robustness_note` 字段。
- 与 Meta 分析、风险偏倚、预注册和研究软件胶囊域建立复核链。
