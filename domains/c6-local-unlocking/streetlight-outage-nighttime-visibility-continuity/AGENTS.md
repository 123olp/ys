# streetlight-outage-nighttime-visibility-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/streetlight-outage-nighttime-visibility-continuity` |
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


本目录承载路灯故障、夜间可见性与公共路径可读性连续性研究域，关注夜间出行、照护和公共服务可达如何受照明状态影响。

## 目录结构

```text
streetlight-outage-nighttime-visibility-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 只整理路灯、夜间可见性、照明故障报告和夜间路径可读性对行动连续性的影响。
- 不提供电气维修、灯杆操作、照明工程、安防部署、犯罪预测、路线建议或个案安全判断。
- 不收集夜间轨迹、位置历史、监控画面、照片元数据或执法资料。

## 维护规则

资料优先回到 FHWA、Open311、地方交通/公共工程和照明标准资料。保持与 `walking-bicycling-micromobility-continuity/` 和 `light-circadian-environment/` 的边界清晰。
