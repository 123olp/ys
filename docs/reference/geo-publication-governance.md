# GEO 发布治理

## 目标

Human Infra 的生成式引擎优化以“可发现、可解析、可引用、可核验”为目标，不以关键词堆砌、批量低质量页面或无法验证的流量归因为目标。公开知识必须先满足项目证据边界，再进入搜索引擎、问答引擎和智能体可消费的发布层。

## 实体图

| 实体 | 唯一公开入口 | 机器职责 |
| --- | --- | --- |
| Tradecat Labs | <https://tradecatlabs.com/> | 实验室组织、项目组合与研究产出的发布者根实体 |
| Human Infra | <https://human-infra.pages.dev/> | Human Infra 项目规范名称、别名与产品关系的入口实体 |
| Human Infra Wiki | <https://wiki.tradecatlabs.com/> | 可引用定义、研究边界、证据来源和交叉链接 |
| Human Infra Tech Tree | <https://tree.tradecatlabs.com/> | 历史技术、当前能力、未来条件与目标依赖关系 |
| 源码仓库 | <https://github.com/tradecatlabs/human_infra> | 研究域、证据登记、治理契约与可复现工具 |

`wiki/config/geo-publication.json` 是三个 Human Infra 产品的名称、描述、URL、发布者和关系真相源。历史入口 `human-infra-wiki.pages.dev`、`human-infra-tech-tree.pages.dev` 与当前账户镜像 `human-infra-wiki-public.pages.dev`、`human-infra-tech-tree-public.pages.dev` 都是持续可用的静态回退入口，不是第二个 canonical。门户与 Wiki 构建过程消费该配置；科技树是独立源码仓库，必须通过构建门禁保持同一实体名称和 URL。实验室主站属于独立 `tradecatlabs` 仓库，本仓库不得生成或部署它。

## 发布契约

每个公开产品必须提供：

1. 唯一 `title`、摘要、canonical 和可索引策略。
2. 与 canonical 一致的 Open Graph 元数据。
3. 不虚构作者、日期、评价或疗效的 Schema.org JSON-LD。
4. 返回真实内容类型和状态码的 `robots.txt`、`sitemap.xml` 与 `llms.txt`。
5. 指向其他正式产品和 GitHub 真相源的实体关系。
6. 页面正文或机器索引中的证据边界与禁止用途。

Wiki 还必须为每个词条生成：

- 从页面首个有效正文段抽取的描述；不得由模型生成新事实。
- 词条 canonical、`Article` JSON-LD 和页面级 Open Graph。
- 与快照页面数严格相等的 sitemap 和 NDJSON 元数据索引。
- 标题、URL、摘要、修订 ID 与别名；修订 ID不等于修订时间。

## 静态发布与成本边界

门户、Wiki 和科技树的公开版本均应由 Cloudflare Pages 静态资产层直接响应。实验室根域名由独立 Academic Pages 主站维护，Human Infra 不复用或覆盖它。Wiki 必须在构建期完成页面外壳注入、内部链接改写、canonical、结构化数据、sitemap 和机器索引生成；标题搜索只能在浏览器端读取仅含标题、别名和 URL 的静态索引。逐页正文 JSON 与模板外壳不得在预渲染后继续发布。任何 `_worker.js`、`_routes.json`、`functions/` 或等价请求时计算入口都属于发布阻塞项，因为它会把静态访问和爬虫抓取错误计入 Workers 请求与 CPU 配额。

## 问题覆盖

| 问题类型 | 主要入口 |
| --- | --- |
| Human Infra 是什么 | 门户、Wiki 首页、项目 README |
| 什么是主体持续性或有效永生 | Wiki 核心词条与 C0-C1 理论 |
| 哪些技术与目标有关、依赖什么 | 科技树节点、关系与 Wiki 跳转 |
| 一项主张由什么证据支持 | Wiki 证据来源、Source Card 与仓库登记表 |
| 当前确定了什么、仍不知道什么 | 证据边界、反证条件、争议与未知 |
| 如何参与、引用或复用 | 门户、Wiki 参与入口、GitHub 与 `CITATION.cff` |

## 指标与归因边界

当前可直接观测并进入发布门禁的指标包括 HTTP 状态码与内容类型、canonical/摘要/Open Graph/JSON-LD 覆盖率、sitemap/快照/NDJSON 条目一致性、正式入口与证据边界覆盖、桌面和移动端可读性、链接可达性与控制台错误。

搜索索引覆盖、抓取频率、品牌提及率、答案引用率、推荐曝光量、自然流量和有效访问需要外部平台数据。没有 Search Console、Cloudflare Web Analytics、引荐日志或问答引擎实验记录时，不得声称 GEO 带来了流量、引用或转化提升。

## 验证

```bash
cd wiki
make pages-build
python3 scripts/audit-geo-publication.py \
  --portal-dir runtime/pages/portal \
  --wiki-dir runtime/pages/wiki
make pages-smoke
```

科技树独立执行 `npm run build:local`，并验证 canonical、JSON-LD、`robots.txt`、`sitemap.xml`、`llms.txt` 和 `entity.jsonld` 全部指向 `tree.tradecatlabs.com`。Wiki 必须以 `wiki.tradecatlabs.com` 为 canonical；两个产品的 `pages.dev` 回退入口必须持续可达。`tradecatlabs.com` 只标识实验室主站和发布组织，不是 Human Infra 门户 canonical。

## 来源方法

本契约吸收本地 GEO 知识库的全景审计、页面审计、品牌实体图、知识库建设、内容可引用性、效果监测和归因边界方法。知识库仅提供方法，不是 Human Infra 内容证据；生命、医学、技术或主体连续性主张仍须通过本项目来源和审查协议。
