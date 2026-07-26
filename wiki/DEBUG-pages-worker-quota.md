# Wiki Pages Worker 配额异常

## Bug

Cloudflare 账户在纯内容站发布后出现接近每日 `100,000` 次 Workers 请求的用量，且存在 CPU 时间消耗。

## Environment

- 平台：Cloudflare Pages
- 站点：`human-infra-wiki.pages.dev`
- 构建入口：`wiki/scripts/build-pages-release.sh`
- 导出入口：`wiki/scripts/export-pages-snapshot.py`

## Reproduction

1. 执行 Wiki Pages 构建。
2. 检查 `wiki/runtime/pages/wiki/`。
3. 观察到发布根目录包含 `_worker.js`。
4. `_worker.js` 的 `fetch()` 对首页、词条、搜索、API 与静态资产请求均处于请求链路上。

## Observations

- 门户发布物没有 `_worker.js` 或 `functions/`。
- 科技树是 Next.js static export，没有 Pages Functions。
- Wiki 导出器中的 `write_worker()` 每次构建都会把 `wiki/pages/wiki-worker.js` 复制为发布根目录 `_worker.js`。
- Wiki 当前发布物约 75 MB、2730 个词条；动态 Worker 只承担模板令牌替换、搜索与随机跳转，没有必须依赖服务端状态的能力。
- Cloudflare Pages Advanced Mode 的 `_worker.js` 会接管项目请求；因此静态内容被包装为函数请求。

## Hypotheses

### H1 ROOT HYPOTHESIS

Wiki 发布根目录中的 `_worker.js` 使本应由 Pages 静态资产层直接响应的请求进入 Workers 运行时。

- Supports：构建产物存在 `_worker.js`，源代码导出默认 `fetch()`，Dashboard 同时出现请求数与 CPU 时间。
- Conflicts：尚未从 Cloudflare 账户分析接口取得逐路径调用明细。
- Test：删除生产 Worker，将词条预渲染为 HTML，并验证发布物不存在任何函数入口。

### H2

门户或科技树含隐藏 Pages Functions。

- Supports：三个项目共享同一账户用量。
- Conflicts：源码与当前构建产物扫描未发现对应函数入口。
- Test：对三个最终发布目录执行函数入口扫描。

### H3

Cloudflare Dashboard 把所有静态资产请求计入 Workers 免费额度。

- Supports：页面访问会产生大量资源请求。
- Conflicts：Cloudflare 定价说明明确区分免费无限的静态资产请求与计入配额的函数请求，CPU 时间也不能由纯静态响应产生。
- Test：发布纯静态版本后观察 Workers 用量增量。

## Experiments

### E1：发布物入口扫描

- Hypothesis：H1
- Command：`find wiki/runtime/pages/wiki -name '_worker.js' -o -name '_routes.json'`
- Result：发现 `wiki/runtime/pages/wiki/_worker.js`。
- Status：confirmed

### E2：其余站点源码扫描

- Hypothesis：H2
- Command：扫描门户、科技树与仓库中的 `_worker.js`、`_routes.json`、`functions/`。
- Result：仅 Wiki 发布物存在 `_worker.js`。
- Status：rejected

### E3：完整静态导出

- Hypothesis：H1
- Command：`bash wiki/scripts/build-pages-release.sh`
- Result：2730 个词条完成预渲染且无 Worker；后续 GEO 审计因 sitemap 中未转义的 `&` 正确失败。
- Status：confirmed
- Follow-up：在 XML 序列化边界转义 URL，重新执行完整构建。

### E4：Wrangler Pages 运行时

- Hypothesis：H1
- Command：`wrangler pages dev wiki/runtime/pages/wiki --port 18888 --ip 127.0.0.1 --compatibility-date 2026-07-26`
- Result：Wrangler 明确报告 `No Functions. Shimming...`；首页、代表词条、搜索和随机入口返回 200，未知词条与 `/api.php` 返回 404，旧 `/index.php/<title>` 返回 301。
- Status：confirmed
- Follow-up：增加静态 `404.html`，防止 Pages 对未知路径返回首页 200。

### E5：发布包重复资产审计

- Hypothesis：删除 Worker 后，正文 JSON 与运行时模板已经没有公开消费者。
- Command：检查 `snapshot/pages/`、`snapshot/article-shell.html`、`snapshot/main-shell.html` 与发布包大小。
- Result：构建阶段仍使用内存中的页面数据和临时模板完成预渲染，发布阶段删除正文 JSON 与模板；最终发布包约 161 MB、2,835 个文件，公开索引只保留 `title`、`normalized`、`aliases` 和 `urlPath`。
- Status：confirmed

### E6：生产部署回归

- Hypothesis：相同纯静态发布物部署到正式 Pages 项目后，公开路由保持完整。
- Command：部署 `human-infra` 与 `human-infra-wiki`，再执行 `bash wiki/scripts/smoke-pages-release.sh`。
- Result：门户、Wiki、科技树三站公开 smoke 全部通过；Wiki 首页、词条、搜索、随机入口、GEO 入口、真实 404 与旧路径重定向均符合契约。
- Status：confirmed
- Boundary：Dashboard 中已经产生的 Workers 当日历史用量不会倒退；应从本次部署之后观察增量，并在 UTC 午夜额度重置后确认静态访问不再消耗 Workers 请求。

## Root Cause

Wiki 把本可在构建期完成的模板渲染放进 Pages `_worker.js`，错误地将静态知识站升级为请求时计算应用，导致所有 Wiki 请求进入 Workers 配额与 CPU 计费面。

