# Childhood Immunization Schedule Record Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/childhood-immunization-schedule-record-continuity` |
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


本目录承载儿童常规免疫排程接口、记录证明、提醒召回、学校托育记录、可及性和隐私边界资料。它处理公共卫生和记录连续性，不处理个体疫苗医学判断。

## 目录结构

```text
childhood-immunization-schedule-record-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 official schedule interface、immunization records、IIS、school/childcare proof、reminder/recall、missed-dose follow-up、consent 和 privacy boundary。
- 关注免疫信息如何在儿科、公共卫生、学校、托育和家庭之间保持连续。
- 不提供疫苗建议、排程解释、补种、禁忌、不良反应、豁免或个体医疗建议。

## 维护规则

- 新增资料优先引用 CDC、state immunization program、AAP、学校/托育官方资料和公共卫生资料。
- 疫苗信息高度易变，引用时必须指向官方当前资料，不在本仓库复制个体排程细节。
- 不把公共卫生资料转化为个人接种计划、豁免策略或风险判断。
