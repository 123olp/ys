# ADR 0068: Add Sixty-Fourth-Wave Mental Health Neurodevelopment Functioning Domains

## Status

Accepted.

## Context

Human Infra 已经有 `mental-health-affective-stability`、`suicide-crisis-response-continuity`、`substance-use-treatment-recovery-continuity`、`dementia-cognitive-decline-care-continuity` 和若干急性神经连续性域。但主体持续性还需要把常见高影响心理健康、神经发育和功能损害状态拆成更可审查的研究域。

抑郁、焦虑、创伤/PTSD、精神病性体验、双相心境发作、ADHD、自闭谱系和进食障碍并不是同一种“情绪不稳定”。它们分别影响动机、威胁调节、记忆与安全感、现实检验、周期性判断、执行功能、感官/沟通适配和身体供能。若全部放入一个心理健康总域，后续资料路由、伦理边界、证据入口和禁止用途都会混杂。

## Decision

新增第 64 波 8 个心理健康、神经发育与功能连续性域：

- `depression-mood-disorder-functioning-continuity`
- `anxiety-stress-threat-regulation-continuity`
- `trauma-ptsd-adversity-recovery-continuity`
- `psychosis-reality-testing-community-continuity`
- `bipolar-mood-episode-stability-continuity`
- `adhd-executive-function-neurodevelopment-continuity`
- `autism-neurodiversity-support-continuity`
- `eating-disorders-nutrition-body-continuity`

## Consequences

- Human Infra 能把“心理状态”从笼统感受拆成动机、威胁调节、创伤恢复、现实检验、心境周期、执行功能、神经多样性支持和身体供能这些不同的主体持续性变量。
- 这些域只做公开资料整理、机制建模、服务连续性、功能结局、反污名和禁止用途声明；不提供诊断、治疗、药物、危机处置、家庭干预、饮食控制、行为训练、个体风险评分或敏感资料收集。
- 后续若新增 WHO、NIMH、CDC、SAMHSA、教育无障碍、工作便利或公共卫生资料，应先进入对应细分域；只有跨诊断总论才回到 `mental-health-affective-stability`。
