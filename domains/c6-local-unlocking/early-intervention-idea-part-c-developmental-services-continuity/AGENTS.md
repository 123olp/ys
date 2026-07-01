# early-intervention-idea-part-c-developmental-services-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/early-intervention-idea-part-c-developmental-services-continuity` |
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


`early-intervention-idea-part-c-developmental-services-continuity/` 是 Human Infra 的 IDEA Part C 早期干预与婴幼儿发育服务执行域，负责研究识别、评估、IFSP、服务协调和转衔如何支撑早期能力形成。

## 目录结构

```text
early-intervention-idea-part-c-developmental-services-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义早期干预域的对象、链路、非目标和来源信号。
- 本域只整理制度入口、服务协调、家庭支持和转衔变量，不做儿童诊断、治疗、IFSP 个案或法律建议。
- 儿童发育记录、评估报告、IFSP、医疗教育记录、视频、照片和家庭身份资料不得进入本域。

## 上下游关系

- 上游：`maternal-newborn-child-development/`、`childcare-family-continuity/`、`healthcare-access-continuity/`。
- 下游：`special-education-iep-504-accommodation-continuity/`、`speech-language-execution-continuity/`、`autism-neurodiversity-support-continuity/`。

## 维护规则

- 新增资料必须说明它影响识别、评估、IFSP、服务协调、等待、转介、转衔还是家庭支持。
- 禁止输出诊断、治疗计划、训练动作、申请策略、学校安置、保险或法律建议。
