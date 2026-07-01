# perimenopause-menopause-midlife-health-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/perimenopause-menopause-midlife-health-continuity` |
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


本目录维护围绝经期、更年期、中年症状负担、骨骼、睡眠、情绪和工作参与资料。它关注中年阶段风险转轨如何影响长期主体持续性。

## 目录结构

```text
perimenopause-menopause-midlife-health-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义围绝经期和中年健康支持如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、月经、病史、用药、癌症风险、性健康或工作资料。
- 资料进入本域时必须保留症状对象、风险边界、共享决策、证据限制和禁止用途。

## 上下游关系

- 上游来自 NIA、HHS OWH、NIH 和更年期健康资料。
- 下游服务 `endocrine-hormonal-regulation/`、`osteoporosis-fracture-prevention-bone-health-continuity/` 和中年健康寿命模型。
- 不替代妇产科、内分泌、骨科、精神健康、药学、工作健康或个体医疗建议。

## 维护规则

- 不写个人激素治疗、补充剂、用药、检查排序、癌症/心血管风险判断、工作证明或治疗建议。
- 不收集或推断个体症状、性健康、癌症风险、用药、身份或工作敏感资料。
- 新增资料必须区分症状负担、长期风险、共享决策、工作参与和证据边界。
