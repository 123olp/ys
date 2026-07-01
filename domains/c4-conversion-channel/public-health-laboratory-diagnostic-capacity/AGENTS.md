# public-health-laboratory-diagnostic-capacity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-health-laboratory-diagnostic-capacity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录维护公共卫生实验室与诊断能力域。它是 Human Infra 的“风险确认层”，负责把不可见风险转化为可审查、可行动、可治理的检测信号。

## 目录结构

```text
public-health-laboratory-diagnostic-capacity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明公共卫生实验室、诊断网络、质量管理、检测时效和实验室扩容如何支撑主体持续性。
- 本域只做系统能力、证据边界和治理资料整理。
- 不新增样本处理、检测协议、病原操作、生物安全规避、个体诊断或医疗建议。

## 维护规则

- 新增材料必须标明来源、适用场景、证据等级和禁止用途边界。
- 实验室方法只允许以非操作性、高层系统能力语言描述。
- 涉及病原、毒物、危险样本或实验室安全的内容，优先收敛到治理、质量、报告和中止条件。
