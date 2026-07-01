# Voice Call Caller ID Authentication Continuity 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/voice-call-caller-id-authentication-continuity` |
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


本目录承载电话可信度、caller ID authentication、robocall、vishing 和号码冒充连续性资料。它只组织公开通信安全资料，不提供 spoofing、拨号、骚扰或实时反诈操作。

## 目录结构

```text
voice-call-caller-id-authentication-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须回到 FCC、FTC、CISA、NIST 或运营商公开标准资料。
- 区分号码身份、通话内容、语音身份、账号恢复和应急通知，不把来电认证写成内容真实性证明。
- 不收集真实电话号码、通话录音、诈骗样本、联系人图谱或通信账号信息。
