# pelvic-floor-continence-function-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pelvic-floor-continence-function-continuity` |
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


本目录维护盆底功能、尿失禁、便失禁、脱垂、康复可及、用品和社会参与资料。它关注排泄控制、行动半径和尊严如何支撑主体持续性。

## 目录结构

```text
pelvic-floor-continence-function-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义盆底和控尿控便功能如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案排泄、产后、性健康、手术、药物、浴厕或身份资料。
- 资料进入本域时必须保留功能对象、转介路径、康复可及、用品可及、羞耻边界和禁止用途。

## 上下游关系

- 上游来自 NIDDK、HHS OWH、泌尿、消化、妇产和康复资料。
- 下游服务 `urogenital-continuity/`、`rehabilitation-functioning/` 和独立生活模型。
- 不替代泌尿科、妇产科、消化科、康复、药学、手术或个体医疗建议。

## 维护规则

- 不写个人盆底训练、诊断、用药、器械、手术、产后恢复、用品选择、家庭处理或保险建议。
- 不收集或推断排泄、性健康、产后、手术、身份或家庭环境敏感资料。
- 新增资料必须区分症状识别、转介、康复可及、用品支持、浴厕环境、羞耻和参与结果。
