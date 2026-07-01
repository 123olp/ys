# satellite-communications-spectrum-orbit-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/satellite-communications-spectrum-orbit-continuity` |
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


本目录维护卫星通信、频谱与轨道连续性资料。它关注连接基础设施的空间层和灾害/偏远场景备用路径。

## 目录结构

```text
satellite-communications-spectrum-orbit-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义卫星通信、频谱、地面站、轨道资源和空间天气如何影响主体持续性。
- 本目录不保存干扰、入侵、规避监管、轨道操作、军事用途或敏感设施资料。

## 上下游关系

- 上游来自 FCC、ITU、NTIA、NOAA 和公开卫星通信治理资料。
- 下游服务偏远医疗、灾害通信、移动连接、边缘数据回传和全球协作。
- 不替代 `geospatial-navigation-location-infrastructure/`；本目录关注通信而不是 PNT 主体。

## 维护规则

- 必须区分通信、定位、遥感、地面站和频谱治理。
- 涉及攻击、干扰或敏感空间操作的内容不得进入本目录。
