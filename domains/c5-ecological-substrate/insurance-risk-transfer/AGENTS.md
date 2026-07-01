# insurance-risk-transfer 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/insurance-risk-transfer` |
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


`insurance-risk-transfer/` 是 Human Infra 的保险与风险转移域，负责研究高成本风险如何通过保险、赔付、担保和风险池被制度性分摊。

## 目录结构

```text
insurance-risk-transfer/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义保险与风险转移域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做覆盖、保费、自付、理赔、拒赔、风险池、保障缺口和制度性风险分摊资料整理。
- 个体投保、理赔、税务、法律、投资、福利、财务规划和保险规避不属于本域。

## 上下游关系

- 上游：`financial-resilience-access/`、`occupational-work-design/`、`legal-identity-civil-registration/`。
- 下游：`healthcare-access-continuity/`、`emergency-preparedness-response/`、`social-protection-benefits-delivery/` 和 `housing-built-environment-stability/`。

## 维护规则

- 新增资料必须说明它影响覆盖、保费、自付、免赔额、理赔、拒赔、等待期、风险池还是保障缺口。
- 禁止输出个体保险选择、理赔策略、规避或欺诈方法。
