# Children Youth Special Health Care Needs Care Coordination Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/children-youth-special-health-care-needs-care-coordination-continuity` |
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


本目录承载 CYSHCN、medical home、照护协调、专科协作、学校接口、保险授权、DME/药品供应和青年转衔资料。它处理复杂儿童照护网络连续性，不处理个体医疗、教育或法律决策。

## 目录结构

```text
children-youth-special-health-care-needs-care-coordination-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 CYSHCN、medical home、care coordination、shared care plan、specialty referral、family caregiver workload、school interface、insurance/DME/medication access 和 transition boundary。
- 关注复杂儿童照护是否能从儿科延伸到专科、家庭、学校、保险、设备、药品和成人系统。
- 不提供诊断、治疗、设备、保险授权、IEP/504、福利资格、护理计划或个体建议。

## 维护规则

- 新增资料优先引用 HRSA/MCHB、AAP、CMS/Medicaid、ACL、IDEA 和公开儿童复杂照护资料。
- 涉及儿童残障、慢病、学校记录、保险、DME 和家庭照护时必须保留高敏感和反歧视边界。
- 不把 care coordination 资料转化为个人资格判断、护理方案或申诉策略。
