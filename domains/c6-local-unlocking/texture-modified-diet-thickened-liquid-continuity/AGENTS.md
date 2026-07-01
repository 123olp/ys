# texture-modified-diet-thickened-liquid-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/texture-modified-diet-thickened-liquid-continuity` |
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

- 维护食物质地、液体稠度、标准化标签、厨房执行和进食接受度的研究边界。
- 将 IDDSI、吞咽资料、营养资料和照护流程资料整理为 Source Card。
- 与 `oropharyngeal-dysphagia-swallow-safety-continuity/`、`prepared-food-restaurant-cafeteria-safety-access-continuity/` 和 `feeding-assistance-mealtime-dignity-continuity/` 保持边界清晰。

## 非目标

- 不提供个人饮食质地、稠化剂、菜单、吞咽训练、过敏处理、厨房操作或 IDDSI 等级建议。
- 不替代言语语言治疗、营养、护理、食品安全、餐饮或临床服务。

## 上游

- `swallowing-dysphagia-aspiration-nutrition/`：吞咽和营养入口总框架。

## 下游

- `prepared-food-restaurant-cafeteria-safety-access-continuity/`：公共熟食和餐饮执行。
- `food-safety-continuity`：食品安全资料边界。
