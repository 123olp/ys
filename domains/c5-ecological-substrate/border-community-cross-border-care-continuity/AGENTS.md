# border-community-cross-border-care-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/border-community-cross-border-care-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录维护边境社区与跨境照护连续性域。它是 Human Infra 的“制度边界和跨境生活接口”层，负责边境交通、语言、公共卫生、医疗记录、家庭支持和身份边界如何影响主体持续性。

## 目录结构

```text
border-community-cross-border-care-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明边境社区、跨境家庭、公共卫生协作、医疗随访、记录和交通边界如何影响主体持续性。
- 本域只做公开边境社区健康、跨境公共卫生、服务可达、语言、交通和风险治理资料整理。
- 不提供个体移民、签证、入境、海关、旅行、跨境就医、药品、路线、执法规避或法律建议。

## 维护规则

- 新增材料必须区分公共卫生协作、医疗连续性、交通时间、语言文化、记录转移、家庭支持和法律边界。
- 不把边境社区写成身份推断、监控、政治宣传、路线建议或监管规避入口。
- 涉及移民、医疗、药品和执法边界时，只写结构性资料，不写个体操作建议。
