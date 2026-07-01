# inflammatory-bowel-disease-digestive-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/inflammatory-bowel-disease-digestive-continuity` |
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


本目录维护炎症性肠病、消化道炎症、营养吸收、flare、用药监测和生活参与资料。它关注 IBD 如何长期消耗体力、有效时间和社会参与。

## 目录结构

```text
inflammatory-bowel-disease-digestive-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义炎症性肠病如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、内镜、化验、药物、营养、学校/工作或保险资料。
- 资料进入本域时必须保留疾病类型、flare、营养/贫血、药物风险、手术路径、参与结果和禁止用途。

## 上下游关系

- 上游来自 NIDDK、CDC、消化病学、免疫学、营养和慢病照护资料。
- 下游服务 `gastrointestinal-barrier-absorption/`、`immune-maintenance/`、`iron-deficiency-anemia-oxygen-carrying-continuity/` 和参与支持模型。
- 不替代消化科、营养、药学、外科、学校/工作便利、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、内镜/化验判读、饮食、药物、生物制剂、免疫抑制、手术、flare 或疫苗建议。
- 不把 IBD 资料写成个人治疗或营养流程。
- 新增资料必须区分 Crohn 病、溃疡性结肠炎、疾病活动、并发症、治疗风险和功能结果。
