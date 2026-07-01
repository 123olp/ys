# community-health-workers-peer-support 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/community-health-workers-peer-support` |
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


本目录承载社区健康工作者、同伴支持者、导航员和可信社区中介如何把服务转化为实际支持。

## 结构

```text
community-health-workers-peer-support/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只讨论社区与同伴支持作为系统接口，不提供医疗、心理、法律、福利或危机个案建议。
- 后续新增材料应优先是角色模型、证据 Source Card、边界清单、培训监督和隐私风险。

## 上下游关系

- 上游：`healthcare-access-continuity/`、`health-literacy-navigation/`、`social-connection-relational-infra/`。
- 下游：`community-resource-navigation/`、`mental-health-affective-stability/`、`social-protection-benefits-delivery/`。
- 相邻域：`health-workforce-capacity/`、`patient-safety-organizational-learning/`、`caregiving-long-term-care/`。

## 维护规则

- 不提供诊断、治疗、用药、心理咨询、危机处理、个案转介或资格建议。
- 不把社区关系写成可替代专业服务、监督、报酬、隐私和制度责任的廉价方案。
- 若新增角色清单、培训框架或证据卡，必须同步维护本文件和相关索引。
