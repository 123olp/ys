# Runaway Homeless Youth Outreach Shelter Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/runaway-homeless-youth-outreach-shelter-continuity` |
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


本目录承载离家与无家可归青年外展、短期庇护、转接和发展连续性资料。它是 Human Infra 中“青少年到成年转变连续性”的安全入口之一。

## 目录结构

```text
runaway-homeless-youth-outreach-shelter-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录离家/无家可归青年、街头外展、basic center、transitional living、家庭调解、教育医疗转介和隐私安全边界。
- 关注服务是否能可信接住青年，而不是个案行动指导。
- 不提供逃离路线、庇护所定位、家庭冲突处理、危机处置、法律、医疗、移民或心理建议。

## 维护规则

- 新增资料必须优先使用 ACF、Youth.gov、HUD、SAMHSA、CDC 或地方公共服务公开资料。
- 涉及未成年人时必须写清隐私、位置、身份、家庭关系和安全边界。
- 不把宣传性服务口号当作效果证据；必须区分制度入口、服务模型、评估数据和个案叙事。
