# caregiver-training-skills-safety-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/caregiver-training-skills-safety-continuity` |
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


本目录维护家庭照护者训练、技能理解和安全边界资料。它关注培训机制和风险变量，不提供护理操作教学。

## 目录结构

```text
caregiver-training-skills-safety-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明照护者训练如何影响家庭照护质量、照护者损伤、被照护者安全和再入院风险。
- 本目录只整理公开培训机制、健康素养、任务边界和资料可及性。
- 不保存护理视频、家庭照片、病历、设备型号、个人照护计划或健康资料。

## 维护规则

- 新增资料必须区分训练机制、专业护理操作、出院教育、康复训练和医疗建议。
- 不输出转移技巧、药物管理、感染控制操作、设备操作、急救或个体安全方案。
- 涉及照护者能力时，必须保留专业评估、同意、尊严和非责备边界。
