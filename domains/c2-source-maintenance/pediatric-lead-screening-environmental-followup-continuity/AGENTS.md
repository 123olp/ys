# Pediatric Lead Screening Environmental Followup Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pediatric-lead-screening-environmental-followup-continuity` |
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


本目录承载儿童血铅筛查、结果通知、公共卫生随访、环境暴露、住房修复接口和长期支持资料。它处理筛查信号到环境行动的连续性，不处理个体治疗或法律策略。

## 目录结构

```text
pediatric-lead-screening-environmental-followup-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 pediatric blood lead screening、result notification、public-health follow-up、housing/water exposure pathways、environmental investigation、remediation handoff 和 privacy/stigma boundary。
- 关注儿童铅暴露信号是否能连接住房、水源、公共卫生、儿科、学校和家庭支持。
- 不提供检测解释、治疗、环境采样施工、租赁法律策略、责任判断或个体医疗建议。

## 维护规则

- 新增资料优先引用 CDC、EPA、HUD、Medicaid、州/地方公共卫生和住房 code enforcement 公开资料。
- 涉及儿童、家庭、住房、租赁和环境暴露时必须保留隐私、反污名和法律边界。
- 不把环境风险资料转化为个案房屋安全认证、施工指令或争议策略。
