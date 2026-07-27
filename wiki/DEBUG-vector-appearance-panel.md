# Vector 外观面板在 Pages 静态快照中消失

## Bug

`https://human-infra-wiki.pages.dev/` 在桌面宽屏中保留了 Vector 2022 的右侧栏空间，但“外观”面板没有显示文字大小、页面宽度和颜色模式控件。

## Environment

- MediaWiki 1.46 + Vector 2022
- 本地源站：`http://127.0.0.1:18782`
- 静态发布：Cloudflare Pages
- 复现日期：2026-07-27

## Reproduction

```bash
curl -fsSL https://human-infra-wiki.pages.dev/ -o /tmp/wiki-live.html
python3 - <<'PY'
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("/tmp/wiki-live.html", encoding="utf-8").read(), "lxml")
print(len(soup.select("#vector-appearance input")))
PY
```

修复前结果：`0`。Vector 外观面板完整状态应包含 8 个单选控件。

## Observations

1. 本地 MediaWiki 原始响应、静态构建产物和线上 Pages 都包含 `#vector-appearance`，但容器中只有 pinnable header。
2. 本地页面经浏览器执行 ResourceLoader 后，`#vector-appearance` 中出现 8 个控件：
   - 文本：小、标准、大；
   - 宽度：标准、宽；
   - 颜色：自动、浅色、深色。
3. Vector 上游 `Appearance.less` 明确使用 `.client-nojs .vector-appearance-landmark { display: none; }`。
4. `export-pages-snapshot.py` 无条件删除全部 `<script>`，因此 `skins.vector.clientPreferences` 不会运行。

## Hypotheses

### H1: 右栏被自定义首页 CSS 覆盖

- Supports：页面右侧出现大面积空白。
- Conflicts：DOM 中 `#vector-appearance` 存在，且 Vector 自身明确在 `client-nojs` 下隐藏该 landmark。
- Test：比较本地原始响应、浏览器增强后 DOM 和线上 DOM。
- Status：rejected。

### H2: Vector 配置关闭了外观功能

- Supports：服务端容器没有控件。
- Conflicts：HTML 具有 `vector-feature-appearance-pinned-clientpref-1`，浏览器执行 ResourceLoader 后能生成全部控件。
- Test：对本地页面执行浏览器渲染并统计控件。
- Status：rejected。

### H3: 静态导出删除 ResourceLoader，但没有冻结其生成结果

- Supports：导出器删除所有脚本；原始响应控件数为 0；浏览器增强后控件数为 8；线上控件数为 0。
- Conflicts：无。
- Test：在同一页面上比较原始 DOM 与浏览器增强 DOM。
- Status：confirmed（ROOT HYPOTHESIS）。

## Experiments

### E1: 同源三态 DOM 对照

- Hypothesis：H3。
- Input：本地原始 HTML、本地浏览器增强 HTML、线上静态 HTML。
- Expected：只有浏览器增强 HTML 含 8 个外观控件。
- Result：本地原始 `0`、本地浏览器增强 `8`、线上静态 `0`。
- Verdict：confirmed。

## Root Cause

静态导出器删除了负责生成 Vector 2022 外观控件的 ResourceLoader 脚本，却仍发布只有空容器的服务端 HTML，并保留 `client-nojs` 隐藏语义，导致右侧布局槽存在而原生外观面板缺失。

## Fix

已固定官方中文 Wikipedia Vector 外观组件的 DOM 快照，在静态导出时注入该原生组件，附带 Vector 原生 `skins.vector.clientPreferences` 样式，并用最小静态适配器维护对应的 document classes 与浏览器本地偏好。

## Regression Evidence

### GREEN 1: 构建期结构门禁

```text
make pages-build
Wiki 快照完成: pages=2730 aliases=1
GEO 发布契约通过
Pages 发布产物完成
```

构建脚本要求首页存在 8 个唯一 `skin-client-pref-*` 控件，并要求加载 `/assets/vector-client-preferences.js`；任一条件不满足即失败。

### GREEN 2: 浏览器行为

Selenium 在 2048x1138 视口验证：

```text
browser-contract PASS:
controls=8
class-switch=3/3
persistence=3/3
panel=visible
console=[]
```

依次选择“大”“宽”“深色”后，HTML 分别进入：

- `vector-feature-custom-font-size-clientpref-2`
- `vector-feature-limited-width-clientpref-0`
- `skin-theme-clientpref-night`

刷新后单选状态和 document classes 均保持。截图证据：`/tmp/hi-wiki-appearance-night-fixed.png`。

### Counterfactual sensitivity

修复前同一结构检查得到 `0/8`，无法通过新增构建门禁；浏览器中 `.vector-appearance-landmark` 被 `client-nojs` 规则隐藏。新增门禁对原缺陷具有反事实敏感性。
