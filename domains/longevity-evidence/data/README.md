# 数据目录

这里存放 Longevity Evidence 子域的公开数据源样例、原始快照和清洗后数据。

## 规则

- `raw/` 用于原始 API 响应或下载文件。
- `processed/` 用于清洗后的结构化数据。
- `manual/` 用于人工整理的首批 MVP 数据。
- 每份数据必须记录来源、抓取时间和处理脚本。

`raw/` 和 `processed/` 是可再生成的数据产物，已在根 `.gitignore` 中按多子域路径忽略；需要保留样例或发布快照时，应先写清来源、版本和体积边界。

## 当前文件

- `manual/interventions.json`：首批 20 个干预对象、类别、别名和检索词。
- `raw/`：采集脚本保存的原始响应。
- `processed/`：采集脚本生成的 JSONL 索引和汇总。
- `processed/hagr/`：HAGR 官方 zip 快照解压后的 CSV 文件。
