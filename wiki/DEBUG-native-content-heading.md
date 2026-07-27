# MediaWiki 词条正文重复原生页面标题

## Bug

部分种子词条以 `= 页面标题 =` 开始。MediaWiki/Vector 已在页面外壳中生成原生
页面 `H1`，正文再次生成同名 `H1`，造成重复标题层级、目录语义和机器解析歧义。

## Environment

- MediaWiki 1.46
- Vector 2022
- 种子内容：`wiki/content/*.wiki`
- 静态公开快照：`https://human-infra-wiki.pages.dev/`

## Reproduction

1. 扫描所有受治理 `.wiki` 种子文件的全部正文行。
2. 将匹配 `= 非等号内容 =` 的行判为越权声明页面一级标题。
3. 修复前扫描返回 `verdict=FAIL count=50`。
4. 浏览器抽检“证据地图与支持边界”，可见原生页名和正文各生成一个同名 `H1`。

结构化回归证据：`REGRESSION_EVIDENCE-native-content-heading.json`。

## Hypotheses

### H1: Vector 页面外壳未生成页面标题

- Conflicts：导出 HTML 中存在 `h1#firstHeading.mw-first-heading`。
- Status：rejected。

### H2: 重复标题由静态导出器注入

- Conflicts：本地动态 MediaWiki 与受治理 Wikitext 都包含第二个同名 `H1`。
- Status：rejected。

### H3: 种子正文错误复制了 MediaWiki 已拥有的页面标题

- Supports：50 个源文件的首个非空行使用一级 Wikitext 标题；移除该行后正文只保留
  Vector 原生页面标题。
- Status：confirmed（ROOT HYPOTHESIS）。

## Root Cause

早期批量词条把 Markdown 式“正文自带标题”习惯迁移到 Wikitext，忽略了
MediaWiki 页面标题属于皮肤外壳所有，导致内容层重复声明 `H1`。

## Fix

- 删除 50 个受治理种子页面首部的重复一级标题。
- 在 `CONTENT-STANDARD.md` 与 `AGENTS.md` 固化页面标题所有权。
- 在 `validate-source.sh` 增加全部正文行的一级标题门禁。

## Repair Boundary

- `wiki/content/` 中命中的 50 个种子词条
- `wiki/scripts/validate-source.sh`
- Wiki 内容标准、目录记忆和本调试记录

## Frozen Nodes

- MediaWiki、Vector、ResourceLoader 源码
- 中文维基百科首页上游快照、模板和视觉结构
- 与 Wiki 无关的并行工作区改动

## Reverification Required

- [x] 未修复源文件扫描 RED
- [x] 修复后 `make validate` GREEN
- [x] 人工恢复一个重复标题时门禁反事实失败
- [x] 导入后动态页面只保留一个原生 `h1#firstHeading`
- [x] Pages 重建与静态运行时审计通过

## Audit Case Sampling

- Decision：`no-case`
- Reason：根因已固化为内容标准、模块记忆和确定性源级 Gate；项目没有
  `governance/evidence/audit-cases/`，不另建重复真相源。
