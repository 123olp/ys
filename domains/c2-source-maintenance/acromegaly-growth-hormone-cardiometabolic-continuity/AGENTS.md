# acromegaly-growth-hormone-cardiometabolic-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acromegaly-growth-hormone-cardiometabolic-continuity` |
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


本目录维护肢端肥大症、GH/IGF-1 过量、心血管代谢、睡眠呼吸、关节软组织和长期监测资料。它关注缓慢激素过量如何侵蚀结构稳定和行动质量。

## 目录结构

```text
acromegaly-growth-hormone-cardiometabolic-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义肢端肥大症如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、影像、照片、睡眠报告、处方、手术、血压血糖、关节影像或保险资料。
- 资料进入本域时必须保留 GH/IGF-1 过量、诊断延迟、心血管代谢、睡眠呼吸、关节软组织和禁止用途。

## 上下游关系

- 上游来自 NIDDK、MedlinePlus、垂体、睡眠、心血管、代谢和骨关节资料。
- 下游服务 `pituitary-disorders-hormone-axis-continuity/`、`sleep-disordered-breathing-screening-treatment-continuity/`、`cardiovascular-resilience/` 和骨关节功能模型。
- 不替代内分泌科、神经外科、睡眠医学、心血管、骨科、药师、保险或个体医疗建议。

## 维护规则

- 不写个人 IGF-1/GH 判读、MRI 判读、睡眠报告、手术、放疗、药物、并发症筛查或外貌判断建议。
- 不把肢端肥大症资料写成照片诊断、治疗选择或术后管理流程。
- 新增资料必须区分激素状态、诊断延迟、并发症负担、治疗连续性、监测边界和功能结果。
