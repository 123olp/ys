# 0028. Add Twenty-Fourth-Wave Externalized Subject Continuity Domains

Date: 2026-06-30

## Status

Accepted.

## Context

Human Infra 已经覆盖主体的生理、照护、资源、公共服务、复杂医疗和风险治理层。但“主体持续性”还依赖一组外部化条件：经历和资料能否长期保存，账号和数字资产能否在失能或死亡边界下交接，身体和环境状态能否连续观测，知识和项目上下文能否被外部记忆承载，神经接口能否安全扩展行动与沟通带宽，机器人能否把工具增强从信息层推进到物理行动层。

这些域不能被简单塞进 cognitive augmentation、digital identity、assistive technology 或 measurement feedback。它们各自拥有独立失败模式：资料丢失、账号继承失败、传感器误读、外部知识系统幻觉、神经数据滥用、机器人机械伤害和照护责任漂移。若不拆出，Human Infra 会低估“外部化主体”在有效永生与主体连续性中的基础作用。

## Decision

Add six formal domains:

- `domains/c3-generation-engine/life-logging-personal-archives-continuity/`
- `domains/c4-conversion-channel/digital-legacy-data-succession/`
- `domains/c3-generation-engine/wearables-continuous-sensing-personal-informatics/`
- `domains/c3-generation-engine/personal-knowledge-management-cognitive-offloading/`
- `domains/c2-source-maintenance/brain-computer-interface-neurotechnology-governance/`
- `domains/c3-generation-engine/robotics-embodied-assistance-care-automation/`

Update root navigation, docs navigation, reference maps, radar, ethics boundaries, changelog and repository checks so the new domains are discoverable and validated.

## Consequences

- Externalized subject continuity becomes a first-class Human Infra layer instead of being hidden inside broad AI, identity, assistive technology or measurement categories.
- Safety boundaries must explicitly prohibit surveillance, account takeover, legal advice, medical advice, device tampering, neural data abuse, unsafe robot automation and AI memory overclaiming.
- Future evidence work can organize source cards around personal digital archiving, digital legacy, continuous sensing, cognitive offloading, BCI governance and embodied assistance.

## Non-Goals

- No legal, estate, tax, account recovery, medical device, BCI usage, rehabilitation, product selection or personal data recovery advice.
- No instructions for bypassing authentication, platform policy, device safety limits, neural data protections, robot safety controls or clinical governance.
- No claim that personal archives, digital legacy, external memory, BCI or robots are sufficient for consciousness preservation, personality continuity or immortality.
- No endorsement of specific platforms, devices, companies, AI services, legal services, storage providers, robots or neurotechnology products.
