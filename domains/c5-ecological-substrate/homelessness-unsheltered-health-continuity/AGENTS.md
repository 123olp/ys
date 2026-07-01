# homelessness-unsheltered-health-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/homelessness-unsheltered-health-continuity` |
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


本目录维护无家可归、露宿状态与健康连续性域。它是 Human Infra 的“没有稳定住所时主体是否仍被接住”层，负责住房缺失如何连锁影响健康、身份、安全、福利和恢复。

## 目录结构

```text
homelessness-unsheltered-health-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明露宿、庇护、住房服务、外展、医疗、卫生、安全和福利入口如何影响主体持续性。
- 本域只做公开无家可归、住房连续性、外展、公共卫生和社区服务资料整理。
- 不提供个体庇护、住房申请、法律救济、福利申请、露宿规避、执法规避或生存技巧。

## 维护规则

- 新增材料必须区分住房稳定、庇护服务、街头外展、医疗连续性、身份文件和安全暴露。
- 不把无家可归状态写成个人失败、城市治理目标或治安问题。
- 涉及具体地点和弱势人群时，禁止提供可用于定位、骚扰、驱逐或剥削的信息。
