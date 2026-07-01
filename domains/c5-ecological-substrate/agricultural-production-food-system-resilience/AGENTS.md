# Agricultural Production Food System Resilience

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/agricultural-production-food-system-resilience` |
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


本目录承载农业生产与食物系统韧性研究，关注食物供给在进入市场和家庭之前的生产底座。

## 目录结构

```text
agricultural-production-food-system-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究农业生产、作物、畜牧、灌溉、种子、肥料、劳动力、设备和气候适应。
- 上游连接土壤、水资源、生态服务、天气气候和关键投入品；下游连接食物安全、供应链和宏观稳定。
- 不提供个体农业操作、农药兽药使用、投资、贸易、投机或监管规避建议。

## 维护规则

- 新增资料必须说明其尺度：全球、国家、区域、农场、供应链或家庭。
- 农业产量、粮价和气候情景必须标明不确定性，不写成确定预测。
- 涉及食品、动物、环境、劳动和贸易规则时，只做公共研究索引，不做具体合规建议。
