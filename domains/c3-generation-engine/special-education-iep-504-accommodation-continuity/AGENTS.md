# special-education-iep-504-accommodation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/special-education-iep-504-accommodation-continuity` |
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


本目录承载特殊教育、IEP、Section 504 与学校便利连续性研究域，关注残障学生支持如何维持学习参与和主体能力发展。

## 目录结构

```text
special-education-iep-504-accommodation-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 IDEA、IEP、504、合理便利、相关服务和程序保障如何进入主体持续性模型。
- `AGENTS.md`：说明本目录职责、证据边界和维护规则。

## 维护规则

- 资料必须优先回到 IDEA、OSEP、OCR、州教育机构和权威技术援助中心。
- 不写个人 IEP/504 策略、due process、申诉、安置选择、诊断解释或法律/医疗/教育建议。
- 不把残障支持简化为成绩提升工具；必须同时关注参与、沟通、自主、尊严、安全和家庭负担。
- 涉及纪律、交通、心理健康或医疗支持时，链接到对应学校服务域，不在本域吞并全部问题。
