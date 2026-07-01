# biobanking-biospecimen-quality-chain-of-custody 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/biobanking-biospecimen-quality-chain-of-custody` |
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


本目录维护生物样本库、样本质量和保管链。它是生命科学证据从人体材料进入数据系统之前的物质可信层。

## 目录结构

```text
biobanking-biospecimen-quality-chain-of-custody/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义样本采集、预分析变量、冷链、追踪和保管链如何影响 Human Infra 证据质量。
- 本目录不保存样本数据、个人身份、实验 SOP 或可执行采样协议。
- 资料必须区分研究样本库、临床样本、公共资源标准和企业服务声明。

## 上下游关系

- 上游来自研究伦理、同意治理、样本库标准和生物安全资料。
- 下游服务多组学、生物年龄钟、癌症控制、细胞重编程和临床转化证据。
- 不替代 `blood-organ-tissue-biovigilance-transplantation/` 的临床供体安全和生物警戒职责。

## 维护规则

- 不提供非法采样、规避同意、样本匿名化绕行或生物安全规避策略。
- 不把样本质量指标写成个人诊断或治疗建议。
- 若新增样本相关结论，必须写明样本来源、处理条件、质量边界和适用对象。
