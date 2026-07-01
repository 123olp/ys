# personal-safety-violence-prevention 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/personal-safety-violence-prevention` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


`personal-safety-violence-prevention/` 是 Human Infra 的人身安全与暴力预防域，负责研究暴力、胁迫、犯罪伤害和受害者支持如何影响主体持续性。

## 目录结构

```text
personal-safety-violence-prevention/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义人身安全与暴力预防域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做暴力预防、求助入口、受害者服务、法律保护、医疗/心理创伤支持和恢复路径资料整理。
- 自卫战术、武器、报复、跟踪、监控、定位、危险对抗和专业服务替代不属于本域。

## 上下游关系

- 上游：`risk-engineering/`、`social-connection-relational-infra/`、`digital-identity-security/`。
- 下游：`access-to-justice-legal-aid/`、`housing-built-environment-stability/`、`mental-health-affective-stability/`、`healthcare-access-continuity/`。

## 维护规则

- 新增资料必须说明它影响暴力类型、求助入口、隐私、转介、医疗创伤支持、法律保护、住房安全还是恢复连续性。
- 禁止输出自卫、武器、报复、跟踪、监控、定位、危险对抗或破坏求助路径的信息。
