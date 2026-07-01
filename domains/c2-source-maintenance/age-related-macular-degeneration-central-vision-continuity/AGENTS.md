# age-related-macular-degeneration-central-vision-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/age-related-macular-degeneration-central-vision-continuity` |
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

- 维护 AMD 中央视觉连续性的研究边界、变量表、证据入口和禁止用途。
- 将黄斑状态、中央视力、阅读速度、面孔识别、治疗随访和低视力衔接整理为 Source Card、机制链和模型变量。
- 与 `vision-eye-health-continuity/`、`low-vision-rehabilitation-assistive-technology-continuity/`、`digital-accessibility-assistive-design/` 保持边界清晰。

## 非目标

- 不提供诊断、影像解释、注射治疗、补剂、复查间隔、驾驶/工作资格或个体预后判断。
- 不替代眼科、视网膜专科、低视力康复、药师或照护团队。

## 上游

- `vision-eye-health-continuity/`：视觉输入总框架。
- `aging-frailty-resilience/`：老年功能和照护风险背景。
- `healthcare-access-continuity/`：视网膜专科和长期随访可及性。

## 下游

- `low-vision-rehabilitation-assistive-technology-continuity/`：中央视力损失后的补偿路径。
- `personal-knowledge-management-cognitive-offloading/`：外部记忆和读写辅助接口。
- `time-allocation-effective-time/`：阅读与精细任务摩擦。
