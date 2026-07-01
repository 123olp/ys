# contraception-family-planning-access-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/contraception-family-planning-access-continuity` |
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


本目录维护避孕可及、家庭计划、选择自主、医学适用性和供应连续资料。它关注主体如何把生育时间、身体风险、照护责任和长期资源纳入可选择路径。

## 目录结构

```text
contraception-family-planning-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义避孕和家庭计划可及如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案性行为、妊娠、伴侣、药物、病史、位置或身份资料。
- 资料进入本域时必须保留选择自主、医学适用性、咨询质量、隐私、胁迫防护和禁止用途。

## 上下游关系

- 上游来自 CDC、HHS OWH、公共卫生和生殖健康服务资料。
- 下游服务 `reproductive-fertility-continuity/`、`pregnancy-parental-work-continuity/` 和资源计划模型。
- 不替代临床咨询、妇产科、药学、法律援助、保险导航或个体医疗建议。

## 维护规则

- 不写个人避孕选择、禁忌判定、用药/器械、紧急处理、流产、妊娠处理、法律或保险建议。
- 不收集或推断未成年人、伴侣、性行为、妊娠状态、身份或定位资料。
- 新增资料必须区分选择范围、医学适用性、咨询质量、费用覆盖、供应连续、隐私和胁迫防护。
