# carbon-monoxide-alarm-combustion-appliance-safety-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/carbon-monoxide-alarm-combustion-appliance-safety-continuity` |
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


本目录承载一氧化碳报警、燃烧设备和停电备用能源安全连续性研究域，关注不可见暴露如何破坏主体判断和生命安全。

## 文件

```text
carbon-monoxide-alarm-combustion-appliance-safety-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 只整理官方资料、变量链路和非操作性边界。
- 不提供燃气维修、发电机使用、报警器安装、通风设计、急救、中毒诊断、现场处置、保险或法律建议。
- 不收集家庭地址、设备型号、报警记录、燃气系统照片、健康资料或位置数据。

## 上下游

- 上游：`energy-access-resilience/`、`fuel-thermal-energy-service-continuity/`、`household-emergency-preparedness-resilience/`。
- 下游：`chemical-safety-poison-control-toxicology/`、`emergency-preparedness-response/`、`housing-built-environment-stability/`。
