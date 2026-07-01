# Postpartum Care Recovery Follow Up Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/postpartum-care-recovery-follow-up-continuity` |
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


本目录承载产后照护、恢复、随访、并发症延续管理、警示信号、医保覆盖、家庭支持和转回 primary care 资料。它处理连续性和系统接口，不处理个体产后医疗决策。

## 目录结构

```text
postpartum-care-recovery-follow-up-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 postpartum visit、ongoing care、warning signs、coverage、referral、family/work load 和 primary care transition。
- 关注产后高风险窗口是否被医疗、家庭和工作系统接住。
- 不提供症状分诊、用药、伤口、复工、运动、哺乳、避孕、心理危机或急诊建议。

## 维护规则

- 新增资料优先引用 ACOG、CDC、HRSA、CMS、NIH/NICHD、WHO 或公开母婴健康资料。
- 保留产后隐私、心理健康、家庭暴力、工作歧视、保险覆盖和照护负担边界。
- 不把公共资料转化为个人恢复计划或风险判断。
