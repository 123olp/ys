# Wiki 静态快照伪交互能力专项排查

## Bug

- 标题：静态导出删除 MediaWiki 运行时后仍暴露不可用操作入口
- 症状：公开 Wiki 中登录、讨论、查看源代码、历史、页面工具、变体和编辑段落等入口仍可见，但点击后无有效目标；`sortable` 表格失去排序能力。
- 首次发现位置 / 时间：`https://human-infra-wiki.pages.dev/`，2026-07-27。

## Environment

- 仓库 / 模块：`wiki/scripts/export-pages-snapshot.py`
- 运行环境：MediaWiki 1.46 + Vector 2022 -> Cloudflare Pages 纯静态快照
- 依赖 / 版本：Python、BeautifulSoup、lxml
- 配置差异：本地 MediaWiki 有 ResourceLoader 和后端操作路由，公开 Pages 无函数、无 MediaWiki 运行时。

## Reproduction

1. 构建或读取 `wiki/runtime/pages/wiki/`。
2. 运行 `python3 wiki/scripts/audit-static-runtime-contract.py --output wiki/runtime/pages/wiki`。
3. 观察不可用操作 ID、`href="#"` 和无运行时动态类。

## Observations

- O1：导出器无条件删除所有 `<script>`，公开快照只保留两个明确的静态适配能力：搜索和 Vector 外观偏好。
- O2：`static_href_from_mediawiki()` 将特殊页和带 `action` 的链接改写为 `#`，但没有移除其交互外观。
- O3：首页包含登录、讨论、源代码、历史、特殊页面和页面工具等 10 组不可用入口；普通词条还包含多个“编辑源代码”入口。
- O4：`历史技术谱系` 保留 `sortable` 类，但 `mediawiki.page.ready` 已被删除，表格无法排序。
- O5：主菜单、语言选择、页内目录和外观偏好具有静态 CSS 或明确适配器，属于应保留能力。
- O6：原静态补丁无条件显示右侧外观面板，导致小于 Vector `1120px` 网格断点时面板进入普通文档流并占据正文首屏；原生 Vector 移动端会隐藏该钉住面板。

## Hypotheses

### H1: （ROOT HYPOTHESIS）导出器没有建立运行时能力白名单

- Supports：导出器按少量固定选择器删除操作控件，其他同类入口继续泄漏；特殊页统一改写为 `#`。
- Conflicts：无。
- Test：新增静态运行时契约审计器，对当前发布物执行全量 HTML 检查。

### H2: 失效入口来自首页模板正文

- Supports：首页正文存在若干操作性链接。
- Conflicts：登录、讨论、页面工具和变体均来自 Vector 外壳；普通词条也复现。
- Test：比较首页与普通词条中的节点祖先和稳定 ID。

### H3: 只需补回完整 ResourceLoader

- Supports：本地 MediaWiki 中这些控件可用。
- Conflicts：公开架构契约明确要求纯静态、只读、无 Pages Functions；登录、编辑、历史等能力需要后端，不能由前端脚本恢复。
- Test：按能力依赖分类，确认仅搜索、语言选择、目录和外观偏好可在静态端真实保留。

## Experiments

### E1

- Hypothesis：H1。
- Change：只新增审计器，不修改导出行为。
- Expected：当前发布物稳定失败，并列出不可用操作入口、空目标链接和 `sortable`。
- Result：审计器对修复前发布物返回 exit 1，报告 `issues=123046 pages=2735`；问题覆盖所有页面外壳，并包含无目标链接、不可用操作 ID 与 `sortable`。
- Verdict：confirmed。
- Revert：删除审计器即可恢复实验前状态。

### E2

- Hypothesis：H1 的同类表现还包括“静态适配未保持原生响应式条件”。
- Change：对比本地原生 Vector 与静态快照的 390px / 1440px 浏览器几何。
- Expected：原生移动端隐藏右侧外观面板，静态移动端不应将其放入正文前。
- Result：原生移动端 `#vector-appearance visible=false`、正文 `top=84`；修复前静态移动端面板可见且占据首屏。
- Verdict：confirmed。
- Revert：不适用，实验只读取浏览器状态。

### E3

