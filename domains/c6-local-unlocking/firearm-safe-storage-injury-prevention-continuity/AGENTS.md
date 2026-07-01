# firearm-safe-storage-injury-prevention-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/firearm-safe-storage-injury-prevention-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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


本目录承载枪支安全储存与伤害预防连续性研究域，关注高致死工具可及性如何进入主体持续性的公共卫生风险模型。

## 文件

```text
firearm-safe-storage-injury-prevention-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 只整理公共卫生证据、系统变量、政策评估边界和禁止用途。
- 不提供购买、持有、携带、操作、储存步骤、锁具选择、战术、自卫、绕过安全装置、法律或个体风险建议。
- 不收集武器型号、存放位置、家庭成员、地址、心理健康个案或暴力事件细节。

## 上下游

- 上游：`personal-safety-violence-prevention/`、`suicide-crisis-response-continuity/`、`child-protection-family-safety/`。
- 下游：`trauma-system-hemorrhage-control-continuity/`、`domestic-violence-coercive-control-safety-continuity/`、`risk-engineering/`。
