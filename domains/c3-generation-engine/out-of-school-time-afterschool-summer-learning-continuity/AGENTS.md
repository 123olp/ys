# out-of-school-time-afterschool-summer-learning-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/out-of-school-time-afterschool-summer-learning-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


`out-of-school-time-afterschool-summer-learning-continuity/` 是 Human Infra 的课外、放学后和暑期学习照护执行域，负责研究学校日历外时间如何影响儿童安全、学习轮次和照护者工作连续性。

## 目录结构

```text
out-of-school-time-afterschool-summer-learning-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义课外/暑期学习照护域的对象、链路、非目标和来源信号。
- 本域只整理公开项目类型、服务变量和执行断点，不做活动推荐、学习计划、接送安排或项目质量背书。
- 儿童身份、成绩、出勤、位置、照片、项目申请、家庭排班和交通资料不得进入本域。

## 上下游关系

- 上游：`childcare-family-continuity/`、`school-enrollment-attendance-continuity/`、`learning-skill-acquisition/`。
- 下游：`school-meals-nutrition-access-continuity/`、`school-transportation-safe-routes-continuity/`、`time-allocation-effective-time/`。

## 维护规则

- 新增资料必须说明它影响放学后时段、暑期断点、监督、安全、学习延续、餐食、交通、项目承接还是家庭排班。
- 禁止输出课外班推荐、夏令营建议、补习计划、出勤安排、接送路线或学校个案判断。
