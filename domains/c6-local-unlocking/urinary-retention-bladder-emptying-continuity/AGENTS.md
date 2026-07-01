# urinary-retention-bladder-emptying-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/urinary-retention-bladder-emptying-continuity` |
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


`domains/c6-local-unlocking/urinary-retention-bladder-emptying-continuity/` 保存尿潴留和膀胱排空连续性研究资料。

## 职责

- 维护急性/慢性尿潴留、膀胱排空、梗阻、神经源性因素和设备依赖边界。
- 将排泄出口失败连接到疼痛、感染、肾脏压力、急性服务和行动中断。
- 保留来源、证据等级、非目标和禁止用途。

## 非目标

- 不提供导尿、用药、设备、检查解释、急诊分诊、护理操作或个体治疗建议。
- 不收集个人排尿日志、尿量、影像、尿流或可识别医疗资料。

## 上游

- `urogenital-continuity/`
- `renal-hepatic-clearance/`
- `neuro-continuity/`

## 下游

- `catheter-associated-uti-device-infection-continuity/`
- `acute-kidney-injury-renal-replacement-continuity/`
- `benign-prostatic-hyperplasia-luts-continuity/`
