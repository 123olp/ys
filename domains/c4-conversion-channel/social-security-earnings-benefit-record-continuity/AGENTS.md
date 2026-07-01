# social-security-earnings-benefit-record-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/social-security-earnings-benefit-record-continuity` |
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


本目录承载社会保险收入记录、工作 credits 和福利记录连续性资料。它研究几十年的劳动和缴费历史如何在老年、失能或家庭风险边界转化为稳定保障。

## 目录结构

```text
social-security-earnings-benefit-record-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分收入记录、工作 credits、账户访问、福利声明、记录纠错、代表收款和身份保护。
- 本域不保存个人社会保险、收入、税务或福利资料，不提供申领、申诉、退休策略、残障、Medicare、法律、财务或移民建议。

## 维护规则

- 引用资料优先来自 SSA、官方社会保险机构、税务机构和社会保险研究。
- 必须保留资格边界、个人建议边界、身份保护、记录纠错、代表收款保护和反欺诈边界。
- 不把福利记录连续性写成确定收益承诺，也不输出任何操纵资格或冒用身份路径。
