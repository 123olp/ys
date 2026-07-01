# ai-hardware-accelerator-performance-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-hardware-accelerator-performance-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


本目录维护 AI 硬件加速器性能连续性资料。它把模型能力落到硬件、能效、驱动和运行可得性。

## 目录结构

```text
ai-hardware-accelerator-performance-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AI 加速器、性能基准、能效、内存、互连和软件栈如何影响主体持续性。
- 本目录不保存硬件采购建议、供应商报价、云凭据、配额绕过、驱动破解或滥用算力方法。

## 上下游关系

- 上游来自 MLCommons、NIST AI、绿色软件和公开硬件评测资料。
- 下游服务 AI agent、AI 药物发现、科研仿真、个人 AI 工具和自动化系统。
- 不替代 AI 模型评测域；本目录只处理硬件执行层。

## 维护规则

- 每条资料必须区分训练、推理、边缘、数据中心和科研工作负载。
- 不把 benchmark 排名直接转化为项目价值判断。
