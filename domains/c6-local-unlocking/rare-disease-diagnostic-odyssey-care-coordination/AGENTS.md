# rare-disease-diagnostic-odyssey-care-coordination 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/rare-disease-diagnostic-odyssey-care-coordination` |
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


本目录维护罕见病诊断漫游与照护协调域。它是 Human Infra 的“低概率高复杂性疾病路径不断线”层，负责罕见病、未确诊疾病、专家网络和研究窗口如何影响主体持续性。

## 目录结构

```text
rare-disease-diagnostic-odyssey-care-coordination/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明罕见病、诊断漫游、基因检测、专家转诊、患者登记和孤儿药如何进入主体持续性模型。
- 本域只做公开资料整理和证据边界维护。
- 不提供个体诊断、遗传咨询、治疗建议、临床试验报名建议、患者组织背书或家族风险判断。

## 维护规则

- 新增资料必须区分诊断协调、研究登记、孤儿药、患者支持和真实治疗证据。
- 涉及基因检测、家族风险和未确诊疾病时，必须保留不确定性、适用对象和专业服务边界。
- 不把病例故事写成普遍治疗承诺，不把低患病率场景写成泛化个人风险预测。
