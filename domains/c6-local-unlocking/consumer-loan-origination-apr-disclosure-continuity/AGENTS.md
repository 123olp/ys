# 消费贷款发放、APR 披露与还款义务连续性目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/consumer-loan-origination-apr-disclosure-continuity` |
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


## 目录结构

```text
consumer-loan-origination-apr-disclosure-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义消费贷款发放、APR 披露、费用、还款计划和服务连续性如何影响主体跨期资源。
- `AGENTS.md`：说明本域维护边界和禁止用途。

## 维护规则

- 只沉淀消费贷款机制、披露要求、还款义务、服务转移和证据边界，不写个案贷款申请或还款策略。
- 涉及美国制度时优先使用 CFPB、FTC、Federal Reserve 和官方消费者金融资料。
- 不把本域写成贷款推荐、再融资建议、逃债、虚假申请、规避信用审查、金融规划、法律或个案催收建议。
