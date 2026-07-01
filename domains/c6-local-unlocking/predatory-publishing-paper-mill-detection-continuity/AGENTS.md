# predatory-publishing-paper-mill-detection-continuity 目录说明

本目录负责掠夺性出版、paper mill 和系统性出版操控信号的证据防火墙。

## 结构

```text
predatory-publishing-paper-mill-detection-continuity/
├── AGENTS.md
└── README.md
```

## 边界

- 只维护筛查信号、证据污染风险、出版透明度和模型过滤边界。
- 上游：`domains/c4-conversion-channel/trustworthy-scientific-communication-peer-review/`、`domains/c4-conversion-channel/research-misconduct-investigation-correction-continuity/`。
- 下游：系统综述筛选、Source Card、证据等级和活证据更新。
- 不提供论文买卖、伪造审稿、检测规避、引用操控、图片伪造或指控代写。

## 维护规则

使用 COPE、Think Check Submit、DOAJ、STM Integrity Hub 和 Retraction Watch 作为锚点。异常信号只能触发降级、复核或不可评价，不得自动形成不端结论。