## Fix

- 构建期为首页和全部词条生成静态 HTML。
- 用静态 JavaScript + `snapshot/index.json` 保留标题搜索与随机跳转。
- 用 Pages 原生 `_redirects` 兼容旧的 `/index.php/*` 路径。
- 删除生产 `_worker.js`，构建和 smoke test 对函数入口实行零容忍。

## Regression Evidence

修复完成后必须证明：

1. Wiki 构建产物不存在 `_worker.js`、`_routes.json` 或 `functions/`。
2. 首页、代表词条、搜索、随机入口、robots、sitemap 与 GEO 机器入口可用。
3. 旧 `/index.php/<title>` 路径由静态重定向兼容。
4. 三个公开站的发布目录均通过静态发布门禁。

本地回归结果：

- 2730 个 canonical Wiki 词条全部生成静态 HTML。
- 发布物不存在 `_worker.js`、`_routes.json`、`functions/`、`snapshot/pages/` 或运行时模板。
- `bash wiki/scripts/validate-source.sh`：PASS。
- `python3 wiki/scripts/audit-geo-publication.py ...`：PASS。
- Wrangler Pages Runtime：`No Functions. Shimming...`。

## Conclusion

根因已由源码入口、构建产物和 Wrangler `No Functions` 运行时证据共同确认。修复后的 Wiki 使用构建期预渲染、静态搜索索引、Pages 原生重定向和真实 404，不再需要生产 Worker。

## 2026-07-27 三站生产巡检

### Scope

- 公开入口：`human-infra.pages.dev`、`human-infra-wiki.pages.dev`、`human-infra-tech-tree.pages.dev`。
- 视口：桌面端 `1440x1000`、移动端 `390x844`。
- 检查面：HTTP 状态、真实 404、函数入口、资源加载、浏览器控制台、横向溢出、关键搜索交互、图像状态和图标按钮可访问名称。

### Observation

- 门户、Wiki 首页和代表词条未发现控制台错误、失败请求、坏图或横向溢出。
- 科技树页面没有失败请求或布局溢出，但桌面端和移动端各产生 15 条 `Invalid image URL: ""` 警告。
- 数据源中恰有 15 个节点用空字符串表达“没有图片”；空值是合法缺省状态，不是非法 URL。
- 初始关闭图片后再开启图片时，数据加载逻辑可能把图片字段永久丢弃。
- 连接重置令牌没有进入可见元素缓存键，重置动作可能命中旧缓存。
- 搜索、筛选、缩放和设置中的图标按钮缺少稳定的可访问名称。

### Root Cause

科技树把“图片缺失”和“图片地址非法”合并为同一校验分支，同时让图片可见性状态参与数据规范化。前者制造无效告警，后者让视图开关改变底层数据；此外，连接重置状态未进入缓存身份，导致动作语义与缓存契约不一致。

### Fix

- `validateImageUrl()` 将 `null`、`undefined` 和去空白后的空字符串视为合法缺省，只对非空且格式错误的值告警。
- 节点数据始终执行相同的图片规范化，`showImages` 只控制渲染，不再改写数据。
- 将连接重置令牌纳入可见元素缓存键，保证重置会触发重新计算。
- 为搜索、筛选、缩放、设置和筛选移除按钮补齐 `type`、`aria-label`、`title` 与必要的展开状态。

### Regression Evidence

- 科技树数据治理：2415 个原始节点、3749 条原始连接；Human Infra 裁剪结果为 299 个节点、382 条连接；布局交叉从 3916 降至 546，全部门禁通过。
- Next.js 静态导出：9/9 页面生成完成；首页 first-load JavaScript 为 137 kB；所有路由保持静态。
- 本地桌面端与移动端：控制台错误/警告为 0，失败请求为 0，横向溢出为 0。
- 搜索 `CRISPR` 可用；移动端搜索可展开；所有可见按钮均具有可访问名称。
- 科技树静态发布包为 52 MB、2522 个文件，不含 `_worker.js`、`_routes.json` 或 `functions/`。
- Cloudflare Pages 部署完成：`c3fde2f2.human-infra-tech-tree.pages.dev`，正式别名继续使用 `human-infra-tech-tree.pages.dev`。
- 生产桌面端与移动端：门户、Wiki、代表词条和科技树均无控制台错误/警告、失败请求、坏图或横向溢出。
- 生产科技树搜索 `CRISPR` 返回结果；移动端搜索可展开；所有可见按钮均具有可访问名称。
- 生产 `llms.txt`、`entity.jsonld`、`sitemap.xml` 和 `robots.txt` 均返回 200。
- `bash wiki/scripts/smoke-pages-release.sh`：PASS。

### Residual Finding

移动端横向画布会渲染与视口边界相交的节点；当节点主体几乎完全位于左侧视口之外时，边缘可能短暂露出部分 `TIME UNRESOLVED` 标签。页面没有文档级横向溢出，拖拽、搜索、缩放和连线保持可用。该问题应在虚拟化可见性判定中增加“最小可见面积”或节点包围盒裁剪规则，不能用全局 `overflow: hidden` 代替，否则会破坏横向平移和边缘连接。

### Delivery Risk

科技树源码位于独立本地仓库，当前没有配置远程仓库，且存在此前已部署的竖向布局改造与尚未上线的 GEO 改动。源码提交、线上部署和主仓库证据并非同一原子事务；发布时必须记录实际构建输入，禁止把“Pages 已部署”误写成“源码已推送远程”。
