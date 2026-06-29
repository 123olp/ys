# Human Infra 架构说明

Human Infra 是以人类任务执行为中心的基础设施项目。根目录只承载总项目入口、稳定理论文档和子域路由，不直接承载某一个具体产品的全部数据与脚本。

## 目录结构

```text
human_infra/
├── .github/              # GitHub 协作模板与远程质量门禁
│   ├── AGENTS.md         # .github 目录说明
│   ├── ISSUE_TEMPLATE/   # issue 模板
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/        # GitHub Actions 工作流
├── AGENTS.md              # 记录总项目架构、职责边界和维护规则
├── human-infra-dashboard.html # 静态 Web 看板：展示主体持续性与生命路径预测模型
├── singularity-human-infra.html # 专项 Web 展示页：将《奇点更近》学习资料转译为 Human Infra 价值与预测模型
├── web/                   # Observable Framework 正式 Web 应用：科研叙事、预测模型和交互图表
│   ├── AGENTS.md          # web 目录说明
│   ├── README.md          # 本地运行、构建和页面职责
│   └── src/               # Framework 页面、组件、样式和展示数据
├── tools/                 # 仓库检查脚本和可复用工程工具
│   ├── AGENTS.md          # tools 目录说明
│   ├── check_repository.py
│   ├── arxiv_html_paper_tool.py
│   └── arxiv-html-paper/  # arXiv HTML papers 复用模板包
├── README.md              # Human Infra 定位、边界、目录和变更日志
├── docs/                  # 总理论、域地图、伦理边界和原始资料归档
│   ├── AGENTS.md          # docs 目录说明
│   ├── README.md          # docs 入口和阅读顺序
│   ├── decisions/         # 架构与域边界决策记录
│   ├── explanations/      # 概念解释和理论文章
│   ├── how-to/            # 任务导向操作说明
│   ├── reference/         # 域地图、伦理边界、术语和标准
│   ├── source-notes/      # 最新原始资料的改名归档
│   └── tutorials/         # 学习路径
└── domains/               # 可独立演化的子域
    ├── AGENTS.md          # 子域目录维护规则
    ├── biostasis-cryopreservation/ # 生物停滞与冷冻保存
    ├── cancer-control/    # 癌症控制
    ├── cellular-reprogramming/ # 细胞重编程与表观遗传年轻化谱系
    ├── cognitive-augmentation/ # 认知增强与工具放大
    ├── disembodied-cns/   # 去具身外部维持型中枢生命系统
    ├── future-waiting/    # 去未来 / 压缩等待路径
    ├── governance-rights/ # 治理与主体权利
    ├── immune-maintenance/# 免疫系统维护
    ├── longevity-evidence/# 原 Biocat 长寿证据账本
    ├── measurement-feedback/ # 测量、预测与反馈
    ├── memory-editing/    # 记忆编辑与人格连续性
    ├── neuro-continuity/  # 神经与身份连续性
    ├── regenerative-medicine/ # 再生医学与组织修复
    ├── resource-social-infra/ # 资源与社会基础设施
    └── risk-engineering/  # 风险工程
```

## 职责边界

- `.github/` 只放 GitHub 协作模板和远程质量门禁，不放长期知识正文。
- `human-infra-dashboard.html` 是根目录静态展示入口，只承载可直接打开的模型看板，不承载数据采集、个人预测或生产服务逻辑。
- `singularity-human-infra.html` 是根目录专项展示入口，用于把《奇点更近》学习资料转译为 Human Infra 的价值展示、预测模型和 D3 可视化，不作为事实核验或医学建议。
- `web/` 是 Observable Framework 正式 Web 应用目录，用于多页科研叙事、书籍转译、预测模型和交互可视化；它不承载采集脚本、个人预测服务或医学决策逻辑。
- `tools/` 保存仓库维护脚本和可迁移工程工具；其中 arXiv HTML papers 复用工具只负责资源安装、资产校验和 Astro 模板生成，不承载 Human Infra 正文理论。
- `docs/` 只放 Human Infra 的上位理论、域边界、伦理原则和原始资料归档，不放具体采集脚本。
- `domains/` 中每个子域必须有独立 README 和 AGENTS，明确自身对象、非目标、证据要求和上下游关系。
- `domains/longevity-evidence/` 承接原 Biocat，负责长寿干预证据、临床试验、药品安全、公开数据源和采集脚本。
- `domains/cellular-reprogramming/` 负责山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑等细胞状态可重写谱系，不提供实验协议或人体应用建议。
- `domains/regenerative-medicine/` 负责干细胞、组织工程、器官再生、类器官、移植和生物制造的高层研究框架。
- `domains/cancer-control/` 负责癌症预防、早筛、治疗、复发、肿瘤演化和长期风险治理。
- `domains/immune-maintenance/` 负责免疫衰老、感染防御、慢性炎症、自身免疫和免疫监视。
- `domains/neuro-continuity/` 负责大脑、记忆、意识、人格和主体身份连续性。
- `domains/future-waiting/` 负责度规红移固有时差分路径（黑洞等待室）等“压缩等待 / 去未来”思想实验、证据边界和风险约束。
- `domains/disembodied-cns/` 负责去具身外部维持型中枢生命系统的高层架构建模，不提供实验操作协议。
- `domains/memory-editing/` 负责记忆编辑的概念、证据、验证和伦理边界，不提供可执行神经操控步骤。
- `domains/biostasis-cryopreservation/` 负责冷冻保存、生物停滞、休眠和等待未来修复路径。
- `domains/cognitive-augmentation/` 负责 AI 辅助、外部记忆、学习系统、脑机接口和行动放大工具。
- `domains/risk-engineering/` 负责事故、灾害、暴力、环境风险、系统故障和尾部风险工程。
- `domains/resource-social-infra/` 负责食物、水、能源、住房、医疗、照护、金融、教育、就业和社会支持。
- `domains/governance-rights/` 负责主体权利、法律身份、同意、退出、数据权、AI 治理和研究伦理。
- `domains/measurement-feedback/` 负责主体状态测量、风险评分、生物标志物、可穿戴、预测模型和反馈闭环。
- 原始资料归档在 `docs/source-notes/`；稳定结论必须沉淀到 `docs/` 或对应子域 README，不能长期依赖零散临时文件名。

