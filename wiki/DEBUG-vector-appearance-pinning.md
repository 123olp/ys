# Vector 外观面板缺少原生固定状态机

## Bug

- 标题：Pages 静态 Wiki 的 Vector 外观面板无法隐藏、恢复或响应断点
- 症状：桌面右栏长期占位，但“隐藏”按钮不可见；顶部“外观”入口无法接管面板；正文宽度不会随固定状态变化。
- 首次发现位置 / 时间：`https://human-infra-wiki.pages.dev/`，2026-07-27

## Environment

- 仓库 / 模块：`wiki/scripts/vector-client-preferences-static.js`
- 运行环境：Cloudflare Pages 纯静态快照
- 依赖 / 版本：MediaWiki 1.46、Vector 2022、BackstopJS 6.3.25 内置 Playwright
- 配置差异：本地 MediaWiki 执行 Vector ResourceLoader；Pages 删除 ResourceLoader，只运行静态偏好适配器。

## Reproduction

1. 构建或打开当前 Pages Wiki 静态快照。
2. 使用 2048px 宽桌面视口检查 `#vector-appearance`。
3. 尝试隐藏右侧外观面板、从顶部入口恢复，并跨 1120px 断点调整视口。

## Observations

- O1：发布物包含原生 pinned/unpinned 容器、pinnable header 和 8 个偏好单选项。
- O2：静态适配器只处理字号、宽度和颜色的 document classes。
- O3：页面始终保持 `client-nojs`，Vector 的固定/隐藏按钮显示规则不会启用。
- O4：本地 MediaWiki 在 2048px 下把面板放在 pinned container；在 1119px 下自动移入 unpinned container。
- O5：现有回归只验证 8 个控件、类切换和偏好持久化，没有验证固定状态机。

## Hypotheses

### H1: 首页右栏 57% / 43% 布局挤压了 Vector 外观面板

- Supports：问题在首页右侧最明显。
- Conflicts：官方与本地首页内容栏几何一致，外观面板属于独立的 `.vector-column-end`。
- Test：分别测量首页内容栏与 Vector end column。
- Status：rejected。

### H2: Vector 外观组件 HTML 不完整

- Supports：交互不可用。
- Conflicts：发布物已经包含两个容器、header、pin/unpin 按钮和全部 data attributes。
- Test：静态解析发布物并检查组件契约。
- Status：rejected。

### H3: 静态适配器没有实现 Vector pinnable element 状态机（ROOT HYPOTHESIS）

- Supports：适配器没有处理 pin/unpin、DOM 移动、断点、ARIA 或固定状态持久化。
- Conflicts：无。
- Test：对当前发布物执行完整浏览器行为契约。
- Status：confirmed。

### H4: 线上同源回归超时来自浏览器容器未继承宿主代理

- Supports：宿主启用了标准代理变量，Docker 容器默认不继承。
- Conflicts：若 Pages 本身不可达，宿主请求也会失败。
- Test：分别从宿主与浏览器容器访问同一 Pages URL，再显式传递标准代理变量重放。
- Status：confirmed。

### H5: Pages smoke 误报来自输入 URL 尾斜杠未正规化

- Supports：脚本会在入口变量后继续拼接 `/` 和资源路径。
- Conflicts：使用默认无尾斜杠地址时全站 smoke 应通过。
- Test：分别传入有尾斜杠和无尾斜杠的同一生产地址。
- Status：confirmed。

## Experiments

### E1: 当前静态发布物行为基线

- Hypothesis：H3。
- Change：新增只读 Playwright 行为测试，不修改生产代码。
- Expected：当前版本在“隐藏按钮可见”断言处失败。
- Result：失败率 100%，失败指纹指向 `“隐藏”按钮不可见: display=none`；测试前后被测文件 digest 一致。
- Verdict：confirmed
- Revert：测试文件不改变发布行为。

### E2: 首次 GREEN 的刷新持久化失败

- Hypothesis：H3 修复仍未持久化，或测试在 reload 时污染存储。
- Change：检查测试初始化脚本的执行时机。
- Expected：若初始化脚本在每次导航执行，则它会在 reload 前清除刚保存的固定状态。
- Result：Playwright `addInitScript` 会在每个新文档执行；测试确实在 reload 时删除了目标 localStorage。
- Verdict：confirmed
- Classification：测试缺陷，不能计入产品失败。
- Revert：删除多余的存储清理；每次测试使用全新 BrowserContext 提供天然空存储。

### E3: 线上同源回归首次超时

- Hypothesis：H4。
- Change：分别用宿主 `curl` 和容器 Playwright 访问同一 Pages URL。
- Expected：若只是容器代理缺失，宿主请求成功，容器导航超时；显式传递标准代理变量后可获得产品行为结论。
- Result：宿主返回 HTTP 200；容器首次导航超时；传递代理变量后测试立即在旧版“隐藏”按钮不可见处得到预期 RED。
- Verdict：confirmed
- Classification：测试运行环境缺陷，不计入产品失败。
- Revert：无；门禁仅显式继承已有标准代理变量，不引入站点代理配置。

### E4: 线上全站 smoke 首次误报

- Hypothesis：H5。
- Change：先用带尾斜杠 URL 运行，再用脚本默认 URL 重放。
- Expected：若 H5 成立，前者失败，后者通过；正规化输入后两者都应通过。
- Result：带尾斜杠运行失败，默认 URL 完整通过；输入正规化后带尾斜杠运行也通过。
- Verdict：confirmed
- Classification：测试入口缺陷，不计入产品失败。
- Revert：删除三行尾斜杠正规化即可恢复旧行为。

## Root Cause

- Pages 静态导出保留了 Vector pinnable DOM，却只适配了三个偏好组；`client-nojs` 使 pinnable 按钮和顶部外观入口保持隐藏，且没有代码维护容器移动、断点、ARIA 与固定状态持久化。

## Fix

- 在现有静态适配器内补齐 Vector appearance-pinned 状态机；复用原生容器、类名、按钮和 1120px 断点，并扩展静态结构审计与浏览器回归。

## Regression Evidence

- 回归证据契约：Required
- 契约文件：`REGRESSION_EVIDENCE-vector-appearance-pinning.json`
- 测试：`make vector-appearance-check`
- 结果：RED 失败、GREEN 通过、反事实重放再次失败。
- 备注：测试摘要在三阶段保持一致；旧适配器摘要在 RED 与反事实阶段一致。

## Failed Nodes

- Vector 静态外观交互

## First Invalid Node

- `wiki/scripts/vector-client-preferences-static.js`

## Upstream Lineage

- Vector 服务端 DOM -> ResourceLoader pinnable runtime -> Pages 静态导出 -> 静态偏好适配器

## Downstream Blast Radius

- 外观侧栏隐藏、顶部恢复、正文扩宽、断点响应、固定偏好持久化和键盘可访问性

## Lowest Common Refinement Ancestor

- Vector 外观组件固定状态

## Repair Boundary

- 静态偏好适配器、最小原生状态 CSS、浏览器行为门禁

## Frozen Nodes

- 首页 Wikitext、TemplateStyles、Vector 原生 DOM、8 个偏好控件、MediaWiki 源站

## Invalidated Nodes

- 旧的“8 个控件存在即完整”验收结论

## Reverification Required

- Pages 构建、静态运行时审计、桌面 pin/unpin、刷新持久化、1120px 断点、无横向溢出
