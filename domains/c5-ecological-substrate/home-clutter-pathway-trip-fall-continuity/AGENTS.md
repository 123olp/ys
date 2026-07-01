# home-clutter-pathway-trip-fall-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-clutter-pathway-trip-fall-continuity` |
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


本目录承载家庭通道杂物、绊倒暴露与行动连续性研究域，关注日常物品流如何改变主体在家庭空间中的移动、安全和照护执行。

## 目录结构

```text
home-clutter-pathway-trip-fall-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义通道杂物、地面路径、临时堆放、绊倒暴露和家庭任务连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 CDC、NIA、公共卫生、职业治疗、消防通道和住房安全资料。
- 不写整理羞辱、收纳产品导购、家庭改造教程、跌倒急救、医疗诊断、照护监控、保险或法律建议。
- 新增指标必须注明口径：路径位置、物品类型、可见性、行动主体、任务场景、跌倒/延迟/回避后果。
- 涉及儿童、老人、残障者、术后恢复和独居者时，必须保留隐私、尊严和照护边界。
