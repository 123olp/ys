# hypogonadism-testosterone-sex-hormone-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/hypogonadism-testosterone-sex-hormone-continuity` |
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


本目录维护性腺功能低下、睾酮/性激素、青春期/成人阶段、骨骼肌肉、性功能、生育和长期监测资料。它关注性激素轴如何影响身体能力、关系参与和未来选择权。

## 目录结构

```text
hypogonadism-testosterone-sex-hormone-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义性腺功能低下如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、精液报告、处方、身体照片、青春期资料、性生活资料、伴侣或保险资料。
- 资料进入本域时必须保留性腺轴、阶段语境、骨骼肌肉影响、生育接口、商业夸大和禁止用途。

## 上下游关系

- 上游来自 MedlinePlus、内分泌、泌尿男科、生殖、骨骼肌肉和性健康资料。
- 下游服务 `endocrine-hormonal-regulation/`、`male-factor-infertility-sperm-health-continuity/`、`erectile-dysfunction-vascular-sexual-function-continuity/` 和骨骼肌肉模型。
- 不替代内分泌科、泌尿科、生殖专科、青春期医学、性医学、药师、保险或个体医疗建议。

## 维护规则

- 不写个人睾酮/LH/FSH/雌激素/精液判读、激素用药、剂量、补剂、健身、性功能或生育建议。
- 不把性腺功能低下资料写成 testosterone therapy、增肌、性表现或自我诊断流程。
- 新增资料必须区分中枢/性腺来源、年龄阶段、功能结果、治疗风险、商业误导和监测边界。
