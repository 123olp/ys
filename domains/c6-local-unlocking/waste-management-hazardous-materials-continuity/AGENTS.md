# waste-management-hazardous-materials-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/waste-management-hazardous-materials-continuity` |
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


本目录维护废弃物管理、危险材料与处置连续性域。它是 Human Infra 的“残余风险治理层”，负责防止废物、污染源和危险材料反向侵蚀主体持续性。

## 目录结构

```text
waste-management-hazardous-materials-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明废弃物系统、危险材料治理、医疗废物和处置连续性如何支撑栖居、公共卫生和环境安全。
- 本域只做公共系统、风险分类、服务连续性和治理资料整理。
- 不提供危险材料处理、处置、储存、运输、清理、规避监管或非法倾倒方法。

## 维护规则

- 新增材料必须区分固体废物、医疗废物、危险废物、污染控制和循环利用。
- 所有危险材料内容必须停留在非操作性、公共治理和服务连续性层。
- 涉及灾害或事故时，只描述系统接口和官方响应边界，不替代现场指挥。
