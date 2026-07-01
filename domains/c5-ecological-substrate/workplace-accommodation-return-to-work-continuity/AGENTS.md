# workplace-accommodation-return-to-work-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/workplace-accommodation-return-to-work-continuity` |
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


本目录维护工作场所合理便利、stay-at-work 和 return-to-work 连续性的资料与边界。

## 文件结构

```text
workplace-accommodation-return-to-work-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 描述功能状态变化后，工作系统如何通过任务调整、环境调整、辅助技术和阶段性复工接住主体。
- 本目录只做机制和资料研究，不做个人便利、法律、医疗、职业康复或雇主合规建议。
- 涉及给付和收入时链接到残障收入、工伤和带薪假域；涉及功能恢复时链接到康复和辅助技术域。

## 维护规则

- 新增资料必须区分公共法规、雇主实践、医学复工评估和职业康复资料。
- 不把“合理便利”写成固定清单；必须保留任务、环境、功能和法律辖区边界。
- 不输出个人申请、争议处理、雇主规避或医学证明操作建议。
