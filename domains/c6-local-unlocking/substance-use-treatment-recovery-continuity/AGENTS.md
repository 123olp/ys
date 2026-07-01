# substance-use-treatment-recovery-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/substance-use-treatment-recovery-continuity` |
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


本目录维护物质使用障碍治疗与恢复连续性域。它是 Human Infra 的“成瘾风险被治疗和恢复系统接住”层，负责治疗入口、恢复支持、过量预防和长期服务连续性。

## 目录结构

```text
substance-use-treatment-recovery-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明物质使用障碍治疗、恢复支持、同伴支持、过量预防、减害治理和服务连续性如何影响主体持续性。
- 本域只做公开治疗、恢复、公共卫生和服务系统资料整理。
- 不提供戒断、排毒、药物、剂量、非法物质、现场处置、法律策略、检测规避或个体治疗建议。

## 维护规则

- 新增材料必须区分暴露控制、治疗入口、恢复支持、同伴支持、过量预防、服务保留和反污名。
- 不把成瘾、复发或过量风险写成道德失败、治安标签或商业营销对象。
- 涉及药物和减害时，只写公共框架与安全边界，不写操作步骤或个体建议。
