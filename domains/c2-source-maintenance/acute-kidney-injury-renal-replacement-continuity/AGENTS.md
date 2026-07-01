# acute-kidney-injury-renal-replacement-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acute-kidney-injury-renal-replacement-continuity` |
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


本目录维护急性肾损伤、肾脏替代治疗和内环境急性支持资料。它是代谢废物、容量、电解质和酸碱失控时的生命支持域。

## 目录结构

```text
acute-kidney-injury-renal-replacement-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AKI 和肾脏替代治疗如何影响急性死亡、恢复能力和长期肾功能。
- 本目录只维护系统级资料和证据边界，不保存实验室、尿量、透析参数、病历、保险或设备日志。
- 资料进入本域时必须保留 AKI 阶段、支持方式、内环境变量、恢复结局和禁止用途。

## 上下游关系

- 上游来自 KDIGO、NKF、NIH、ICU、肾脏病和内环境稳态资料。
- 下游服务 `renal-hepatic-clearance/`、`fluid-electrolyte-acid-base-homeostasis/`、`intensive-care-organ-support-delirium-continuity/` 和恢复负担建模。
- 不替代肾脏科、ICU、透析中心、医生、营养师、保险计划或个人医疗建议。

## 维护规则

- 不写透析参数、适应证、饮食、补液、用药或实验室解读建议。
- 不把公开 AKI 资料写成个人肾病管理工具。
- 新增资料必须区分急性支持、长期清除功能和资源可达性。
