# safety-critical-software-formal-methods 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/safety-critical-software-formal-methods` |
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


本目录维护安全关键软件、形式化方法和高可靠系统工程资料。它是高风险工具可信域。

## 目录结构

```text
safety-critical-software-formal-methods/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义软件规格、验证、运行时监控和失效安全如何影响 Human Infra。
- 本目录不保存攻击、绕过安全机制、关闭监控、规避认证或篡改安全关键系统材料。
- 资料必须区分形式化证明、测试、认证、运行时监控和现场可靠性数据。

## 上下游关系

- 上游来自形式化方法、软件工程、系统安全、医疗设备软件、航空航天和关键基础设施控制。
- 下游服务 AI 代理、医疗设备、生命支持、交通、电网、通信和高风险自动化。
- 不替代 `cybersecurity-resilience-critical-services/`；本目录聚焦正确性和失效安全。

## 维护规则

- 不把证明、测试或认证写成绝对安全承诺。
- 不提供规避安全控制、绕过认证或攻击安全关键系统的步骤。
- 新增案例必须标注系统边界、风险等级、验证方法、失效模式和剩余未知项。
