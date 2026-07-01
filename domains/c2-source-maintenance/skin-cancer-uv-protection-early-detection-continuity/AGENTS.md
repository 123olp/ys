# skin-cancer-uv-protection-early-detection-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/skin-cancer-uv-protection-early-detection-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


本目录维护 UV 暴露、皮肤癌预防、日晒防护、早期识别、转诊可及和户外职业环境资料。它关注环境暴露如何进入癌症风险与行动连续性。

## 目录结构

```text
skin-cancer-uv-protection-early-detection-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 UV 防护和皮肤癌早识别如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案皮肤照片、肤色、职业、定位、基因或身份资料。
- 资料进入本域时必须保留暴露对象、防护环境、早识别、转诊、公平和禁止用途。

## 上下游关系

- 上游来自 CDC、USPSTF、NCI、职业暴露和公共卫生资料。
- 下游服务 `cancer-screening-early-detection-continuity/`、`skin-barrier-wound-healing/` 和职业健康模型。
- 不替代皮肤科、肿瘤科、职业安全、药学、保险或个体医疗建议。

## 维护规则

- 不写个人皮损判断、照片诊断、防晒产品选择、筛查周期、治疗、活检、用药或转诊建议。
- 不收集或推断皮肤照片、肤色、基因、身份、职业或定位敏感资料。
- 新增资料必须区分 UV 暴露、防护环境、风险沟通、早期识别、转诊和公平可及。
