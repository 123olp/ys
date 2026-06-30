# 0034. Add Thirtieth-Wave Quantitative Methodology Domains

Date: 2026-06-30

## Status

Accepted.

## Context

Human Infra 已经完成大量研究域发散，覆盖生物医学平台、社会基础设施、生命线服务、认知工具、风险治理和未来等待路径。下一步的核心问题不再只是“还有哪些域”，而是这些域如何进入同一套可审查的定量链路。

项目的预测链路已经明确为：

```text
技术/干预 T
  -> 影响变量 X
  -> 改变主体状态 S
  -> 改变风险函数 lambda(t)
  -> 改变生存曲线 S(t)
  -> 改变有效寿命、有效时间和未来选择权
```

这条链路需要方法学基础设施：因果推断区分相关与干预效果，生存分析表达风险和健康寿命，数字孪生组织动态状态，实施科学处理真实采用和坚持，不确定性量化防止虚假精确，数据质量审查阻止偏差进入模型。

这些能力不能只并入 `measurement-feedback/`、`life-path-prediction-model-governance`、`clinical-trials-regulatory-science-translation/` 或 `research-infrastructure-open-science-translation/`。它们各自是让 Human Infra 从定性谱系走向定量预测的独立方法学域。

## Decision

Add six formal quantitative methodology domains:

- `domains/causal-inference-target-trial-emulation/`
- `domains/survival-analysis-healthspan-risk-modeling/`
- `domains/human-digital-twin-life-course-simulation/`
- `domains/implementation-science-adherence-behavior-change/`
- `domains/uncertainty-quantification-model-calibration/`
- `domains/data-quality-missingness-representativeness/`

Update root navigation, docs navigation, reference maps, radar, ethics boundaries, changelog and repository checks so the new domains are discoverable and validated.

## Consequences

- Human Infra now has a method layer for turning research domains into causal questions, survival endpoints, state simulation, implementation gates, calibration checks and data quality gates.
- Future research pages can explain why a technology is not judged by narrative force, but by identifiable mechanisms, estimable effects, adoption probability, uncertainty and evidence quality.
- The prediction model can stay rigorous without outputting individual death dates, deterministic lifespan promises or medical decisions.
- Research domain expansion now has an explicit path from qualitative genealogy to quantitative model contracts.

## Non-Goals

- No individual lifespan prediction, death-date prediction, diagnosis, treatment recommendation, insurance scoring, hiring score or automated eligibility decision.
- No claim that current Human Infra models are clinically validated or suitable for individual decision support.
- No replacement for `measurement-feedback/`; this wave defines the statistical and methodological substrate that makes measurement interpretable.
- No data collection, personal data processing, hidden risk scoring, data re-identification, p-hacking or uncertainty laundering.
