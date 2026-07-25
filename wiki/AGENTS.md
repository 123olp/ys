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
├── Dockerfile                # MediaWiki 与固定版本 Page Forms 镜像
├── Makefile                  # 常用运维命令入口
├── compose.yaml              # MediaWiki 与 MariaDB 服务编排
├── env.example               # 非敏感环境变量样例
├── config/
│   └── HumanInfraSettings.php # 站点权限、皮肤、扩展和版权配置
├── docker/
│   └── entrypoint.sh         # 运行时目录和 LocalSettings 装载
├── portal/                   # 独立多语言入口，不承载研究正文
│   ├── index.html            # 语言选择与搜索入口
│   ├── languages.json        # 语言状态与展示顺序真相源
│   ├── app.js                # API 统计与语言路由
│   ├── styles.css            # Wikipedia 中性配色与响应式布局
│   ├── default.conf.template # Nginx 健康检查和运行时端口注入
│   └── assets/               # Human Infra 门户品牌资产
├── content/
│   ├── manifest.tsv          # 种子页面标题与文件映射真相源
│   └── *.wiki                # 首页、政策、模板、表单和分类种子
├── scripts/
│   ├── bootstrap.sh          # 幂等安装、升级、导入和启动
│   ├── import-content.sh     # 按 manifest 幂等更新种子页面
│   ├── backup.sh             # 数据库、上传文件和配置备份
│   ├── restore.sh            # 显式确认后的完整恢复
│   ├── smoke-test.sh         # HTTP、扩展、页面和数据库验证
│   └── validate-source.sh    # 跟踪配置与内容契约检查
└── runtime/                  # 忽略：数据库、上传、安装配置和备份
```

## 职责边界

- `compose.yaml` 和 `Dockerfile` 固定可复现基础设施；不得把密码写入其中。
- `portal/` 是语言选择层，只负责版本发现、搜索路由和语言状态；禁止存放研究结论或伪造尚未建立的语言版本。
- `config/` 只保存可公开的站点策略；MediaWiki 生成的 `LocalSettings.php` 属于运行时。
- `content/` 是首次安装和可重复导入的种子，不是整个 Wiki 数据库的镜像。
- `Human Infra:首页` 是中文项目首页；`Template:首页/*` 是其模块；`Portal:` 只做专题导航，不成为并行正文真相源。
- `runtime/` 和 `.env` 不得提交；数据迁移必须使用备份包。
- 科技树只保存稳定节点 ID、标题和目标路由；词条正文、引用和修订历史归 Wiki。
- 外部通用概念优先链接公共 Wikipedia；项目专有概念、模型和研究域进入本地 Wiki。

## 依赖与验证

`bootstrap.sh` 依赖 Docker Compose、OpenSSL 和 curl。修改基础设施、门户、首页或 Portal 后运行：

```bash
cd wiki
make validate
make smoke
```

修改模板或表单后还必须运行 `make import`，并在浏览器中验证创建、编辑、引用和历史页面。
