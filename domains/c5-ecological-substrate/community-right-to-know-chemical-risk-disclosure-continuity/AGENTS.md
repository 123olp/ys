# community-right-to-know-chemical-risk-disclosure-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/community-right-to-know-chemical-risk-disclosure-continuity` |
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


`domains/c5-ecological-substrate/community-right-to-know-chemical-risk-disclosure-continuity/` 是 Human Infra 的社区化学风险知情权与披露连续性域，负责把设施报告和公共风险信息建模为准备、监督和信任基础设施。

## 目录结构

```text
community-right-to-know-chemical-risk-disclosure-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 EPCRA、TRI、Tier II、RMP、公众风险沟通和环境正义接口。
- 本域只整理公开制度、信息结构、使用边界和非操作性风险模型。
- 设施侦察、攻击、规避报告、骚扰、法律策略和实时事故判断不属于本域。

## 上下游关系

- 上游：`chemical-safety-poison-control-toxicology/`、`civic-data-open-government-transparency/`、`governance-rights/`。
- 下游：`chemical-release-shelter-evacuation-continuity/`、`social-determinants-community-vulnerability/`、`emergency-preparedness-response/`。

## 维护规则

- 新增资料必须说明它支持风险可见性、应急规划、公众沟通、环境正义还是治理边界。
- 不得写入敏感设施滥用、规避监管、恐慌传播、个体健康判断或法律建议。
