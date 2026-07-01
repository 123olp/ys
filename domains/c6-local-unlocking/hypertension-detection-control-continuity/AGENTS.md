# hypertension-detection-control-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/hypertension-detection-control-continuity` |
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


本目录维护高血压检测、确认、长期控制和随访连续性资料。它是主体在卒中、心衰、肾衰和高血压危象之前的上游风险控制域。

## 目录结构

```text
hypertension-detection-control-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义高血压筛查、测量质量、确认、控制率和长期坚持如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案血压、用药、病史、检查、设备或位置资料。
- 资料进入本域时必须保留筛查对象、测量条件、确认路径、随访责任、证据强度和禁止用途。

## 上下游关系

- 上游来自 USPSTF、CDC、NHLBI 和高血压控制项目资料。
- 下游服务 `cardiovascular-resilience/`、`hypertensive-crisis-end-organ-risk-continuity/` 和肾脏风险建模。
- 不替代医生、护士、药师、急诊、远程监测服务或个体医疗建议。

## 维护规则

- 不写血压读数判断、降压药、剂量、家庭处理、设备选择、检查排序、急诊分诊或治疗建议。
- 不把系统级血压控制研究写成个人健康管理工具。
- 新增变量必须区分筛查、确认、控制、坚持、随访和靶器官预防阶段。
