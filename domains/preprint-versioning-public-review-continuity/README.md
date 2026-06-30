# Preprint Versioning Public Review Continuity

`preprint-versioning-public-review-continuity/` 研究预印本、版本链、公开评论、后续期刊版本和公共审查如何影响早期技术信号进入 Human Infra。

> 核心问题：预印本能加速知识扩散，也能把未审查、后续大改或被撤回的结论提前推入模型与传播材料。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要尽早识别未来技术窗口
  -> 很多前沿信号先以预印本、公开评论和社区审查出现
  -> 预印本状态、版本差异和后续发表状态决定信号可用等级
  -> 因此预印本版本与公开评审连续性是早期证据接入门槛
```

## 关注对象

- Preprint、version history、withdrawal、journal version、public review、commentary、post-publication peer review 和 overlay review。
- medRxiv、bioRxiv、arXiv、OSF Preprints、PubPeer、PREreview、eLife reviewed preprints 等信号类型。
- 与 `technology-foresight-horizon-scanning/` 的边界：技术预见域发现弱信号；本域判断预印本弱信号的审查状态和版本稳定性。
- 与 `trustworthy-scientific-communication-peer-review/` 的边界：可信传播域是总入口；本域聚焦预印本生命周期。

## Human Infra 模型链路

```text
预印本版本与公开评审 T
  -> 改变 review_status、version_delta、public_comment_signal、journal_linkage 变量 X
  -> 改变早期证据在 Source Card、雷达和模型中的等级 S
  -> 改变过早采用、错误传播、错过早期窗口和版本漂移风险 λ(t)
  -> 影响技术预见、研究组合和主体持续性路径选择
```

## 非目标

- 不提供论文代写、预印本刷评、评论操控、同行评审伪造、抢发策略或平台规避。
- 不把预印本写成已验证临床结论，也不因未同行评审而自动排除。
- 不抓取非公开审稿材料或平台后台数据。

## Source Signals

- ASAPbio preprint resources: https://asapbio.org/preprints
- medRxiv policies: https://www.medrxiv.org/content/about-medrxiv
- bioRxiv about: https://www.biorxiv.org/about-biorxiv
- PubPeer: https://pubpeer.com/
- PREreview: https://prereview.org/

## 下一步

- 给 Source Card 增加 `preprint_server`、`version_number`、`public_review_status`、`journal_version_link` 和 `version_delta_note` 字段。
- 在技术雷达中区分 “preprint signal” 与 “peer-reviewed evidence”。
