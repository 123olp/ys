---
id: STD-REPOSITORY-CI-PRIVACY
type: standard
status: current
owner: engineering
created: 2026-08-08
last_reviewed: 2026-08-08
review_cycle: P90D
---

# 仓库与 CI 隐私标准

## 目标

隐私门禁必须同时防止秘密或本机身份进入当前文件、Git 可达历史、提交元数据和 CI 日志。删除当前文件不能消除历史泄漏，门禁自身也不能通过错误输出再次泄漏命中值。

## 扫描面

- 当前 Git 跟踪文件与敏感文件名。
- CI 目标提交的完整可达提交、提交消息和历史 blob。
- author/committer 名称与邮箱，必须统一为项目规范身份。
- `.github/workflows/` 的权限、事件、Action 固定方式、checkout 深度和凭据持久化设置。
- 可部署项目还必须扫描构建物；构建物扫描由对应产品门禁负责。

## CI 信任边界

- 工作流权限默认只读；不得使用 `pull_request_target` 执行不受信代码。
- 第三方 Action 必须固定到 40 位提交 SHA，并保留版本注释。
- checkout 必须使用完整历史且 `persist-credentials: false`。
- 纯标准库隐私预检必须先于 Bundler、npm、pip 和项目依赖安装。
- 工作流不得引用 repository secrets、启用 shell trace、打印环境变量或上传失败现场。
- CI shell 必须 fail-fast、拒绝未定义变量并启用 `pipefail`。

## 日志契约

CI 失败只允许输出：规则 ID、发现总数和由规则、路径、行号、修订组合生成的不可逆 `location_id`。禁止输出命中值、相对路径、提交消息、作者身份、邮箱、环境变量和异常原文。本地模式可以输出相对位置，但仍不得输出命中值。

## 性能边界

历史扫描时间复杂度必须为 O(唯一可达对象总字节数)，使用 `git cat-file --batch` 流式读取，不得为每个 blob 启动子进程或一次性保留全部对象正文。扫描器必须限制错误输出数量，避免日志放大。

## 例外

禁止用宽泛路径 allowlist、关闭规则或跳过历史扫描处理假阳性。例外必须精确绑定非秘密对象，经过独立复核，并记录失效条件。真实秘密一旦进入历史，必须立即吊销或轮换，再执行历史清理；重写历史不能替代凭据轮换。
