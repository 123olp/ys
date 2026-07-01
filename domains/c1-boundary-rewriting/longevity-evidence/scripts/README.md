# 脚本目录

这里放置 Longevity Evidence 子域的数据采集、清洗、校验和导出脚本。

## 规则

- 脚本必须可重复执行。
- 外部 API 调用必须设置超时、分页和速率限制。
- 原始数据保存到本子域的 `data/raw/`，清洗结果保存到本子域的 `data/processed/`。
- 医学判断和证据评分规则放在文档或配置中，不硬编码在采集脚本里。

## 当前脚本

- `collect_mvp_data.py`：采集首批干预的 PubMed、OpenAlex、ClinicalTrials.gov 和 openFDA 数据。
- `collect_core_data.py`：采集 HAGR、PubChem、openFDA 不良事件聚合和 Drugs@FDA 数据。

运行示例：

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 10
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
```
