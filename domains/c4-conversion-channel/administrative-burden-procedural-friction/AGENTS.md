# administrative-burden-procedural-friction 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/administrative-burden-procedural-friction` |
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


本目录承载行政负担、程序摩擦、证明成本、等待成本和制度任务成本如何消耗主体资源。

## 结构

```text
administrative-burden-procedural-friction/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只讨论制度流程的系统性负担，不处理个案申请、规避审核、福利策略或法律判断。
- 后续新增材料应优先是行政负担 Source Card、变量契约、失败模式和跨服务摩擦案例。

## 上下游关系

- 上游：`public-service-design-accessibility/`、`language-access-plain-communication/`、`digital-identity-security/`。
- 下游：`social-protection-benefits-delivery/`、`access-to-justice-legal-aid/`、`disaster-recovery-relief-continuity/`。
- 相邻域：`time-allocation-effective-time/`、`health-literacy-navigation/`、`community-resource-navigation/`。

## 维护规则

- 不提供个案申请、虚假证明、规避审核、福利、税务、法律或争议处理建议。
- 不把行政负担研究用于筛除、拒付、压制申诉或提高制度门槛。
- 若新增流程图、负担指标或案例，必须同步维护本文件和相关索引。
