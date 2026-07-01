# patient-portal-account-message-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/patient-portal-account-message-continuity` |
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


## 职责

本目录承载 patient portal、账号入口、secure messaging、通知路由、proxy access 和患者可见医疗任务资料。

## 边界

- 只研究医疗门户作为主体可见性和通信基础设施。
- 不代写医生消息、门户请求、投诉、授权或账号恢复材料。
- 不保存 portal 凭证、验证码、MRN、member ID、PHI、代理授权或联系方式。

## 结构

```text
patient-portal-account-message-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 patient portal、patient-facing API、proxy access、secure messaging 和普通数字身份。
- 涉及个体病历、门户账号、医疗沟通或隐私争议的内容必须转回官方渠道和专业人员。
