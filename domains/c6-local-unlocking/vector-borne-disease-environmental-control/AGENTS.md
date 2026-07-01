# vector-borne-disease-environmental-control 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/vector-borne-disease-environmental-control` |
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


本目录维护病媒传播疾病与环境控制域。它是 Human Infra 的“生态感染风险层”，负责蚊、蜱、蚤等病媒如何通过气候、水环境、动物宿主、住房、土地使用和公共卫生系统影响主体持续性。

## 目录结构

```text
vector-borne-disease-environmental-control/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明病媒传播疾病、生态环境、公共卫生监测、病媒控制和社区风险沟通如何支撑主体持续性。
- 本域只做公开疾病、环境控制、One Health、气候风险和公共卫生资料整理。
- 不提供个体诊断治疗、旅行医学、产品选择、农药操作、现场灭杀、动物处理、检疫规避或个人安全判断。

## 维护规则

- 新增材料必须区分蚊媒、蜱媒、蚤媒、动物宿主、气候水文、住房环境、监测预警、控制措施和生态副作用。
- 不把病例地图、模型、虫媒监测、气候预测或 AI 输出写成个体感染、旅行、居住或资产风险结论。
- 涉及农药、现场控制和公共卫生响应时，只写治理边界和证据，不写操作步骤。
