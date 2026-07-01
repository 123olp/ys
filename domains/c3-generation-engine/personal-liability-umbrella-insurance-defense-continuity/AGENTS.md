# 个人责任伞形保险与法律防御连续性目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/personal-liability-umbrella-insurance-defense-continuity` |
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


## 目录结构

```text
personal-liability-umbrella-insurance-defense-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义个人责任、伞形保险、法律防御成本、coverage dispute 和资产暴露如何影响主体未来选择权。
- `AGENTS.md`：说明本域维护边界和禁止用途。

## 维护规则

- 只沉淀责任保险、伞形保险、limits、defense costs、claim notice 和 coverage dispute 边界，不写个案投保或诉讼策略。
- 涉及美国制度时优先使用 NAIC、州保险监管机构、州法院公共资料和官方消费者资料。
- 不把本域写成保险推荐、法律防御建议、资产隐藏、判决规避、保险欺诈、诉讼策略或法律建议。
