# outbreak-case-investigation-contact-tracing-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/outbreak-case-investigation-contact-tracing-continuity` |
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


`domains/c6-local-unlocking/outbreak-case-investigation-contact-tracing-continuity/` 是 Human Infra 的暴发病例调查与接触追踪连续性域，负责把病例到接触者的执行链建模为传播阻断和服务转介基础设施。

## 目录结构

```text
outbreak-case-investigation-contact-tracing-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义病例调查、接触追踪、暴露通知、隐私保护和转介支持的对象、链路、非目标和来源信号。
- 本域只整理公开公共卫生资料、变量模型、风险边界和禁止用途。
- 个体诊断、接触者识别、定位追踪、隐私侵害、污名化和规避公共卫生措施不属于本域。

## 上下游关系

- 上游：`immunization-public-health-surveillance/`、`public-health-laboratory-diagnostic-capacity/` 和 `health-data-privacy-governance/`。
- 下游：`isolation-quarantine-work-school-continuity/`、`community-testing-screening-access-continuity/`、`school-workplace-outbreak-operations-continuity/` 和 `social-connection-relational-infra/`。

## 维护规则

- 新增资料必须说明它支持病例调查、接触者通知、转介服务、隐私保护还是信任治理。
- 不能把追踪资料写成个体名单、定位工具、惩罚机制、传播规避或诊断治疗建议。
