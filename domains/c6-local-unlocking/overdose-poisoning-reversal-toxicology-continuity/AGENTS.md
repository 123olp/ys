# overdose-poisoning-reversal-toxicology-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/overdose-poisoning-reversal-toxicology-continuity` |
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


本目录维护药物过量、中毒、毒物中心、逆转窗口和毒理急救系统资料。它是可逆毒性暴露进入主体持续性模型的急性救援域。

## 目录结构

```text
overdose-poisoning-reversal-toxicology-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义中毒/过量逆转系统如何影响急性死亡、脑缺氧和恢复入口。
- 本目录只维护公共资料和证据边界，不保存物质使用史、用药、身份、定位、急救记录、病历或法律资料。
- 资料进入本域时必须保留暴露类型、救援窗口、咨询/转运路径、恢复连接和禁止用途。

## 上下游关系

- 上游来自 Poison Help、CDC、NIH/NIDA、毒物中心、EMS 和公共卫生监测资料。
- 下游服务 `chemical-safety-poison-control-toxicology/`、`substance-use-treatment-recovery-continuity/` 和急性死亡风险建模。
- 不替代毒物中心、EMS、急诊、医生、危机热线、治疗机构、法律或执法机构。

## 维护规则

- 不写中毒处理、解毒药、纳洛酮操作、剂量、物质使用或规避方法。
- 不输出可被用于自伤、投毒、滥用、检测规避或执法规避的内容。
- 新增资料必须区分预防、急性逆转、转运和长期恢复。
