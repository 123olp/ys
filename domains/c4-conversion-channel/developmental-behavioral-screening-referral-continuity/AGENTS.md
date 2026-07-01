# Developmental Behavioral Screening Referral Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/developmental-behavioral-screening-referral-continuity` |
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


本目录承载儿童发育监测、行为筛查、家庭观察、转介、早期干预和随访闭环资料。它处理发育信号进入支持系统的连续性，不处理个体诊断或训练方案。

## 目录结构

```text
developmental-behavioral-screening-referral-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 developmental monitoring、screening interface、caregiver observations、referral handoff、early intervention、language/culture access 和 child data boundary。
- 关注筛查信号是否能进入评估、转介、服务和家庭支持闭环。
- 不提供发育诊断、量表解释、治疗训练、学校安置、福利资格或育儿建议。

## 维护规则

- 新增资料优先引用 CDC、AAP、IDEA Part C、HRSA、教育和公共卫生公开资料。
- 涉及儿童发育、神经多样性、残障、家庭观察和学校记录时必须保留反污名和数据最小化边界。
- 不把筛查资料写成标签化、预测化或监控化儿童工具。
