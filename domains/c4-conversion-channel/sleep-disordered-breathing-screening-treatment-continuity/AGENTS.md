# sleep-disordered-breathing-screening-treatment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/sleep-disordered-breathing-screening-treatment-continuity` |
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


本目录维护睡眠呼吸障碍、夜间低氧、诊断转介、治疗坚持和设备连续性资料。它是主体恢复系统、警觉性和心血管风险之间的交叉域。

## 目录结构

```text
sleep-disordered-breathing-screening-treatment-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义睡眠呼吸障碍如何通过低氧、疲劳、事故和心血管负荷影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案睡眠报告、血氧、病史、设备或驾驶资料。
- 资料进入本域时必须保留对象、诊断路径、治疗可及、坚持、随访和禁止用途。

## 上下游关系

- 上游来自 NHLBI、USPSTF、CDC 和睡眠医学资料。
- 下游服务 `sleep-circadian-recovery/`、`respiratory-oxygenation/` 和心血管风险模型。
- 不替代睡眠医学、呼吸科、牙科、职业安全、驾驶安全或个体医疗建议。

## 维护规则

- 不写个人诊断、睡眠报告判读、CPAP 参数、设备选择、治疗方案、驾驶限制或保险建议。
- 不把筛查不确定性写成普遍筛查推荐。
- 新增资料必须区分症状识别、诊断、治疗、坚持、设备维护和安全暴露阶段。
