# eating-disorders-nutrition-body-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/eating-disorders-nutrition-body-continuity` |
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


本目录承载进食障碍、身体形象、营养风险和服务连续性资料。它关注身体供能、心理安全和主体尊严，而不是饮食控制或治疗建议。

## 结构

```text
eating-disorders-nutrition-body-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须避免体重、热量、审美、快速减重、补偿行为和可模仿危险行为的细节化表达。
- 必须区分公共教育、医疗风险、心理服务、营养安全、反污名和禁止用途。
- 不保存体重、照片、饮食记录、热量、身体尺寸、病历、家庭冲突、治疗记录或敏感身份资料。
