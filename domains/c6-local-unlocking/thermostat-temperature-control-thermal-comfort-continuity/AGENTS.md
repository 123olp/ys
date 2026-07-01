# thermostat-temperature-control-thermal-comfort-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/thermostat-temperature-control-thermal-comfort-continuity` |
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


本目录承载温控器与室内温度控制连续性研究域，关注温控系统如何把供暖制冷能力转化为稳定的居住、睡眠、照护和工作条件。

## 目录结构

```text
thermostat-temperature-control-thermal-comfort-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义温控器、设定点、传感器、远程控制、热舒适和家庭任务结果如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 DOE/Energy Saver、CDC、EPA、ASHRAE/建筑环境资料、HVAC 专业资料和能源援助资料。
- 不写安装接线、设备购买、具体设定点处方、智能家居配置、账单优化或个案健康建议。
- 新增指标必须注明口径：设定点、传感器、占用需求、热暴露、能源负担、权限控制或任务后果。
- 涉及极端冷热、断网、租房控制或脆弱人群时，必须保留医疗、应急和专业维护边界。
