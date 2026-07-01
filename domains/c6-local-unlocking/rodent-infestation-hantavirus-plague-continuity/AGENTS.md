# Rodent Infestation Hantavirus Plague Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/rodent-infestation-hantavirus-plague-continuity` |
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


本目录承载啮齿动物侵入、污染和相关疾病风险如何影响居住连续性的研究资料。

## 文件

```text
rodent-infestation-hantavirus-plague-continuity/
├── AGENTS.md
└── README.md
```

- `README.md`：定义鼠害、啮齿动物污染、住房可用性和主体持续性边界。
- `AGENTS.md`：记录本目录职责、上下游和维护规则。

## 上游

- `../household-cleaning-disinfection-pest-control-continuity/`
- `../housing-built-environment-stability/`
- `../animal-health-zoonotic-interface-one-health/`

## 下游

- `../post-flood-mold-moisture-indoor-recovery-continuity/`
- `../emergency-food-water-storage-treatment-continuity/`
- `../chronic-infectious-disease-care-continuity/`

## 边界

不提供捕杀、毒饵、清理步骤、病原采样、动物处理、诊疗或施工方案。
