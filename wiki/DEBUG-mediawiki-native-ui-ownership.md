# MediaWiki 原生 UI 所有权恢复

## Bug

Cloudflare Pages 静态快照使用项目自写 JavaScript 模拟 Vector 2022 的外观偏好与
pinnable 状态机。虽然控件 DOM 和 CSS 类来自上游，但运行时所有权已经偏离
MediaWiki/Vector 原生实现。

## Environment

- MediaWiki 1.46
- Vector 2022
- 本地动态源站：`http://127.0.0.1:18782`
- Cloudflare Pages：纯静态、无 PHP、无 MediaWiki ResourceLoader
- 回滚基线：`b3c769916252af6248067061c64b259daea86a83`

## Reproduction

```bash
python3 wiki/scripts/check-mediawiki-native-ui.py
```

修复前必须因 `vector-client-preferences-static.js`、冻结控件 DOM 和导出器注入逻辑
存在而失败。

## Observations

1. MediaWiki 原始响应只输出空的 `#vector-appearance` 容器和 pinnable data
   contract，不输出外观单选控件。
2. 原生 `skins.vector.js` 调用 `pinnableElement.init()`，并通过
   `mw.loader.using(['skins.vector.clientPreferences', ...])` 生成控件。
3. 原生模块依赖 `mw.loader`、`mw.user.clientPrefs`、MediaWiki 消息系统、
   `mw.Api` 和 ResourceLoader 模块图。
4. Cloudflare Pages 纯静态发布物没有 PHP、`load.php`、MediaWiki API 或
   ResourceLoader 请求时模块解析能力。
5. 当前项目通过 `vector-client-preferences-static.js` 重新实现上述部分状态机，
   违反“MediaWiki 原生 UI 行为不得由项目重写”的新约束。

## Hypotheses

### H1: 直接把 `skins.vector.clientPreferences` 单文件复制到 Pages 即可

- Supports：模块代码来自 Vector 上游。
- Conflicts：模块通过 `mw.loader.impl` 注册，依赖 `mw.user.clientPrefs`、
  `mw.Api`、消息和其他 ResourceLoader 模块，不能独立执行。
- Test：读取本地 `/load.php?modules=skins.vector.clientPreferences` 输出和依赖。
- Status：rejected。

### H2: 保留当前适配器，只声明 DOM 和 CSS 来自 Vector 即可满足原生约束

- Supports：当前视觉和状态类与 Vector 接近。
- Conflicts：事件绑定、存储、断点迁移和 DOM 移动由项目代码拥有。
- Test：检查静态发布物脚本来源和事件所有者。
- Status：rejected。

### H3: 动态站使用完整 MediaWiki；静态快照只保留原生无脚本阅读能力

- Supports：动态站可完整运行 ResourceLoader；静态站不会伪造缺失的原生能力。
- Conflicts：静态公开站不再提供外观偏好交互。
- Test：动态站验证原生模块与 8 个控件；静态站验证无自写适配器、无伪控件。
- Status：confirmed（ROOT HYPOTHESIS）。

## Experiments

### E1: 原始响应、原生模块和浏览器增强三态核对

- Hypothesis：H3。
- Input：本地 MediaWiki 原始 HTML、`skins.vector.js`、
  `skins.vector.clientPreferences` 和浏览器增强 DOM。
- Expected：原始 HTML 为 0 个控件，浏览器执行原生模块后为 8 个控件。
- Result：原始 HTML 为 0；原生模块明确调用 client preferences render；
  浏览器增强状态已有 8 控件证据。
- Verdict：confirmed。

## Root Cause

纯静态 Pages 缺少 MediaWiki ResourceLoader 运行时，项目此前用自写适配器填补了
能力缺口，导致 Vector 交互所有权从上游框架漂移到项目代码。

## Fix

删除自写适配器和冻结控件快照；动态预览继续使用完整 MediaWiki；
静态发布物降级为 Vector 原生无脚本阅读模式，不发布失效外观控件。
导出器只负责移除无法运行的外观入口，并将根元素规范化为
`vector-feature-appearance-pinned-clientpref-0`；它不生成控件、不绑定事件、
不保存偏好，也不模拟 pinnable 状态。

## Regression Evidence

- 契约：`wiki/REGRESSION_EVIDENCE-mediawiki-native-ui.json`
- RED：修复前发布物包含 `/assets/vector-client-preferences.js`，同一所有权门禁
  返回 exit 1。
- GREEN：重建静态发布物后，同一门禁返回 exit 0；静态运行时契约同时检查
  2737 个 HTML，死链接、内部缺失路由、表单 action、动态标记、伪操作控件和
  重复 ID 均为 0。
- Counterfactual：临时重放修复前的首页发布物后，同一门禁重新返回 exit 1；
  随后恢复生成产物并再次返回 exit 0。
- Browser：动态 MediaWiki 由 ResourceLoader 原生生成 8 个 Vector 外观控件，
  验证字号持久化、钉住/取消钉住和 `1120px` 响应式迁移。

## Repair Boundary

- `wiki/scripts/export-pages-snapshot.py`
- `wiki/scripts/audit-static-runtime-contract.py`
- `wiki/scripts/check-mediawiki-native-ui.py`
- `wiki/scripts/check-mediawiki-native-runtime.{sh,js}`
- Wiki 发布契约、模块 AGENTS 和调试记录

## Frozen Nodes

- MediaWiki 1.46 与 Vector 2022 源码
- ResourceLoader 模块图与原生控件 DOM
- Wiki 词条、模板、首页内容和用户并行改动

## Audit Case Sampling

- Decision：`no-case`
- Reason：该问题已直接晋升为模块 AGENTS 硬约束、发布契约和机械 Gate；
  当前仓库没有 `governance/` 项目案例库，另建平行案例只会复制同一真相。
- Reusable root cause：在缺少框架运行时的静态发布面复制增强后 DOM 与部分状态机，
  会把 UI 所有权从上游框架转移到项目胶水代码。
- Evidence：本调试记录、原生 UI 所有权门禁、结构化 RED/GREEN/反事实契约。

## Reverification Required

- [x] 修复前发布物 RED
- [x] 修复后静态发布物 GREEN
- [x] 修复前发布物 counterfactual RED
- [x] 动态 MediaWiki 原生浏览器行为 GREEN
- [x] 本地静态快照桌面与移动端只读外观复核
