---
id: GOV-PROJECT-OPERATING-MODEL
type: context
status: current
owner: engineering
created: 2026-08-06
last_reviewed: 2026-08-06
review_cycle: P90D
---

# Project Operating Model

本文件是项目级人类入口和代理入口的共享操作模型。它只记录项目当前应该如何被理解、修改、验证和交付；不替代代码、契约、ADR、任务包、README 或 AGENTS。

## 项目一句话定义

Human Infra 以“主体持续性和有效永生”为目标，把身体、认知、时间、资源、技术、社会支持与风险治理组织为可研究、可建模、可验证的人类基础设施。

## 业务模型

- 核心用户：主体自身、研究共同体、未来自我与家庭支持系统。
- 核心对象：主体的持续存在、行动、学习、修复、选择和进入未来能力。
- 关键流程：先防死亡和失能，再维护身体与认知，然后提升学习与技术采用能力，最后治理远期路径与风险。
- 不属于本项目的范围：不做医疗、法律、投资或政策建议，不承诺永生，不把远期预测当已验证事实。

## 技术模型

- 主要运行形态：文档知识库 + 结构化研究域 + 静态/交互发布 + CI 门禁。
- 核心模块：`docs/`、`domains/`、`governance/`、`tools/`、`web/`。
- 数据事实源：根 `README.md`、`docs/reference/`、`governance/`、`domains/` 和机器可读 JSON/YAML 契约。
- 外部依赖：GitHub Actions、Cloudflare Pages/Wrangler、公开学术数据库与工具官网。
- 主要验证入口：`make check`、`make public-product-boundary`、`python3 tools/check_repository.py`。

## 工具链模型

工具链边界以 `context/TOOLCHAIN_MODEL.md` 为准。这里仅记录最短摘要：

- 构建：
- 测试：
- 类型检查：
- 格式 / lint：
- 发布 / 回滚：

最短摘要：

- 构建：静态站点和展示物按各自 `README.md` 构建；年表本身不需要构建。
- 测试：`make check`、`make public-product-boundary`。
- 类型检查：按具体模块 README 执行；年表门禁以 JSON Schema 校验替代。
- 格式 / lint：`git diff --check`、JSON `python3 -m json.tool`。
- 发布 / 回滚：发布入口由 `.github/` 或平台配置管理；代码回滚使用 Git 版本控制。

## 目录和真相源地图

| 事实类型 | 真相源 | 备注 |
|---|---|---|
| 项目操作模型 | `governance/context/PROJECT_OPERATING_MODEL.md` | 人类和代理的项目入口 |
| 上下文路由 | `governance/context/CONTEXT-ROUTER.md` | 任务类型到最小上下文包 |
| 工程流程 | `governance/processes/DOCUMENT_DRIVEN_DEVELOPMENT.md` | 文档先行和文档回填规则 |
| 工具链边界 | `governance/context/TOOLCHAIN_MODEL.md` | 成熟工具、项目脚本和禁用做法 |
| 机器契约 | `governance/context/project_operating_model_contract.v1.yaml` | 脚本和 agent 可读取的契约 |
| 产品源码边界 | `tools/audit_public_product_boundary.py` | 阻止 Wiki、科技树和永生年表源码回流公开仓库 |
| 架构决策 | `governance/decisions/adr/` | 不可逆或高影响决策 |
| 任务证据 | `governance/tasks/` | 执行计划、状态、验收、closeout |

## 变更入口

非平凡工程变更开始前必须判断：

- 是否需要先更新本操作模型。
- 是否需要更新文档驱动开发流程。
- 是否需要更新工具链模型。
- 是否需要新增或更新 ADR、Gate、module context、contracts、catalog、README 或 AGENTS。

## 验证入口

```bash
python3 governance/tools/governance_context_bundle.py --project-root . --task-type docs
python3 governance/tools/validate_governance_package.py --project-root . --strict
python3 governance/tools/governance_health_report.py --project-root . --strict
```

## 最近一次 review

- 日期：2026-08-06
- 结论：PASS
- 后续动作：持续补充年表事件数据和来源卡。
