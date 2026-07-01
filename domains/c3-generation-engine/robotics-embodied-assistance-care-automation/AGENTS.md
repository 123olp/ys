# robotics-embodied-assistance-care-automation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/robotics-embodied-assistance-care-automation` |
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


本目录维护机器人、具身辅助与照护自动化域。它是 Human Infra 的“物理行动增强”层，负责机器人、外骨骼、家庭辅助和照护自动化如何影响独立生活、康复和长期任务执行能力。

## 目录结构

```text
robotics-embodied-assistance-care-automation/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明机器人、具身辅助、照护自动化、外骨骼、安全标准和性能测量如何进入主体持续性模型。
- 本域只做公开资料整理和证据边界维护。
- 不提供设备选购、改装、维修、康复处方、照护替代、临床训练、安全认证或绕过安全限制的方法。

## 维护规则

- 新增资料必须区分辅助技术、医疗器械、照护服务、家庭自动化、工业机器人和研究原型。
- 涉及照护和家庭场景时，必须记录隐私、依赖、机械安全、人工接管、责任归属和维护风险。
- 不把机器人陪伴写成真实关系替代，不把自动化写成照护责任消失。
