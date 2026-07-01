# municipal-311-service-request-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/municipal-311-service-request-continuity` |
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


本目录承载市政 311 与非紧急服务请求连续性研究域，关注个人观察如何转成地方政府可派单、可跟踪、可复盘的公共服务对象。

## 目录结构

```text
municipal-311-service-request-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 只整理 311、Open311、服务请求分类、状态回传、责任部门和公开数据如何影响公共空间问题恢复。
- 不提供紧急报警替代、投诉代写、执法规避、骚扰举报、个人跟踪、法律策略或个案申诉建议。
- 不收集地址、照片、车牌、邻居身份、账号、投诉记录或敏感位置资料。

## 维护规则

新增资料优先回到 Open311、地方 311/open data、USA.gov 地方政府、公共服务设计和开放政府资料。保持与 `public-service-design-accessibility/` 和 `civic-data-open-government-transparency/` 的边界清晰。
