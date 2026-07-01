# gene-therapy-genome-editing-delivery-safety 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/gene-therapy-genome-editing-delivery-safety` |
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


`domains/c6-local-unlocking/gene-therapy-genome-editing-delivery-safety/` 保存基因治疗、基因编辑、递送平台和长期安全边界资料。

## 目录结构

```text
gene-therapy-genome-editing-delivery-safety/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义基因治疗、基因编辑、递送和长期安全在 Human Infra 中的位置、关注变量、非目标和来源入口。
- `AGENTS.md`：记录本目录职责、允许新增材料类型和安全边界。

## 职责边界

- 本域关注基因层干预如何改变主体持续性变量。
- 可以整理论文、监管指南、长期随访要求、风险变量和平台分类。
- 不保存载体设计、编辑序列、实验协议、剂量、给药、制造、临床应用或 DIY 生物操作内容。
- 涉及人体研究、监管路径和真实世界证据时，必须链接到 `clinical-trials-regulatory-science-translation/`。

## 维护规则

- 每条主张必须标明证据层级：体外、动物、人体早期、批准适应证或上市后。
- 不把“能编辑”写成“能延寿”；必须说明中间变量和风险门槛。
- 新增文件或子目录时同步更新本文件。
