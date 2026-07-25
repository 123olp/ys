# Human Infra Wiki 架构说明

`wiki/` 是项目内部知识词条与科技树详情页系统。它复用 MediaWiki，不自研百科引擎；仓库保存可复现定义，运行时状态保持隔离。

## 目录结构

```text
wiki/
├── AGENTS.md                 # 本目录职责与维护边界
├── README.md                 # 部署、使用、备份和恢复入口
├── CONTENT-STANDARD.md       # 词条内容、引用和命名规范
├── ROUTING-CONTRACT.md       # 科技树节点到内外 Wiki 的跳转契约
├── Dockerfile                # MediaWiki 与固定版本 Page Forms 镜像
├── Makefile                  # 常用运维命令入口
├── compose.yaml              # MediaWiki 与 MariaDB 服务编排
├── env.example               # 非敏感环境变量样例
├── config/
│   └── HumanInfraSettings.php # 站点权限、皮肤、扩展和版权配置
├── docker/
│   └── entrypoint.sh         # 运行时目录和 LocalSettings 装载
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
- `config/` 只保存可公开的站点策略；MediaWiki 生成的 `LocalSettings.php` 属于运行时。
- `content/` 是首次安装和可重复导入的种子，不是整个 Wiki 数据库的镜像。
- `runtime/` 和 `.env` 不得提交；数据迁移必须使用备份包。
- 科技树只保存稳定节点 ID、标题和目标路由；词条正文、引用和修订历史归 Wiki。
- 外部通用概念优先链接公共 Wikipedia；项目专有概念、模型和研究域进入本地 Wiki。

## 依赖与验证

`bootstrap.sh` 依赖 Docker Compose、OpenSSL 和 curl。修改基础设施后运行：

```bash
cd wiki
make validate
make smoke
```

修改模板或表单后还必须运行 `make import`，并在浏览器中验证创建、编辑、引用和历史页面。
