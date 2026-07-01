# semiconductor-advanced-packaging-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/semiconductor-advanced-packaging-continuity` |
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


本目录维护半导体先进封装连续性资料。它解释芯片从晶圆能力转化为系统级算力的封装接口。

## 目录结构

```text
semiconductor-advanced-packaging-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义先进封装、chiplet、HBM、互连、测试和热管理如何影响主体持续性。
- 本目录不保存工艺参数、封装设计文件、供应商报价、采购策略或出口管制规避材料。

## 上下游关系

- 上游来自 CHIPS packaging program、JEDEC、SEMI 和公开封装可靠性资料。
- 下游服务 AI 硬件、数据中心、边缘智能、医学设备和传感器平台。
- 不替代 `semiconductor-manufacturing-metrology-continuity/`；本目录只管封装与系统集成层。

## 维护规则

- 每条资料必须说明它支持的是封装能力、测试可靠性、产能韧性还是算力转化边界。
- 不把产业路线图写成确定的主体收益。
