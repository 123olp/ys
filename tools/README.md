# Tools

`tools/` contains repository maintenance scripts. These scripts support the knowledge base itself; they are not product code.

## Current Tools

- `arxiv_html_paper_tool.py`: installs, verifies, and scaffolds the reusable arXiv HTML papers reader framework for Astro projects.
- `audit_core_claim_evidence_matrix.py`: verifies that the core Human Infra Claim-Evidence Matrix keeps required source anchors, claim IDs, evidence gates, prohibited-use boundaries, method URLs, and index links.
- `audit_human_infra_maturity_gap_register.py`: verifies that the 100% maturity gap register keeps value, research-framework, and quantitative-model gates aligned with the maturity roadmap, local evidence paths, and blocked-state boundaries.
- `audit_human_infra_page_claim_consistency.py`: verifies that major README, Web and paper pages keep required Human Infra Claim IDs, claim-spine labels and prohibited-use boundary phrases from `docs/reference/human-infra-page-claim-consistency.json`.
- `audit_human_infra_audience_claim_map.py`: verifies that value clarity has audience-specific Claim ID entry points and adjacent-project boundary distinctions from `docs/reference/human-infra-audience-claim-map.json`.
- `audit_human_infra_paper_claim_register.py`: verifies that every arXiv-style paper page has paper-specific strong claims, core Claim IDs, falsifiers, downgrade actions, registered source data paths and prohibited-use boundaries from `docs/reference/human-infra-paper-claim-register.json`.
- `audit_human_infra_domain_falsifier_coverage.py`: verifies that C1 and the current 20 priority C2 research domains keep falsifier, downgrade-condition, variable-interface and prohibited-use scaffolding from `docs/reference/human-infra-domain-falsifier-coverage.json`.
- `audit_human_infra_domain_claim_evidence_matrix.py`: verifies that the current 26 priority research domains are joined to domain claims, variable-contract sources, falsifier sources and extracted Source Card IDs from `docs/reference/human-infra-domain-claim-evidence-matrix.json`.
- `audit_human_infra_domain_source_card_field_extraction.py`: verifies that each current domain matrix seed row has endpoint candidates, source IDs, population-boundary slots, uncertainty-channel slots, transfer-boundary slots and next field-extraction actions from `docs/reference/human-infra-domain-source-card-field-extraction.json`.
- `audit_human_infra_c2_longtail_coverage_register.py`: verifies that `docs/reference/human-infra-c2-longtail-coverage-register.json` covers every C2 source-maintenance domain from `classification.tsv`, distinguishes 20 reviewed priority domains from 184 long-tail uncovered domains, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-promotion-queue.json` selects the first high-impact C2 long-tail domains, keeps them tied to the coverage register, requires candidate sources and promotion steps, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-source-extraction-queue.json` derives the first-batch promotion queue into 48 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_first_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-source-extraction-register.json` completes all 48/48 C2 long-tail first-batch source-context extraction rows with required fields, downgrade triggers, blocked uses and index links.
- `audit_human_infra_c2_longtail_first_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-local-review-register.json` locally reviews all 48/48 C2-LT-B1 extraction rows, maps them back to queue/register evidence, preserves blocked uses, and routes only to independent fresh review.
- `audit_human_infra_c2_longtail_first_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-independent-fresh-review-protocol.json` covers all 48 locally reviewed C2-LT-B1 rows in four review batches without embedding verdicts.
- `audit_human_infra_c2_longtail_first_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json` records 48/48 bounded fresh-review verdicts and keeps reviewed artifact promotion plus model admission controlled.
- `audit_human_infra_c2_longtail_first_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json` promotes exactly the 42 eligible C2-LT-B1 verdict rows into 252 reviewed artifacts, preserves 6 blocked rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_blocked_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json` covers exactly the 6 non-eligible C2-LT-B1 rows with source-resolution candidates while keeping artifact promotion and model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_source_resolution_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json` fresh-reviews the 6 source-resolution rows, allows only corrected source re-extraction, and keeps direct artifact fill plus model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json` derives exactly the selected corrected source candidates into re-extraction tasks while keeping route-only candidates, artifact promotion and model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json` covers all 10 corrected re-extraction tasks with required source identity, endpoint, uncertainty, transfer boundary, downgrade and model-position fields while preserving route/index/fulltext blocking and model-admission boundaries.
- `audit_human_infra_c2_longtail_first_batch_corrected_source_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json` fresh-reviews all 10 corrected extraction outputs, allows only 5 bounded artifact-prep rows, preserves 5 lineage/route/index/fulltext blocked rows and keeps model admission blocked.
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json` promotes exactly the 5 eligible corrected rows into 30 bounded reviewed artifacts, preserves 5 blocked corrected rows, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_second_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-promotion-queue.json` selects 12 non-B1 C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_second_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-source-extraction-queue.json` derives the second-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_second_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-source-extraction-register.json` completes all 24/24 C2 long-tail second-batch source-context extraction rows with required fields, downgrade triggers, blocked uses and index links.
- `audit_human_infra_c2_longtail_second_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-local-review-register.json` locally reviews all 24/24 C2-LT-B2 extraction rows, maps them back to queue/register evidence, preserves blocked uses, and routes only to independent fresh review.
- `audit_human_infra_c2_longtail_second_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json` covers all 24 locally reviewed C2-LT-B2 rows in two review batches without embedding verdicts.
- `audit_human_infra_c2_longtail_second_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-independent-fresh-review-verdict-register.json` fresh-reviews all 24 C2-LT-B2 rows, allows only 23 bounded artifact-fill rows, preserves 1 downgrade-before-fill row and keeps model admission blocked.
- `audit_human_infra_c2_longtail_second_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-second-batch-reviewed-card-artifact-register.json` promotes exactly the 23 eligible C2-LT-B2 rows into 138 bounded reviewed artifacts, preserves 1 downgrade-before-fill row, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_promotion_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-promotion-queue.json` selects 12 non-B1/B2 neuro-sensory-cognitive C2 long-tail domains, binds 24 web-checked candidate sources, preserves required promotion steps and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_source_extraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-source-extraction-queue.json` derives the third-batch promotion queue into 24 domain-source extraction tasks with required slots, questions, blocked uses, index links and model-admission boundaries.
- `audit_human_infra_c2_longtail_third_batch_source_extraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-source-extraction-register.json` completes all 24/24 C2-LT-B3 source-context extraction rows with required fields, downgrade triggers, blocked uses, source-resolution flags and index links.
- `audit_human_infra_c2_longtail_third_batch_local_review_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-local-review-register.json` locally reviews all 24/24 C2-LT-B3 extraction rows, preserves five source-resolution/manual-access issue rows, keeps blocked uses complete, and routes only to independent fresh review or source resolution.
- `audit_human_infra_c2_longtail_third_batch_source_resolution_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-source-resolution-register.json` covers the five C2-LT-B3 local-review issue rows, prepares seven corrected/split/route-normalized candidates, preserves blocked uses and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_independent_fresh_review_protocol.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-protocol.json` splits the 24 locally reviewed C2-LT-B3 rows into two fresh-review batches, includes the five source-resolution issue rows, and keeps verdicts, reviewed artifacts and model admission outside the protocol.
- `audit_human_infra_c2_longtail_third_batch_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json` completes 24/24 C2-LT-B3 fresh-review verdicts, routes five issue rows to corrected-source re-extraction, keeps one row downgrade-before-fill, and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_queue.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-reextraction-queue.json` derives seven corrected/split/route-normalized source candidates from the five C2-LT-B3 source-resolution-supported issue rows while keeping artifact promotion and model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-reextraction-register.json` completes all seven C2-LT-B3 corrected re-extraction tasks with required source identity, endpoint, uncertainty, transfer-boundary, downgrade and model-position fields while preserving route/split blocking and model-admission boundaries.
- `audit_human_infra_c2_longtail_third_batch_corrected_source_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-fresh-review-verdict-register.json` fresh-reviews all seven C2-LT-B3 corrected extraction outputs, allows only six bounded artifact-prep rows, preserves one duplicate/split route blocked row, records the AAO-HNS publisher-route access update and keeps model admission blocked.
- `audit_human_infra_c2_longtail_third_batch_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json` promotes 18 original eligible rows and 6 corrected eligible rows into 144 bounded reviewed artifacts, preserves EXT-022 downgrade-before-fill and C2LTB3-CREXT-004 duplicate/split route blocking, and keeps model admission blocked.
- `audit_human_infra_domain_source_specific_extraction_queue.py`: verifies that the 26 domain field rows derive into 81 domain-source reading tasks over 20 source anchors from `docs/reference/human-infra-domain-source-specific-extraction-queue.json`, while keeping calibrated modeling blocked until exact claim, endpoint, population, uncertainty and transfer-boundary fields are extracted.
- `audit_human_infra_domain_source_specific_extraction_register.py`: verifies the completed 81/81 domain-source extraction rows from `docs/reference/human-infra-domain-source-specific-extraction-register.json`, including source-role decisions, endpoint binding, blocked uses and index links.
- `audit_human_infra_domain_source_card_promotion_queue.py`: verifies that the 81 completed domain-source field rows derive into fresh-review, Source Card, variable-card, endpoint-card, uncertainty-card, transfer-boundary-card and downgrade-check promotion tasks from `docs/reference/human-infra-domain-source-card-promotion-queue.json`, while keeping model admission blocked.
- `audit_human_infra_source_context_local_review_register.py`: verifies that all 20 locally reviewed source anchors match the promotion queue, source evidence, affected tasks, blocked uses and index links from `docs/reference/human-infra-source-context-local-review-register.json`.
- `audit_human_infra_card_promotion_prep_register.py`: verifies that the 81 locally reviewed promotion tasks have prepared Source/variable/endpoint/uncertainty/transfer/downgrade artifact IDs, reviewer questions, blocked uses and index links from `docs/reference/human-infra-card-promotion-prep-register.json`, while keeping independent fresh review and model admission blocked.
- `audit_human_infra_independent_fresh_review_protocol.py`: verifies that the independent fresh-review protocol in `docs/reference/human-infra-independent-fresh-review-protocol.json` batches the 81 prepared artifact packs, matches prep-register source counts, preserves verdict taxonomy and keeps verdicts outside the protocol artifact.
- `audit_human_infra_independent_fresh_review_verdict_register.py`: verifies that `docs/reference/human-infra-independent-fresh-review-verdict-register.json` records cumulative independent fresh-review verdict batches over reviewed source anchors and promotion packets, while preserving blocked uses, source-role boundaries and index links.
- `audit_human_infra_reviewed_card_artifact_register.py`: verifies that `docs/reference/human-infra-reviewed-card-artifact-register.json` promotes all 81 fresh-reviewed promotion packets into 486 reviewed Source/variable/endpoint/uncertainty/transfer-boundary/downgrade artifact entities while keeping model admission and individual-use claims blocked.
- `audit_human_infra_future_boundary_route_card_register.py`: verifies that `docs/reference/human-infra-future-boundary-route-card-register.json` covers future waiting, biological stasis, neuro-identity continuity and AI-enabled acceleration route cards with required gate dimensions, abort gates and blocked model admission.
- `audit_human_infra_falsifier_source_card_backfill.py`: verifies that current paper strong claims and C1/C2 priority-domain falsifier rows have Source Card anchor backfill, evidence roles, supported-use boundaries and transfer boundaries from `docs/reference/human-infra-falsifier-source-card-backfill.json`.
- `audit_human_infra_falsifier_source_card_extraction.py`: verifies that all current source anchors from `docs/reference/human-infra-falsifier-source-card-extraction.json` map to exact source identity, Human Infra domains, paper claims, model positions, transfer boundaries and the human-readable source-note pack.
- `check_repository.py`: verifies required files, required directories, temporary filename cleanup, Python cache cleanup, and local Markdown links.
- `update_domain_doc_contracts.py`: regenerates standard README/AGENTS metadata, research-skeleton, maintenance-contract, and agent-workflow blocks for every formal research domain from the possibility-space classification table.

