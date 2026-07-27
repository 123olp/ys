# Vector 外观组件上游

- 上游页面：`https://zh.wikipedia.org/wiki/Wikipedia:首页`
- 上游组件：Vector 2022 `#vector-appearance`
- 获取日期：2026-07-27
- 运行时来源：MediaWiki 1.46 / Vector `skins.vector.clientPreferences`
- 许可证：GPL-2.0-or-later（Vector）；页面界面文本按 Wikimedia 项目适用许可使用

`appearance-controls.html` 只保存浏览器执行 Vector 原生 ResourceLoader 后生成的三个 client-preferences portlet。固定/隐藏按钮、pinned/unpinned 容器和 pinnable data attributes 直接来自 MediaWiki 的 Vector 页面外壳。仓库不得为该组件另建视觉层；刷新时必须从固定 Vector 版本重新抓取 DOM、核对控件数量和字段，再更新快照。

Cloudflare Pages 发布物不运行 MediaWiki 后端与 ResourceLoader，因此 `scripts/export-pages-snapshot.py` 在原生 `#vector-appearance` 容器中冻结这份 DOM；`scripts/vector-client-preferences-static.js` 把原生单选值映射回 Vector 已定义的 document classes，并按 Vector 的 pinned/unpinned 容器契约维护固定状态、`1120px` 断点和浏览器本地匿名偏好。
