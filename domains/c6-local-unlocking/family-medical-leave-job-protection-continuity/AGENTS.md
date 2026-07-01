# family-medical-leave-job-protection-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/family-medical-leave-job-protection-continuity` |
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


本目录维护家庭医疗假与岗位保护连续性的资料、边界和机制链路。

## 文件结构

```text
family-medical-leave-job-protection-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的稳定说明，描述家庭医疗事件如何通过岗位保护、反报复和复工机制影响主体持续性。
- 本目录只维护公开制度、研究框架和资料索引，不承载个人请假、法律、HR、福利或医疗建议。
- 涉及工资替代时链接到 `paid-sick-family-leave-wage-replacement-continuity/`；涉及孕产育儿时链接到 `pregnancy-parental-work-continuity/`；涉及长期能力变化时链接到 `workplace-accommodation-return-to-work-continuity/` 或 `disability-income-work-capacity-benefit-continuity/`。

## 维护规则

- 新增资料必须标明 jurisdiction、适用对象、证据类型和非建议边界。
- 不把联邦、州、雇主政策和保险计划混写成单一规则。
- 不写个人资格判断、申请策略、争议处理策略或表单填报建议。
