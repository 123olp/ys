# personal-knowledge-management-cognitive-offloading 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/personal-knowledge-management-cognitive-offloading` |
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


本目录维护个人知识管理与认知卸载域。它是 Human Infra 的“外部记忆与项目上下文”层，负责笔记、检索、知识库、AI 助手和工作流如何降低认知摩擦并提升长期创造能力。

## 目录结构

```text
personal-knowledge-management-cognitive-offloading/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明个人知识管理、认知卸载、外部记忆、检索和 AI 协作如何进入主体持续性模型。
- 本域只做公开资料整理和证据边界维护。
- 不提供隐私抓取、账号接入、版权规避、监控方案、医疗/法律/财务建议或具体工具背书。

## 维护规则

- 新增资料必须区分笔记系统、知识库、AI 检索、代理工作流和主体记忆连续性。
- 涉及 AI 辅助时，必须记录来源、可追溯性、幻觉风险、权限边界和人工复核要求。
- 不把外部知识系统写成意识替代，不把自动总结当作事实源。
