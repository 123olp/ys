# motion-sickness-transport-virtual-environment-tolerance-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/motion-sickness-transport-virtual-environment-tolerance-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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

- 维护运动病、模拟器病、VR/AR 不适、感官冲突、交通耐受和恢复时间的研究边界。
- 将交通、空间计算、模拟训练、远程协作和任务可用性资料整理为 Source Card。
- 与 `transportation-access-mobility/` 和 `human-factors-ergonomics-task-systems-continuity/` 保持边界清晰。

## 非目标

- 不提供药物、补剂、暴露训练、设备推荐、驾驶旅行许可、禁忌判断或个体耐受预测。
- 不替代临床、职业健康、交通安全、航空/海事医学或设备合规评估。

## 上游

- `vestibular-balance-spatial-orientation/`：前庭和平衡总框架。
- `human-factors-ergonomics-task-systems-continuity/`：人因和任务系统。

## 下游

- `transportation-access-mobility/`：交通服务可达。
- `personal-automation-integration-workflows-continuity/`：XR/远程工具的可用性约束。
