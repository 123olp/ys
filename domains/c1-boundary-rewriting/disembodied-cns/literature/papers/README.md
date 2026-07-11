# 离线文献镜像

本目录保存 `disembodied-cns` 文献包的本地镜像。它用于离线阅读、证据复核和来源追踪，不改变 `source-signals.md` 与 `source-cards.md` 的证据等级。

## 目录结构

```text
papers/
├── README.md
├── manifest.tsv
├── html/
│   └── MSB-SIG-*.html
└── pdf/
    └── MSB-SIG-*.pdf
```

## 文件职责

- `manifest.tsv` 记录每条来源的原始 URL、最终 URL、本地 PDF、本地 HTML、下载状态和失败原因。
- `html/` 保存官方页面、PubMed 页面、PMC 页面或监管页面快照。
- `pdf/` 只保存可通过开放或官方下载路径取得的 PDF。

## 当前状态

- 已为 `MSB-SIG-001` 到 `MSB-SIG-025` 建立本地入口。
- PDF 已下载：`MSB-SIG-006`、`MSB-SIG-007`、`MSB-SIG-012`、`MSB-SIG-013`、`MSB-SIG-014`、`MSB-SIG-015`、`MSB-SIG-016`、`MSB-SIG-020`。
- 其余来源保存为 HTML 快照；部分 PMC 页面虽然显示 PDF UI，但脚本请求返回 NCBI 下载挑战或 OA API 不开放，因此不绕过访问限制。

## 使用边界

- 本目录是来源镜像，不是完整版权论文库。
- HTML 快照可用于离线定位来源语境，但不能替代正式 PDF 原文核验。
- 任何未取得 PDF 的条目必须继续按 `manifest.tsv` 的状态说明引用，不得写成“全文已下载”。
- 新增下载项必须同步更新 `manifest.tsv`、本文件和上级 `literature/README.md`。
