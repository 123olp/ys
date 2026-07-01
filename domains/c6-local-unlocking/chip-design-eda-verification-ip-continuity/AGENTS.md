# chip-design-eda-verification-ip-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chip-design-eda-verification-ip-continuity` |
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


本目录维护芯片设计、EDA、验证和 IP 连续性资料。它关注算力硬件被制造之前的设计可信性。

## 目录结构

```text
chip-design-eda-verification-ip-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 EDA、验证、IP、ISA 和硬件设计供应链如何影响主体持续性。
- 本目录不保存芯片设计文件、专有 IP、EDA license、硬件攻击样例或商业采购资料。

## 上下游关系

- 上游来自公开硬件设计、EDA、ISA、验证和硬件安全资料。
- 下游服务半导体制造、AI 加速器、医疗设备、机器人和安全关键硬件。
- 不替代软件供应链域；本目录只处理硬件设计资产。

## 维护规则

- 资料进入本域时必须区分设计工具、验证方法、IP 许可、硬件安全和供应链来源。
- 不提供侵权、破解、后门、规避或攻击性硬件内容。
