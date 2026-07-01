# ai-red-teaming-adversarial-testing-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-red-teaming-adversarial-testing-continuity` |
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


本目录维护 AI 红队、安全测试和对抗性评估资料。它是 AI 系统发布前暴露失败模式、约束危险能力和验证缓解措施的治理层。

## 目录结构

```text
ai-red-teaming-adversarial-testing-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AI 红队、安全测试、滥用场景和缓解验证如何影响主体持续性。
- 本目录只维护测试框架、分类和治理边界，不保存攻击 payload、漏洞利用细节或可复用越狱语料。
- 资料进入本域时必须保留测试范围、授权状态、缓解状态和不可公开细节。

## 上下游关系

- 上游来自 NIST Dioptra、MITRE ATLAS、OWASP LLM Top 10、NIST AI RMF 和安全治理文献。
- 下游服务 `ai-agent-tool-permission-sandbox-continuity/`、`ai-incident-reporting-post-deployment-monitoring-continuity/` 和 release gate 设计。
- 不替代 `cybersecurity-resilience-critical-services/`；该域关注一般网络安全，本目录关注 AI 系统红队。

## 维护规则

- 不记录可操作攻击步骤、越狱样例、漏洞利用或防护绕过方法。
- 不把“已红队”写成“已安全”。
- 若新增风险分类影响安全边界文档，必须同步更新 `docs/reference/ethics-and-safety-boundaries.md`。
