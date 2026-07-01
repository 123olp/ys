# portable-air-cleaner-room-filtration-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/portable-air-cleaner-room-filtration-continuity` |
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


本目录承载便携式空气清洁器与房间级过滤连续性研究域，关注家庭端局部空气恢复能力。

## 目录结构

```text
portable-air-cleaner-room-filtration-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义便携式空气清洁器、房间过滤、滤芯维护、噪声、电源和任务连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、CDC、ASHRAE、地方公共卫生和灾害室内空气资料。
- 不写产品排名、购买建议、CADR 处方、设备改装、房间安全认证或实时灾害判断。
- 新增指标必须注明口径：房间大小、过滤状态、滤芯状态、噪声、电源、使用时长、污染物类型或任务结果。
- 涉及野火、化学事故、感染暴发或医学风险时，必须保留撤离、公共卫生和医疗边界。
