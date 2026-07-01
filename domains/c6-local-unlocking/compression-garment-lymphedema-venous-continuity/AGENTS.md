# compression-garment-lymphedema-venous-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/compression-garment-lymphedema-venous-continuity` |
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


本目录承载压迫衣物、淋巴水肿、静脉回流、适配替换、穿脱能力和皮肤风险连续性研究域，关注体液回流支持如何维持肢体功能。

## 目录结构

```text
compression-garment-lymphedema-venous-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义压迫用品和淋巴/静脉支持如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 NCI、MedlinePlus、Medicare、DME、淋巴水肿治疗、血管和伤口感染资料。
- 不写压迫等级、尺寸测量、包扎技术、产品选择、覆盖资格、治疗方案或个体诊断建议。
- 涉及皮肤破损、急性肿胀、感染或血栓风险时，只能写风险边界和转诊条件，不写处置步骤。
- 新增指标必须注明口径：适配、替换、穿脱能力、覆盖/费用、皮肤风险、感染风险或功能影响。
