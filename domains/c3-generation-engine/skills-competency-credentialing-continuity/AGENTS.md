# skills-competency-credentialing-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/skills-competency-credentialing-continuity` |
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


本目录承载技能、胜任力与微证书连续性资料。它研究主体如何把真实能力、作品经验和训练结果转成可比较、可组合、可携带的证明，而不是只依赖学历或岗位名称。

## 目录结构

```text
skills-competency-credentialing-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分技能本体、胜任力框架、微证书、数字徽章、测评可靠性、作品证据和平台互操作。
- 本域不保存个人技能档案，不评估个人能力，也不提供求职包装、测评作弊、证书购买或培训推荐。

## 维护规则

- 引用资料优先来自 O*NET、Credential Engine、标准组织、教育评估研究和公开技能框架。
- 必须保留测评有效性、偏差、可携带性、平台锁定、隐私和反伪造边界。
- 不把技能凭证写成就业承诺、能力排名、自动录用依据或规避筛查方法。
