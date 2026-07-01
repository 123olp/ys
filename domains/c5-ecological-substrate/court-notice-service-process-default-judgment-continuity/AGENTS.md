# court-notice-service-process-default-judgment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/court-notice-service-process-default-judgment-continuity` |
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


`court-notice-service-process-default-judgment-continuity/` 是 Human Infra 的法院通知、送达与缺席判决连续性域，负责研究主体是否真正收到、理解并回应法律程序。

## 目录结构

```text
court-notice-service-process-default-judgment-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义法院通知、送达与缺席判决连续性域的对象、链路、非目标、来源信号和下一步。
- 本域只整理通知机制、程序可达、缺席风险和救济边界，不写个案法律策略。

## 维护规则

- 新增资料必须说明它影响送达、通知、地址质量、语言可达、无障碍、回应期限、缺席后果、执行路径还是救济机制。
- 优先使用 U.S. Courts、FRCP、NCSC、Legal Services Corporation、state court self-help 和法院官方资料。
- 禁止输出个案送达、答辩、撤销缺席判决、驱逐、债务、家庭法院、保护令或法律建议。
- 禁止指导躲避送达、伪造通知、隐藏地址、滥用程序、规避执行、骚扰当事人或干扰司法。
