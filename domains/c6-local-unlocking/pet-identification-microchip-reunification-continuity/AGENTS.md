# pet-identification-microchip-reunification-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pet-identification-microchip-reunification-continuity` |
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


本目录承载宠物身份识别、微芯片、登记和失主重聚连续性资料。它关注宠物关系对象如何被系统识别和找回，不做个案寻宠或所有权判断。

## 结构

```text
pet-identification-microchip-reunification-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分身份识别、登记更新、收容扫描、重聚流程、隐私、诈骗和家庭纠纷边界。
- 资料优先回到 AVMA、FEMA/Ready.gov、地方动物控制公开资料和收容系统公开标准。
- 不保存微芯片号、地址、电话、GPS、宠物照片、收容记录、家庭纠纷或私人寻宠线索。
