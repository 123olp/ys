# campus-mental-health-crisis-student-support-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/campus-mental-health-crisis-student-support-continuity` |
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


本目录承载校园心理健康、危机响应和学生恢复支持连续性研究域，关注心理支持如何保护生命安全、学习时间和返校路径。

## 目录结构

```text
campus-mental-health-crisis-student-support-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义校园心理咨询、危机响应、休学返校、隐私同意和社区转介如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料必须优先回到 SAMHSA、988、ED、CDC、高校 counseling/crisis/leave policy 和公开研究资料。
- 不写心理诊断、治疗、危机干预、风险评估、强制处置、用药、热线替代或个案建议。
- 涉及心理健康资料时，只讨论系统变量、容量和服务断点，不处理个人危机、诊断、风险或家庭资料。
- 新增指标必须注明口径：counseling capacity、wait time、crisis response、leave、re-entry、retention 或 safety outcome。
