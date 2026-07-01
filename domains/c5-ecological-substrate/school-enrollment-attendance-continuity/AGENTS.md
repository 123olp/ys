# school-enrollment-attendance-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/school-enrollment-attendance-continuity` |
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


本目录承载学校入学与出勤连续性研究域，关注儿童能否稳定进入学校、持续出勤、完成学籍交接并保留学习与服务入口。

## 目录结构

```text
school-enrollment-attendance-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义入学、出勤、长期缺勤、学籍交接和无家可归学生保护如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 入学出勤资料必须优先回到教育部门、NCES、McKinney-Vento/NCHE、州和地方教育机构等公开来源。
- 不写个人入学、出勤申诉、truancy、学区选择、儿童福利或法律操作建议。
- 涉及儿童和家庭资料时，只讨论制度变量、断裂模式和服务连续性，不处理个人识别信息。
- 若新增数据表或指标，必须注明口径：日出勤、慢性缺勤、退出、转学、临时住所、学籍交接或恢复服务。
