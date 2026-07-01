# citizenship-nationality-statelessness-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/citizenship-nationality-statelessness-continuity` |
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


`citizenship-nationality-statelessness-continuity/` 是 Human Infra 的公民身份、国籍与无国籍连续性域，负责研究国家成员资格如何支撑主体被承认、被保护和跨境行动。

## 目录结构

```text
citizenship-nationality-statelessness-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义公民身份、国籍与无国籍连续性域的对象、链路、非目标、来源信号和下一步。
- 本域只沉淀公开制度资料、变量框架、证据边界和跨域接口。

## 维护规则

- 新增资料必须说明它影响国籍取得、国籍证明、自然化、无国籍风险、领事保护、家庭团聚还是服务入口。
- 优先使用 USCIS、State Department、UNHCR、UN Legal Identity Agenda、UNICEF 和各国官方资料。
- 禁止输出个案公民身份、国籍、自然化、无国籍、护照、签证、税务或法律建议。
- 禁止提供身份伪造、国籍规避、文件滥用、投票资格规避、移民欺诈或跨境制度绕过方法。
