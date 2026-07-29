# 门户本地化动态资源 404

## 现象

`https://tradecatlabs.com/` 的 HTML、CSS 和主要脚本均可正常加载，但简体中文浏览器会请求
`/portal/wikipedia.org/assets/l10n/zh-hans-<hash>.json` 并收到 404。页面仍可见，因此只检查
HTTP 200 或首屏截图无法发现该缺陷。

## 根因

Wikimedia 门户脚本根据浏览器语言和 `index.html` 中的 `translationsHash` 动态拼接本地化
资源路径。原快照保留了该脚本与哈希，却只复制了顶层 `assets/`，没有镜像
`portal/wikipedia.org/assets/l10n/`。这是上游运行时资源依赖不完整，不是 Cloudflare
路由或缓存问题。

## 修复

- 从 `www.wikipedia.org` 保存与当前 `translationsHash` 一致的简体、繁体中文原始 JSON。
- `build-portal-release.py` 将上游 `portal/` 资源树复制到发布物。
- `check-main-domain-release.py` 从生成 HTML 读取哈希，验证两份 JSON 存在、可解析且语言代码一致。
- `validate-source.sh` 将两份 JSON 纳入源快照必备文件。

## 回归证据

修复前运行 `make main-domain-build`：

```text
RuntimeError: 主域名门户缺少 Wikimedia 本地化资源: zh-hans-f8b41854.json
```

补齐资源后原命令通过：

```text
主域名静态门户契约通过。
```

生产发布还必须使用真实中文浏览器会话验证：所有响应状态小于 400，且无 `console.error`
和 `pageerror`。
