# radon-asbestos-indoor-hazard-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/radon-asbestos-indoor-hazard-continuity` |
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


本目录维护氡、石棉与室内长期危害连续性域。它是 Human Infra 的“不可见建筑暴露层”，负责建筑遗留危害如何影响呼吸、癌症风险、住房稳定和长期健康寿命。

## 目录结构

```text
radon-asbestos-indoor-hazard-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明氡、石棉和室内长期危害如何通过住房、学校、工作场所和公共建筑影响主体持续性。
- 本域只做公开资料、监管边界、暴露机制、长期风险和治理变量整理。
- 不提供检测解释、设备购买、缓解系统设计、石棉采样/拆除、施工、房产、保险、诉讼或医学建议。

## 维护规则

- 新增材料必须区分氡、石棉、建筑年代、地质条件、通风、维护翻新、职业暴露和公共建筑管理。
- 不把检测读数、建筑材料照片、地图或 AI 输出写成个体医疗、房屋安全、工程合规或法律责任结论。
- 涉及危险材料时，只写官方边界、治理变量和禁止用途，不写可执行处理步骤。
