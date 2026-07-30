# Cloudflare Pages 发布契约

## 目标

实验室主站、Human Infra 门户、Wiki 与科技树是四个独立发布对象。根域名只属于实验室主站；Human Infra 仓库只维护门户、Wiki 和科技树产品关系，不得构建或部署实验室主站。

| 产品 | 所有者 / Pages 项目 | canonical | 持续可用入口 | 发布对象 |
| --- | --- | --- | --- | --- |
| 实验室主站 | `tradecatlabs` 仓库 / `human-infra-main` | <https://tradecatlabs.com/> | <https://human-infra-main.pages.dev/> | Academic Pages 实验室站点 |
| Human Infra 门户 | 本仓库 / `human-infra` | <https://human-infra.pages.dev/> | 同左 | Wikimedia 语言门户适配发布物 |
| Human Infra Wiki | 本仓库 / `human-infra-wiki-public` | <https://wiki.tradecatlabs.com/> | `human-infra-wiki.pages.dev`、`human-infra-wiki-public.pages.dev` | MediaWiki 只读静态快照 |
| Human Infra 科技树 | 科技树源码仓库 / `human-infra-tech-tree-public` | <https://tree.tradecatlabs.com/> | `human-infra-tech-tree.pages.dev`、`human-infra-tech-tree-public.pages.dev` | Historical Tech Tree 派生科技树 |

自定义子域名和对应 Pages 项目必须位于同一 Cloudflare 账户。禁止绑定 `tradecat.org`，禁止通过 Worker、Pages Functions、Tunnel 或跨账户反向代理拼接产品。添加自定义子域名不得删除、重定向或禁用原有 `pages.dev` 入口。

## 所有权边界

- `tradecatlabs.com`、`human-infra-main` 及实验室主站内容只由 `tradecatlabs` 仓库维护。
- 本仓库不得包含构建、检查、部署或绑定实验室根域名的脚本、Make target 或 Pages 配置。
- Wiki 内容、模板、分类、表单和修订历史的运行时真相源是本地 MediaWiki 与 MariaDB。
- `wiki/content/` 是可重复导入的受治理种子，不等于完整数据库。
- `wiki/portal/` 是语言门户源码，视觉和 DOM 归 Wikimedia 官方门户发布物。
- `wiki/runtime/pages/` 是忽略的构建产物，不能手工修改或提交。
- `wiki/config/geo-publication.json` 是 Human Infra 三个产品的 URL 与实体关系真相源。
- 科技树由其正式源码仓库独立构建和部署，Wiki 不复制其运行时。

## 能力边界

公开 Wiki 是发布时点的只读纯静态快照，保留 MediaWiki Vector 阅读结构、内部词条链接、分类、静态标题搜索、语言选择、页内目录和打印。登录、编辑、讨论、历史浏览、变体切换、特殊页面、实时 API、VisualEditor、Page Forms、Vector 外观偏好和数据库写入只在本地 MediaWiki 可用。

静态发布采用能力白名单。任何控件进入公开快照前，必须证明其目标路由、状态变化和用户反馈在无 MediaWiki 后端、无 ResourceLoader 的条件下真实成立。`href="#"`、空菜单、不可操作的编辑链接、失效折叠按钮和未加载 tablesorter 却保留的 `sortable` 类均阻断发布。

## 发布流程

```bash
cd wiki
make validate
make smoke
make pages-build
make pages-deploy
make pages-smoke
```

`pages-build` 从本地 MediaWiki API 枚举全部非讨论命名空间，以有界并发导出页面正文，并分别复用 MediaWiki 首页外壳与普通文章外壳。普通文章必须携带其自身 Vector 目录和完整页面类，内部链接改写为 `/wiki/<title>/` 静态路径，同源资源必须本地化。标题搜索只读取静态索引；旧 `/index.php` 路由只允许使用 Pages 原生 `_redirects` 和静态兼容页。

`pages-deploy` 只创建或更新 `WIKI_PAGES_PROJECT` 指定的 Wiki 项目，默认是第二账户的 `human-infra-wiki-public`；它不得部署门户、科技树或实验室主站。科技树由其源码仓库独立部署。自定义域名绑定属于 Cloudflare 发布控制面，不得通过修改页面内容模拟。

## DNS 控制面前提

- Wrangler OAuth 只用于创建 Pages deployment 和管理 Pages 自定义域关联，不代表拥有 Zone DNS 编辑权限。
- Pages 自定义域显示 `CNAME record not set` 时，必须在 `tradecatlabs.com` 所属账户单独创建 DNS 记录；不得通过 Worker、Functions、Tunnel 或页面重定向绕过。
- DNS API 令牌必须采用最小权限：`Zone / Zone / Read` 与 `Zone / DNS / Edit`，资源限定为 `Specific zone / tradecatlabs.com`。
- 客户端 IP 过滤默认留空；只有执行环境出口 IP 固定且已纳入运维契约时才允许启用。
- Wiki 记录为 `wiki CNAME human-infra-wiki-public.pages.dev`，科技树记录为 `tree CNAME human-infra-tech-tree-public.pages.dev`，均由 Cloudflare 代理。
- 令牌不得写入仓库、脚本、命令历史、构建产物或日志；只允许通过当前进程环境变量临时注入，并在任务完成后撤销。

## 发布门禁

1. 快照必须包含 `Human Infra:首页`。
2. 页面索引数必须与导出成功数一致，任何页面失败都终止构建。
3. 发布产物不得包含 `tradecat.org`。
4. 本仓库不得包含 `main-domain-build`、`main-domain-smoke`、`human-infra-main` 部署调用或 `tradecatlabs.com` 发布输出目录。
5. Wiki 首页必须保留 `mp-2012` DOM，门户必须保留 `www-wikipedia-org` DOM。
6. Wiki 首页必须使用 `page-Main_Page` 外壳且不得继承普通文章目录；页脚许可证和 MediaWiki 徽标必须可达。
7. 普通词条目录、页面类、链接、标题和修订上下文必须绑定当前词条。
8. 门户必须保留上游脚本依赖的 DOM 契约，不得制造浏览器异常或资源 404。
9. 门户和 Wiki 必须生成原生 `404.html`，未知路径必须返回 HTTP 404。
10. 发布物必须是纯静态资产，禁止 `_worker.js`、`_routes.json`、`functions/` 或等价请求时计算入口。
11. 静态词条 HTML、快照索引、sitemap 与 NDJSON 数量必须一致。
12. Vector 外观偏好只归完整 MediaWiki ResourceLoader 所有；静态快照不得模拟其状态机。
13. `audit-static-runtime-contract.py` 必须全量拒绝伪操作入口、失效内部路由、运行时操作 ID、ResourceLoader 资源和失效动态类。
14. `wiki.tradecatlabs.com` 的 canonical、Open Graph、JSON-LD、robots 和 sitemap 必须一致指向 Wiki 子域名。
15. `tree.tradecatlabs.com` 的 canonical、Open Graph、JSON-LD、robots 和 sitemap 必须一致指向科技树子域名。
16. `pages-smoke` 必须同时验证自定义子域名、历史 `pages.dev` 回退入口和当前账户 `pages.dev` 镜像，且不得允许任一入口调用 Functions。

## 回滚

Cloudflare Pages 保留历史 deployment。内容回滚应将对应项目的上一已验证 deployment 提升为 production。自定义域名故障时，可以临时移除该子域名绑定，`pages.dev` 回退入口仍保持可用；不得回退到 Worker、Functions、Tunnel 或根域名复用方案。本地 MediaWiki 数据不随静态发布回滚。
