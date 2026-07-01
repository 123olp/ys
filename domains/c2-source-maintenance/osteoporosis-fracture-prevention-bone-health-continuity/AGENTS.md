# osteoporosis-fracture-prevention-bone-health-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/osteoporosis-fracture-prevention-bone-health-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


本目录维护骨质疏松筛查、骨折风险、治疗坚持和骨折后功能恢复资料。它是主体在跌倒后长期失能、机构化和有效时间损失之前的结构性风险控制域。

## 目录结构

```text
osteoporosis-fracture-prevention-bone-health-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义骨质疏松筛查、骨折风险、治疗坚持、跌倒接口和骨折后恢复如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案骨密度、影像、跌倒史、骨折史、用药、体重或诊疗资料。
- 资料进入本域时必须保留筛查对象、损害收益权衡、行动结局、康复接口和禁止用途。

## 上下游关系

- 上游来自 USPSTF、NIH/NIAMS、BHOF 和骨健康资料。
- 下游服务 `musculoskeletal-integrity/`、`fall-risk-prevention-home-safety-continuity/` 和康复功能建模。
- 不替代医生、骨科、内分泌科、康复团队、物理治疗或个体医疗建议。

## 维护规则

- 不写骨密度解读、补剂、药物、运动、跌倒训练、影像、骨折处理、手术或个体建议。
- 不把系统级骨健康研究写成个人骨折风险工具。
- 新增变量必须区分筛查、风险识别、治疗可及、坚持、跌倒接口和骨折后恢复。
