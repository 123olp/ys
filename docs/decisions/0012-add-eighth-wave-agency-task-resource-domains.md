# 0012 Add Eighth Wave Agency Task Resource Domains

## Status

Accepted

## Context

Research Domain Atlas 已把 Human Infra 的域生成规则定义为先验条件追溯：凡是主体持续性成立所需的必要条件、支撑条件、风险条件或反馈条件，都可以被抽象为研究域。

前七波已经覆盖分子维护、生理稳态、身体结构、未来等待、外部风险和基础社会资源。但 Human Infra 的核心对象不是单纯活着的身体，而是能够持续完成任务、学习、判断、恢复和进入未来的主体。当前仍缺少六类“日历时间转化为有效行动”的条件：

- 时间必须被注意力和执行功能组织起来。
- 延长时间必须通过学习、反馈和技能迁移变成能力复利。
- 日历寿命必须转化为可支配、可恢复、可行动的有效时间。
- 医疗、住房、学习、工具和恢复资源需要财务入口与冲击缓冲。
- 工作系统同时塑造收入、风险暴露、压力、学习机会和恢复边界。
- 主体判断依赖可信信息、证据链和抗误导的信息环境。

这些方向不能被简单塞进 `cognitive-augmentation/`、`resource-social-infra/` 或 `governance-rights/`，因为它们有独立机制、数据源、失败模式和伦理边界。

## Decision

新增第八波 6 个主体代理与任务资源研究域：

- `attention-executive-control/`
- `learning-skill-acquisition/`
- `time-allocation-effective-time/`
- `financial-resilience-access/`
- `occupational-work-design/`
- `information-integrity-trust/`

每个域先只创建 `README.md` 和 `AGENTS.md`，不创建空数据、脚本或复杂目录。

## Consequences

- Human Infra 可以更准确表达“寿命延长的二阶效应”：注意力、学习轮次、有效时间、财务缓冲、工作环境和信息判断共同决定主体能否把更长时间转化为更大可能性空间。
- `research-domain-atlas.md`、`research-domain-radar.md` 和 `domain-map.md` 增加第八波域的先验位置、来源信号和禁止用途。
- 仓库结构检查脚本把第八波目录和文件纳入必需项。

## Non-goals

- 不提供 ADHD、心理、神经诊断治疗、药物、补剂、神经刺激或个体注意力增强建议。
- 不提供个体教育、考试、就业、移民、职业规划、劳动争议、工伤、薪酬、福利、保险、税务、投资或借贷建议。
- 不提供政治操控、舆论操纵、平台规避、假账号、虚假内容生产、传播策略或社工式影响手段。
- 不新增生产率压榨、员工监控、组织控制或把主体变成产出机器的方案。
