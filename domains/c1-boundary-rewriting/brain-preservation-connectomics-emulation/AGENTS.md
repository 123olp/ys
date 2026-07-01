# brain-preservation-connectomics-emulation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/brain-preservation-connectomics-emulation` |
| 所属层级 | `C1` - 可能性边界改写层 |
| 父级容器 | `domains/c1-boundary-rewriting` |
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


本目录维护脑保存、连接组学和全脑仿真假设。它是人格信息连续性的远期审查域，不是上传技术承诺。

## 目录结构

```text
brain-preservation-connectomics-emulation/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义脑信息保存、连接组读取、全脑仿真和身份连续性如何进入 Human Infra。
- 本目录不保存脑保存操作、遗体处理流程、神经数据采集方案或上传执行路线。
- 资料必须区分神经科学事实、保存技术、连接组测量、仿真假设和身份哲学争议。

## 上下游关系

- 上游来自神经科学、连接组学、脑保存、显微成像、计算神经科学和人格同一性哲学。
- 下游服务去具身中枢、冷冻保存、数字连续性、记忆编辑和主体连续性理论。
- 不替代 `biostasis-cryopreservation/`；本目录聚焦大脑信息可保存、可读取和可仿真性。

## 维护规则

- 不声称上传、数字永生或全脑仿真已经可行。
- 不提供脑保存操作、人体实验、遗体处理或神经采集步骤。
- 新增案例必须标注证据阶段、保存尺度、读取能力、身份假设和伦理边界。
