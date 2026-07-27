# MediaWiki CLI 内容导入后的 Web 缓存一致性

## Bug

通过 `maintenance/run.php edit` 导入的新模板和 `MediaWiki:Sidebar` 已写入数据库，
但本地 Vector 页面仍显示导入前内容。直接访问模板页可看到新修订，首页转录结果和
全站侧栏却保持旧状态。

## Environment

- MediaWiki 1.46
- Vector 2022
- CLI 内容导入：`wiki/scripts/import-content.sh`
- Web 入口：`http://127.0.0.1:18782`
- 主缓存：`CACHE_ACCEL`

## Reproduction

1. 通过 CLI 导入更新后的首页模板和 `MediaWiki:Sidebar`。
2. 运行原流程中的 `runJobs --maxjobs=100` 与 `purgePage`。
3. 请求首页并检查交易猫实验室资助声明与实验室链接。

RED 结果：首页断言为 `funding=False, lab=False`，而关于页直接正文为
`funding=True, lab=True`。

## Hypotheses

### H1: 受治理源文件或数据库修订未更新

- Conflicts：模板页与 `MediaWiki:Sidebar` 均存在新修订，直接请求模板可见新内容。
- Status：rejected。

### H2: 首页未记录模板反向依赖

- Conflicts：`prop=transcludedin` 与 `templatelinks` 均显示首页依赖参与建设和关联项目模板。
- Status：rejected。

### H3: CLI 导入与 Web 进程的加速缓存相互隔离

- Supports：`$wgMainCacheType=3`，CLI parser/message cache 操作后 Web 页面仍旧；
  重启 Wiki Web 进程后同一断言立即转绿。
- Status：confirmed（ROOT HYPOTHESIS）。

## Experiments

### E1: 清空作业队列

- Result：剩余 240 个 `refreshLinks` 作业归零，首页仍旧。
- Verdict：不足以修复。

### E2: `purgeList --db-touch` 与 API recursive purge

- Result：首页 `page_touched` 更新，页面仍旧。
- Verdict：排除单纯 CDN/page touched 问题。

### E3: 原生 parser/message cache 清理后重启 Web 进程

- Result：首页变为 `funding=True, lab=True`；关于页保持
  `funding=True, lab=True`。
- Verdict：confirmed。

## Root Cause

CLI 导入进程完成数据库写入后，原流程只处理有限数量作业并调用页面 purge；
Web 进程持有的 `CACHE_ACCEL` 模板和系统消息缓存没有被可靠替换，导致数据库修订与
Vector 实际输出不一致。

## Fix

导入流程改为清空作业队列、运行 MediaWiki 原生 `rebuildmessages`、清理 SQL parser
cache、重启 Wiki Web 服务并等待 API 就绪。现有 smoke 增加首页和关于页的资助声明、
GitHub 仓库及交易猫实验室精确链接断言。

## Repair Boundary

- `wiki/scripts/import-content.sh`
- `wiki/scripts/smoke-test.sh`
- 受治理 Wiki 内容与本调试记录

## Frozen Nodes

- MediaWiki、Vector 和 ResourceLoader 源码
- 首页上游布局与 CSS
- 其他研究词条和用户并行改动

## Audit Case Sampling

- Decision：`no-case`
- Reason：根因已进入导入流程和 smoke Gate；仓库当前没有 `governance/` 案例库，
  不另建重复真相源。

## Reverification Required

- [x] 导入后旧首页 RED
- [x] 清空作业与 page purge 仍 RED
- [x] 原生缓存清理与 Web 重启后 GREEN
- [x] 固定流程完整 smoke
- [x] Pages 静态快照重建与审计
