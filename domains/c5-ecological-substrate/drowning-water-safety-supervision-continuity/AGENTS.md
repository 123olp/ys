# drowning-water-safety-supervision-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/drowning-water-safety-supervision-continuity` |
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


本目录承载溺水、水域安全和监督连续性研究域，关注水域暴露如何成为分钟级主体中止风险。

## 文件

```text
drowning-water-safety-supervision-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 只整理系统级变量、公开来源、证据边界和模型链路。
- 不提供游泳、救援、复苏、活动许可、儿童监控、设备选择或个体安全建议。
- 涉及儿童和家庭水域时不得收集影像、定位、健康史、游泳能力或家庭布局资料。

## 上下游

- 上游：`personal-safety-violence-prevention/`、`parks-recreation-green-space-access-continuity/`、`water-sanitation-hygiene-continuity/`。
- 下游：`trauma-system-hemorrhage-control-continuity/`、`respiratory-oxygenation/`、`functioning-quality-of-life-outcomes/`。
