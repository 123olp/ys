# Pregnancy Loss Stillbirth Bereavement Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pregnancy-loss-stillbirth-bereavement-continuity` |
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


本目录承载妊娠丧失、死产、医疗交接、悲伤支持、工作学校调整、记录接口、文化仪式和后续妊娠咨询边界资料。它处理恢复与支持连续性，不处理个体医疗、法律或心理危机建议。

## 目录结构

```text
pregnancy-loss-stillbirth-bereavement-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 miscarriage、stillbirth、pregnancy loss、bereavement、work/school adjustment、records interface 和 peer support。
- 关注妊娠丧失后身体、心理、家庭、工作学校和未来计划的连续性。
- 不提供症状分诊、治疗、原因解释、再次怀孕、法律、请假、仪式、心理危机或责任判断。

## 维护规则

- 新增资料优先引用 CDC、ACOG、March of Dimes、NIH/NICHD、vital records 或公开心理支持资料。
- 涉及死亡、胎儿/新生儿、家庭关系、文化仪式和心理危机时必须保留高敏感边界。
- 不把支持资料转化为个体医学、法律、工作或精神健康建议。