Reusable tool package:

- `arxiv-html-paper/`: templates, consumer contract, governance docs, and usage notes for the arXiv HTML papers reuse kit.

Key arXiv reuse documents:

- [arxiv-html-paper/CONTRACT.md](arxiv-html-paper/CONTRACT.md): stable consumption contract.
- [arxiv-html-paper/CONSUMER_GUIDE.md](arxiv-html-paper/CONSUMER_GUIDE.md): guide for other projects.
- [arxiv-html-paper/GOVERNANCE.md](arxiv-html-paper/GOVERNANCE.md): maintenance and compatibility governance.
- [arxiv-html-paper/MAINTENANCE.md](arxiv-html-paper/MAINTENANCE.md): operational runbook.

## Commands

From the repository root:

```bash
python3 tools/check_repository.py
python3 tools/audit_core_claim_evidence_matrix.py
python3 tools/audit_human_infra_maturity_gap_register.py
python3 tools/audit_human_infra_page_claim_consistency.py
python3 tools/audit_human_infra_audience_claim_map.py
python3 tools/audit_human_infra_paper_claim_register.py
python3 tools/audit_human_infra_domain_falsifier_coverage.py
python3 tools/audit_human_infra_domain_claim_evidence_matrix.py
python3 tools/audit_human_infra_domain_source_card_field_extraction.py
python3 tools/audit_human_infra_c2_longtail_coverage_register.py
python3 tools/audit_human_infra_c2_longtail_first_batch_promotion_queue.py
python3 tools/audit_human_infra_c2_longtail_first_batch_source_extraction_queue.py
python3 tools/audit_human_infra_c2_longtail_first_batch_source_extraction_register.py
python3 tools/audit_human_infra_c2_longtail_first_batch_local_review_register.py
python3 tools/audit_human_infra_c2_longtail_first_batch_independent_fresh_review_protocol.py
python3 tools/audit_human_infra_c2_longtail_first_batch_independent_fresh_review_verdict_register.py
python3 tools/audit_human_infra_c2_longtail_first_batch_reviewed_card_artifact_register.py
python3 tools/audit_human_infra_domain_source_specific_extraction_queue.py
python3 tools/audit_human_infra_domain_source_specific_extraction_register.py
python3 tools/audit_human_infra_domain_source_card_promotion_queue.py
python3 tools/audit_human_infra_source_context_local_review_register.py
python3 tools/audit_human_infra_card_promotion_prep_register.py
python3 tools/audit_human_infra_independent_fresh_review_protocol.py
python3 tools/audit_human_infra_independent_fresh_review_verdict_register.py
python3 tools/audit_human_infra_falsifier_source_card_backfill.py
python3 tools/audit_human_infra_falsifier_source_card_extraction.py
python3 tools/update_domain_doc_contracts.py
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
make claim-matrix-audit
make maturity-gap-audit
make page-claim-audit
make audience-claim-map-audit
make paper-claim-audit
make domain-falsifier-audit
make domain-claim-matrix-audit
make domain-field-extraction-audit
make c2-longtail-coverage-audit
make c2-longtail-first-batch-promotion-audit
make c2-longtail-first-batch-source-extraction-audit
make c2-longtail-first-batch-source-extraction-register-audit
make c2-longtail-first-batch-local-review-audit
make c2-longtail-first-batch-independent-fresh-review-protocol-audit
make c2-longtail-first-batch-independent-fresh-review-verdict-audit
make c2-longtail-first-batch-reviewed-card-artifact-audit
make c2-longtail-first-batch-blocked-source-resolution-audit
make c2-longtail-first-batch-source-resolution-fresh-review-verdict-audit
make c2-longtail-first-batch-corrected-source-reextraction-queue-audit
make c2-longtail-first-batch-corrected-source-reextraction-register-audit
make c2-longtail-first-batch-corrected-source-fresh-review-verdict-audit
make c2-longtail-first-batch-corrected-source-reviewed-card-artifact-audit
make c2-longtail-second-batch-promotion-audit
make c2-longtail-second-batch-source-extraction-audit
make c2-longtail-second-batch-source-extraction-register-audit
make c2-longtail-second-batch-local-review-audit
make c2-longtail-second-batch-independent-fresh-review-protocol-audit
make c2-longtail-second-batch-independent-fresh-review-verdict-audit
make c2-longtail-second-batch-reviewed-card-artifact-audit
make c2-longtail-third-batch-promotion-audit
make c2-longtail-third-batch-source-extraction-audit
make c2-longtail-third-batch-source-extraction-register-audit
make c2-longtail-third-batch-local-review-audit
make c2-longtail-third-batch-source-resolution-audit
make c2-longtail-third-batch-independent-fresh-review-protocol-audit
make c2-longtail-third-batch-independent-fresh-review-verdict-audit
make c2-longtail-third-batch-corrected-source-reextraction-queue-audit
make c2-longtail-third-batch-corrected-source-reextraction-register-audit
make c2-longtail-third-batch-corrected-source-fresh-review-verdict-audit
make c2-longtail-third-batch-reviewed-card-artifact-audit
make domain-source-queue-audit
make domain-source-extraction-audit
make domain-source-promotion-audit
make source-context-local-review-audit
make card-promotion-prep-audit
make independent-fresh-review-protocol-audit
make independent-fresh-review-verdict-audit
make falsifier-source-audit
make falsifier-source-extraction-audit
make check
make clean
```
