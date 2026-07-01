# cooking-ventilation-range-hood-indoor-air-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/cooking-ventilation-range-hood-indoor-air-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


本目录承载烹饪通风、抽油烟机与厨房室内空气连续性研究域，关注餐食任务如何在不放大空气负担的情况下持续。

## 目录结构

```text
cooking-ventilation-range-hood-indoor-air-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义烹饪排风、厨房空气污染、餐食准备和家庭任务连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、CDC、USFA、建筑运行、公共卫生和住房资料。
- 不写燃气维修、排风安装、电气改造、管道设计、火灾处置、CO 急救、产品推荐或个案安全认证。
- 新增指标必须注明口径：烹饪源、排风状态、污染物类型、厨房结构、使用频率、居住者任务或恢复结果。
- 涉及燃气泄漏、CO、火灾、食品安全或医学风险时，必须保留对应专业边界。
