# Cloudflare Pages 发布契约

## 目标

Human Infra 的公开 Web 面只使用 Cloudflare `pages.dev` 域名。

| 产品 | Pages 项目 | 固定入口 | 发布对象 |
| --- | --- | --- | --- |
| 语言门户 | `human-infra` | <https://human-infra.pages.dev/> | Wikimedia 官方门户快照与最小路由适配 |
| Wiki | `human-infra-wiki` | <https://human-infra-wiki.pages.dev/> | 本地 MediaWiki 生成的只读快照 |
| 科技树 | `human-infra-tech-tree` | <https://human-infra-tech-tree.pages.dev/> | Historical Tech Tree 派生的 Human Infra 科技树 |

禁止为这三个产品绑定 `tradecat.org` 或其他自定义域名，禁止恢复 Cloudflare Tunnel 作为公开发布路径，禁止把已退役的 Research Narrative 部署到任一 Pages 项目。

## 真相源

- Wiki 内容、模板、分类、表单和修订历史的运行时真相源是本地 MediaWiki 与 MariaDB。
- `wiki/content/` 是可重复导入的受治理种子，不等于完整数据库。
- `wiki/portal/` 是语言门户源码，视觉和 DOM 归 Wikimedia 官方门户发布物。
- `wiki/runtime/pages/` 是忽略的构建产物，不能手工修改或提交。
- 科技树由其正式源码仓库独立构建和部署，Wiki 不复制科技树运行时。

## 能力边界

公开 Wiki 是发布时点的只读快照，保留 MediaWiki Vector 阅读结构、内部词条链接、分类和标题搜索。登录、编辑、历史浏览、实时 API、VisualEditor、Page Forms 和数据库写入只在本地 MediaWiki 可用。公开快照不得伪装为可编辑站点，也不得成为新的内容真相源。

## 发布流程

```bash
cd wiki
make validate
make smoke
make pages-build
make pages-deploy
make pages-smoke
```

`pages-build` 从本地 MediaWiki API 枚举全部非讨论命名空间，以 8 路有界并发导出页面正文，并复用一份 MediaWiki 原生皮肤壳和静态资源。`pages-deploy` 只创建或更新 `human-infra` 与 `human-infra-wiki` 两个 Pages 项目，不修改科技树项目。`pages-smoke` 必须验证三个固定入口、Wiki 首页 DOM、普通词条、标题搜索和科技树产品标识。

## 发布门禁

1. 快照必须包含 `Human Infra:首页`。
2. 页面索引数必须与导出成功数一致，任何页面失败都终止构建。
3. 发布产物不得包含 `tradecat.org`。
4. Wiki 首页必须保留 `mp-2012` DOM，门户必须保留 `www-wikipedia-org` DOM。
5. Pages Worker 只负责快照路由、模板注入和只读标题搜索，不承载内容编辑、医学模型或数据库。
6. 远端 smoke 全部通过后，才能把发布视为完成。

## 回滚

Cloudflare Pages 保留历史 deployment。需要回滚时使用 Pages 控制台或 Wrangler 将上一个已验证 deployment 提升为 production；本地 MediaWiki 数据不随静态发布回滚。若构建失败，继续保留上一版公开快照，不得重新开放 Tunnel 绕过门禁。
