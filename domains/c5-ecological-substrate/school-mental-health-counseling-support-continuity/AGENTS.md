# school-mental-health-counseling-support-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/school-mental-health-counseling-support-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录承载学校心理健康、咨询和支持连续性研究域，关注学校恢复层如何保护学生学习参与和长期行动能力。

## 目录结构

```text
school-mental-health-counseling-support-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义学校心理健康服务、咨询、社工、危机转介和社区照护衔接如何进入 Human Infra 模型。
- `AGENTS.md`：说明本目录职责、非目标和维护规则。

## 维护规则

- 资料必须优先回到 SAMHSA、CDC、教育部门、州教育/行为健康机构和公开学校心理健康资料。
- 不写个人心理治疗、危机处置、安全计划、转介选择、投诉策略、用药或医疗/法律建议。
- 不处理学生心理、危机、家庭、纪律、残障或医疗个人资料。
- 涉及自伤或暴力风险时，只保留公共安全边界和转介类别，不提供操作性个案处理。
