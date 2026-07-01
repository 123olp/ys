# cervical-cancer-hpv-prevention-screening-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cervical-cancer-hpv-prevention-screening-continuity` |
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


本目录维护宫颈癌 HPV 预防、筛查、异常追踪、阴道镜入口、生殖/性健康和公平可及资料。它是癌症控制与感染预防、性/生殖健康交叉的器官特异域。

## 目录结构

```text
cervical-cancer-hpv-prevention-screening-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 HPV 预防、宫颈筛查、异常结果闭环和生殖/性健康服务如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案 HPV、宫颈细胞学、阴道镜、病理、性史、生殖史或治疗资料。
- 资料进入本域时必须保留 HPV 预防、筛查对象、异常追踪、隐私污名、生殖健康和禁止用途。

## 上下游关系

- 上游来自 NCI、CDC 和宫颈癌/HPV 公开资料。
- 下游服务 `cancer-control/`、`sexual-health-sti-prevention-continuity/`、生殖健康和幸存者建模。
- 不替代医生、妇科、肿瘤科、病理科、疫苗服务、性健康服务、保险服务或个体医疗建议。

## 维护规则

- 不写个人 HPV/宫颈筛查结果解释、疫苗建议、筛查频率、阴道镜、病理、治疗、用药、手术或个体建议。
- 不把系统级宫颈癌研究写成 HPV 解释器、异常结果处理器、疫苗推荐器或商业检测推广。
- 新增变量必须区分 HPV 预防、筛查覆盖、异常追踪、隐私污名、生殖健康和公平性。
