# osteoarthritis-joint-function-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/osteoarthritis-joint-function-continuity` |
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


本目录维护骨关节炎、关节功能、移动能力、辅助器具、康复和长期参与资料。它关注退行性关节病如何压缩行动半径和独立生活。

## 目录结构

```text
osteoarthritis-joint-function-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义骨关节炎关节功能如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案影像、药物、运动、体重、手术或康复资料。
- 资料进入本域时必须保留关节部位、功能结果、辅助技术、康复路径、手术边界和禁止用途。

## 上下游关系

- 上游来自 NIAMS、CDC、WHO、风湿/骨科和康复资料。
- 下游服务 `musculoskeletal-integrity/`、`assistive-technology-access/` 和跌倒预防模型。
- 不替代风湿科、骨科、康复医学、疼痛医学、营养、药学、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、影像判读、运动、止痛药、注射、补充剂、手术、康复或设备建议。
- 不把关节炎证据写成个体治疗或手术时机判断。
- 新增资料必须区分症状、结构改变、功能限制、生活参与和照护负担。
