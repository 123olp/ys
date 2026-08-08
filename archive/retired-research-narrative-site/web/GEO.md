# Human Infra GEO 发布与治理契约

本文规定 Human Infra 面向传统搜索引擎、生成式问答引擎和智能体生态的公开发布方式。目标是提高真实知识资产被发现、理解、引用和正确推荐的概率，不承诺平台排名、引用率或流量提升。

## 方法来源

本轮方法主要复用 `<local-geo-knowledge-base>` 中的 `yao-geo-skills` 与 `geo-citation-lab`：

- `panorama-audit`：全景审计与 10 维实施完整性；
- `page-audit`：页面可抓取、语义结构、引用块和技术健康；
- `brand-graph`：项目实体、别名、事实和来源关系；
- `knowledge-base-builder`：Fact Card、实体关系和机器知识库；
- `article-friendly` / `content-refiner`：定义、数字、对比、步骤、边界和来源块；
- `execution-roadmap`：P0/P1/P2 改进路径；
- `effect-monitor` / `tracking`：平台分开采样、基线窗口和归因边界。

外部方法仓库是只读参考，不复制其未经本项目验证的数据或效果声明。

## 初始基线

2026-07-13 实施前：

| 维度 | 基线 |
| --- | --- |
| 研究域完整性 | 994 个正式域，路径、README、AGENTS 覆盖完整 |
| 公开 Markdown 内链 | 已抽样审计，无破损链接 |
| 正式站点 | Astro 配置声明 GitHub Pages URL，但 Pages API 返回 404 |
| 子路径发布 | 缺少 `/human_infra` base，静态资源和站内链接会逃逸到域名根路径 |
| 抓取入口 | 无站点级 robots、sitemap、llms.txt |
| 页面元数据 | 共享布局缺 canonical、作者、OG、Twitter 和 JSON-LD |
| 机器知识入口 | 没有把 C1-C6 与 994 个域发布为稳定实体索引 |
| GitHub 发布链 | 只有仓库检查，没有 Web 构建与 Pages 部署工作流 |
| 效果数据 | 没有主流 AI 引擎的固定 Prompt 基线，禁止声称品牌提及率或引用率提升 |

## 目标发布架构

```text
classification.tsv / research evidence
  -> domain-registry.ts / site.ts
  -> human-readable pages + JSON-LD
  -> llms.txt / llms-full.txt / knowledge-index.json
  -> robots.txt / sitemap-index.xml
  -> GitHub Pages
  -> build-time GEO audit
  -> engine-specific prompt sampling
  -> observed / recoverable / unobservable metrics
```

### 单一真相源

- 项目实体、发布者、规范 URL 与复核日期：`src/lib/site.ts`。
- C1-C6 域物理分类：`../domains/_possibility-space-control/classification.tsv`。
- 页面实体与公开入口：`PUBLIC_PAGES`。
- 优先域有界主张、来源、反证与候选端点：`src/lib/evidence-registry.ts` 对 `docs/reference/` 四个现有寄存器的只读投影。
- GEO 外部监测问题：`src/data/geo-monitoring-prompt-bank.json`。
- 指标定义与可观测性：`/geo-metrics.json`。
- 构建后技术结果：`dist/geo-readiness-audit.json`。

## 实体与关系契约

核心实体：`ResearchProject`、`Publisher`、`SubjectContinuity`、`Tier`、`ResearchDomain`、`Claim`、`SourceCard`、`Falsifier`、`SafetyBoundary`、`Page`。

核心关系：

| 关系 | 含义 |
| --- | --- |
| `classified_as` | 研究域归入 C1-C6 层级 |
| `supports_claim` | 来源在限定语境内支持主张 |
| `falsifies_claim` | 证据触发主张失败或降级 |
| `blocked_by_boundary` | 安全、证据或模型门禁阻止外推 |
| `uses_source` | Fact Card 或页面引用来源 |
| `maps_to_model_position` | 域只进入指定模型位置 |
| `published_as` | 仓库对象被发布为页面或机器资源 |

JSON-LD 只能表达页面正文和仓库已经公开的事实，不得用结构化数据添加正文不存在的疗效、可行性、排名、资质或推荐。

## 页面可引用契约

高价值页面至少包含：

