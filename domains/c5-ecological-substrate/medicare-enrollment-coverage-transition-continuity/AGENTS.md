# medicare-enrollment-coverage-transition-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/medicare-enrollment-coverage-transition-continuity` |
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


本目录维护 Medicare 参保窗口、覆盖选项和制度转换连续性域。它是 Human Infra 的晚年/残障医疗支付转换层，不是 Medicare 计划选择或销售建议入口。

## 目录结构

```text
medicare-enrollment-coverage-transition-continuity/
├── AGENTS.md
└── README.md
```

## 职责

- 记录 Medicare enrollment periods、coverage options、Part D、MA、Medigap 和 transition risk。
- 区分制度转换研究、个体计划选择、保险销售、理赔账单和医疗建议。
- 保留 Medicare.gov、CMS 和公开政策资料的来源与边界。

## 维护规则

- 新增资料必须说明覆盖类型、窗口、适用边界和非目标。
- 不保存 Medicare number、SSN、药物清单、医生名单、收入资产或保险凭证。
- 不输出 plan comparison、个案参保建议、SEP 判断、罚金判断或申诉策略。
