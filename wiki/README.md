# Human Infra Wiki

Human Infra Wiki 是科技树节点的知识详情层，也是项目专有概念、研究域和证据来源的可修订知识库。语言入口直接复用 Wikimedia 官方 `www.wikipedia.org` 门户发布物；中文站使用 MediaWiki 1.46、MariaDB 11.8、Vector、VisualEditor 和 Page Forms，保持 Wikipedia 同系阅读与编辑体验。

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

## 信息架构

```text
多语言门户
  -> 中文语言版本
  -> Human Infra:首页
  -> Portal:专题
  -> 研究域 / 技术节点 / 证据来源
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

中文首页由固定的中文维基百科首页 Wikitext、页首、TemplateStyles 和渲染 HTML 快照生成；`Template:首页/*` 仅维护 Human Infra 内容。生成产物禁止手工修改，上游固定修订、哈希与许可记录在 `homepage-upstream/UPSTREAM.md`。顶级专题使用 `Portal:` 命名空间，Portal 只组织导航、边界和跨词条关系，不复制词条正文。

## 常用命令

```bash
make up          # 启动
make stop        # 停止
make logs        # 查看日志
make import      # 重新导入受治理的种子页面
make smoke       # 验证 HTTP、数据库、扩展和关键页面
make backup      # 创建时间戳备份包
make validate    # 检查源码契约和 Compose 配置
make homepage-check   # 校验官方首页快照和生成产物未漂移
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
