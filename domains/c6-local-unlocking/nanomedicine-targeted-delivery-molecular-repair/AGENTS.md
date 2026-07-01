# nanomedicine-targeted-delivery-molecular-repair 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/nanomedicine-targeted-delivery-molecular-repair` |
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


本目录维护纳米医学、靶向递送和远期分子修复证据。它是先进治疗从“有效载荷存在”走向“可到达、可控制、可监测”的递送基础设施域。

## 目录结构

```text
nanomedicine-targeted-delivery-molecular-repair/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义纳米递送、材料风险、靶向释放和分子修复设想如何影响主体持续性。
- 本目录不保存实验配方、材料合成步骤、给药方案或人体实验操作协议。
- 资料必须区分临床可用纳米药物、临床前递送平台、动物实验和远期纳米机器人叙事。

## 上下游关系

- 上游来自纳米材料、药物递送、材料毒理、肿瘤治疗、核酸药物和监管科学。
- 下游服务基因治疗、癌症控制、再生医学、药物安全和未来分子修复模型。
- 不替代 `gene-therapy-genome-editing-delivery-safety/`；本目录聚焦递送平台和材料界面。

## 维护规则

- 不提供自制纳米材料、非临床给药、规避监管或人体实验方案。
- 不把纳米机器人、分子机器或概念演示写成现实医学能力。
- 新增案例必须标注临床阶段、载体类型、靶组织、有效载荷、证据等级和长期安全未知项。
