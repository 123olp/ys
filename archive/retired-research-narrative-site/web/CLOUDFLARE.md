# Cloudflare Pages 发布

Cloudflare Pages 承载 Human Infra 的公开只读站点。它发布 Astro 生成的 HTML、D3
脚本、论文页和机器可读端点，不运行 MediaWiki、MariaDB，也不接收 Wiki 编辑。

## Git 集成

在 Cloudflare Dashboard 中创建 Pages 项目并连接
`tradecatlabs/human_infra`，使用以下配置：

| 配置 | 值 |
| --- | --- |
| Production branch | `main` |
| Root directory | `web` |
| Build command | `npm run audit:cloudflare` |
| Build output directory | `dist` |
| Node.js version | `22` |

生产环境变量：

```text
PUBLIC_SITE_ORIGIN=https://human-infra.pages.dev
```

若 Pages 项目名或自定义域名不同，必须将 `PUBLIC_SITE_ORIGIN` 改为最终公开源站，
且不得包含末尾 `/`。该值决定 canonical URL、站点地图、`robots.txt`、JSON-LD
与 LLM 入口。

## 本地验证

```bash
cd web
npm ci
PUBLIC_SITE_ORIGIN=https://human-infra.pages.dev npm run audit:cloudflare
```

成功后，`dist/geo-readiness-audit.json` 必须为 `pass`。Cloudflare Pages 只消费
`dist/`，不得直接发布 `src/`、研究账本或 Wiki 运行时数据。

## 直接上传

Git 集成不可用时，可以使用 Cloudflare 官方 Wrangler CLI：

```bash
cd web
PUBLIC_SITE_ORIGIN=https://human-infra.pages.dev npm run audit:cloudflare
npx wrangler@latest pages deploy dist --project-name human-infra
```

直接上传需要 Cloudflare 登录或 `CLOUDFLARE_API_TOKEN` 与
`CLOUDFLARE_ACCOUNT_ID`。不要把凭据写入仓库。

## 回滚

Cloudflare Pages 可从部署历史回滚到前一版本。GitHub Pages 流水线继续保留，
使用 `/human_infra` 子路径构建，作为独立的免费回滚与验证通道。

## Wiki 边界

`wiki/` 当前是 MediaWiki、MariaDB 和上传卷组成的动态系统，不能部署到 Pages。
公开 Wiki 的零成本路径是后续新增受审计的静态导出流水线；在该流水线完成前，
Pages 不得伪装成可编辑 Wiki，也不得把本地 `18782` 地址暴露为公开链接。
