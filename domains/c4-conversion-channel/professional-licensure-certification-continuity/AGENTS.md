# professional-licensure-certification-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/professional-licensure-certification-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录承载职业执照、专业认证与注册资格连续性资料。它研究主体如何在制度中持续证明被授权执行某类高信任任务，以及执照失效、不可携带和纠错失败如何影响行动能力。

## 目录结构

```text
professional-licensure-certification-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分职业执照、专业认证、注册资格、继续教育、纪律记录、恢复机制和跨地区互认。
- 本域不保存个人执照资料，不解释个人资格，也不提供考试、申请、合规、法律、就业或纪律个案建议。

## 维护规则

- 引用资料优先来自劳工统计、职业执照查找、州/行业发证机构、标准组织和职业监管资料。
- 必须保留授权范围、公众安全、继续合规、惩戒透明、申诉和恢复边界。
- 不把职业资格写成规避监管、无证执业、身份冒用或考试作弊路径。
