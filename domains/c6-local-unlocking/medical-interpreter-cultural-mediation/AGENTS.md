# medical-interpreter-cultural-mediation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medical-interpreter-cultural-mediation` |
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


本目录维护医疗解释、语言可达与文化中介域。它是 Human Infra 的“临床理解和同意接口”层，负责语言、文化和沟通障碍如何影响主体持续性。

## 目录结构

```text
medical-interpreter-cultural-mediation/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明医疗解释、语言协助、CLAS、文化中介和知情同意理解如何进入主体持续性模型。
- 本域只做公开资料整理和边界维护。
- 不提供实时医疗解释、临床文本权威翻译、同意书法律解释、个体医疗/保险/移民/法律建议或文化标签化判断。

## 维护规则

- 新增资料必须区分一般语言可达、医疗解释、文化适宜服务、健康素养和法律同意。
- 涉及医疗文本和紧急场景时，必须明确机器翻译和 AI 总结不能替代专业解释服务。
- 不把语言、文化、族群或移民状态写成风险归因或服务排除理由。
