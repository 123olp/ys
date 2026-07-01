# campus-safety-title-ix-clery-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/campus-safety-title-ix-clery-continuity` |
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


本目录承载校园安全、Title IX 和 Clery 连续性研究域，关注高校安全报告、支持措施、公开数据和权利程序如何保护学生持续学习与恢复。

## 目录结构

```text
campus-safety-title-ix-clery-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义校园安全、Title IX、Clery、报告机制和支持性措施如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料必须优先回到 ED OCR、Campus Safety and Security Data、Clery materials、高校 annual security report 和 Title IX/public safety 政策。
- 不写个人报案、投诉、证据保存、法律策略、安全计划、纪律申诉、危机处置或校园警务建议。
- 涉及伤害和事件资料时，只讨论公开制度变量、报告断点和权利边界，不处理个人事件、身份、位置或证据。
- 新增指标必须注明口径：reported crime、timely warning、supportive measure、grievance process、retaliation 或 campus climate。
