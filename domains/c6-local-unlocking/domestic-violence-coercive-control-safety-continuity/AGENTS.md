# domestic-violence-coercive-control-safety-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/domestic-violence-coercive-control-safety-continuity` |
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


本目录维护亲密伴侣暴力、家庭暴力与胁迫控制安全连续性域。它是 Human Infra 的“关系内部暴力不吞噬主体持续性”层，负责公开资料中的求助入口、服务转介、保密、住房、医疗、儿童和法律接口如何影响恢复能力。

```text
domestic-violence-coercive-control-safety-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 IPV/DV、胁迫控制、经济虐待、技术辅助控制、服务转介和安全连续性边界。
- `AGENTS.md`：说明本目录职责、禁止用途和上下游关系。

## 维护规则

- 新增资料必须优先来自 DOJ OVW、CDC、HHS、OVC、HUD 或同等公共机构。
- 必须区分公共资料整理与个案安全计划、法律策略、证据策略、庇护所定位。
- 不保存可识别受害者、家庭、儿童、庇护所、服务人员或施暴者的信息。
- 不输出跟踪、监控、定位、胁迫、报复、武器、自卫战术或规避执法内容。
