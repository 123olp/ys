# public-accommodation-accessibility-service-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-accommodation-accessibility-service-continuity` |
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


本目录承载公共场所无障碍与服务接入连续性研究域，关注无障碍接口如何让主体平等进入医疗、交通、学习、购物、住宿和社区任务系统。

## 目录结构

```text
public-accommodation-accessibility-service-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义公共场所、政府服务、商业服务、有效沟通、服务动物和合理便利如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 ADA.gov、DOJ、地方政府、无障碍专业资料和公共服务设计公开资料。
- 不写 ADA 诉讼策略、服务动物欺诈、伪造残障文件、规避规则、骚扰机构或个案法律建议。
- 涉及无障碍数据时只讨论服务接口、合理便利、有效沟通、临时中断、恢复渠道和任务连续性。
