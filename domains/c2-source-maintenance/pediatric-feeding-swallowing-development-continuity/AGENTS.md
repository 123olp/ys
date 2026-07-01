# pediatric-feeding-swallowing-development-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pediatric-feeding-swallowing-development-continuity` |
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

- 维护儿童摄食、吞咽、增长、感官负担、家庭压力和学校餐食参与的研究边界。
- 将儿科、ASHA、营养、学校和早期干预资料整理为 Source Card。
- 与 `developmental-language-disorder-child-communication-continuity/`、`wic-benefit-redemption-infant-maternal-nutrition-continuity/` 和 `school-meals-nutrition-access-continuity/` 保持边界清晰。

## 非目标

- 不提供儿童诊断、喂养计划、训练、质地调整、食物引入、学校服务资格、责任判断或个体风险评级。
- 不替代儿科、言语语言治疗、营养、职业治疗、学校护理或早期干预服务。

## 上游

- `swallowing-dysphagia-aspiration-nutrition/`：吞咽和营养入口总框架。
- `childcare-family-continuity/`：家庭照护连续性。

## 下游

- `school-meals-nutrition-access-continuity/`：学校餐食参与。
- `school-health-services-chronic-condition-continuity/`：学校健康支持边界。
