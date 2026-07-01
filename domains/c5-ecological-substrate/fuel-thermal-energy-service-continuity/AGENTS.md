# Fuel Thermal Energy Service Continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/fuel-thermal-energy-service-continuity` |
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


本目录承载燃料、取暖、制冷和热能服务连续性研究，关注外部能源系统如何维持可居住、可照护、可恢复的热环境。

## 目录结构

```text
fuel-thermal-energy-service-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究取暖燃料、燃气、液体燃料、丙烷、区域能源、热泵、备用燃料、关键设施热负荷和热服务恢复。
- 上游连接能源安全、燃料供应、价格、配送、天气、电网和设备维护；下游连接住房、温度韧性、医疗设施、食品药品冷链和家庭恢复。
- 不提供燃烧设备、燃料储存、管线、锅炉、热泵、发电机、区域能源操作、采购、维修、改装、交易或规避建议。

## 维护规则

- 燃料与热能资料必须保持在公开政策、统计、消费者教育和风险治理层面。
- 不记录可用于破坏、盗取、规避或危险操作能源设施和燃烧设备的细节。
- 涉及实时燃料短缺、取暖/制冷危机或设备危险时，只链接官方和专业机构入口。
