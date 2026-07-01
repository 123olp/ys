# residential-solid-waste-collection-bin-sanitation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/residential-solid-waste-collection-bin-sanitation-continuity` |
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


本目录承载住宅固废收运、垃圾桶卫生和日常残余物流出连续性研究域，关注家庭废弃物如何在不破坏居住卫生和行动能力的情况下离开家庭空间。

## 目录结构

```text
residential-solid-waste-collection-bin-sanitation-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义生活垃圾、回收物、垃圾桶、收运服务、错过收运和家庭任务空间之间的连续性链路。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、市政固废部门、公共卫生部门和多户住宅/物业公开规则。
- 不写非法倾倒、焚烧、规避收费、规避执法、隐私资料丢弃、垃圾混入或邻里冲突操作建议。
- 新增指标必须注明口径：废物流、容器状态、收运频率、错过收运、气味/害虫、可达性或任务空间影响。
- 涉及危险废物、锐器、药品、电池、电子废弃物或灾后碎片时，必须转接到对应专门域。
