# 旅行保险、行程保障与理赔连续性目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/travel-insurance-trip-protection-claims-continuity` |
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
travel-insurance-trip-protection-claims-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义旅行保险、行程取消/中断、旅行医疗、撤离、行李和延误理赔如何影响离家恢复。
- `AGENTS.md`：说明本域维护边界和禁止用途。

## 维护规则

- 只沉淀旅行保险 coverage、covered reasons、documentation、claim 和投诉边界，不写个案购买或索赔策略。
- 涉及美国制度时优先使用 NAIC、U.S. DOT、州保险监管机构、State Department、CDC 和官方旅行资料。
- 不把本域写成保险推荐、退款策略、医疗转运建议、撤离建议、保险欺诈、重复索赔或法律建议。
