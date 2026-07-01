# chronic-liver-disease-masld-mash-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/chronic-liver-disease-masld-mash-continuity` |
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


本目录维护 MASLD/MASH、慢性肝病、纤维化、肝硬化、肝癌风险和代谢共病资料。它关注隐匿肝病如何改变生命风险和有效时间。

## 目录结构

```text
chronic-liver-disease-masld-mash-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 MASLD/MASH 与慢性肝病如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、影像、饮酒、体重、糖尿病、药物或保险资料。
- 资料进入本域时必须保留病程阶段、纤维化风险、代谢共病、肝癌风险、药物安全和禁止用途。

## 上下游关系

- 上游来自 NIDDK、CDC、肝病学、代谢健康和肿瘤预防资料。
- 下游服务 `renal-hepatic-clearance/`、`obesity-adiposity-metabolic-risk-continuity/` 和肝癌预防模型。
- 不替代肝病科、消化科、内分泌、营养、药学、肿瘤、保险或个体医疗建议。

## 维护规则

- 不写个人肝功能、影像、纤维化、饮酒、药物、减重、补充剂、筛查周期或治疗建议。
- 不把 MASLD/MASH 资料写成个人风险评分或监测计划。
- 新增资料必须区分脂肪变、炎症、纤维化、肝硬化、失代偿、肝癌风险和代谢共病。
