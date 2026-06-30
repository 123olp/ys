# 0082 - Add Seventy-Eighth Wave Research Correction Scientific Integrity Domains

## Status

Accepted

## Date

2026-07-01

## Context

Wave 77 added evidence synthesis and guideline translation domains. That solves the question “how do studies become reviews and guidance?”, but it does not fully solve the upstream question “how does the evidence system correct itself when publication, review, incentives or public translation fail?”

Human Infra depends on long-lived evidence memory. If retracted work, paper mill output, citation cascades, weak peer review, unreplicated claims, metric incentives or public overstatement enter the model unchecked, the project can mistake polluted evidence for future technology windows.

## Decision

Add nine research correction and scientific integrity domains:

- `research-misconduct-investigation-correction-continuity/`
- `retraction-expression-concern-correction-continuity/`
- `preprint-versioning-public-review-continuity/`
- `journal-editorial-policy-peer-review-integrity-continuity/`
- `predatory-publishing-paper-mill-detection-continuity/`
- `citation-network-claim-propagation-continuity/`
- `research-metrics-incentives-assessment-continuity/`
- `replication-reproducibility-many-labs-continuity/`
- `science-communication-evidence-translation-continuity/`

Each domain receives only `README.md` and `AGENTS.md` in this slice. No crawler, ranking service, accusation workflow or automated scientific truth scoring is added.

## Rationale

These domains satisfy the Research Domain Atlas rule:

```text
主体持续性模型需要证据
  -> 证据来自研究生态
  -> 研究生态会被不端、撤稿、审稿失灵、paper mill、引用传播、指标激励、不可复制和传播误读污染
  -> 污染证据会改变技术窗口判断、模型输入和行动优先级
  -> 因此科研纠错与科学完整性是主体持续性模型的上游必要条件
```

They are not reducible to `trustworthy-scientific-communication-peer-review/` because that domain is a general semantic filter, while these domains track independent failure modes and source systems.

## Non-goals

- Do not provide misconduct accusations, legal strategy, complaint drafting, data fabrication, p-hacking, publication manipulation or review evasion.
- Do not provide citation gaming, impact-factor optimization, paper mill support or predatory publishing tactics.
- Do not scrape restricted editorial, review or manuscript systems.
- Do not turn retraction, bias, failed replication or funding conflict into automatic moral judgment.
- Do not provide medical, investment, policy lobbying or individual action advice.

## Source Signals

- ORI research misconduct definition: https://ori.hhs.gov/definition-research-misconduct
- COPE Core Practices and Retraction Guidelines: https://publicationethics.org/
- ICMJE Recommendations: https://www.icmje.org/recommendations/
- Crossref Crossmark and Cited-by: https://www.crossref.org/
- Retraction Watch Database: https://retractiondatabase.org/
- ASAPbio preprint resources: https://asapbio.org/preprints
- Think. Check. Submit.: https://thinkchecksubmit.org/
- DORA: https://sfdora.org/
- Leiden Manifesto: https://www.leidenmanifesto.org/
- National Academies reproducibility and science communication reports: https://nap.nationalacademies.org/

## Consequences

- Human Infra can now model not only study synthesis but also research self-correction.
- Source Card and Web paper pages can later add publication state, correction state, preprint version, paper mill signal, citation support, metric pressure, replication status and communication boundary fields.
- Repository structure validation must include the new domain directories and decision document.
