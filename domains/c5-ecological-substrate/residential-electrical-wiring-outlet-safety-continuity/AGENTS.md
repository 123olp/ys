# residential-electrical-wiring-outlet-safety-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/residential-electrical-wiring-outlet-safety-continuity` |
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


本目录承载住宅电气线路与插座安全连续性研究域，关注家庭电气接口如何支撑任务设备并避免过载、触电和火灾风险。

## 目录结构

```text
residential-electrical-wiring-outlet-safety-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义住宅线路、插座、保护装置、过载和家庭任务设备如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 USFA/FEMA、NFPA、CPSC、地方建筑/消防规范和持证电气专业资料。
- 不写接线、配电箱操作、故障诊断、维修步骤、安装教程、品牌推荐或个案住房判断。
- 新增指标必须注明口径：用电接口、保护装置、设备依赖、过载风险、火灾/触电后果或恢复任务。
- 涉及灾后、潮湿环境、医疗设备或儿童场景时，必须保留应急服务和专业转介边界。
