# chronic-pain-functional-restoration-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/chronic-pain-functional-restoration-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


本目录维护慢性疼痛、功能恢复、疼痛干预可及、用药风险和长期参与连续性资料。它关注疼痛如何持续压缩有效时间和主体行动能力。

## 目录结构

```text
chronic-pain-functional-restoration-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义慢性疼痛功能恢复如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案疼痛、用药、影像、工作能力或保险资料。
- 资料进入本域时必须保留疼痛类型、功能结果、证据层级、用药风险、心理社会因素和禁止用途。

## 上下游关系

- 上游来自 CDC、NIH、疼痛医学、康复和职业健康资料。
- 下游服务 `pain-suffering-control/`、`physical-activity-mobility/`、`occupational-work-design/` 和返岗模型。
- 不替代疼痛医学、康复医学、精神健康、药学、工伤、残障、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、用药、阿片类药物、康复动作、神经阻滞、手术、设备或补充剂建议。
- 不把慢性疼痛证据写成自我治疗流程或工伤残障判断。
- 新增资料必须区分疼痛强度、功能干扰、失能、用药风险、恢复目标和生活参与结果。
