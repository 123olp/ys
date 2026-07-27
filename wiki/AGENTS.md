# Human Infra Wiki 架构说明

`wiki/` 是项目内部知识词条与科技树详情页系统。它复用 MediaWiki，不自研百科引擎；仓库保存可复现定义，运行时状态保持隔离。

## 目录结构

```text
wiki/
├── AGENTS.md                 # 本目录职责与维护边界
├── README.md                 # 部署、使用、备份和恢复入口
├── CONTENT-STANDARD.md       # 词条内容、引用和命名规范
├── ROUTING-CONTRACT.md       # 科技树节点到内外 Wiki 的跳转契约
├── LANGUAGE-EDITION-CONTRACT.md # 语言门户与独立语言版本准入契约
├── HOMEPAGE-PORTAL-CONTRACT.md  # 项目首页与专题门户职责契约
├── PAGES-PUBLISHING-CONTRACT.md # pages.dev 唯一公开发布与只读边界
├── Dockerfile                # MediaWiki 与固定版本 Page Forms、ULS 镜像
├── Makefile                  # 常用运维命令入口
├── compose.yaml              # MediaWiki 与 MariaDB 服务编排
├── env.example               # 非敏感环境变量样例
├── config/
│   └── HumanInfraSettings.php # 站点权限、皮肤、扩展和版权配置
├── docker/
│   └── entrypoint.sh         # 运行时目录和 LocalSettings 装载
├── portal/                   # 独立多语言入口，不承载研究正文
│   ├── index.html            # Wikimedia 官方生产门户的本地适配快照
│   ├── languages.json        # 语言状态与展示顺序真相源
│   ├── adapter.js            # 本地 Wiki 路由与搜索胶水
│   ├── UPSTREAM.md           # 官方来源、版本、许可证和刷新流程
│   ├── LICENSE.wikimedia-portals # Wikimedia portals 上游许可证
│   ├── default.conf.template # Nginx 健康检查和 Wiki 公开基址注入
│   └── assets/               # 门户资源及 Wiki 只读复用的品牌与科技树图片种子
├── homepage-upstream/        # 中文维基首页不可手改的上游模板
│   ├── UPSTREAM.md           # mp-2012 来源、许可、转换边界和更新流程
│   └── snapshot/             # 原始 Wikitext、CSS、语言链接、渲染 HTML与哈希元数据
├── vector-upstream/          # Vector 客户端组件的固定上游快照
│   ├── UPSTREAM.md           # 组件来源、许可和静态适配边界
│   └── appearance-controls.html # 官方中文外观面板原生 DOM
├── content/
│   ├── manifest.tsv          # 种子页面标题与文件映射真相源
│   ├── Portal_*.wiki         # 原生 MediaWiki 专题导航与证据边界
│   ├── Category_*.wiki       # 以 Human Infra Wiki 为唯一根的分类图
│   └── *.wiki                # 首页、政策、模板、表单和词条种子
├── scripts/
│   ├── bootstrap.sh          # 幂等安装、升级、导入和启动
│   ├── import-content.sh     # 按 manifest 幂等更新种子页面
│   ├── backup.sh             # 数据库、上传文件和配置备份
│   ├── restore.sh            # 显式确认后的完整恢复
│   ├── refresh-wikipedia-portal.py # 刷新并最小适配官方门户发布物
│   ├── refresh-wikipedia-homepage.py # 抓取并固定中文维基首页原始资产
│   ├── build-wikipedia-homepage.py # 从固定快照注入内容槽位并生成首页
│   ├── run-backstop.sh       # 调用固定 BackstopJS Docker 镜像
│   ├── check-language-selector.sh # 验证 Vector + ULS V2 原生语言选择器
│   ├── check-language-selector.js # Playwright 浏览器行为断言
│   ├── smoke-test.sh         # HTTP、扩展、页面和数据库验证
│   ├── validate-source.sh    # 跟踪配置与内容契约检查
│   ├── export-pages-snapshot.py # 导出逐页目录与页面上下文的 MediaWiki 双外壳只读快照
│   ├── audit-static-runtime-contract.py # 拒绝静态快照中的伪操作入口与失效动态类
│   ├── vector-client-preferences-static.js # 静态页到 Vector 偏好类的最小适配
│   ├── build-pages-release.sh # 预渲染门户与 Wiki 纯静态 Pages 产物
│   ├── deploy-pages-release.sh # 发布两个 Pages 项目
│   └── smoke-pages-release.sh # 验证三个 pages.dev 公开入口
├── visual-regression/        # BackstopJS 配置与浏览器稳定化脚本
│   ├── backstop.contract.json # 标准内容夹具下的模板零容差门禁
│   ├── backstop.wikipedia.json # 官方实时页面对本地页面的原始审计
│   ├── bitmaps_reference/    # 受版本控制的官方标准化组件参考图
│   └── engine_scripts/
│       ├── onReady.js        # 等待字体/图片并关闭动画
│       └── onReadyContract.js # 使用相同内容夹具隔离模板差异
└── runtime/                  # 忽略：数据库、上传、安装配置和备份
```

## 职责边界

