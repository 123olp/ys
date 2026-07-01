# ai-incident-reporting-post-deployment-monitoring-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-incident-reporting-post-deployment-monitoring-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


本目录维护 AI 事故报告、部署后监控和纠错学习资料。它是 AI 工具从发布前评测进入真实运行后的持续审查层。

## 目录结构

```text
ai-incident-reporting-post-deployment-monitoring-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AI 事故、near miss、漂移监控、反馈和纠正措施如何影响主体持续性。
- 本目录只维护事故分类、监控对象和学习闭环，不保存泄露数据、攻击细节或组织内部事故材料。
- 资料进入本域时必须保留来源、事件状态、影响范围、纠正状态和隐私边界。

## 上下游关系

- 上游来自 OECD AI Incidents Monitor、NIST AI RMF、AI Incident Database 和部署后治理文献。
- 下游服务 `ai-evaluation-benchmark-validity-continuity/`、`ai-red-teaming-adversarial-testing-continuity/` 和发布后监控设计。
- 不替代组织安全、法律、监管或事故响应渠道。

## 维护规则

- 不记录攻击复现、事故利用、泄露材料传播或监管规避方法。
- 不把事故数据库条目写成法律结论或责任认定。
- 若新增事故类型影响伦理安全边界，必须同步更新边界文档。
