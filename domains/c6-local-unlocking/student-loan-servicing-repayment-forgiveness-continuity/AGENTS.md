# 学生贷款服务、还款与减免连续性目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/student-loan-servicing-repayment-forgiveness-continuity` |
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
student-loan-servicing-repayment-forgiveness-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义学生贷款服务、还款计划、减免、宽限和记录连续性如何影响主体教育资本与未来选择权。
- `AGENTS.md`：说明本域维护边界和禁止用途。

## 维护规则

- 只沉淀学生贷款服务机制、还款记录、减免规则、违约风险和证据边界，不写个案借款、还款或减免策略。
- 涉及美国制度时优先使用 Federal Student Aid、U.S. Department of Education、CFPB 和官方消费者金融资料。
- 不把本域写成贷款申请、PSLF 教程、债务逃避、收入造假、就业证明造假、金融规划、法律或个案争议建议。
