# immigration-status-residency-work-authorization-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/immigration-status-residency-work-authorization-continuity` |
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


`immigration-status-residency-work-authorization-continuity/` 是 Human Infra 的移民身份、居留与工作授权连续性域，负责研究制度资格如何影响主体在所在地持续生活和行动。

## 目录结构

```text
immigration-status-residency-work-authorization-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义移民身份、居留与工作授权连续性域的对象、链路、非目标、来源信号和下一步。
- 本域只做制度变量、证据边界和跨域关系整理，不写个人移民操作方案。

## 维护规则

- 新增资料必须说明它影响居留资格、工作授权、身份续期、身份变更、雇佣核验、家庭派生资格还是服务入口。
- 优先使用 USCIS、DHS、State Department、I-9/E-Verify、IOM、OECD 和各国官方移民资料。
- 禁止输出签证、绿卡、居留、工作许可、身份变更、延期、申诉、雇佣、税务或法律建议。
- 禁止提供文件伪造、身份隐藏、执法规避、边境规避、签证滥用、雇佣核验绕过或危险迁移方法。
