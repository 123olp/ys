# dry-eye-ocular-surface-comfort-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/dry-eye-ocular-surface-comfort-continuity` |
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

- 维护干眼眼表舒适连续性的研究边界、变量表、证据入口和禁止用途。
- 将眼表不适、视疲劳、屏幕耐受、室内环境、药物副作用和慢性有效时间负担整理为 Source Card、机制链和模型变量。
- 与 `vision-eye-health-continuity/`、`occupational-exposure-industrial-hygiene/`、`light-exposure-circadian-environment-continuity/`、`chronic-pain-functional-restoration-continuity/` 保持边界清晰。

## 非目标

- 不提供诊断、眼药水/药物/补剂建议、隐形眼镜适配、急症判断、产品推荐或个体治疗计划。
- 不替代眼科、验光、免疫/风湿、职业健康或环境评估。

## 上游

- `vision-eye-health-continuity/`：视觉输入总框架。
- `occupational-exposure-industrial-hygiene/`：工作环境暴露和屏幕任务背景。
- `medication-reconciliation-regimen-adherence-continuity/`：药物副作用资料边界。

## 下游

- `attention-focus-cognitive-bandwidth/`：眼表不适与注意力稳定。
- `time-allocation-effective-time/`：屏幕耐受和有效时间负担。
- `workplace-accommodation-return-to-work-continuity/`：工作环境调整和参与连续性。
