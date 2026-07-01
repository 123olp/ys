# community-resource-navigation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/community-resource-navigation` |
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


`domains/c5-ecological-substrate/community-resource-navigation/` 是 Human Infra 的社区资源导航域，负责把本地服务目录、社会需求筛查、转介和闭环回访建模为资源转化接口。

## 目录结构

```text
community-resource-navigation/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义社区资源导航、服务目录、社会需求转介、闭环回访和本地服务断点。
- 本域只做公开资料整理、变量建模、证据边界和资源导航机制分析。
- 个体资格判断、申请建议、机构推荐、资源实时可得承诺、危机替代和敏感需求数据处理不属于本域。

## 上下游关系

- 上游：`resource-social-infra/`、`health-literacy-navigation/`、`digital-inclusion-connectivity/` 和 `social-connection-relational-infra/`。
- 下游：`social-protection-benefits-delivery/`、`healthcare-access-continuity/`、`housing-built-environment-stability/` 和 `food-security-nutrition-access/`。

## 维护规则

- 新增资料必须说明它支持的是资源目录、筛查、匹配、转介、回访、人工协助、数据标准还是隐私治理变量。
- 不能把社区资源资料写成个体资格、申请、危机、医疗或法律建议。
