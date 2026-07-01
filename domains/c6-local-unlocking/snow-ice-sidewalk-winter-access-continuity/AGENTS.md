# snow-ice-sidewalk-winter-access-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/snow-ice-sidewalk-winter-access-continuity` |
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


本目录承载雪冰、人行道冬季通行与季节性可达连续性研究域，关注寒冷季节公共路径是否仍能支撑医疗、食物、工作、学校和照护任务。

## 目录结构

```text
snow-ice-sidewalk-winter-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 只整理雪冰、除雪责任、冻融、公交站阻挡和冬季行人通行如何影响执行连续性。
- 不提供除雪操作、融雪剂配方、法律责任判断、投诉代写、雇佣服务建议、医疗建议或个案路线。
- 不收集住址、轨迹、照片、残障证明、医疗资料、物业资料或罚单材料。

## 维护规则

资料优先回到 CDC、FHWA、FTA、ADA.gov 和地方公共工程/交通资料。保持与 `winter-storm-cold-exposure-power-continuity/` 和 `walking-bicycling-micromobility-continuity/` 的边界清晰。
