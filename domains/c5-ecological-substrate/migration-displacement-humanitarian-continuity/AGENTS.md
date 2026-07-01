# migration-displacement-humanitarian-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/migration-displacement-humanitarian-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


`migration-displacement-humanitarian-continuity/` 是 Human Infra 的迁移、流离失所与人道连续性域，负责研究主体跨地点和跨制度移动后如何保持身份、服务、保护和未来路径。

## 目录结构

```text
migration-displacement-humanitarian-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义迁移、流离失所与人道连续性域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做难民、移民、国内流离失所、身份连续、健康/教育/住所/保护服务和人道协调资料整理。
- 个体移民、庇护、签证、身份、法律建议和危险迁移操作不属于本域。

## 上下游关系

- 上游：`legal-identity-civil-registration/`、`emergency-preparedness-response/`、`planetary-health-environment/`。
- 下游：`healthcare-access-continuity/`、`food-security-nutrition-access/`、`water-sanitation-hygiene-continuity/`、`access-to-justice-legal-aid/`。

## 维护规则

- 新增资料必须说明它影响身份、庇护、医疗、教育、住所、保护、家庭、数据连续性还是服务转介。
- 禁止输出移民/庇护个案建议、边境穿越路线、规避执法、伪造文件、危险旅行或偷渡方法。
