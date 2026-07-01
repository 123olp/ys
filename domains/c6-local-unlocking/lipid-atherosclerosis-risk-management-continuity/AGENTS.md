# lipid-atherosclerosis-risk-management-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/lipid-atherosclerosis-risk-management-continuity` |
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


本目录维护血脂、动脉粥样硬化风险管理和 ASCVD 预防连续性资料。它是主体在心肌梗死、卒中和血管性失能之前的长期风险控制域。

## 目录结构

```text
lipid-atherosclerosis-risk-management-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义血脂检测、风险分层、预防性治疗证据、坚持和二级预防交接如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案血脂、家族史、用药、不良反应、影像或诊疗资料。
- 资料进入本域时必须保留风险模型边界、证据等级、可及性、坚持变量和禁止用途。

## 上下游关系

- 上游来自 USPSTF、CDC、NHLBI 和 ASCVD 风险管理资料。
- 下游服务 `cardiovascular-resilience/`、`acute-coronary-syndrome-reperfusion-continuity/` 和卒中风险建模。
- 不替代医生、药师、心内科、内分泌科或个体医疗建议。

## 维护规则

- 不写血脂解读、药物、剂量、补剂、饮食、运动、检查、风险计算或个体治疗建议。
- 不把系统级 ASCVD 预防研究写成个人用药或保险工具。
- 新增变量必须区分检测、风险分层、治疗可及、坚持、事件预防和二级预防阶段。
