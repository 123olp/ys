# chemical-safety-poison-control-toxicology 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chemical-safety-poison-control-toxicology` |
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


本目录维护化学安全、中毒控制与毒理响应域。它是 Human Infra 的“化学暴露治理层”，负责化学风险、毒物中心、毒理证据和监管边界。

## 目录结构

```text
chemical-safety-poison-control-toxicology/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明化学品安全、中毒控制、毒物中心、毒理证据和暴露治理如何支撑主体持续性。
- 本域只做公开安全、监管、毒理和系统能力资料整理。
- 不提供中毒处理、解毒、化学混配、合成、投毒、规避检测或实时事故处置建议。

## 维护规则

- 新增材料必须区分家庭、职业、环境、消费品、工业和事故暴露。
- 任何涉及剂量、处理、清理或现场处置的内容必须改写为官方求助入口和非操作性边界。
- 不写任何可用于制造、扩大、隐藏或规避化学危害的步骤。
