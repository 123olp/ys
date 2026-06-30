# ai-incident-reporting-post-deployment-monitoring-continuity 目录说明

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
