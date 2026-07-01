# glaucoma-visual-field-protection-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/glaucoma-visual-field-protection-continuity` |
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

- 维护青光眼视野保护连续性的研究边界、变量表、证据入口和禁止用途。
- 将视神经损伤、眼压、视野缺损、随访频率、治疗连续性和功能后果整理为 Source Card、机制链和模型变量。
- 与 `vision-eye-health-continuity/`、`medication-reconciliation-regimen-adherence-continuity/`、`fall-risk-prevention-home-safety-continuity/` 保持边界清晰。

## 非目标

- 不提供诊断、眼压或视野报告解释、药物/激光/手术建议、驾驶许可、工作许可或个体风险判断。
- 不替代眼科、验光、低视力康复、药师或交通安全评估。

## 上游

- `vision-eye-health-continuity/`：视觉输入和眼健康总框架。
- `healthcare-access-continuity/`：眼科随访和服务可及性。
- `medication-reconciliation-regimen-adherence-continuity/`：长期治疗连续性的通用执行层。

## 下游

- `transportation-access-mobility/`：视野丢失与移动/驾驶参与。
- `fall-risk-prevention-home-safety-continuity/`：空间扫描与跌倒风险。
- `low-vision-rehabilitation-assistive-technology-continuity/`：不可逆视觉损失后的补偿路径。
