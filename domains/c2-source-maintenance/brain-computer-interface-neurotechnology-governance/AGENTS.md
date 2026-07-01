# brain-computer-interface-neurotechnology-governance 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/brain-computer-interface-neurotechnology-governance` |
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


本目录维护脑机接口、神经技术与治理域。它是 Human Infra 的“神经-工具高带宽接口”层，负责 BCI、神经数据、神经伦理和设备安全如何影响主体能力、身份边界和未来选择权。

## 目录结构

```text
brain-computer-interface-neurotechnology-governance/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明脑机接口、神经记录/刺激、神经数据、设备安全和神经伦理如何进入主体持续性模型。
- 本域只做公开资料整理和证据边界维护。
- 不提供医疗建议、设备使用、刺激参数、植入建议、临床试验报名、设备破解或神经数据攻击方法。

## 维护规则

- 新增资料必须区分治疗、辅助、增强、研究和商业宣传。
- 涉及神经数据、意图解码和刺激时，必须保留同意、退出、隐私、身份、可逆性和设备安全边界。
- 不把 BCI 写成意识上传，不把神经接口能力写成确定人格连续性证明。
