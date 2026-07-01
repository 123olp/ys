# disaster-volunteer-donations-management-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-volunteer-donations-management-continuity` |
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


## 目录结构

```text
disaster-volunteer-donations-management-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 本域只研究志愿和捐赠协调机制，不发布实时需求、派遣、募捐、支付、库存或现场信息。
- 不保存捐赠者、受助者、志愿者、位置、路线、库存或安保资料。
- 所有内容必须优先指向官方或被认可的灾害志愿协调组织。

## 上下游关系

- 上游：`domains/c5-ecological-substrate/disaster-case-management-long-term-recovery-continuity/`。
- 下游：`domains/c5-ecological-substrate/volunteering-civic-service-participation-continuity/`、`domains/c5-ecological-substrate/food-bank-pantry-community-food-distribution-continuity/`。