## 设计原则

- Human Infra 的上位对象是“人类任务执行系统”，不是单一长寿产品。
- Longevity Evidence 承接原 Biocat，但不再占据根目录概念中心。
- “永生”的不同路径必须按机制拆分：长寿证据、细胞重编程、再生医学、癌症控制、免疫维护、神经连续性、未来等待、生物停滞、去具身中枢、记忆编辑、认知增强、资源环境、治理权利和测量反馈不能混成一个概念桶。
- 所有健康、神经、生命支持相关结论必须保留来源、适用对象、不确定性和伦理边界。
- 新增研究域必须能回到 `docs/reference/research-domain-atlas.md` 的先验条件和域判定契约。
- 自研代码只做连接、清洗、归一化、证据编排和产品表达；优先复用官方 API、公开数据库和成熟工具。

## 维护规则

- 架构级新增、删除、移动目录时，必须同步更新本文件和目标目录下的 `AGENTS.md`。
- 子域新增数据或脚本前，先确认它是否属于现有子域；若不属于，先更新 `docs/reference/domain-map.md` 再建目录。
- 不把远期研究域伪装成当前可执行产品。
- 不把 AI 总结当作事实源；公开结论必须能回到原始资料或公开数据库。
- 应用框架只允许用于明确产品形态和验证路径的展示层；当前正式 Web 展示统一收敛到 `web/` 的 Observable Framework 结构。

## 变更日志

- 2026-06-20：从 Biocat 单项目重组为 Human Infra 总项目；旧 Biocat 迁入 `domains/longevity-evidence/`；新增 `disembodied-cns` 与 `memory-editing` 子域；四份最新资料归档到 `docs/source-notes/`；按 Docs-as-Code 和 Diataxis 补齐根文件、协作模板、文档分层和结构检查脚本。
- 2026-06-22：新增 `domains/future-waiting/` 和度规红移固有时差分路径（黑洞等待室），用于承载“压缩等待 / 去未来”类永生路径思想实验。
- 2026-06-23：新增 GitHub Actions `make check` 门禁和 `.github/AGENTS.md`，准备远程仓库协作入口。
- 2026-06-26：新增根目录静态 Web 看板 `human-infra-dashboard.html`，采用黄金分割三块布局展示主体持续性与生命路径预测模型。
- 2026-06-26：新增专项 Web 展示页 `singularity-human-infra.html`，将《奇点更近》学习资料转译为 Human Infra 价值展示、预测模型和可视化。
- 2026-06-26：新增 `web/` Observable Framework 应用，作为科研叙事、书籍转译、预测模型和交互图表的正式 Web 入口。
- 2026-06-27：新增 `tools/arxiv_html_paper_tool.py` 与 `tools/arxiv-html-paper/`，把 arXiv HTML papers 前端框架沉淀为可复用 Astro 工具链。
- 2026-06-29：新增可控度规等待室假设 working paper 入口和审计账本，把黑洞等待室收敛为固有时差分、退出采用、风险扣减和递归等待的可审查模型。
- 2026-06-30：新增 `domains/cellular-reprogramming/`，承载山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑的机制谱系与安全边界。
- 2026-06-30：新增 `docs/reference/research-domain-atlas.md` 和 10 个研究域骨架，把有效永生的先验条件映射为可独立维护的研究域。
