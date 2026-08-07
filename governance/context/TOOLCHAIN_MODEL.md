---
id: GOV-TOOLCHAIN-MODEL
type: context
status: current
owner: engineering
created: 2026-08-06
last_reviewed: 2026-08-06
review_cycle: P90D
---

# Toolchain Model

本文件记录项目工具链的当前真相，帮助人类和代理优先复用成熟能力、项目既有脚本和稳定验证入口。

## 成熟工具优先

- 优先使用语言标准工具、官方 CLI、包管理器、测试框架、lint/typecheck、数据库迁移工具和云平台能力。
- 自研脚本只用于连接、编排、适配和表达项目特有流程。
- 新增工具前必须证明：已有工具无法满足、引入后总拥有成本更低、验证和回滚路径明确。

## 项目命令

| 场景 | 命令 | 备注 |
|---|---|---|
| 安装依赖 | 按各工具 `README.md` 安装 | 仓库没有统一全局依赖锁文件 |
| 测试 | `make check` | 全量结构、契约与审计门禁 |
| 历史年表门禁 | `make history-timeline-gate` | 年表机器契约 |
| 年表发布原型 | `make history-timeline-preview` | 从三份真相源生成 TimelineJS 数据与原型 |
| 类型检查 | 按具体模块 README 执行 | 无统一类型系统 |
| lint / format | `git diff --check` | 文档和代码空白规范 |
| JSON 校验 | `python3 -m json.tool <file>` | 机器契约语法检查 |
| 构建 | 按 `web/`、`wiki/` 各自 README | 年表本身无需构建 |
| 本地运行 | 静态文件可用本地 HTTP 服务预览 | 不替代生产发布 |
| 发布 | 按 `.github/` 和 Cloudflare 平台配置 | 年表只进 CI，不直接发布 |
| 回滚 | `git revert` / `git checkout <commit> -- <path>` | 只回滚明确授权的变更 |

## 禁止或谨慎使用

- 禁止绕过项目已有脚本直接调用内部实现细节，除非在调试任务中明确说明。
- 禁止新增无 owner、无验证、无回滚说明的脚本。
- 禁止把一次性命令伪装成长期工具链。

## 工具链变更流程

1. 先检查现有命令、脚本、CI 和文档。
2. 记录新增或替换工具的存在性理由。
3. 更新本文件和相关流程文档。
4. 运行最小验证。
5. 在任务 closeout 中记录验证证据和回滚方式。
