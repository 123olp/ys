# Transition Age Youth Mental Health Service Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/transition-age-youth-mental-health-service-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录承载过渡年龄青年心理健康、儿童到成人行为健康转接、校园到社区服务衔接和危机入口资料。它处理系统连续性，不处理个人心理建议。

## 目录结构

```text
transition-age-youth-mental-health-service-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 transition-age youth、behavioral health handoff、同伴支持、危机入口、隐私授权、保险网络和服务转段。
- 关注治疗关系和支持系统如何跨年龄、学校、家庭、保险和社区边界保持连续。
- 不提供诊断、治疗、用药、危机处置、自伤判断、转诊或个案心理建议。

## 维护规则

- 新增资料必须优先引用 SAMHSA、NIMH、CDC、Youth.gov、学校或公共卫生公开资料。
- 涉及危机、自伤、成瘾或暴力时必须保留专业服务和紧急服务边界。
- 不把群体统计、筛查工具或风险因素转化为个人判断。
