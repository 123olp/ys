# Lactation Breastfeeding Support Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/lactation-breastfeeding-support-continuity` |
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


本目录承载哺乳、泵奶、lactation support、WIC 支持、工作学校空间、设备接口和家庭支持资料。它处理支持系统连续性，不处理个体喂养处方。

## 目录结构

```text
lactation-breastfeeding-support-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 lactation support、breastfeeding counseling、pumping time/space、WIC support、work/school interface、feeding referral 和隐私污名边界。
- 关注营养、恢复、工作学习和照护负担是否能被同一个支持系统承接。
- 不提供喂养方案、泵奶参数、疼痛处理、药物、婴儿体重解释、产品推荐或法律资格判断。

## 维护规则

- 新增资料优先引用 CDC、USDA WIC、DOL PUMP at Work、AAP、ACOG 或公开母婴健康资料。
- 不把公共哺乳资料转化为个体医疗、育儿、设备或法律建议。
- 涉及母乳、配方、药物、婴儿体重和工作学校权益时必须保留边界。
