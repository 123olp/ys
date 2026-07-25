# 中文首页上游记录

## 来源

- 上游页面：`https://zh.wikipedia.org/wiki/Wikipedia:首页`
- 页面源修订：`92774903`，时间 `2026-05-24T07:19:34Z`
- 样式页：`Wikipedia:首页/styles.css`
- 样式源修订：`93123966`
- 深色兼容：Wikimedia 生产模块 `ext.wikimediamessages.styles` 的 `.page-Main_Page` 规则
- 获取接口：MediaWiki Action API `prop=revisions`
- 许可证：CC BY-SA 4.0；页面贡献者历史以中文维基百科对应修订历史为准。

## 复用边界

本地首页保留上游 `mp-2012` 根节点、banner、左右栏、栏目块、链接区、TemplateStyles 机制和 WikimediaMessages 首页深色兼容规则。Human Infra 只替换站点名称、栏目文本、内部链接和项目说明；不得暗示本项目隶属于 Wikimedia Foundation 或中文维基百科。

## 更新流程

1. 通过 Action API 固定获取页面源和 `Wikipedia:首页/styles.css` 的修订号。
2. 比较 `mp-2012` DOM、CSS 选择器和依赖扩展，不以截图重写。
3. 只合并上游结构和样式变更，保留 Human Infra 内容模板。
4. 运行 `make import`、`make validate`、`make smoke`。
5. 在桌面、移动端、浅色和深色模式验证首页；确认左右栏、导航和底部链接均可访问。
