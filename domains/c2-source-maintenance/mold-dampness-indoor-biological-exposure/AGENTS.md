# mold-dampness-indoor-biological-exposure 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/mold-dampness-indoor-biological-exposure` |
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


本目录维护霉菌、潮湿与室内生物暴露域。它是 Human Infra 的“潮湿住房与呼吸免疫负荷层”，负责建筑潮湿和室内生物暴露如何影响呼吸、睡眠、心理压力、学习工作和住房稳定。

## 目录结构

```text
mold-dampness-indoor-biological-exposure/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明霉菌、潮湿、室内过敏原和生物气溶胶如何通过住房、学校、照护机构和灾后水损影响主体持续性。
- 本域只做公开健康、住房、建筑维护和风险治理资料整理。
- 不提供医疗建议、采样检测、清理方案、除湿设备购买、施工维修、租房纠纷、保险或法律建议。

## 维护规则

- 新增材料必须区分潮湿来源、霉菌、室内过敏原、通风、灾后水损、住房质量和服务/维修责任。
- 不把照片、气味、传感器、家庭试剂或 AI 输出写成个体医疗、住房安全、保险或法律结论。
- 涉及灾后水损和危险清理时，只写公共边界和治理变量，不写操作步骤。
