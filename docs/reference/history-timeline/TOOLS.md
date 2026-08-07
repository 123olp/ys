# 历史年表工具与指导文献

## 1. 成熟开源工具

### 采集与引用

| 工具 | 用途 | 开源 |
| --- | --- | --- |
| [Zotero](https://www.zotero.org/) | 文献、档案、网页、书目与引用管理 | 是 |
| [Tropy](https://tropy.org/) | 档案照片、手稿和资料对象的整理与元数据管理 | 是 |
| [OpenAlex](https://openalex.org/) | 学术文献元数据检索 | API |
| [Internet Archive](https://archive.org/) | 历史文本、网页快照和开放档案 | 是 |
| [Europe PMC](https://europepmc.org/) | 生物医学开放全文与元数据 | API |

### 数据清洗与建模

| 工具 | 用途 | 开源 |
| --- | --- | --- |
| [OpenRefine](https://openrefine.org/) | 日期、人名、地名和来源数据的清洗、对齐、批处理 | 是 |
| [Wikibase](https://wikiba.se/) | 自托管实体知识库，适合事件、人物、地点、时期关联 | 是 |
| [Git](https://git-scm.com/) | 年表数据版本控制、回滚和协作 | 是 |

### 标注与本体

| 工具/标准 | 用途 | 开源 |
| --- | --- | --- |
| [PeriodO](https://perio.do/) | 历史分期的全球 gazetteer，统一“时期”名称与时间区间 | 是 |
| [CIDOC-CRM](https://www.cidoc-crm.org/) | 文化遗产事件、人物、地点、时间与来源关系本体 | 开放标准 |
| [TEI](https://tei-c.org/) | 历史文本的结构化标注标准 | 开放标准 |
| [EDTF](https://www.loc.gov/standards/datetime/) | 扩展日期时间格式，表达约数、区间和不确定日期 | 开放标准 |
| [Recogito](https://recogito.pelagios.org/) | 文本中地名、人物、事件和关系的协作标注 | 是 |

### 时间线与可视化

| 工具 | 用途 | 开源 |
| --- | --- | --- |
| [TimelineJS](https://timeline.knightlab.com/) | 轻量、成熟的多媒体时间线 | 是 |
| [Neatline](https://neatline.org/) | 地图 + 时间线 + 档案叙事，适合空间历史 | 是 |
| [Heurist](https://heuristnetwork.org/) | 数字人文数据库、时间线、地图和关系网络 | 是 |
| [Palladio](https://hdlab.stanford.edu/palladio/) | 时间、空间、关系多维探索 | 是 |
| [Omeka S](https://omeka.org/s/) | 数字馆藏与展览发布平台 | 是 |
| [D3.js](https://d3js.org/) | 定制化时间轴、关系图和交互可视化 | 是 |

### OCR 与文本化

| 工具 | 用途 | 开源 |
| --- | --- | --- |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | 多语言 OCR | 是 |
| [Transkribus](https://readcoop.eu/transkribus/) | 历史手稿识别与转录 | 部分开源/平台 |

## 2. 推荐工具链

最稳的严肃历史组合：

```text
Zotero/Tropy 采集
  -> OpenRefine 清洗
  -> JSON/YAML 年表数据
  -> PeriodO + EDTF 统一时期与日期
  -> CIDOC-CRM 事件关系
  -> TimelineJS/Neatline 可视化
  -> Git 版本与复核
```

本项目已落地的发布命令：

```bash
make history-timeline-preview
```

该命令从 `timeline.json` / `sources.json` / `periods.json` 生成 `timelinejs.json` 与 `preview.html`。生成物属于机器派生数据，不能手工单独修改。
当前 `preview.html` 使用 ECharts 图表模式；`timelinejs.json` 继续保留 TimelineJS JSON 兼容结构，便于未来切换叙事型发布层。

日期补齐命令：

```bash
python3 tools/backfill_history_timeline_dates.py --workers 4
```

该命令从 Crossref 拉取缺失的完整出版日期，写回 `timeline.json`，并把已核验的 DOI-日期映射缓存到 `date-backfill-cache.json`，支持断点续跑。

## 3. 指导文献

### 历史方法论

- Philippe Ariès, *Western Attitudes Toward Death: From the Middle Ages to the Present*, 1974.
- Philippe Ariès, *The Hour of Our Death*, 1981.
- Arthur O. Lovejoy, *The Great Chain of Being*, 1936.
- Reinhart Koselleck, *Futures Past: On the Semantics of Historical Time*, 1985/2004.
- Michel Foucault, *The Archaeology of Knowledge*, 1969/1972.
- Shawn Graham, Ian Milligan, Scott Weingart, *Exploring Big Historical Data: The Historian's Macroscope*, 2015/2022. DOI: [10.1142/9781783266104](https://doi.org/10.1142/9781783266104).

### 事件与时期建模

- Rabinowitz, Shaw, Golden, Kansa, *Nanopublication beyond the sciences: the PeriodO period gazetteer*, 2016. DOI: [10.7717/peerj-cs.44](https://doi.org/10.7717/peerj-cs.44).
- Shaw, Rabinowitz, Golden, Kansa, *Period Assertion as Nanopublication*, WWW 2015. DOI: [10.1145/2740908.2742021](https://doi.org/10.1145/2740908.2742021).
- van Hage et al., *Design and use of the Simple Event Model (SEM)*, Journal of Web Semantics, 2011. DOI: [10.1016/j.websem.2011.03.003](https://doi.org/10.1016/j.websem.2011.03.003).
- Pustejovsky et al., *TimeML: Robust Specification of Event and Temporal Expressions in Text*, 2003. ACL Anthology: [2003.iwpt-1.13](https://aclanthology.org/2003.iwpt-1.13/).
- Shaw, Troncy, Hardman, *LODE: Linking Open Descriptions of Events*, 2009. CEUR-WS: [Vol-420](https://ceur-ws.org/Vol-420/).

### 数字人文方法

- Jennifer Edmond et al., *The Trouble with Big Data: How Datafication Displaces Cultural Practices*, 2023.
- Claire Warwick, Melissa Terras, Julianne Nyhan, *Digital Humanities in Practice*, 2012.
- Tim Hitchcock, *Big Data for Dead People: Digital Readings and the Conundrums of Positivism*, 2013.

## 4. 工具选用原则

- 优先开源、可自托管、可导出标准格式的工具。
- 不依赖单一 SaaS，数据必须能导出为 JSON、CSV 或 TEI。
- 时间线可视化只是发布层，不能替代来源与证据治理。
- 新工具进入项目前，先验证导出格式、许可证和维护活跃度。

## 5. 2026-08 调研结论：分层技术栈推荐

### 结论

没有单一“最成熟”工具能同时承担采集、治理、模型、可视化和长期保存。对 Human Infra 永生史年表最成熟有效的方案是**分层技术栈**：把机器可读数据、标准引用、审查状态和发布层分离，让可视化工具可以被替换而不损失数据。

### 最终推荐

```text
Zotero / Tropy 采集来源
  -> OpenRefine 清洗与对齐
  -> Git + JSON Schema 年表数据（机器真相源）
  -> EDTF 日期；PeriodO/Wikidata/CIDOC-CRM 时期与事件本体
  -> TimelineJS 叙事时间线 / D3 定制研究可视化
  -> Omeka S / Neatline 仅在需要空间档案展览时引入
  -> Git 版本、复核状态、CI 门禁长期保存
```

### 候选工具成熟度核对

| 工具 | 定位 | 维护活跃度（2026-08 实测） | 数据可导出 | 本项目定位 |
| --- | --- | --- | --- | --- |
| Zotero | 文献与引用管理 | 活跃 | BibTeX/CSV/RDF | 来源采集层 |
| Tropy | 档案照片与手稿管理 | 活跃 | 本地数据库/JSON | 档案采集层 |
| OpenRefine | 数据清洗与实体对齐 | 活跃 | JSON/CSV/RDF | 数据清洗层 |
| Git + JSON Schema | 版本化机器真相源 | 活跃 | 原格式/CI | 核心数据层 |
| EDTF | 不确定日期标准 | 开放标准 | ISO/文本 | 日期契约层 |
| PeriodO | 历史时期 gazetteer | 活跃，`periodo/periodo-client` 最近提交 2026-08-05，CC0 | JSON/CSV/Turtle | 时期参照层 |
| CIDOC-CRM | 事件/人物/地点/来源本体 | 开放标准 | RDF | 事件关系层 |
| TimelineJS | 叙事时间线 | 活跃 | JSON/Google Sheets | 默认发布层 |
| D3.js | 定制交互可视化 | 活跃 | JSON/网页 | 高级分析层 |
| Omeka S | 数字馆藏与展览平台 | 活跃 | RDF/CSV | 可选馆藏层 |
| Neatline | 地图+时间线档案叙事 | 经典版有存量，Neatline S 维护较弱 | Omeka 内部 | 仅空间展览时评估 |
| Wikibase | 自托管知识图谱 | 活跃 | RDF/JSON | 实体关系长大后可选 |
| Heurist | 数字人文数据库 | 活跃 | 数据库/导出 | 备选，不优先 |
| Recogito2 | 文本实体标注 | 不活跃（约 2023-01 后停滞） | 导出 | 暂不引入 |

### 为什么这样最有效

1. 数据先于工具：Git + JSON Schema 保证任何可视化工具失效后，年表仍可复核、回滚和迁移。
2. 标准先于自定义：EDTF 解决不确定日期，PeriodO/CIDOC-CRM 解决时期和事件语义，避免私人字段取代公共标准。
3. 来源与发布分离：TimelineJS/D3 只消费已复核数据，不承载证据判断。
4. 维护风险可隔离：Neatline S 和 Recogito2 维护弱，不进入核心链路；Wikibase 等重量级工具等数据规模真实增长后再评估。

### 指导文献

- TimelineJS3 官方仓库与 JSON 格式：<https://github.com/NUKnightLab/TimelineJS3>
- PeriodO 技术概览：<https://perio.do/technical-overview/>
- PeriodO 官方客户端：<https://github.com/periodo/periodo-client>
- Wikibase 官方入口：<https://wikiba.se/>
- Neatline 官方入口：<https://www.neatline.org/>
- EDTF 规范：<https://www.loc.gov/standards/datetime/>
- CIDOC-CRM：<https://www.cidoc-crm.org/>
