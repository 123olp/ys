# home-hvac-filter-maintenance-indoor-air-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/home-hvac-filter-maintenance-indoor-air-continuity` |
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


本目录承载家庭 HVAC 滤网维护与室内空气连续性研究域，关注滤网维护如何把空气过滤、设备运行和家庭任务连接起来。

## 目录结构

```text
home-hvac-filter-maintenance-indoor-air-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 HVAC 滤网、滤网状态、气流、室内空气负荷和家庭任务连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、DOE、ASHRAE、公共卫生和住房运行资料。
- 不写 HVAC 拆装、风管改造、电气操作、产品推荐、滤网处方、维修教程或现场验收。
- 新增指标必须注明口径：滤网类型、维护状态、气流影响、颗粒物/过敏原负荷、居住者任务或恢复结果。
- 涉及哮喘、COPD、过敏、烟雾或感染暴露时，必须保留医疗和公共卫生边界。
