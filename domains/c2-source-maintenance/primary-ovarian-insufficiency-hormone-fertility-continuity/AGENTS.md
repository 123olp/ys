# primary-ovarian-insufficiency-hormone-fertility-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/primary-ovarian-insufficiency-hormone-fertility-continuity` |
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


本目录维护原发性卵巢功能不全、卵巢激素、生育窗口、骨骼心血管风险、心理社会负担和长期监测资料。它关注 POI 如何影响身体自主、未来选择权和长期健康风险。

## 目录结构

```text
primary-ovarian-insufficiency-hormone-fertility-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 POI 如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、遗传结果、月经记录、妊娠资料、生育计划、ART records、处方、骨密度或保险资料。
- 资料进入本域时必须保留激素状态、生育不确定性、骨骼/心血管接口、心理社会负担、ART/生育保存边界和禁止用途。

## 上下游关系

- 上游来自 MedlinePlus、NICHD、妇科内分泌、生殖、骨骼和心血管资料。
- 下游服务 `menstrual-health-cycle-literacy-continuity/`、`reproductive-fertility-continuity/`、`fertility-preservation-gamete-embryo-cryostorage-continuity/` 和中年健康模型。
- 不替代妇科、生殖内分泌、遗传咨询、骨骼、心血管、心理健康、保险或个体医疗建议。

## 维护规则

- 不写个人 FSH/AMH/雌激素/遗传结果判读、激素治疗、生育保存、IVF、供卵、避孕、骨密度或补剂建议。
- 不把 POI 资料写成生育治疗、激素方案、伴侣沟通或身份危机处置脚本。
- 新增资料必须区分激素状态、生育不确定性、长期健康风险、心理社会负担和功能结果。
