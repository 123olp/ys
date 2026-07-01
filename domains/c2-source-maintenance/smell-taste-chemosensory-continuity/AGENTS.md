# smell-taste-chemosensory-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/smell-taste-chemosensory-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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

- 维护嗅味觉、化学感知、危险识别、食欲和生活质量的研究边界、证据入口、变量表和禁止用途。
- 将嗅觉障碍、味觉障碍、危险气味、营养影响和生活质量资料整理为 Source Card。
- 与 `sensory-continuity/`、`food-safety-contamination-control/`、`nutrition-metabolic-health/`、`chemical-safety-poison-control-toxicology/` 保持边界清晰。

## 非目标

- 不提供诊断、感染判断、神经退行判断、治疗、补剂、药物、嗅觉训练或个体风险结论。
- 不替代耳鼻喉、神经、营养、心理、公共安全或环境安全专业服务。

## 上游

- `sensory-continuity/`：跨感官反馈上位域。
- `chemical-safety-poison-control-toxicology/`：化学危险和中毒响应。
- `food-safety-contamination-control/`：食品污染和系统性控制。

## 下游

- `nutrition-metabolic-health/`：食欲、摄入和饮食质量。
- `mental-health-affective-stability/`：情绪和生活质量。
- `household-emergency-preparedness-resilience/`：家庭替代警报和危险识别。
