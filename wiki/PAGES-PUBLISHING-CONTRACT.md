# Cloudflare Pages 发布契约

## 目标

Human Infra 使用一个品牌主入口与三个持续可用的 `pages.dev` 入口。主域名只负责静态导航，不代理、复制或接管 Wiki 与科技树请求。

| 产品 | 账户 / Pages 项目 | 主入口 | 持续可用入口 | 发布对象 |
| --- | --- | --- | --- | --- |
| 品牌主入口 | 第二 Cloudflare 账户 / `human-infra-main` | <https://tradecatlabs.com/> | `human-infra-main.pages.dev` | MediaWiki 原生首页静态快照、Wiki 与科技树路由 |
| 语言门户回退 | 原 Cloudflare 账户 / `human-infra` | 同上 | <https://human-infra.pages.dev/> | 同一门户的开发与故障回退入口 |
| Wiki | 原 Cloudflare 账户 / `human-infra-wiki` | <https://human-infra-wiki.pages.dev/> | 同左 | 本地 MediaWiki 生成的只读快照 |
| 科技树 | 原 Cloudflare 账户 / `human-infra-tech-tree` | <https://human-infra-tech-tree.pages.dev/> | 同左 | Historical Tech Tree 派生的 Human Infra 科技树 |

`tradecatlabs.com` 的 Zone 与 `human-infra-main` 必须位于同一 Cloudflare 账户。禁止绑定 `tradecat.org`，禁止把 Wiki 或科技树流量经 Worker/Functions 反向代理到另一个账户，禁止恢复 Cloudflare Tunnel 作为公开发布路径，禁止把已退役的 Research Narrative 部署到任一 Pages 项目。

## 真相源

- Wiki 内容、模板、分类、表单和修订历史的运行时真相源是本地 MediaWiki 与 MariaDB。
- `wiki/content/` 是可重复导入的受治理种子，不等于完整数据库。
- `wiki/portal/` 是语言门户源码，视觉和 DOM 归 Wikimedia 官方门户发布物。
- `wiki/runtime/pages/` 是忽略的构建产物，不能手工修改或提交。
- `wiki/config/geo-publication.json` 中的门户 URL 是主域名 canonical；`fallbackUrl` 记录持续存在的 `pages.dev` 回退入口。回退入口不得反向覆盖 canonical。
- 逐页正文 JSON 和模板外壳只属于构建期中间状态，不得进入公开发布物；公开搜索索引只保留标题、别名和静态 URL。
- 科技树由其正式源码仓库独立构建和部署，Wiki 不复制科技树运行时。

## 能力边界

公开 Wiki 是发布时点的只读纯静态快照，保留 MediaWiki Vector 阅读结构、内部词条链接、分类、静态标题搜索、语言选择、页内目录和打印。登录、编辑、讨论、历史浏览、变体切换、特殊页面、实时 API、VisualEditor、Page Forms、Vector 外观偏好和数据库写入只在本地 MediaWiki 可用。公开快照不得伪装为可编辑站点，也不得成为新的内容真相源。

静态发布采用能力白名单，而不是按已知缺陷维护控件黑名单。任何控件要进入公开快照，必须能够证明其目标路由、状态变化和用户反馈在无 MediaWiki 后端、无 ResourceLoader 的条件下仍真实成立；否则必须删除操作外观，或将内容降级为可直接阅读的普通文本。`href="#"`、空菜单、不可操作的编辑链接、失效的折叠按钮和未加载 tablesorter 却保留的 `sortable` 类均属于发布阻断问题。

## 发布流程

```bash
cd wiki
make validate
make smoke
make pages-build
make pages-deploy
make pages-smoke
make main-domain-build
make main-domain-smoke
```

`pages-build` 从本地 MediaWiki API 枚举全部非讨论命名空间，以 8 路有界并发导出页面正文，并分别复用 MediaWiki 首页外壳与普通文章外壳。每篇普通文章必须从同一修订的 MediaWiki 渲染页携带其原生 Vector 目录和完整 `body` 页面类，禁止复用模板文章目录或命名空间状态。外壳中的粘性标题、内部页面链接和修订上下文必须在构建期绑定当前词条，内部链接必须改写为 `/wiki/<title>/` 静态路径。CSS 引用资源以及 HTML `src` / `srcset` 引用的同源资源必须一并本地化。标题搜索在浏览器端读取静态索引；旧 `/index.php` 路由只允许使用 Pages 原生 `_redirects` 和静态兼容页。`pages-deploy` 只创建或更新 `human-infra` 与 `human-infra-wiki` 两个 Pages 项目，不修改科技树项目。`pages-smoke` 必须验证三个固定入口、Wiki 首页 DOM、普通词条目录一致性、标题搜索、真实 404、页脚资源和科技树产品标识。

