# community-testing-screening-access-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/community-testing-screening-access-continuity` |
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


`domains/c4-conversion-channel/community-testing-screening-access-continuity/` 是 Human Infra 的社区检测与筛查可达连续性域，负责把检测入口、筛查项目和结果报告建模为暴发观测基础设施。

## 目录结构

```text
community-testing-screening-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义社区检测、筛查、居家检测、报告、转介、可达公平和不确定性的对象、链路、非目标和来源信号。
- 本域只整理公开检测系统资料和变量模型。
- 检测选择、采样操作、结果解释、诊断治疗、隔离建议和检测规避不属于本域。

## 上下游关系

- 上游：`public-health-laboratory-diagnostic-capacity/`、`immunization-public-health-surveillance/` 和 `clinical-laboratory-diagnostic-quality/`。
- 下游：`outbreak-case-investigation-contact-tracing-continuity/`、`isolation-quarantine-work-school-continuity/` 和 `school-workplace-outbreak-operations-continuity/`。

## 维护规则

- 新增资料必须说明它支持检测进入、筛查覆盖、报告接口、转介路径还是公平评估。
- 不能输出个体诊断、检测解释、采样教程、检测规避或报告操纵内容。
