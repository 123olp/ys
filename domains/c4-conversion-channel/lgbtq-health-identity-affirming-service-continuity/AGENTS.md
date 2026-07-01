# lgbtq-health-identity-affirming-service-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/lgbtq-health-identity-affirming-service-continuity` |
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


本目录维护 LGBTQ 健康、身份承认与肯定性服务连续性域。它是 Human Infra 的“身份承认和反歧视服务入口”层，负责健康、心理、家庭、学校、工作、住房、公共服务和隐私边界如何影响主体持续性。

## 目录结构

```text
lgbtq-health-identity-affirming-service-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明 LGBTQ 健康、身份承认、服务可达、民权、隐私、家庭和社区支持如何影响主体持续性。
- 本域只做公开 LGBTQ health、民权、服务可达、身份承认、隐私和社区支持资料整理。
- 不提供个体医疗、心理、性健康、转诊、身份文件、法律、学校、职场、家庭冲突或危机干预建议。

## 维护规则

- 新增材料必须区分健康服务、身份承认、民权保护、隐私安全、家庭社区支持和反歧视边界。
- 不做性取向、性别认同、家庭关系或风险状态推断，不写 outing、监控、画像或歧视性分类。
- 涉及医疗、心理、性健康、法律、学校和职场服务时，只写结构性资料，不写个体操作建议。
