# patient-data-interoperability 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/patient-data-interoperability` |
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


`domains/c4-conversion-channel/patient-data-interoperability/` 是 Human Infra 的患者数据互操作域，负责把健康记录访问、数据可携带、互操作标准和授权共享建模为连续照护的资料条件。

## 目录结构

```text
patient-data-interoperability/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义患者数据访问、互操作、可携带、授权共享和数据连续性的对象、链路、非目标和来源信号。
- 本域只做公开标准、政策资料、变量建模、证据边界和数据断点分析。
- 个人病历解释、医学判断、保险权益判断、账号破解、授权绕过和隐私规避不属于本域。

## 上下游关系

- 上游：`digital-identity-security/`、`governance-rights/` 和 `health-literacy-navigation/`。
- 下游：`healthcare-access-continuity/`、`medicine-access-treatment-continuity/`、`caregiving-long-term-care/` 和 `measurement-feedback/`。

## 维护规则

- 新增资料必须说明它支持的是访问、互操作、数据可携带、授权、语义一致性、数据质量还是隐私治理变量。
- 不能把互操作资料写成个体数据权利结论、医疗解释或第三方应用背书。
