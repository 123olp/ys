# public-service-design-accessibility 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/public-service-design-accessibility` |
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


本目录承载公共服务设计、客户体验、无障碍、表单负担和公共数字服务入口如何影响主体持续性。

## 结构

```text
public-service-design-accessibility/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只讨论公共服务设计的系统性可达性，不处理个体申请、法律资格或服务结果。
- 后续新增材料应优先是服务设计 Source Card、流程变量和失败模式清单。

## 上下游关系

- 上游：`governance-rights/`、`digital-inclusion-connectivity/`、`language-access-plain-communication/`。
- 下游：`social-protection-benefits-delivery/`、`healthcare-access-continuity/`、`disaster-recovery-relief-continuity/`。
- 相邻域：`digital-identity-security/`、`time-allocation-effective-time/`、`community-resource-navigation/`。

## 维护规则

- 不提供个体申请策略、资格判断、申诉建议或法律意见。
- 不把数字化服务写成可以替代人工帮助和无障碍义务。
- 若新增服务流程图、模板或数据，必须同步维护本文件和相关索引。
