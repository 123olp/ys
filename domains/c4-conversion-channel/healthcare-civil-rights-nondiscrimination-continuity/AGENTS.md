# healthcare-civil-rights-nondiscrimination-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/healthcare-civil-rights-nondiscrimination-continuity` |
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


## 职责

本目录承载医疗民权、反歧视、Section 1557、语言和残障权利、医疗公平和投诉边界资料。

## 边界

- 只研究医疗制度中的民权保护、变量和结构性排除。
- 不提供法律意见、歧视认定、投诉代写、身份判断、诉讼策略或机构合规认证。
- 不保存受保护身份、PHI、投诉证据、机构通信、移民状态、宗教、性别或残障资料。

## 结构

```text
healthcare-civil-rights-nondiscrimination-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分医疗质量差异、民权保护、语言可及、残障便利和个案法律争议。
- 涉及个体歧视、投诉、身份、隐私或法律判断的内容必须转回官方渠道和专业人员。
