# language-access-plain-communication 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/language-access-plain-communication` |
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


`domains/c3-generation-engine/language-access-plain-communication/` 是 Human Infra 的语言可达与清晰沟通域，负责把关键服务材料的可理解性、语言服务和认知可访问性建模为行动能力入口。

## 目录结构

```text
language-access-plain-communication/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义清晰语言、语言可达、有限英语能力服务、CLAS、认知可访问性和理解失败风险。
- 本域只做公开资料整理、变量建模、证据边界和服务理解断点分析。
- 个体法律、医疗、移民、福利、就业材料解释，认证翻译替代和危机沟通替代不属于本域。

## 上下游关系

- 上游：`health-literacy-navigation/`、`digital-inclusion-connectivity/` 和 `governance-rights/`。
- 下游：`social-protection-benefits-delivery/`、`access-to-justice-legal-aid/`、`healthcare-access-continuity/`、`patient-data-interoperability/` 和 `labor-rights-workplace-protection/`。

## 维护规则

- 新增资料必须说明它支持的是 plain language、语言服务、文化适配、认知可访问性、风险沟通还是任务完成变量。
- 不能把清晰沟通写成删减风险、权利、证据边界或不确定性的许可。
