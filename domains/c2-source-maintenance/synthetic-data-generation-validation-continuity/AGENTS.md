# synthetic-data-generation-validation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/synthetic-data-generation-validation-continuity` |
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


本目录维护合成数据生成、验证和边界治理资料。它是把稀缺或敏感数据转化为可审查研究材料前的验证层。

## 目录结构

```text
synthetic-data-generation-validation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义合成数据的隐私、效用、分布保真和下游风险如何影响主体持续性研究。
- 本目录只维护合成数据验证框架，不保存原始敏感数据、生成模型权重或可逆推断材料。
- 资料进入本域时必须保留原始数据边界、生成方法、隐私验证、效用验证和禁止用途。

## 上下游关系

- 上游来自 NIST、ICO、数据治理、隐私工程和合成数据评估资料。
- 下游服务 `ai-data-provenance-contamination-drift-continuity/`、`ai-evaluation-benchmark-validity-continuity/` 和仿真/模型验证页面。
- 不替代 `privacy-preserving-computation/`；该域关注计算机制，本目录关注合成数据产物验证。

## 维护规则

- 不记录重新识别、成员推断、隐私攻击或合成数据洗白方法。
- 不把合成数据写成自动匿名化或自动合规。
- 若新增合成数据字段影响 Source Card 或数据模板，必须同步更新索引。
