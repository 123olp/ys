# education-record-transcript-verification-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/education-record-transcript-verification-continuity` |
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


本目录承载教育记录、成绩单与学历核验连续性资料。它研究学习历史如何成为未来教育、就业、执照和服务入口的证明层，以及记录错误、隐私边界和核验断点如何影响主体持续性。

## 目录结构

```text
education-record-transcript-verification-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分教育记录访问、更正、授权披露、学历核验、学校关闭记录转移和数字凭证。
- 本域不保存个人教育记录，不解释个人成绩单，也不提供升学、就业、移民、法律、认证或背景调查个案建议。

## 维护规则

- 引用资料优先来自教育主管部门、FERPA/学生隐私资源、学校记录管理、标准组织和官方数据系统。
- 必须保留学生隐私、授权披露、记录更正、身份匹配和反伪造边界。
- 不把教育记录核验写成学历背书、申请策略、排名判断或绕过背景调查的方法。
