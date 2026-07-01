# geospatial-navigation-location-infrastructure 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/geospatial-navigation-location-infrastructure` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录承载 Human Infra 中“空间定位、导航和位置基础设施”研究域。

## 结构

```text
geospatial-navigation-location-infrastructure/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义空间位置层如何影响主体持续性、关注对象、非目标、Source Signals 和下一步。
- 本目录只做公开资料整理、变量建模、边界说明和跨域接口，不放实时地图、导航服务、跟踪脚本或个人位置数据。

## 上下游关系

- 上游：`docs/reference/research-domain-atlas.md`、`docs/reference/domain-map.md`、`transportation-access-mobility/`、`emergency-alerts-communications/`、`community-resource-navigation/`。
- 下游：服务可达性、应急响应、灾后恢复、供应链、天气风险、公共服务和资源导航模型。

## 维护规则

- 公开结论必须回到官方测绘、导航、地理空间标准或公共数据来源。
- 不写跟踪、骚扰、目标定位、规避执法、危险路线或攻击基础设施内容。
- 涉及实时灾害、应急、交通或导航时，只做模型和来源索引，不替代官方系统。
