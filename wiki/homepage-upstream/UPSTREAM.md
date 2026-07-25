# 中文首页上游记录

## 来源

- 上游页面：`https://zh.wikipedia.org/wiki/Wikipedia:首页`
- 页面源修订：`92774903`，时间 `2026-05-24T07:19:34Z`
- 页首模板：`Wikipedia:首页/banner`，修订 `92431348`，时间 `2026-04-27T02:10:05Z`
- 样式页：`Wikipedia:首页/styles.css`
- 样式源修订：`93123966`，时间 `2026-06-19T04:54:47Z`
- 深色兼容：Wikimedia 生产模块 `ext.wikimediamessages.styles` 的 `.page-Main_Page` 规则
- 获取接口：MediaWiki Action API `prop=revisions`
- 许可证：CC BY-SA 4.0；页面贡献者历史以中文维基百科对应修订历史为准。

## 固定快照

`snapshot/` 保存未经人工改写的上游资产：

| 文件 | 内容 |
| --- | --- |
| `Wikipedia_Home.wiki` | 官方首页原始 Wikitext |
| `Wikipedia_Home_banner.wiki` | 官方页首模板原始 Wikitext |
| `Wikipedia_Home_styles.css` | 官方 TemplateStyles 原始 CSS |
| `Wikipedia_Home_rendered.html` | Action API 返回的官方渲染 HTML |
| `metadata.json` | 修订号、时间、来源链接与逐文件 SHA-256 |

快照是首页结构与样式的真相源。`content/Human_Infra_Main_Page.wiki`、`content/Template_Home_Header.wiki` 和 `content/Template_Home_styles_css.wiki` 均为生成产物，禁止手工编辑。

## 复用边界

本地首页保留上游 `mp-2012` 根节点、banner、左右栏、栏目块、链接区和 TemplateStyles 机制。Human Infra 只通过 `Template:首页/*` 内容槽位替换站点名称、栏目文本、内部链接和项目说明；不得暗示本项目隶属于 Wikimedia Foundation 或中文维基百科。

生成器只允许两类适配：

1. 将上游动态内容模板替换为 Human Infra 内容槽位，同时保留上游外层 DOM。
2. 页首站点标识由 Human Infra 内容槽位提供，因此生成 CSS 不加载上游 Wikipedia 标志背景；蓝色横幅仍使用同一 Wikimedia Commons 资源，只把协议相对 URL 规范化为 TemplateStyles 允许的 HTTPS URL。原始 CSS 始终完整保存在快照中。
3. MediaWiki 1.46 会给原始 `<h1>` 增加 `.mw-heading1` 包装，而 Wikimedia 生产渲染中的首页标题仍是直接 `<h1>`；生成 CSS 只抵消该包装层的额外字号放大，使页首恢复官方 120px 几何契约。
4. 官方移动端的空标志槽高度为 0；本地品牌图只在 `720px` 及以上视口显示，使移动端页首继续遵守上游 240px 几何契约。

任何新增结构或样式适配都必须先进入生成器并具备唯一锚点断言，不得直接修改生成产物。

## 更新流程

1. 运行 `make homepage-refresh` 固定获取官方 Wikitext、页首、CSS、渲染 HTML 和元数据。
2. 审查修订差异、`mp-2012` DOM、CSS 选择器和依赖扩展；不得以截图重写。
3. 运行 `make homepage-build` 从快照重新生成本地首页。
4. 运行 `make homepage-check`，确认快照哈希和生成产物均未漂移。
5. 运行 `make import`、`make validate`、`make smoke`。
6. 在桌面、移动端、浅色和深色模式验证首页。
