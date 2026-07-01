# ADR 0090: Add Eighty-Sixth-Wave Chronic Neuro, Neuromuscular, and Post-Infectious Continuity Domains

## Status

Accepted

## Date

2026-07-01

## Context

Human Infra 的先验追问已经把“有效永生 / 主体持续性最大化”拆成可维护的研究域。第八十五波补齐了慢性专科负担与功能恢复，但慢性神经退行、神经肌肉连接、运动神经元、脊髓通路和感染后长期状态仍容易被塞进一般 `neuro-continuity`、`musculoskeletal-integrity`、`immune-maintenance`、`respiratory-oxygenation`、`fatigue-risk-alertness-continuity` 或 `chronic-infectious-disease-care-continuity`。

这些对象有独立病程、功能结果、照护断点、证据体系和禁止用途边界。官方资料来源包括 NINDS 对 Parkinson's disease、Multiple Sclerosis、ALS、Huntington's disease、Spinal Muscular Atrophy、Muscular Dystrophy、Myasthenia Gravis、Spinal Cord Injury 的资料，以及 CDC 对 ME/CFS 和 Long COVID 的资料。

## Decision

新增第八十六波 10 个正式研究域：

- `domains/parkinsons-disease-movement-control-continuity/`
- `domains/multiple-sclerosis-demyelination-function-continuity/`
- `domains/amyotrophic-lateral-sclerosis-motor-neuron-continuity/`
- `domains/huntington-disease-genetic-neurodegeneration-continuity/`
- `domains/spinal-muscular-atrophy-motor-neuron-continuity/`
- `domains/muscular-dystrophy-progressive-weakness-continuity/`
- `domains/myasthenia-gravis-neuromuscular-junction-continuity/`
- `domains/spinal-cord-injury-paralysis-secondary-complications-continuity/`
- `domains/me-cfs-post-exertional-energy-limitation-continuity/`
- `domains/long-covid-post-acute-infection-continuity/`

每个域只创建 `README.md` 和 `AGENTS.md`。本轮不创建数据采集脚本、诊断工具、个人风险评分、疗法建议或医学决策系统。

## Consequences

- 慢性神经退行、神经肌肉和感染后状态进入 Human Infra 的主体持续性地图。
- 运动控制、脱髓鞘、运动神经元、遗传神经退行、神经肌肉接头、脊髓通路、能量限制和感染后多系统负担获得独立索引。
- 所有相关资料必须保留来源、证据边界和禁止用途。
- 仓库结构检查必须把 10 个新目录、20 个新域文件和本 ADR 纳入 required set。
