# Longevity Evidence

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/longevity-evidence` |
| 分级 | `C1` - 可能性边界改写层 |
| 控制轴 | 寿命边界 |
| 分级理由 | 直接承载延长寿命和长寿逃逸相关证据账本。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何直接改写主体持续性边界，例如寿命、死亡、时间差分、身份连续性或未来抵达能力？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


Longevity Evidence 承接原 Biocat，是 Human Infra 中负责健康寿命、长寿干预、公开证据、临床试验和安全风险的子域。

一句话定位：

> 用可追溯证据判断每一种长寿方法有没有证据、效果多大、风险在哪里。

## 项目边界

本子域做证据整理、数据结构化和信息服务，不做医疗诊断、个性化用药建议或治疗方案推荐。

首批对象聚焦：

- 干预方法：药物、补剂、运动、饮食、睡眠、检测与疗法。
- 证据材料：论文、综述、人体研究、动物实验、临床试验和公开数据库。
- 评估维度：证据等级、效果大小、适用对象、风险、不确定性和更新频率。

## 与 Human Infra 的关系

Longevity Evidence 属于 Human Infra 的 L0/L1 生存、安全与生理基础设施部分。它回答“哪些健康寿命干预有证据”，但不负责全部人类运行问题。

远期“去具身中枢生命系统”和“记忆编辑”不放在本子域内，因为它们不是普通健康干预证据页，而是独立高风险研究域。

## 目录

```text
longevity-evidence/
├── AGENTS.md
├── README.md
├── data/
│   ├── README.md
│   ├── manual/
│   └── processed/
├── docs/
│   ├── collection-run-2026-05-29-expanded.md
│   ├── collection-run-2026-05-29.md
│   ├── data-inventory.md
│   ├── data-sources.md
│   ├── evidence-model.md
│   ├── mvp-roadmap.md
│   └── product-brief.md
└── scripts/
    ├── README.md
    ├── collect_core_data.py
    └── collect_mvp_data.py
```

## MVP

第一版目标仍是可信的长寿证据账本：

1. 整理 20 个高关注长寿干预。
2. 为每个干预建立证据页。
3. 标注人体证据、动物证据、临床试验、安全风险和证据缺口。
4. 输出可复用的数据结构，后续接入展示页、订阅产品或研究报告。

## 运行示例

从仓库根目录运行：

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 10
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
```
