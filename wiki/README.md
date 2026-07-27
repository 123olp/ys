# Human Infra Wiki

Human Infra Wiki 是科技树节点的知识详情层，也是项目专有概念、研究域和证据来源的可修订知识库。语言入口直接复用 Wikimedia 官方 `www.wikipedia.org` 门户发布物；中文站使用 MediaWiki 1.46、MariaDB 11.8、Vector、UniversalLanguageSelector、VisualEditor 和 Page Forms，保持 Wikipedia 同系阅读与编辑体验。

## 一键部署

前提：Docker Engine 与 Docker Compose 可用。

```bash
cd wiki
./scripts/bootstrap.sh
```

默认入口：

- 多语言门户：`http://localhost:18784/`
- 中文 Wiki：`http://localhost:18782/`
- 中文项目首页：`http://localhost:18782/index.php?title=Human_Infra:首页`
- 管理员：`HumanInfraAdmin`
- 初始密码：仅保存在本机 `wiki/.env`

Windows 11 可直接访问这些 `localhost` 地址。若端口冲突，在 `.env` 同步修改 `WIKI_PORTAL_PORT`、`WIKI_PORT` 与 `WIKI_SERVER` 后重新执行 `./scripts/bootstrap.sh`。

生产入口：

- 多语言门户：<https://human-infra.pages.dev/>
- 中文 Wiki：<https://human-infra-wiki.pages.dev/>
- 科技树：<https://human-infra-tech-tree.pages.dev/>

公开入口只使用 Cloudflare Pages，不绑定自定义域名，也不通过 Tunnel 暴露本地容器。语言门户是 Wikimedia 官方门户快照；中文 Wiki 是本地 MediaWiki 在发布时预渲染的纯静态只读快照，保留原生 Vector 阅读结构、内部链接、分类和浏览器端标题搜索。发布产物禁止包含 Pages Worker 或 Functions，因此正常页面和静态资源请求不消耗 Workers 函数配额。登录、编辑、讨论、历史、变体切换、特殊页面、实时 API、VisualEditor 与 Page Forms 只在本地 MediaWiki 可用；公开快照会移除这些操作入口，并由静态运行时契约审计器阻止无目标链接和失效动态控件进入发布物。完整边界和回滚方式见 [Pages 发布契约](PAGES-PUBLISHING-CONTRACT.md)。

静态快照同时冻结 Vector 2022 原生外观面板，提供文本大小、页面宽度和颜色模式。控件 DOM 与样式来自固定的 Vector/Wikipedia 上游快照，静态适配器只把选择映射到 Vector 已定义的 document classes，并在当前浏览器保存匿名偏好；它不建立独立设置系统。钉住面板遵循 Vector 原生 `1120px` 桌面断点，窄屏和移动端保持隐藏，不能挤占正文首屏。

## 信息架构

```text
多语言门户
  -> 中文语言版本
  -> Human Infra:首页
  -> Portal:专题
  -> 研究域 / 技术节点 / 证据来源
  -> Category:Human Infra Wiki 单根分类体系
```

语言版本准入遵循 [语言版本契约](LANGUAGE-EDITION-CONTRACT.md)，首页和专题层遵循 [首页与专题门户契约](HOMEPAGE-PORTAL-CONTRACT.md)。门户上的多语言入口当前切换 MediaWiki 界面语言；独立内容版本目前只开放中文，不能把界面翻译误写为内容版本。

## 内容入口

首页提供三类标准录入：

| 类型 | 用途 | 必填核心 |
| --- | --- | --- |
| 研究域 | C1-C6 研究域的对象、边界和证据状态 | 域 ID、层级、对象、持续性作用、证据状态 |
| 技术节点 | 科技树历史节点、当前技术和未来条件节点 | 节点 ID、阶段、状态、依赖、证据来源 |
| 证据来源 | 论文、报告、数据集和权威页面 | 来源 ID、类型、引文、链接、支持边界 |

录入前阅读 [内容标准](CONTENT-STANDARD.md)。科技树接入遵循 [跳转契约](ROUTING-CONTRACT.md)。

中文首页由固定的中文维基百科首页 Wikitext、页首、TemplateStyles 和渲染 HTML 快照生成；`Template:首页/*` 仅维护 Human Infra 内容。生成产物禁止手工修改，上游固定修订、哈希与许可记录在 `homepage-upstream/UPSTREAM.md`。顶级专题使用 `Portal:` 命名空间；Portal 复用 MediaWiki 原生排版，按概览、精选研究、路线、证据边界、开放问题、参与建设和相关门户组织内容，不复制词条正文。全部内容分类必须通过有限父链追溯到 `Category:Human Infra Wiki`。

