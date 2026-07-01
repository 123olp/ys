# isolation-quarantine-work-school-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/isolation-quarantine-work-school-continuity` |
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


`domains/c5-ecological-substrate/isolation-quarantine-work-school-continuity/` 是 Human Infra 的隔离、检疫与工作学校连续性域，负责把传播阻断措施建模为生活系统和任务系统的约束。

## 目录结构

```text
isolation-quarantine-work-school-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义隔离、检疫、病假、返校返工、远程替代、照护交接和服务支持的对象、链路、非目标和来源信号。
- 本域只整理公开公共卫生和制度接口资料。
- 个体隔离命令、返校返工许可、雇佣法律、医疗建议、规避措施和证明伪造不属于本域。

## 上下游关系

- 上游：`outbreak-case-investigation-contact-tracing-continuity/`、`community-testing-screening-access-continuity/` 和 `immunization-public-health-surveillance/`。
- 下游：`school-workplace-outbreak-operations-continuity/`、`workplace-accommodation-return-to-work-continuity/`、`education-access-lifelong-learning/` 和 `caregiving-long-term-care/`。

## 维护规则

- 新增资料必须说明它支持传播阻断、收入学习连续性、照护交接还是服务支持。
- 不能输出个案隔离判断、返工返校许可、法律意见、检测规避或医学建议。