- Hypothesis：H1 还会出现在非主入口和别名页的表单 action 上。
- Change：扩展审计器，拒绝除 `/search/` 以外的显式表单 action，暂不修改导出器。
- Expected：审计器应发现依赖 MediaWiki Page Forms 后端、但未出现在主入口截图中的表单。
- Result：审计器返回 exit 1，在 `wiki/Main_Page/index.html` 中定位 3 个 `/index.php/Special:表格起始` action。
- Verdict：confirmed；导出器必须按能力白名单移除这些表单，不能只巡检公开首页。
- Revert：删除 action 检查可恢复实验前状态。

### E4

- Hypothesis：H1 还包括“链接样式正常、但静态目标文件不存在”的深层死路由。
- Change：让审计器解析全部内部 `/wiki/` 链接并验证对应 `index.html` 是否存在，暂不修复链接。
- Expected：固定页脚、特殊生成页和历史别名中的遗漏应被确定性列出。
- Result：审计器返回 exit 1，定位 5 个缺失路由；其中隐私政策和免责声明分别被 2733 个页面引用，另有搜索页、404 页和“首页”旧标题各 1 个来源页面。
- Verdict：confirmed；公开快照必须补齐真实固定页面，并把特殊生成页和首页别名绑定到现有静态路由。
- Revert：删除内部路由检查可恢复实验前状态。

## Root Cause

- 静态导出器删除了 MediaWiki/Vector 客户端运行时和后端操作能力，却使用不完整的控件黑名单维护外壳；未被列入黑名单的原生操作继续进入每个静态页面，特殊页和 action 链接又被统一改写为 `href="#"`，最终形成大规模伪交互能力。

## Fix

- 将公开发布边界改为静态能力白名单：移除依赖后端或 ResourceLoader 的操作容器和编辑入口；将无目标正文链接降级为文本；展开折叠内容；将 `sortable` 表格降级为普通表格；保留搜索、语言选择、页内目录、打印和 Vector 外观偏好。外观面板仅在 Vector 原生 `1120px` 桌面网格断点以上显示，移动端保持隐藏。

## Regression Evidence

- 回归证据契约：Required
- 测试：`wiki/scripts/audit-static-runtime-contract.py`
- RED：仅加入审计器、尚未修复导出器时，审计返回 exit 1，`issues=123046 pages=2735`。
- 响应式 RED：修复伪控件但尚未恢复原生断点时，审计返回 exit 1，唯一问题为“Vector 外观面板未限定在原生 1120px 桌面断点”。
- 隐藏路径 RED：加入表单 action 审计后，中间发布物返回 exit 1，在别名页发现 3 个依赖后端的 Page Forms 表单。
- 内部路由 RED：加入目标文件存在性审计后，中间发布物返回 exit 1，发现 5 个缺失静态路由，其中两个固定页脚入口影响 2733 个页面。
- GREEN：`make pages-build` 完成 2732 个词条页面与 2737 个发布 HTML 检查，结果为 `dead_links=0 internal_routes=0 form_actions=0 dynamic_markers=0 operational_controls=0`。
- Source GREEN：`make validate` 通过 Wikipedia 首页快照、生成契约和 Wiki source contract。
- Browser GREEN：Chrome 1440×1000 与 390×844 分别检查首页、普通词条和历史技术谱系；8 个外观选项均存在，桌面可见、移动端隐藏，禁止控件、死链接、动态类和横向溢出均为 0；普通词条目录存在。
- Counterfactual sensitivity：同一审计器能够同时拒绝修复前的大规模伪控件发布物和缺少响应式断点的中间版本，不是只对最终输出硬编码 PASS。
- 备注：审计器是发布边界的机器 Gate，浏览器矩阵用于验证 CSS 可见性和响应式行为。

## Repair Boundary

- `wiki/scripts/export-pages-snapshot.py`
- `wiki/scripts/audit-static-runtime-contract.py`
- Wiki Pages 构建、校验与线上 smoke 门禁

## Frozen Nodes

- MediaWiki、Vector、Wikimedia 首页模板和官方样式
- 搜索、语言选择、目录与外观偏好现有静态能力
- Wiki 正文研究内容与用户并行改动

## Reverification Required

- [x] 当前发布物 RED
- [x] 修复后全量 Pages 构建 GREEN
- [x] 修复前发布物 counterfactual RED
- [x] 本地静态发布物桌面端与移动端 DOM、可见性和截图检查
- [ ] 公开 pages.dev DOM、内部固定页与浏览器可见性检查
