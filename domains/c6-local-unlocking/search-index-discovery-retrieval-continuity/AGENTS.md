# search-index-discovery-retrieval-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/search-index-discovery-retrieval-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
| 路径真相源 | `domains/_possibility-space-control/classification.tsv` |
| 复核状态 | `heuristic-v0.1` |

### 文件职责

- `README.md` 面向读者，说明研究对象、Human Infra 价值链路、证据边界、非目标和下一步资料入口。
- `AGENTS.md` 面向维护者和代理，说明目录结构、上下游依赖、禁止事项、更新规则和验证要求。

### 更新规则

- 修改本域对象、边界或上下游关系时，必须同步检查 README、AGENTS 和分类表中的 `physical_path`。
- 新增资料优先沉淀为 Source Signals、Source Cards、Claim-Evidence Matrix 或明确的证据段落，不把未经核验的摘要写成稳定结论。
- 若发现当前层级不符合“可能性空间控制力”标尺，先修改 `_possibility-space-control/rubric.md` 或 `classification.tsv`，再移动目录。

### 禁止事项

- 不把研究域写成个体行动处方、临床建议、法律建议、投资建议、工程操作手册或规避规则指南。
- 不在本目录保存无来源、无边界、无证据等级的断言。
- 不绕过父级 C1-C6 物理目录直接在 `domains/` 根目录新增正式研究域。
<!-- domain-agent-contract:end -->


本目录承载搜索、索引、发现与检索连续性研究域，关注资料和服务如何在需要时被找到、验证和复用。

## 目录结构

```text
search-index-discovery-retrieval-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义搜索、索引、元数据、sitemap、schema、链接可达和检索审计如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 Sitemaps、Schema.org、W3C Data on the Web、Library of Congress 和信息检索研究。
- 不写排名操纵、垃圾 SEO、爬虫规避、隐私绕过、抓取滥用或提示注入方案。
- 涉及搜索系统时只讨论可发现性、元数据、权限、来源验证和检索质量边界。
- 新增指标必须注明口径：索引覆盖、检索成功率、断链率、来源可验证性、权限错配或查询成本。
