# pharmaceutical-quality-supply-integrity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/pharmaceutical-quality-supply-integrity` |
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


本目录维护药品质量、制造与供应完整性域。它是 Human Infra 的“治疗物质质量层”，负责药品制造质量、假劣药、污染、短缺、追溯和供应完整性。

## 目录结构

```text
pharmaceutical-quality-supply-integrity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明药品质量、GMP、污染、假劣药、短缺、冷链、追溯和召回如何影响主体持续性。
- 本域只做公开药品质量、制造监管、供应完整性和风险治理资料整理。
- 不提供药品购买、制备、复配、检测、进口、商业采购、个体用药或非法渠道建议。

## 维护规则

- 新增材料必须区分药品可及、药品质量、上市后安全和供应链连续性。
- 不把药品短缺、召回或监管公告写成个人治疗或采购建议。
- 涉及制造、检测、冷链或仓储时，只写监管和质量体系，不写操作步骤。
