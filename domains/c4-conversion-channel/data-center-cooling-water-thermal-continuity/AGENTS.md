# data-center-cooling-water-thermal-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/data-center-cooling-water-thermal-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录维护数据中心冷却、水与热管理连续性资料。它关注算力设施的热约束和环境承载边界。

## 目录结构

```text
data-center-cooling-water-thermal-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义冷却、水耗、热密度、冗余和环境约束如何影响 AI 与数字服务连续性。
- 本目录不保存施工方案、冷却系统操作步骤、供应商报价、现场参数或许可建议。

## 上下游关系

- 上游来自 IEA、DOE、ASHRAE、OCP 和公开数据中心可持续资料。
- 下游服务 AI 算力、云服务、数字保存、科研计算和远程协作。
- 不替代 `compute-data-center-ai-infrastructure/`；本目录只拆冷却和热管理层。

## 维护规则

- 必须区分能源指标、水指标、可靠性指标和环境影响指标。
- 不把单一效率指标写成整体可持续结论。
