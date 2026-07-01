# outpatient-laboratory-specimen-result-routing-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/outpatient-laboratory-specimen-result-routing-continuity` |
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


## 职责

本目录承载门诊检验医嘱、标本采集、结果回传和异常结果闭环资料，关注检测能力如何转化为主体可用的行动信号。

## 边界

- 只整理公开资料、机制、变量、证据边界和研究问题。
- 不解释检验结果、推荐检测、提供采样 SOP、诊断治疗、账单策略或认证规避。
- 不保存检验单、结果、病历、保险、标本标签、门户账号或个案健康资料。

## 结构

```text
outpatient-laboratory-specimen-result-routing-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分检验质量、标本执行、结果路由、患者访问和异常 follow-up。
- 个体检测、诊断、治疗和紧急异常结果问题必须回到医疗专业人员或急救渠道。