1. 一个自足的规范定义；
2. 三到五个可单独抽取的事实、变量或判断；
3. 一个因果链、对比表或审查步骤；
4. 明确的适用边界、非目标或反证条件；
5. 发布者、复核日期、canonical URL 和来源入口；
6. 与站点实体一致的 JSON-LD。

强主张必须能够回到 `source_id / publisher / URL or artifact / verification_date / extraction_note / confidence_tier`。AI 回答、模型记忆和未核验第三方转述不能作为正式来源。

## 8 维内容评分

每项 1-5 分：语义密度、结构规范性、可引用性、权威信号、可读性、鲁棒性、新颖性、跨域贡献。任一维度低于 3 进入修复清单；均分低于 4 时，优先修复现有页面，不扩张同类内容。

这套人工评分不与 `audit:geo` 的机械通过率混为一谈。机械门禁只证明发布结构完整，不证明内容被 AI 引擎引用。

## 指标与归因

### 自动观测

- crawler entry coverage；
- public page metadata coverage；
- sitemap coverage；
- domain registry coverage；
- project-base URL violations；
- 构建成功率与审计通过率。

### 外部采样

- 品牌/实体出现率；
- 候选率与推荐率；
- 描述准确率；
- 答案引用率与引用位置；
- 多轮答案稳定性；
- 引用段落与答案的相似度。

外部指标按引擎、入口、模型/表面、语言和日期分别保存。每个 Prompt 每个观察窗口至少重复三次。没有基线、对照 Prompt、观察窗口和外部事件记录时，不做强因果归因。

### 归因标签

- `observed`：仓库、站点或分析系统直接观测；
- `recoverable`：可通过平台导出、日志或人工复核恢复；
- `unobservable`：平台未提供证据，禁止伪造精确值。

## 执行与验证

本地开发：

```bash
cd web
npm ci
npm run dev -- --port 18774
```

模拟 GitHub Pages 并运行完整 GEO 门禁：

```bash
cd web
npm run audit:geo
```

门禁验证：

- 站点级抓取文件存在；
- 机器 JSON 可解析；
- 994 个域完整进入知识索引；
- 13 个公开页面具备 canonical、作者、社交元数据、JSON-LD 和语义正文；
- 30 条优先域主张、21 个来源锚点、60 条反证和 90 个候选端点进入有界证据图；
- 每条证据图关系边均能解析到存在的节点，来源支持边保留 source ID 与迁移边界；
- sitemap 覆盖所有公开 HTML 页面；
- 子路径构建不产生逃逸到域名根路径的内部链接；
- `.txt`、`.json`、`.css`、`.js` 等文件型 URL 不被错误改写为目录型尾斜杠；
- 页面引用的项目内部链接和静态资源均能映射到真实构建产物；
- 外部 AI 指标仍保持“未采样”，不会被技术门禁伪装成效果结果。

## 路线图

### P0：发布面闭环

- [x] GitHub Pages 子路径与内部链接契约；
- [x] sitemap、robots、llms 与完整机器上下文；
- [x] 994 域机器知识索引；
- [x] 共享 canonical、作者、OG、Twitter 与 JSON-LD；
- [x] 构建时 GEO 门禁；
- [x] Pages 部署工作流。

### P1：外部发现与基线

- [ ] 首次远程部署并确认 GitHub Pages 可访问；
- [ ] 将 GitHub About website 指向正式站点；
- [ ] 提交主流搜索平台站点地图；
- [ ] 按 Prompt Bank 建立各 AI 引擎独立基线；
- [ ] 记录引用 URL、描述错误和边界遗漏。

### P2：证据图深化

- [x] 把 Claim、Source Anchor、Falsifier、Endpoint 与 Domain 的证据边发布成可查询图；
- [x] 为公开 Fact Card 建立来源、反证、禁止用途和迁移边界门禁；
- [ ] 为 C1 优先域完成独立 fresh review，并补齐来源级人群、效应量、不确定性与复核日期；
- [ ] 以页面 8 维评分选择内容修复顺序；
- [ ] 只有观察数据形成后，评估引用吸收与自然流量变化。

## 禁止做法

- 不堆砌关键词，不批量生成缺少来源的页面；
- 不把搜索排名、页面数量或流量直接等同于 AI 引用可信度；
- 不在 schema 中添加正文没有的事实；
- 不用 AI 自己的回答证明项目被 AI 推荐；
- 不保证排名、收录、引用或流量；
- 不将研究域登记表达为临床有效、产品可用或模型准入。
