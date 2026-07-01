# online-safety-digital-harm-prevention 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/online-safety-digital-harm-prevention` |
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


本目录维护在线安全与数字伤害预防域。它是 Human Infra 的“数字空间可安全参与和可恢复”层，负责网络霸凌、在线骚扰、数字胁迫、儿童在线保护和平台求助路径如何影响主体持续性。

## 目录结构

```text
online-safety-digital-harm-prevention/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明网络霸凌、在线骚扰、数字虐待、儿童在线保护、平台治理和受害者支持如何影响主体持续性。
- 本域只做公开在线安全、数字伤害预防、平台求助和儿童保护资料整理。
- 不提供跟踪、骚扰、doxxing、勒索、非自愿影像、儿童剥削、账号入侵、规避平台或规避执法内容。

## 维护规则

- 新增材料必须区分账号安全、平台治理、在线骚扰、儿童保护、数字虐待、诈骗诱导和心理伤害。
- 不输出可用于定位、识别、羞辱、勒索或二次伤害受害者的信息。
- 涉及儿童和性剥削时，只写保护、举报和禁止边界，不写操作细节。
