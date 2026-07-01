# trauma-system-hemorrhage-control-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/trauma-system-hemorrhage-control-continuity` |
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


本目录维护创伤系统、出血控制、创伤中心和事故后急性修复资料。它是外部事故风险进入主体持续性模型的救援系统域。

## 目录结构

```text
trauma-system-hemorrhage-control-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义创伤系统和出血控制如何影响突然死亡、残障和康复连续性。
- 本目录只维护系统框架和证据边界，不保存事故照片、伤情、身份、定位、病历或法律材料。
- 资料进入本域时必须保留损伤机制、系统层级、转运路径、时间窗、结局和禁止用途。

## 上下游关系

- 上游来自 WHO、ACS、National Academies、EMS 和创伤质量改进资料。
- 下游服务 `emergency-medical-services-prehospital-care/`、`surgical-anesthesia-perioperative-safety/`、`transfusion-blood-management-hemorrhage-continuity/` 和功能恢复建模。
- 不替代 EMS、创伤中心、医生、急救培训、法律、保险或现场指挥。

## 维护规则

- 不写止血、现场急救、战术医疗、手术或事故处理教程。
- 不输出暴力、武器伤或灾害现场的操作建议。
- 新增资料必须区分预防、院前、院内和康复阶段。
