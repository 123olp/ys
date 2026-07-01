# tinnitus-sound-tolerance-sleep-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/tinnitus-sound-tolerance-sleep-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
| 路径真相源 | `domains/_possibility-space-control/classification.tsv` |
| 复核状态 | `heuristic-v0.1` |

### 文件职责

- `README.md` 面向读者，说明研究对象、Human Infra 价值链路、证据边界、非目标和下一步资料入口。
- `AGENTS.md` 面向维护者和代理，说明目录结构、上下游依赖、禁止事项、更新规则和验证要求。

### 更新规则

- 修改本域对象、边界或上下游关系时，必须同步检查 README、AGENTS 和分类表中的 `physical_path`。
- 新增资料优先沉淀为 Source Signals、Source Cards、Claim-Evidence Matrix 或明确的证据段落，不把未经核验的摘要写成稳定结论。
- 若发现当前层级不符合“可能性空间控制力”标尺，先修改 `_possibility-space-control/rubric.md` 或 `classification.tsv`，再移动目录。

### 禁止事项

- 不把研究域写成个体行动处方、临床建议、法律建议、投资建议、工程操作手册或规避规则指南。
- 不在本目录保存无来源、无边界、无证据等级的断言。
- 不绕过父级 C1-C6 物理目录直接在 `domains/` 根目录新增正式研究域。
<!-- domain-agent-contract:end -->


## 职责

- 维护耳鸣、声音耐受和睡眠连续性的研究边界、变量表、证据入口和禁止用途。
- 将耳鸣烦扰、听觉敏感、睡眠中断、注意力负担和心理交叉资料整理为 Source Card、机制链和模型变量。
- 与 `hearing-auditory-communication-continuity/`、`sleep-circadian-recovery/`、`depression-mood-functioning-continuity/` 保持边界清晰。

## 非目标

- 不提供诊断、药物、补剂、设备、声音疗法参数、产品推荐、急症判断或个体预后。
- 不替代耳鼻喉、听力学、睡眠医学、心理健康、神经或急诊专业服务。

## 上游

- `hearing-auditory-communication-continuity/`：听觉沟通总框架。
- `noise-induced-hearing-loss-prevention-continuity/`：噪声暴露和听觉损伤背景。
- `sleep-circadian-recovery/`：睡眠恢复总框架。

## 下游

- `attention-focus-cognitive-bandwidth/`：耳鸣与注意力占用。
- `time-allocation-effective-time/`：耳鸣烦扰造成的有效时间损耗。
- `mental-health-emotional-regulation/`：长期烦扰和情绪负担。