首页底部语言入口由 Vector、UniversalLanguageSelector、MediaWiki interwiki
数据和固定的官方跨语言链接共同生成。该入口属于皮肤运行时，不属于首页
Wikitext；不得用自定义 HTML/CSS 仿制。

Human Infra 品牌标识只有一个受版本控制的源文件：`portal/assets/human-infra-mark.svg`。Compose 将它只读提供给 Vector 皮肤，`make import` 再通过 MediaWiki 原生 `importImages` 导入本地文件仓库供首页模板引用；不得依赖 InstantCommons 上的占位品牌文件。首页“研究图谱”使用 `portal/assets/human-infra-tech-tree.png`，它是 Human Infra 科技树实际页面的渲染截图，通过同一原生图片导入链路发布，不以 CSS 背景或外链图片绕过 MediaWiki 文件系统。

## 常用命令

```bash
make up          # 启动
make stop        # 停止
make logs        # 查看日志
make import      # 重新导入受治理的种子页面
make smoke       # 验证 HTTP、数据库、扩展和关键页面
make language-selector-check # 验证 ULS V2 的 347 语言入口与开关行为
make portal-search-check # 验证生产门户只查询 Human Infra Wiki
make vector-appearance-check # 自启临时静态服务，验证外观面板固定、隐藏、断点与持久化
make backup      # 创建时间戳备份包
make validate    # 检查源码契约和 Compose 配置
make homepage-check   # 校验官方首页快照和生成产物未漂移
make homepage-reference # 生成标准化模板契约参考图
make homepage-compare   # 对模板契约执行零容差像素门禁
make homepage-audit-reference # 生成未经标准化的官方整页参考图
make homepage-audit     # 诊断官方整页与本地内容页的全部可见差异
make pages-build        # 生成门户与 Wiki Pages 发布产物
make pages-deploy       # 发布 human-infra 与 human-infra-wiki
make pages-smoke        # 验证三个 pages.dev 公开入口
```

更新官方语言门户快照：

```bash
python3 scripts/refresh-wikipedia-portal.py
make validate
make smoke
```

更新中文维基百科首页固定模板：

```bash
make homepage-refresh
make homepage-build
make homepage-check
make import
make homepage-reference
make homepage-compare
```

`make language-selector-check` 使用固定的 BackstopJS/Playwright 镜像点击
Vector 原生语言入口，验证 ULS V2 能展开并呈现 347 个语言条目；截图证据写入
忽略目录 `runtime/language-selector-open.png`。

首页视觉比较由固定版本 `backstopjs/backstopjs:6.3.25` 执行，不再维护自研像素或 DOM 几何比较器。`homepage-compare` 使用相同标准内容夹具比较模板、样式和响应式结构；`homepage-audit` 保留官方实时内容与本地研究内容的原始差异，用于诊断而不作为合格门禁。两套配置都要求相同尺寸且零像素差异，不能通过提高容差伪造对齐。官方标准化组件参考图保存在 `visual-regression/bitmaps_reference/` 并进入版本控制；只有确认上游修订、模板和浏览器版本均正确后才能运行 `make homepage-reference` 更新参考图。本项目不提供 BackstopJS `approve` 入口，避免把本地失败截图批准成官方标准。

HTML 报告入口：

```text
模板契约：wiki/runtime/visual-regression/contract/html_report/index.html
原始审计：wiki/runtime/visual-regression/html_report/index.html
```

## 备份与恢复

备份保存在 `runtime/backups/<timestamp>/`，包括压缩数据库、上传文件、`LocalSettings.php` 和校验清单。

```bash
./scripts/backup.sh
RESTORE_CONFIRM=restore ./scripts/restore.sh runtime/backups/<timestamp>
```

恢复会覆盖当前数据库、上传文件和运行时配置，必须先建立新的备份。

## 升级规则

1. 在 `Dockerfile` 和 `compose.yaml` 更新固定版本。
2. 先执行 `make backup`。
3. 执行 `docker compose --env-file .env build --pull wiki`。
4. 执行 `./scripts/bootstrap.sh`，它会运行 MediaWiki 数据库更新。
5. 执行 `make smoke` 并人工验证首页、表单、VisualEditor、引用和历史记录。

不要使用 `latest` 标签，不要在运行容器里手工安装扩展。
