# Historical Tech Tree 完整抓取与落盘契约

## 目标

对 `https://www.historicaltechtree.com/` 保存可离线重放、可校验、可追溯的本地研究快照。抓取结果用于分析纵向知识树、节点关系、详情面板和交互行为，不授予第三方内容或资产的再分发权。

## 工作流来源

Windows 侧已验证的抓取方法来自：

```text
D:\.projects\epub-translator\work\philosophy-knowledge-graph\
├── download_dataset.ps1
├── sync-upstream.ps1
├── verify-web.ps1
├── browser-smoke.mjs
└── site-mirror\
```

它提供的方法链是：

```text
公开数据接口识别
  -> Chrome/CDP 记录真实页面请求与渲染 DOM
  -> aria2 按确定清单下载页面、API、脚本、样式、字体和图片
  -> 保存原始响应、响应头、网络清单和逐文件 SHA-256
  -> 本地 HTTP 重放
  -> Chrome 验证页面非空、节点数量、缩放控件、节点详情与断网闭合
```

哲学知识图谱只作为工作流参考，不是 Historical Tech Tree 的内容快照。需要导入参考批次时使用：

```bash
python3 tools/tech-tree-reference-capture/import_workflow_reference.py
```

## Windows 执行

在 PowerShell 中执行：

```powershell
powershell -ExecutionPolicy Bypass -File `
  "<wsl-home>\.projects\human_infra\tools\tech-tree-reference-capture\capture-historical-tech-tree.ps1"
```

抓取器默认输出到：

```text
D:\.projects\human-infra-reference-captures\historical-tech-tree\<run-id>\
├── raw/                    # 原始页面、API 和响应头
├── mirror/                 # 按 URL 路径保存的离线站点
├── browser/                # 渲染 DOM、截图和 Chrome 网络证据
├── evidence/               # URL、文件、哈希、计数与验收报告
└── source-code/            # 固定提交号的公开源码快照

D:\.projects\human-infra-reference-captures\historical-tech-tree\
├── historical-tech-tree-<run-id>.zip
└── historical-tech-tree-<run-id>.zip.sha256.json
```

批次目录不可覆盖；复抓必须使用新批次，避免证据漂移。

## 完成标准

- `/api/inventions` 与 `?detail=true` 均可解析，节点数不少于 2,400、连接数不少于 3,700，且所有连接端点均存在。
- API 声明的每个 `localImage` 均被保存；不得用远程 Wikimedia 图替代缺失的本地图片。
- Chrome 观察到的同源 CSS、JavaScript、字体、图片和数据请求全部进入下载清单。
- 原始核心响应单独记录来源 URL、HTTP 状态、Content-Type、字节数；所有原始响应、镜像、浏览器证据和源码文件均记录字节数与 SHA-256。
- 原始响应与离线重放副本彼此分离，任何重写只能发生在 `mirror/`。
- ZIP 可解压，且其内容包含完整证据目录。
- 在线与离线 Chrome 门禁均通过：标题和主体存在、节点可见、缩放控件存在、节点可进入详情状态。
- 离线门禁期间不允许请求 `historicaltechtree.com` 或其他远程运行时资源。
- 公开源码仓库 `etiennefd/hhr-tech-tree` 的提交号和 MIT 代码许可必须与“数据不属于 MIT”分别记录。

## 边界

- 不绕过登录、付费墙、验证码、robots 或访问控制。
- 不把第三方站点代码直接并入 Human Infra 正式 `web/`。
- 不把可显示误报为交互完整；缩放和节点详情必须由浏览器门禁证明。
- 上游未声明再分发许可证，快照仅限本地研究与比较。
