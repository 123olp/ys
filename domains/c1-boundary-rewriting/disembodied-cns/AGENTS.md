# Disembodied CNS 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/disembodied-cns` |
| 所属层级 | `C1` - 可能性边界改写层 |
| 父级容器 | `domains/c1-boundary-rewriting` |
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

<!-- domain-agent-workflow:start -->
## 代理执行流程

1. 先读本目录 `README.md`，确认研究对象、分级理由、Human Infra 追问和使用边界。
2. 再读父级层目录的 `README.md` 与 `AGENTS.md`，确认 `C1` 层的根本性标尺和同层相邻域。
3. 需要移动、拆分、合并或重命名本域时，先更新 `domains/_possibility-space-control/classification.tsv`，再运行 `python3 tools/update_domain_doc_contracts.py`。
4. 新增资料时先落到 Source Signals 或 Source Cards；只有完成证据边界复核后，才沉淀为稳定叙述。
5. 输出结论时必须同时写清：它影响什么变量、通过什么机制、证据等级是什么、不能推出什么。

## 补齐优先级

- P1 Source trail：补来源、日期、版本、作者、原始链接和本地路径。
- P2 Variable map：补输入变量、中间机制、状态变量、风险变量和输出指标。
- P3 Claim-Evidence Matrix：补主张、证据、适用范围、不确定性、反例和禁用外推。
- P4 Relation links：补上游依赖、下游输出、同层相邻域和可能的迁移路径。
- P5 Reader path：补新手入口、术语、最小阅读顺序和下一步研究任务。

## 验证要求

- 批量更新域文档后，必须运行 `python3 tools/update_domain_doc_contracts.py` 并确认第二次运行更新数为 0。
- 结构或链接变化后，必须运行 `make check`。
- 提交前必须运行 `git diff --check`，避免 Markdown 空白和格式错误。
- 不得把 `web/`、临时下载、个人资料或未核验论文缓存混入域文档提交。
<!-- domain-agent-workflow:end -->

`disembodied-cns/` 是去具身外部维持型中枢生命系统研究域。它只做高层系统建模、证据问题、风险分类和伦理边界，不提供实验操作协议。

## 目录结构

```text
disembodied-cns/
├── AGENTS.md
├── README.md
├── docs/
│   ├── brain-body-interface-protocol-contract.md
│   ├── brain-body-interface-protocol-register.json
│   ├── body-function-substitution-minimal-sufficient-body.md
│   └── minimal-sufficient-body-claim-evidence-matrix.json
└── literature/
    ├── README.md
    ├── papers/
    │   ├── README.md
    │   ├── manifest.tsv
    │   ├── html/
    │   └── pdf/
    ├── source-cards.md
    └── source-signals.md
```

## 文件职责

- `README.md`：定义具身半自主开放生命系统与去具身外部维持型中枢生命系统的对照、接口架构、研究对象和非目标。
- `docs/body-function-substitution-minimal-sufficient-body.md`：承载“身体功效替代 - 脑身接口协议 - 最小充分身体”理论模块，把软件工程的接口化、SLO、可观测性、闭环控制、冗余、回滚和安全案例迁移到主体持续性生命系统建模。
- `docs/brain-body-interface-protocol-contract.md`：定义脑-身交换通道进入 Source Card、Claim-Evidence Matrix 和模型桥接前必须具备的字段、状态和中止边界。
- `docs/brain-body-interface-protocol-register.json`：保存脑-身接口协议的机器可审计记录，只允许 L2/Q2 候选变量和保守状态，不承载工程、临床、个体预测或生存收益声称。
- `docs/minimal-sufficient-body-claim-evidence-matrix.json`：保存本域稳定主张到 Source Cards、协议行、变量、反证、降级动作和禁止外推边界的机器可审计矩阵。
- `literature/README.md`：说明文献包结构、维护规则和禁止外推边界。
- `literature/papers/README.md`：说明本地 PDF/HTML 镜像的目录、状态、版权边界和使用规则。
- `literature/papers/manifest.tsv`：记录 `MSB-SIG-*` 来源的本地 PDF、HTML 快照、下载状态和失败原因。
- `literature/papers/html/`：保存官方页面、PubMed 页面、PMC 页面或监管页面快照。
- `literature/papers/pdf/`：只保存可通过开放或官方下载路径取得的 PDF。
- `literature/source-signals.md`：记录候选论文、监管资料、标准和技术项目，只作为待复核来源信号。
- `literature/source-cards.md`：把已读来源整理为 claim、变量、机制、证据类型、边界、反证条件和迁移位置。

## 上下游关系

- 上游依赖 `docs/explanations/human-runtime-infrastructure.md` 的 Human Infra 总模型和 `docs/reference/ethics-and-safety-boundaries.md` 的安全边界。
- 与 `memory-editing/` 共享主体连续性、可表达性、可退出性和尊严原则。
- 不依赖 `longevity-evidence/` 的数据采集脚本；两者只共享证据追溯和风险表达原则。

## 维护规则

- 新增内容必须保持非操作性、非实验步骤、非人体改造指南。
- 新增或更新本地文献镜像时，必须同步更新 `literature/papers/manifest.tsv`；受限 PDF、NCBI 下载挑战、FTP 失败或非 OA 来源必须明确标记，不得绕过访问限制或伪装为已下载全文。
- 技术讨论必须围绕系统边界、接口、控制、反馈、故障、验证和伦理。
- 本域优先采用“接口因果作用”判据：先描述原生器官经由脑-身接口实际交换了什么、以何方向/频率/精度/误差边界交换、对主体状态产生什么闭环作用，再讨论候选替代实现；不得用器官名称、设备外形或功能相似性直接替代接口等价证明。
- 维护本域时必须把“脑-身接口协议”当作第一对象，把心脏、肺、肝脏、肾脏、四肢、传感器、执行器、控制器和神经接口都视为协议实现细节；新增条目若不能说明交换内容、方向、频率、延迟、精度、误差、闭环角色和主体状态依赖，只能进入来源信号，不能进入稳定主张。
- 任何“身体替代”“器官替换”“最小充分身体”叙述都必须从脑-身接口协议开始：交换内容、方向、频率、精度、允许误差、闭环效果、主体状态依赖和 abort gate 未定义前，只能作为来源信号或概念草案，不能写成等价、可行或收益主张。
- “身体功效替代”相关内容必须先区分脑-身接口协议、接口等价、自然器官功效、人工替代接口、主体连续性条件和当前证据边界，不能把 BrainEx、OrganEx、ECMO、人工胰腺、BCI、人工心脏或器官芯片等局部证据外推成去具身长期主体保存已经可行。
- 修改脑-身接口协议字段、状态或 Source Card 锚点时，必须同步更新 `docs/brain-body-interface-protocol-register.json` 并运行 `python3 tools/audit_human_infra_brain_body_interface_protocol_register.py`。
- 修改本域稳定主张、证据锚点、反证、降级动作或禁止外推边界时，必须同步更新 `docs/minimal-sufficient-body-claim-evidence-matrix.json` 并运行 `python3 tools/audit_human_infra_minimal_sufficient_body_claim_evidence_matrix.py`。
- 不宣称当前技术已经实现脱离身体的长期人格保存。
