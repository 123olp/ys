# nutrition-insecurity-screening-referral-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/nutrition-insecurity-screening-referral-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录承载营养不安全筛查、HRSN 识别、closed-loop referral 和社区食物资源转接研究，关注主体的营养需求如何从医疗观察信号进入可执行支持链。

## 文件结构

```text
nutrition-insecurity-screening-referral-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- `README.md` 是该域稳定入口，新增资料先归入对象、执行断点、证据来源或边界。
- 保持与 `food-security-nutrition-access`、`social-prescribing-community-referral-continuity` 和具体 Food is Medicine 干预域的边界：本域只处理筛查和转接链路。
- 禁止写成个人筛查、福利申请、保险、医疗、饮食处方或个案转介指南。
- 新增来源优先使用 HHS、CMS、USDA、NIH、AHRQ、CDC 或公开项目评估资料。
