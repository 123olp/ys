# human-ai-oversight-handoff-accountability-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/human-ai-oversight-handoff-accountability-continuity` |
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


本目录维护人机监督、交接和问责资料。它是 AI 参与主体任务后保持人类控制权、解释权和纠错权的边界层。

## 目录结构

```text
human-ai-oversight-handoff-accountability-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义人类监督、人工接管、升级路径、责任归属和申诉机制如何影响主体持续性。
- 本目录只维护监督与问责框架，不保存个案审批、私有绩效数据、法律责任材料或组织内部决策日志。
- 资料进入本域时必须保留 AI 角色、人类角色、交接条件、记录边界和不可替代责任。

## 上下游关系

- 上游来自 NIST AI RMF、Human-AI Interaction Guidelines、Human-AI Teaming 和人因工程资料。
- 下游服务 `ai-agent-tool-permission-sandbox-continuity/`、`automation-bias-mode-confusion-oversight-continuity/` 和 AI 协作流程设计。
- 不替代法律、合规、人力资源或组织治理渠道。

## 维护规则

- 不记录规避审核、伪造授权、转移责任或操控审批方法。
- 不把人在场写成有效监督。
- 若新增监督字段影响 AI 运行契约或安全边界，必须同步更新索引。
