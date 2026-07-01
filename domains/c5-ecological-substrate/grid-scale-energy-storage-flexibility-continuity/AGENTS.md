# grid-scale-energy-storage-flexibility-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/grid-scale-energy-storage-flexibility-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录维护电网级储能与灵活性连续性资料。它关注能源系统的时间缓冲、调度和关键服务保障。

## 目录结构

```text
grid-scale-energy-storage-flexibility-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义储能、需求响应、灵活负荷和备用容量如何影响主体持续性。
- 本目录不保存安装方案、消防操作、投资建议、套利策略、项目报价或危险操作步骤。

## 上下游关系

- 上游来自 DOE、NREL、IEA、Sandia 和公开电网灵活性资料。
- 下游服务关键服务、数据中心、医疗、通信、交通和住房环境控制。
- 不替代 `electric-grid-reliability-resilience-continuity/`；本目录关注灵活性和时间缓冲。

## 维护规则

- 必须记录储能类型、持续时长、服务角色、安全边界和退化风险。
- 不把储能容量直接等同于韧性或主体收益。
