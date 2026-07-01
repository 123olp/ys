# post-quantum-cryptography-long-term-data-security 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/post-quantum-cryptography-long-term-data-security` |
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


本目录维护后量子密码和长周期数据安全资料。它是数字主体连续性的密码迁移域。

## 目录结构

```text
post-quantum-cryptography-long-term-data-security/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义量子威胁、密码迁移、长期保密和身份资料安全如何影响 Human Infra。
- 本目录不保存攻击步骤、破解工具、密钥窃取、漏洞利用或规避身份验证资料。
- 资料必须区分标准、迁移指南、组织实践、产品声明和长期风险假设。

## 上下游关系

- 上游来自密码学标准、网络安全、身份系统、长期数据治理和协议工程。
- 下游服务数字身份、健康数据隐私、个人档案、研究数据和长期授权记录。
- 不替代 `cybersecurity-resilience-critical-services/`；本目录聚焦后量子和长期密码寿命。

## 维护规则

- 不提供攻击、破解、绕过审计或规避身份验证策略。
- 不把任何算法、库或产品写成永久安全。
- 新增资料必须标注标准状态、适用场景、迁移阶段、长期风险和回滚/替换边界。
