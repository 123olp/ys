# tobacco-nicotine-cessation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/tobacco-nicotine-cessation-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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


本目录维护烟草、尼古丁依赖、戒烟支持、政策环境和复吸预防资料。它是主体在癌症、COPD、心血管事件和长期资源损耗之前的高杠杆风险控制域。

## 目录结构

```text
tobacco-nicotine-cessation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义烟草/尼古丁筛查、咨询、quitline、药物可及、政策环境和复吸预防如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案使用史、戒断症状、药物、年龄、学校或家庭资料。
- 资料进入本域时必须保留公共健康层级、成瘾边界、青少年保护、证据强度和禁止用途。

## 上下游关系

- 上游来自 CDC、USPSTF、WHO 和烟草控制资料。
- 下游服务 `substance-exposure-control/`、`cancer-control/`、`respiratory-oxygenation/` 和心血管风险建模。
- 不替代医生、戒烟服务、心理服务、药师、学校服务或个体医疗建议。

## 维护规则

- 不写戒烟药物、剂量、替代品、电子烟策略、戒断处理、孕期或青少年个案建议。
- 不生成使用技巧、购买渠道、商业推广、年龄限制规避或违法规避内容。
- 新增变量必须区分筛查、咨询、治疗可及、政策、复吸预防和公平性。
