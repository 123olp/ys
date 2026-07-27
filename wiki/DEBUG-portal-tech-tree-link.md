# Human Infra 语言门户缺少科技树入口

## Bug

- 标题：语言门户声明连接 Wiki 与科技树，但页面没有科技树链接
- 症状：桌面和移动端均只能进入 Wiki 词条，无法从组织门户进入科技树
- 首次复现：`https://human-infra.pages.dev/`，2026-07-27

## Environment

- 模块：Wikimedia portals 上游快照适配层
- 页面：`portal/index.html`
- 生成器：`scripts/refresh-wikipedia-portal.py`

## Reproduction

```bash
python3 - <<'PY'
from pathlib import Path
page = Path("portal/index.html").read_text(encoding="utf-8")
assert 'href="https://human-infra-tech-tree.pages.dev/"' in page
PY
```

修复前断言失败；浏览器矩阵也确认所有 `a[href]` 中不存在科技树地址。

## Observations

- O1：门户元数据和发布契约同时声明 Wiki 与科技树为公开产品。
- O2：上游 `other-projects` 卡片结构已经存在，不需要增加布局或样式。
- O3：生成器的 `WIKI_ENTRIES` 只支持 Wiki 标题，经 `adapter.js` 统一改写为 Wiki URL。
- O4：科技树是独立 Pages 项目，必须保留直接外部 URL，不能伪装成 Wiki 词条。

## Hypotheses

### H1：门户生成模型只表达内部 Wiki 目标（ROOT HYPOTHESIS）

- Supports：所有项目卡都使用 `data-hi-title`，没有外部产品入口类型。
- Conflicts：无。
- Test：用原生 `other-project` 卡片直接链接科技树，再检查生成源和页面。

## Experiment

- Hypothesis：H1
- Change：在 Wiki 首页卡后插入一张原生 `other-project` 科技树卡。
- Expected：门户新增可点击科技树入口，视觉仍完全由 Wikimedia 上游 CSS 所有。
- Result：源码门禁、桌面/移动端链接检查通过。
- Verdict：confirmed
- Revert：删除生成器和快照中的科技树卡片即可回滚。

## Root Cause

门户复用了 Wikimedia 的项目导航视觉结构，但适配器把所有入口都建模成内部
Wiki 页面，导致独立部署的科技树产品没有可表达的导航目标。

## Fix

- 保留 Wikimedia `other-projects`、`other-project` 与现有图标结构。
- 使用固定公开地址 `https://human-infra-tech-tree.pages.dev/`。
- 不新增 CSS、JavaScript 路由或自定义组件。
- `validate-source.sh` 对直接科技树链接执行 fail-closed 检查。

## Regression Evidence

- RED：`runtime/regression/portal-tech-tree-link-red.json`。
- GREEN：`runtime/regression/portal-tech-tree-link-green.json`。
- 反事实：`runtime/regression/portal-tech-tree-link-counterfactual.json`。
- 契约：`REGRESSION_EVIDENCE-portal-tech-tree-link.json`。
