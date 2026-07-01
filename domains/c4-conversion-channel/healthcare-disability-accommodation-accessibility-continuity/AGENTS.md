# healthcare-disability-accommodation-accessibility-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/healthcare-disability-accommodation-accessibility-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


## 职责

本目录承载医疗残障便利、无障碍医疗设备、辅助沟通、合理修改和医疗民权资料。

## 边界

- 只研究残障主体进入医疗系统的结构性条件和失败模式。
- 不提供法律意见、投诉策略、便利申请、设备处方、转移技巧或医疗建议。
- 不保存残障证明、病历、诊断、PHI、机构投诉或联系方式。

## 结构

```text
healthcare-disability-accommodation-accessibility-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分公共无障碍、医疗设备可达、辅助沟通和具体医疗服务。
- 涉及个体法律权利、设备选择、医疗行动或投诉的内容必须转回官方渠道和专业人员。
