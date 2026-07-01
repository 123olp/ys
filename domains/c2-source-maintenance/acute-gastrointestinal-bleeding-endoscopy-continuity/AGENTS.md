# acute-gastrointestinal-bleeding-endoscopy-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acute-gastrointestinal-bleeding-endoscopy-continuity` |
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


本目录维护急性消化道出血、内镜可及、输血接口和复发预防资料。它是血液供应、消化道病变和急性休克风险交界的研究域。

## 目录结构

```text
acute-gastrointestinal-bleeding-endoscopy-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义急性 GI 出血如何改变血容量、贫血、休克、再出血和有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、生命体征、血红蛋白、图片、用药、内镜或病历资料。
- 资料进入本域时必须区分识别、稳定、输血接口、内镜可及、抗凝背景和复发预防。

## 上下游关系

- 上游来自 ACG、NIDDK、AABB 和消化道出血 guideline/public materials。
- 下游服务 `transfusion-blood-management-hemorrhage-continuity/`、`blood-oxygen-hemostasis/` 和 `surgical-anesthesia-perioperative-safety/`。
- 不替代医生、急诊、消化科、内镜团队、输血医学或个体医疗建议。

## 维护规则

- 不写便血/呕血判断、停药、抗凝处理、输血、内镜、药物、饮食、急诊分诊或预后建议。
- 不把系统级出血服务链研究写成个人风险评分或治疗工具。
- 新增变量必须区分上消化道、下消化道、失血、休克、内镜、输血和再出血。
