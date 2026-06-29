# High-Risk Citation Context Review

Date: 2026-06-29T00:00:00.000Z
Input: `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json`
Output JSON: `web/src/data/effective-immortality-flywheel/HIGH_RISK_CITATION_CONTEXT_REVIEW.json`

## Summary

Verdict: `PASS_WITH_LIMITATIONS`

Reason: `high_risk_contexts_reviewed_with_source_boundaries`

All locally HIGH/BLOCKER citation contexts have a source-bounded local review and explicit boundary action. Fresh independent citation-context review remains required before formal submission.

This is a local source-bounded review of HIGH/BLOCKER citation contexts. It improves the local evidence chain but does not replace a fresh independent reviewer thread.

| Metric | Count |
| --- | ---: |
| High or blocker contexts | 1 |
| Reviewed contexts | 1 |
| Missing review contexts | 0 |

## Reviewed Contexts

| Context | Local verdict | Claims | References | Action |
| --- | --- | --- | ---: | --- |
| CTX2 | KEEP_WITH_BOUNDARY | CL1, CL2 | 3 | Keep the context only as T -> E measurement language; keep fresh reviewer review required before formal submission. |

## Missing Review Contexts

- None

## Context Details

### CTX2: Grossman Health Capital; WHO HALE; NICE QALY

- Risk tier: HIGH
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL1, CL2
- Used for: 把日历寿命转译为健康质量、有效时间和质量调整时间。
- Supports: T -> E 的测量语言和健康质量调整视角。
- Does not support: 不能完整定义主体连续性，也不能替代个体医学判断。
- Action: Keep the context only as T -> E measurement language; keep fresh reviewer review required before formal submission.

| Reference | Verification | Context support | Boundary | Action |
| --- | --- | --- | --- | --- |
| `grossman1972healthcapital` | METADATA_VERIFIED_FULL_TEXT_RESTRICTED | WEAK_FOR_CONTEXT_WITH_METADATA_ONLY | Do not let Grossman alone carry the claim that effective time includes agency, subject continuity, or future option value. | Keep as lineage source; fresh reviewer should inspect full text if a stronger health-capital claim is made. |
| `whohale7752` | OFFICIAL_PAGE_VERIFIED | SUPPORTS_HEALTH_ADJUSTED_TIME | HALE is population-health measurement language; it does not define subject continuity, individual medical advice, agency, or future option value. | Use for health-adjusted time only. |
| `niceEconomicEvaluation` | OFFICIAL_PAGE_VERIFIED | SUPPORTS_QALY_QUALITY_AND_LENGTH_LANGUAGE | QALY is a health-economic index with assumptions and valuation choices; it cannot fully represent dignity, identity continuity, agency, subjective time, or option space. | Use for quality-adjusted time only; keep extra Human Infra fields for agency and option value. |

#### `grossman1972healthcapital`: On the Concept of Health Capital and the Demand for Health

- Source role: Health capital lineage and economic-theory entry point.
- Inspected source(s): <https://api.crossref.org/works/10.1086/259880>; <https://ideas.repec.org/a/ucp/jpolec/v80y1972i2p223-55.html>; <https://EconPapers.repec.org/RePEc:ucp:jpolec:v:80:y:1972:i:2:p:223-55>
- Support judgment: WEAK_FOR_CONTEXT_WITH_METADATA_ONLY
- Evidence note: Crossref and RePEc verify the article metadata, DOI, Journal of Political Economy venue, year, and page range. The accessible metadata supports using the source as the health-capital lineage entry, but the local audit did not extract full-text passages because the available PDF is scanned/restricted.
- Boundary note: Do not let Grossman alone carry the claim that effective time includes agency, subject continuity, or future option value.
- Action: Keep as lineage source; fresh reviewer should inspect full text if a stronger health-capital claim is made.

#### `whohale7752`: Healthy life expectancy (HALE) metadata

- Source role: Official public-health metric for health-adjusted expected years.
- Inspected source(s): <https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752>
- Support judgment: SUPPORTS_HEALTH_ADJUSTED_TIME
- Evidence note: WHO defines HALE as the average years expected in full health and states that it captures fatal and non-fatal outcomes by adjusting life expectancy across health states.
- Boundary note: HALE is population-health measurement language; it does not define subject continuity, individual medical advice, agency, or future option value.
- Action: Use for health-adjusted time only.

#### `niceEconomicEvaluation`: Economic evaluation

- Source role: Policy evaluation language for QALYs and lifetime health effects.
- Inspected source(s): <https://www.nice.org.uk/process/pmg36/chapter/economic-evaluation-2>
- Support judgment: SUPPORTS_QALY_QUALITY_AND_LENGTH_LANGUAGE
- Evidence note: NICE states that health effects should be expressed in QALYs and explains that QALYs combine life expectancy with health-related quality of life within the model time horizon.
- Boundary note: QALY is a health-economic index with assumptions and valuation choices; it cannot fully represent dignity, identity continuity, agency, subjective time, or option space.
- Action: Use for quality-adjusted time only; keep extra Human Infra fields for agency and option value.


## Scope

This artifact checks the local highest-risk citation context against accessible source metadata and official/source pages. It records source-support boundaries and recommended prose actions. It does not claim that the whole paper has passed sentence-level citation-context review.
