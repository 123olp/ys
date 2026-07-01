# disability-services-independent-living 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/disability-services-independent-living` |
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


本目录维护残障服务与独立生活域。它是 Human Infra 的“能力状态变化后仍能自主行动”层，负责社区支持、个人协助、无障碍、辅助技术和权利保护如何影响主体持续性。

## 目录结构

```text
disability-services-independent-living/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明独立生活、HCBS、个人协助、合理便利、辅助技术、无障碍和社区融合如何影响主体持续性。
- 本域只做公开残障服务、社区生活、公共服务无障碍和权利框架资料整理。
- 不提供福利申请、资格判断、法律投诉、医疗诊断、护理计划、辅助设备处方或家庭个案建议。

## 维护规则

- 新增材料必须区分辅助技术、环境无障碍、公共服务无障碍、个人协助、HCBS、合理便利和独立生活理念。
- 不把残障状态写成能力价值下降、制度负担或排除参与的理由。
- 涉及服务资格和法律权利时，只写公共框架和资料入口，不写个案策略。
