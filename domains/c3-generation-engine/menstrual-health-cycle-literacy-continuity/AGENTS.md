# menstrual-health-cycle-literacy-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/menstrual-health-cycle-literacy-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


本目录维护月经健康、周期素养、用品可及、疼痛/出血负担和学校/工作参与资料。它关注周期性身体信号如何影响有效时间和行动连续性。

## 目录结构

```text
menstrual-health-cycle-literacy-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义月经健康和周期素养如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案月经、性行为、妊娠、未成年人、学校、工作或身份资料。
- 资料进入本域时必须保留教育对象、资源可及、异常信号、转介边界、隐私和禁止用途。

## 上下游关系

- 上游来自 NICHD、HHS OWH、ACOG 和公共卫生资料。
- 下游服务 `reproductive-fertility-continuity/`、`pain-suffering-control/` 和学校/工作参与模型。
- 不替代妇产科、儿科、学校健康服务、药学、心理服务或个体医疗建议。

## 维护规则

- 不写个人周期判读、妊娠判断、用药、激素治疗、检查排序、诊断、用品选择或证明建议。
- 不收集或推断未成年人、性行为、妊娠状态、身份、学校或定位资料。
- 新增资料必须区分周期素养、用品可及、疼痛/出血负担、参与支持、异常转介和污名降低。
