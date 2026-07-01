# home-health-hospice-palliative-care-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-health-hospice-palliative-care-continuity` |
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


本目录维护居家医疗、缓和医疗、安宁疗护与临终连续性域。它是 Human Infra 的“严重疾病可承受持续性”层，负责症状、照护、目标和家庭支持如何不断线。

## 目录结构

```text
home-health-hospice-palliative-care-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明居家医疗、缓和医疗、安宁疗护、严重疾病照护和照护者支持如何影响主体持续性。
- 本域只做公开资料整理和边界维护。
- 不提供个体资格判断、临床决策、用药镇痛、护理操作、预立指示、保险福利、机构选择、法律或协助死亡建议。

## 维护规则

- 新增资料必须区分居家医疗、缓和医疗、安宁疗护、临终支持和普通长期照护。
- 涉及疼痛、症状、生命末期和家庭决策时，必须保留专业医疗、法律和危机服务边界。
- 不把尊严、目标照护或临终支持写成缩短生命、转嫁照护责任或放弃主体权利。
