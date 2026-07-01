# caregiving-long-term-care 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/caregiving-long-term-care` |
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


`caregiving-long-term-care/` 是 Human Infra 的照护与长期照护域，负责研究主体失能、慢病、认知退行或生活支持需求出现后，照护网络是否能持续接住主体。

## 目录结构

```text
caregiving-long-term-care/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义照护与长期照护域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做照护系统、长期照护、照护者负担、照护连续性和尊严边界的资料整理。
- 个体护理计划、机构选择、保险福利、法律监护和医学处理不属于本域。

## 上下游关系

- 上游：`healthcare-access-continuity/`、`rehabilitation-functioning/`、`social-connection-relational-infra/`。
- 下游：`housing-built-environment-stability/`、`assistive-technology-access/`、`pain-suffering-control/` 和 `mental-health-affective-stability/`。

## 维护规则

- 新增资料必须标明它讨论的是照护需求、照护供给、照护者负担、长期照护质量还是照护转移。
- 禁止把照护资料改写成个体护理操作或机构选择建议。
