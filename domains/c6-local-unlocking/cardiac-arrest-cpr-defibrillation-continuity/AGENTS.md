# cardiac-arrest-cpr-defibrillation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/cardiac-arrest-cpr-defibrillation-continuity` |
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


本目录维护心脏骤停、CPR、AED/除颤和复苏系统资料。它是主体从分钟级死亡边界返回的急性救援域。

## 目录结构

```text
cardiac-arrest-cpr-defibrillation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义心脏骤停救援链如何影响主体持续性、脑灌注和未来选择权。
- 本目录只维护研究框架、变量和证据边界，不保存个案急救记录、心电图、定位、视频或身份资料。
- 资料进入本域时必须保留来源、对象、系统层级、可逆时间窗、结局指标和禁止用途。

## 上下游关系

- 上游来自 AHA、CDC CARES、EMS 系统、复苏科学和公共 AED 资料。
- 下游服务 `emergency-medical-services-prehospital-care/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和急性死亡风险建模。
- 不替代官方急救培训、EMS、医生、医院、公共安全机构或个人医疗建议。

## 维护规则

- 不写 CPR/AED 操作教程或个案急救判断。
- 不把“公共知识整理”写成实时急救指令。
- 若新增系统绩效字段，必须同步更新索引和安全边界。
