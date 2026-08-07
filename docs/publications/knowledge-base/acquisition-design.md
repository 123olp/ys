# 有效永生知识库：采集设计（KB Design & Acquisition Plan）

## 目标

把"有效永生"主题的全部相关文献与资源采集、下载、登记进知识库，支撑三件套（史/指南/手册）的证据链。

## 目录设计

```text
.research/literature/effective-immortality-kb/     # 原文缓存（git 忽略）
├── metadata/          # PubMed/arXiv 检索元数据 JSON（title/PMID/DOI/abstract）
├── pdf/               # 开放获取 PDF（按分类子目录）
│   ├── aging-mechanism/     # 衰老机制
│   ├── intervention/        # 长寿干预
│   ├── health-evidence/     # 健康手册证据
│   ├── digital-path/        # 数字迁移/脑保存
│   └── philosophy/          # 哲学（SEP/IEP 词条）
└── manifest.json      # 采集清单：查询词、批次、状态、下载结果

docs/publications/knowledge-base/catalog.md        # 资料总索引（登记层，已建）
docs/publications/knowledge-base/acquisition-log.md # 采集日志（每批记录）
```

## 采集批次（P2 推进）

| 批次 | 主题 | 检索源 | 对应作品集 |
| --- | --- | --- | --- |
| A1 | 衰老机制（Hallmarks/线粒体/衰老细胞/蛋白稳态） | PubMed/Europe PMC | 指南-维护、手册 |
| A2 | 长寿干预（CR/禁食/Senolytics/NAD+/重编程） | PubMed/Europe PMC | 指南-维护、手册-候选区 |
| A3 | 健康证据（运动/睡眠/营养/补剂/社交） | PubMed/Europe PMC | 手册七维度 |
| A4 | 数字路径（脑保存/连接组/意识/BCI） | PubMed/arXiv | 指南-数字 |
| A5 | 哲学判据（同一性/绵延/意识/死亡） | SEP/IEP（开放） | 指南-哲学判据 |
| A6 | 历史与思想运动（超人类主义/冷冻史） | 权威机构页/开放文献 | 永生史 |

## 采集流程（每批）

1. PubMed E-utilities `esearch`（查询词 + 日期过滤 + 综述优先）
2. `esummary`/`efetch` 拿元数据（PMID/DOI/title/abstract/year）
3. Europe PMC 检查开放获取（`OPEN_ACCESS`），可下则下载 PDF/XML 到分类目录
4. 登记 `manifest.json` + 追加 `catalog.md` 条目
5. 采集日志写入 `acquisition-log.md`

## 下载边界

- 只下载：PMC 开放获取、arXiv、出版社开放 PDF、作者公开副本、SEP/IEP 词条
- 不绕过：付费墙、登录墙、Cloudflare 挑战
- 付费文献：只登记元数据（状态=metadata-only），不下载

## 证据纪律（贯穿）

- 综述优先于单篇；系统综述/元分析优先于叙述性综述
- 动物/机制文献与人体证据分开标注（物理规律约束）
- 每条文献登记后必须可回溯到 catalog ID
