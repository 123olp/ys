---
id: GATE-0004
type: gate
status: active
owner: engineering
created: 2026-08-08
last_reviewed: 2026-08-08
review_cycle: P90D
severity: BLOCK
detectability: script+review
source: STD-REPOSITORY-CI-PRIVACY
---

# 仓库与 CI 不得泄露隐私

## 阻止条件

- 当前文件、历史 blob、提交消息或构建物命中本机身份或高置信凭据规则。
- author/committer 不符合项目规范身份。
- CI 使用可变 Action 引用、持久化 checkout 凭据、浅历史或高于只读的默认权限。
- 项目依赖安装发生在隐私预检之前。
- 工作流引用 secrets、使用 `pull_request_target`、开启 shell trace、打印环境变量或上传失败现场。
- CI 错误日志回显命中值、路径、提交消息、身份、邮箱或环境变量。
- 隐私扫描器负例、日志脱敏断言或可信输入建立失败。

## 原因

Git 历史和 CI 日志都是长期复制面。只扫描当前文件会漏掉已删除秘密；在错误消息中回显命中内容会让门禁本身成为二次泄漏源。

## 检查方式

- 本地：`make privacy-audit`。
- 完整历史：`python3 tools/audit_repository_privacy.py --scope all --revision HEAD --report-mode ci`。
- 远端：GitHub Actions 必须在项目依赖安装前运行同一完整历史预检。
- Review：核对工作流权限、固定 SHA、checkout 配置、执行顺序和失败日志。

## 可操作错误提示

隐私门禁阻止了变更。请在本地模式定位相对位置，移除或轮换真实秘密，并在必要时执行经批准的历史清理；禁止把命中值粘贴到 issue、PR、日志或聊天中。

## 最小修复

- 当前树命中：从跟踪文件移除并改用受控 secret store。
- 历史命中：先轮换凭据，再隔离备份、重写历史并处理 fork/PR/cache 残留。
- CI 配置命中：恢复只读、固定 SHA、完整历史、非持久化凭据和依赖安装前预检。
- 日志命中：切换 CI 脱敏模式，只保留规则、数量和 `location_id`。
