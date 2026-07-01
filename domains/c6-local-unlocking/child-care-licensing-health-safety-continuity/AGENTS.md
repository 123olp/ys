# child-care-licensing-health-safety-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/child-care-licensing-health-safety-continuity` |
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


`child-care-licensing-health-safety-continuity/` 是 Human Infra 的托育许可、健康与安全执行域，负责研究许可、检查、健康安全标准和事件透明如何支撑儿童照护安全。

## 目录结构

```text
child-care-licensing-health-safety-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义托育许可健康安全域的对象、模型链路、非目标和来源信号。
- 本域只做制度、标准、指标和公开来源整理，不做托育机构认证、排名、推荐或事故判断。
- 禁止收集儿童照片、事故材料、监控影像、医疗记录、投诉材料、机构账号或身份信息。

## 上下游关系

- 上游：`childcare-family-continuity/`、`public-service-design-accessibility/`、`product-safety-recall-systems/`。
- 下游：`child-protection-family-safety/`、`infant-safe-sleep-suid-risk-reduction-continuity/`、`public-health-surveillance-immunization/`。

## 维护规则

- 新增资料必须说明它影响许可、检查、人员比例、背景审查、健康安全、事故预防、信息透明还是应急准备。
- 禁止输出机构合规判断、儿童安全处置、医疗建议、法律建议或家庭个案指导。
