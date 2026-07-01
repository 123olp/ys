# prepared-food-restaurant-cafeteria-safety-access-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/prepared-food-restaurant-cafeteria-safety-access-continuity` |
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


本目录承载熟食、餐馆与 cafeteria 安全可达连续性研究域，关注不能做饭或离家时外部餐食如何支撑任务执行。

## 目录结构

```text
prepared-food-restaurant-cafeteria-safety-access-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义餐馆、食堂、外卖、即食餐、过敏原和食品安全信息如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 FDA Food Code、CDC food safety、地方健康部门、FDA food allergies 和公开餐饮监管资料。
- 不写餐馆推荐、点餐建议、饮食处方、过敏医疗建议、外卖平台规避、差评攻击、食品制备流程或个案投诉策略。
- 涉及餐饮数据时只讨论安全信号、菜单/过敏原信息、可达性、支付、营业时段、特殊饮食和任务连续性。
