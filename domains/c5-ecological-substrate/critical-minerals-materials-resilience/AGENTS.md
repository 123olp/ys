# critical-minerals-materials-resilience 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/critical-minerals-materials-resilience` |
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


本目录维护关键矿物、材料与韧性域。它是 Human Infra 的“未来技术物质输入层”，负责关键材料约束如何影响 AI、能源、医疗设备、制造和公共服务连续性。

## 目录结构

```text
critical-minerals-materials-resilience/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明关键矿物、关键材料、替代、回收和供应韧性如何影响主体持续性。
- 本域只做公开资源、政策、产业韧性、材料依赖和环境社会风险资料整理。
- 不提供投资、交易、采购、制裁规避、非法采矿、危险回收或受管制物资获取建议。

## 维护规则

- 新增材料必须区分资源储量、加工能力、供应集中、替代/回收、环境社会风险和技术依赖。
- 不把材料价格、矿业新闻或商业公告写成投资建议。
- 涉及危险材料处理或提取时，只写公共治理和安全边界，不写操作步骤。
