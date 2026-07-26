# 科技树到 Wiki 的路由契约

## 目标

Historical Tech Tree 风格前端只负责关系、阶段和状态展示。点击节点后，通用公共概念跳到外部 Wikipedia，Human Infra 专有概念跳到本地 Wiki。

## 节点字段

```json
{
  "id": "technology.partial-reprogramming",
  "label": "部分细胞重编程",
  "knowledgeTarget": {
    "kind": "internal-wiki",
    "title": "部分细胞重编程"
  }
}
```

`knowledgeTarget.kind` 只允许：

- `internal-wiki`：项目专有词条；本地编辑环境生成 `/index.php?title=<encoded title>`，公开只读环境生成 `/wiki/<encoded title>/`；
- `external-wikipedia`：公共通用词条，必须保存完整 HTTPS URL；
- `unresolved`：尚无合格词条，前端不得伪造跳转。

## 不变量

- 节点 `id` 是跨科技树、Wiki 和证据资产的稳定主键。
- 页面标题可以改名，改名后必须在旧标题建立重定向。
- 科技树不复制 Wiki 正文和参考文献，只可缓存一句摘要。
- 本地页面不存在时显示“待建词条”，不得静默跳到搜索结果。
- 外部链接必须指向具体词条，不得只指向 Wikipedia 首页。

## URL 解析

本地开发基址默认为 `http://localhost:18782`：

```text
internal-wiki
  -> http://localhost:18782/index.php?title=%E9%83%A8%E5%88%86%E7%BB%86%E8%83%9E%E9%87%8D%E7%BC%96%E7%A8%8B
```

公开只读入口：

```text
internal-wiki
  -> https://human-infra-wiki.pages.dev/wiki/%E9%83%A8%E5%88%86%E7%BB%86%E8%83%9E%E9%87%8D%E7%BC%96%E7%A8%8B/
```

生产解析器必须同时替换基址和路由形式，但不得改变节点 ID、目标类型或页面标题。历史 `/index.php/<title>` 由 Pages 静态重定向兼容；不得用 Worker 维持旧路由。
