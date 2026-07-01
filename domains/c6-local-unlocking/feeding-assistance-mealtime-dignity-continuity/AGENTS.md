# feeding-assistance-mealtime-dignity-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/feeding-assistance-mealtime-dignity-continuity` |
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

- 维护进食协助、用餐环境、照护时间、辅助工具、摄入量和尊严的研究边界。
- 将长期照护、CMS、ASHA、营养、职业治疗和尊严资料整理为 Source Card。
- 与 `caregiving-long-term-care/`、`dignity-personhood-respect-continuity/` 和 `texture-modified-diet-thickened-liquid-continuity/` 保持边界清晰。

## 非目标

- 不提供喂食技巧、姿势、速度、饮食质地、培训方案、护理处置、机构合规判断或虐待判定。
- 不替代护理、营养、言语语言治疗、职业治疗、长期照护监管或法律服务。

## 上游

- `swallowing-dysphagia-aspiration-nutrition/`：吞咽与营养入口总框架。
- `caregiving-long-term-care/`：照护系统。

## 下游

- `dignity-personhood-respect-continuity/`：人格尊严和关系体验。
- `home-delivered-meals-congregate-nutrition-services-continuity/`：送餐/集体餐服务。
