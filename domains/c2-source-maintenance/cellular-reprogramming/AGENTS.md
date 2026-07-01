# cellular-reprogramming 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cellular-reprogramming` |
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


`domains/c2-source-maintenance/cellular-reprogramming/` 保存细胞重编程与表观遗传年轻化谱系。它关注“细胞状态能否被安全、可控、可测量地重写”，不是人体抗衰疗法指南。

## 目录结构

```text
cellular-reprogramming/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑的域边界、证据等级、非目标和第一批来源线索。
- `AGENTS.md`：记录本目录职责、允许新增的材料类型和安全边界。

## 职责边界

- 本域研究细胞身份、表观遗传年龄、组织功能、重编程风险和主体持续性的关系。
- 本域可以整理论文、综述、商业公告、临床试验入口和机制图，但必须保留来源和证据等级。
- 本域不承载长寿干预证据账本；具体干预证据、临床试验和药品安全归 `domains/c1-boundary-rewriting/longevity-evidence/`。
- 本域不承载实验协议、载体设计、剂量、给药、细胞培养步骤或人体应用建议。

## 维护规则

- 新增资料前先判断它属于机制谱系、证据账本还是医疗安全边界；机制谱系留在本域，证据账本转到 `longevity-evidence/`。
- 任何主张必须区分体外细胞、动物、局部器官、人体安全性试验和人体疗效。
- 任何“年轻化”表述必须同时审查细胞身份保持、去分化风险、肿瘤风险和长期功能终点。
- 不把商业融资、平台宣传或早期安全性试验写成疗效已经成立。
- 若新增文件或子目录，必须同步更新本文件的目录结构和文件职责。