`main-domain-build` 只从已通过 Wiki 发布门禁的 `runtime/pages/wiki/index.html`、`404.html`、`assets/`、`images/` 与 `resources/` 生成 `runtime/pages/main-domain/`。它不得消费 Wikimedia 语言门户 HTML，不得编写新页面框架，只允许把 canonical 改为 `tradecatlabs.com`，把 Wiki 内链与搜索路由到正式 Wiki，并把 MediaWiki 首页中的“历史技术谱系”入口路由到正式科技树。该产物独立部署到第二账户的 `human-infra-main`，不得触发科技树构建或旧账户发布。主域名上线后，`main-domain-smoke` 必须同时验证主域名与三个旧 `pages.dev` 入口，证明它们并存。

## 发布门禁

1. 快照必须包含 `Human Infra:首页`。
2. 页面索引数必须与导出成功数一致，任何页面失败都终止构建。
3. 发布产物不得包含 `tradecat.org`。
4. Wiki 首页必须保留 `mp-2012` DOM，门户必须保留 `www-wikipedia-org` DOM。
5. Wiki 首页必须使用 `page-Main_Page` 外壳且不得继承普通文章目录；页脚许可证和 MediaWiki 徽标必须返回成功。
6. 普通词条目录必须来自该词条自身的 MediaWiki Vector 渲染结果；不得把外壳来源页面的目录传播给其他词条。
7. 门户必须保留其上游脚本依赖的 DOM 契约；不得在保留脚本时删除对应节点并制造浏览器异常。
8. 普通词条的页面类、内部链接、canonical、标题和公开修订说明必须绑定当前词条；不具备后端支持的粘性操作栏、登录回跳与永久修订链接不得进入公开快照。
9. 静态快照必须保留 Vector 语言菜单的无脚本开合状态，不得让关闭的下拉内容造成移动端横向溢出。
10. 语言门户和 Wiki 必须生成 Pages 原生 `404.html`；未知路径必须返回 HTTP 404，不得以首页 HTML 和 200 形成软 404。
11. 公开发布物必须是纯静态资产，禁止包含 `_worker.js`、`_routes.json`、`functions/` 或其他请求时计算入口；模板注入、词条路由索引和 GEO 元数据必须在构建期完成。
12. 静态词条 HTML 数必须与快照索引数严格相等；每个索引项必须有唯一 `urlPath` 和对应静态文件。
13. Wrangler Pages 本地验证必须报告 `No Functions`，远端 smoke 全部通过后才能把发布视为完成。
14. Vector 外观偏好只能由完整 MediaWiki ResourceLoader 的 `skins.vector.js` 与 `skins.vector.clientPreferences` 提供。静态快照必须移除外观入口和控件，声明原生 `appearance-pinned-clientpref-0` 无脚本状态；禁止冻结浏览器增强 DOM、复制上游模块片段、加载自写适配器或模拟 pinnable 状态机。
15. `audit-static-runtime-contract.py` 必须全量扫描静态 HTML，拒绝无目标链接、缺少目标文件的内部 Wiki 路由、非搜索表单 action、运行时操作 ID、ResourceLoader 资源以及失效的折叠和排序标记；构建期审计与线上抽样 smoke 均通过后才能发布。
16. 主域名必须通过 `check-main-domain-release.py`：`generator` 必须来自 MediaWiki，Vector 关键 DOM 必须存在，标签/ID/class、TemplateStyles、脚本和样式表引用必须与 Wiki 首页完全一致，`assets/`、`images/`、`resources/` 必须逐文件哈希一致；任何自写 UI、CSS、适配器、`_worker.js`、`_routes.json` 或 `functions/` 都必须阻塞发布。
17. `tradecatlabs.com` 上线不得删除、重定向或禁用 `human-infra.pages.dev`、`human-infra-wiki.pages.dev` 与 `human-infra-tech-tree.pages.dev`。

## 回滚

Cloudflare Pages 保留历史 deployment。需要回滚主域名时，先从 `human-infra-main` 移除 `tradecatlabs.com` 的自定义域名绑定，再保留三个原有 `pages.dev` 入口作为服务面；需要回滚内容时使用 Pages 控制台或 Wrangler 将上一个已验证 deployment 提升为 production。本地 MediaWiki 数据不随静态发布回滚。若构建失败，继续保留上一版公开快照，不得重新开放 Tunnel 或 Worker 代理绕过门禁。
