# immunization-public-health-surveillance 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/immunization-public-health-surveillance` |
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


`domains/c2-source-maintenance/immunization-public-health-surveillance/` 是 Human Infra 的免疫与公共卫生监测域，负责把疫苗、传染病监测、感染防控、AMR、One Health 和废水监测建模为群体风险屏障。

## 目录结构

```text
immunization-public-health-surveillance/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义免疫计划、传染病监测、公共卫生应急、感染防控和废水监测的对象、链路、非目标和来源信号。
- 本域只做公开公共卫生资料、变量模型、系统边界和禁止用途整理。
- 疫苗个体建议、诊断治疗、疫情预测保证、公共卫生规避、病原体操作和传播策略不属于本域。

## 上下游关系

- 上游：`immune-maintenance/`、`antimicrobial-resilience/` 和 `planetary-health-environment/`。
- 下游：`healthcare-access-continuity/`、`emergency-preparedness-response/`、`risk-engineering/` 和 `medicine-access-treatment-continuity/`。

## 维护规则

- 新增资料必须说明它支持的是免疫计划、病例监测、实验室网络、IHR、IPC、HAI、AMR、One Health、废水监测还是风险沟通。
- 不能把公共卫生资料写成个体医疗建议、规避策略或疫情确定性预测。
