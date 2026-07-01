# snap-eligibility-recertification-abawd-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/snap-eligibility-recertification-abawd-continuity` |
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


本目录维护 SNAP 资格、续期、工作要求和 E&T 行政链路连续性域。它是 Human Infra 的食物援助资格维护层，不是个案申请、申诉或福利策略入口。

## 目录结构

```text
snap-eligibility-recertification-abawd-continuity/
├── AGENTS.md
└── README.md
```

## 职责

- 记录 SNAP eligibility、recertification、notice、ABAWD、work requirements 和 E&T 如何影响主体持续性。
- 区分资格维护、支付兑换、食品零售、食品银行和灾害供餐的边界。
- 保留 USDA FNS 与公开行政负担资料的来源、适用对象和不确定性。

## 维护规则

- 新增资料必须说明来源、州级差异、适用对象和禁止用途。
- 不保存个人收入、家庭组成、案件号、EBT 卡信息、身份材料或门户凭证。
- 稳定结论回写 README；临时资料进入 `docs/source-notes/` 或上位研究文档。
