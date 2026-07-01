# adult-day-services-supervision-transport-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/adult-day-services-supervision-transport-continuity` |
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


本目录维护成人日间服务、日间监督、活动参与、餐食、交通和照护者喘息连续性资料。它是长期照护执行层，不是服务推荐或个人照护计划入口。

## 目录结构

```text
adult-day-services-supervision-transport-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义 adult day services 如何影响白天监督、社交参与、交通、照护者时间和居家持续性。
- 本目录只整理公开制度资料、服务机制、变量和边界。
- 不保存个人健康、认知、行为、地址、交通、照护者、保险或支付资料。

## 维护规则

- 新增资料必须区分 adult day services、home care、respite、senior center、congregate meals 和机构长期照护。
- 不推荐具体机构、项目、路线或个人安排。
- 不输出资格判断、福利申请、护理操作、医疗判断或安全监督方案。
