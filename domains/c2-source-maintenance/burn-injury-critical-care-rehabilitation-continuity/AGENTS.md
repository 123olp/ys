# burn-injury-critical-care-rehabilitation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/burn-injury-critical-care-rehabilitation-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


本目录维护烧伤重症、烧伤中心、皮肤屏障重建和长期康复资料。它是身体边界急性毁损后的救援与重建研究域。

## 目录结构

```text
burn-injury-critical-care-rehabilitation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义烧伤如何影响皮肤屏障、感染、疼痛、功能、身份和长期行动能力。
- 本目录只维护系统级资料和证据边界，不保存伤口照片、身份、定位、病历、事故证据或康复个案资料。
- 资料进入本域时必须保留严重程度、照护阶段、功能结局、心理社会负担和禁止用途。

## 上下游关系

- 上游来自 WHO、American Burn Association、CDC、防火、创伤和康复资料。
- 下游服务 `skin-barrier-wound-healing/`、`trauma-system-hemorrhage-control-continuity/`、`rehabilitation-functioning/` 和长期功能恢复建模。
- 不替代 EMS、烧伤中心、医生、护士、康复师、心理支持、法律、保险或个体医疗建议。

## 维护规则

- 不写烧伤急救、伤口处理、敷料、液体、止痛、抗感染、手术或瘢痕处理建议。
- 不收集或分析伤口照片和事故证据。
- 新增资料必须区分急性生存、重建、康复和长期社会参与。
