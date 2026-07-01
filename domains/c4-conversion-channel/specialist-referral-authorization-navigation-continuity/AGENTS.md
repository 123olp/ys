# specialist-referral-authorization-navigation-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/specialist-referral-authorization-navigation-continuity` |
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

本目录承载专科转诊、授权、资料转交和闭环回传连续性资料，关注主体如何从初级照护或服务入口进入正确专科窗口。

## 边界

- 只整理公开资料、机制、变量、证据边界和研究问题。
- 不提供专科推荐、病情判断、加急策略、授权申诉、病历摘要代写或规避路径。
- 不保存诊断、病历、保险、影像、授权号、预约或个案健康资料。

## 结构

```text
specialist-referral-authorization-navigation-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分转诊识别、授权、资料流、预约闭环和反馈回传。
- 个案转诊、医疗、保险和法律问题必须回到照护团队、保险方或官方渠道。
