# Venomous Bites Stings Envenomation Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/venomous-bites-stings-envenomation-continuity` |
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


本目录承载有毒动物咬蜇伤和毒液暴露如何影响主体行动连续性的研究资料。

## 文件

```text
venomous-bites-stings-envenomation-continuity/
├── AGENTS.md
└── README.md
```

- `README.md`：定义有毒咬蜇伤、毒物中心/急诊连接和行动连续性边界。
- `AGENTS.md`：记录本目录职责、上下游和维护规则。

## 上游

- `../parks-recreation-green-space-access-continuity/`
- `../occupational-exposure-industrial-hygiene/`
- `../animal-health-zoonotic-interface-one-health/`

## 下游

- `../overdose-poisoning-reversal-toxicology-continuity/`
- `../anaphylaxis-allergic-emergency-continuity/`
- `../after-hours-urgent-care-triage-continuity/`

## 边界

不提供急救步骤、抗毒素建议、动物识别诊断、捕捉处理、个体风险判断或旅行许可。