- `compose.yaml` 和 `Dockerfile` 固定可复现基础设施；不得把密码写入其中。
- `portal/` 是语言选择层，视觉、DOM 与通用控件行为归 Wikimedia 官方门户；本项目只维护品牌内容和本地路由适配，禁止新增平行视觉 CSS、存放研究结论或伪造尚未建立的语言版本。保留上游脚本时必须同时保留其依赖的官方 DOM，即使对应组件默认隐藏；不得裁掉节点后留下空指针脚本。`human-infra-mark.svg` 同时作为 Wiki 皮肤图标和 MediaWiki 本地文件仓库的受治理品牌种子；`human-infra-tech-tree.png` 是首页“研究图谱”槽位使用的项目科技树渲染证据，二者都必须通过 `importImages` 进入本地文件仓库。
- 门户到 Wiki 的公开路由由 `WIKI_PUBLIC_URL` 注入；未设置时才回退到同主机加 `WIKI_PUBLIC_PORT` 的本地开发地址。不得在门户 HTML 中硬编码部署域名。
- 公开环境只允许使用 `human-infra.pages.dev`、`human-infra-wiki.pages.dev` 和 `human-infra-tech-tree.pages.dev`。语言门户和 Wiki 由 Cloudflare Pages 发布，科技树由其独立 Pages 项目发布；禁止恢复自定义域名、Cloudflare Tunnel 或退役的 Research Narrative。
- 本地 MediaWiki 是可编辑真相源；公开 Wiki 是构建期预渲染的只读纯静态快照。导出器按页面类型选择首页/文章外壳，在构建期注入正文、原生 Vector 目录、页面类、标题、链接和修订上下文；标题搜索只读取静态索引。生产发布物禁止包含 `_worker.js`、`_routes.json` 或 `functions/`，不得为了路由、搜索或模板注入恢复请求时计算层。快照移除 ResourceLoader 后，只允许补回 Vector 原生控件所需的最小无脚本状态规则，不得建立平行视觉层。
- 公开快照采用静态能力白名单：保留正文导航、搜索、语言选择、页内目录、打印和已提供明确静态适配器的 Vector 外观偏好；登录、编辑、讨论、历史、特殊页面、变体切换、永久修订链接、可折叠内容与表格排序等依赖后端或 ResourceLoader 的能力必须移除或展开为只读内容，禁止留下 `href="#"`、空菜单或伪可用控件。
- `runtime/pages/` 是忽略的确定性发布产物；必须由 `make pages-build` 重建，禁止手工维护。门户和 Wiki 产物必须包含 Pages 原生 `404.html`，防止未知路径退化为首页软 404。发布与回滚遵循 `PAGES-PUBLISHING-CONTRACT.md`。
- `config/` 只保存可公开的站点策略；MediaWiki 生成的 `LocalSettings.php` 属于运行时。
- `content/` 是首次安装和可重复导入的页面种子，不是整个 Wiki 数据库的镜像；`import-content.sh` 必须先通过 MediaWiki 原生 `importImages` 导入图片种子，再导入引用它的页面，并在作业队列完成后用 `purgePage` 的标准输入契约刷新项目首页解析缓存。
- `homepage-upstream/snapshot/` 是中文首页结构与样式真相源；`Human Infra:首页`、页首和样式均由生成器从该快照产生，禁止手工改写生成产物。
- `vector-upstream/` 固定浏览器执行 Vector 原生模块后生成的外观组件 DOM；Pages 构建只能注入该快照并复用 Vector 原生 CSS 类。静态偏好适配器只允许切换 Vector 已定义的字号、宽度和颜色状态类，不得绘制平行控件或新增视觉语义；钉住面板必须遵循 Vector 原生 `1120px` 桌面网格断点，禁止在移动端进入正文流。
- 首页底部语言入口归 Vector + UniversalLanguageSelector + MediaWiki interwiki 运行时所有；官方语言链接作为固定快照进入生成链，禁止在首页 Wikitext 或 CSS 中复制按钮外观。
- `visual-regression/` 只保存 BackstopJS 配置、浏览器状态稳定脚本、视觉夹具和受版本控制的官方组件参考图；像素比较、差异图与报告由 BackstopJS 提供，禁止新增自研截图比较器。模板契约套件负责零容差 Gate，实时整页套件只负责诊断有意内容差异；禁止用 `approve` 把本地失败图替换为官方标准。
- `Template:首页/*` 只替换研究内容，禁止自建平行首页布局；`Portal:` 只做专题导航，不成为并行正文真相源。
- `Portal_*.wiki` 必须使用 MediaWiki 原生标题、列表、表格和链接，覆盖概览、精选研究、路线、证据边界、开放问题、参与建设和相关门户；禁止在正文重复页面 H1 或通过 `MediaWiki:Common.css` 建立平行门户视觉层。
- `Category:Human Infra Wiki` 是分类图唯一根；新增分类必须能沿父分类有限追溯到该根。模板维护分类只写入模板的 `<noinclude>`，不得污染调用页面。
- `runtime/` 和 `.env` 不得提交；数据迁移必须使用备份包。
- 科技树只保存稳定节点 ID、标题和目标路由；词条正文、引用和修订历史归 Wiki。
- 外部通用概念优先链接公共 Wikipedia；项目专有概念、模型和研究域进入本地 Wiki。

## 依赖与验证

`bootstrap.sh` 依赖 Docker Compose、OpenSSL 和 curl。修改基础设施、门户、首页或 Portal 后运行：

```bash
cd wiki
make validate
make smoke
make language-selector-check
make homepage-compare
make pages-build
make pages-deploy
make pages-smoke
```

修改模板或表单后还必须运行 `make import`，并在浏览器中验证创建、编辑、引用和历史页面。
