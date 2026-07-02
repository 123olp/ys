# Tools

`tools/` contains repository maintenance scripts. These scripts support the knowledge base itself; they are not product code.

## Current Tools

- `arxiv_html_paper_tool.py`: installs, verifies, and scaffolds the reusable arXiv HTML papers reader framework for Astro projects.
- `audit_core_claim_evidence_matrix.py`: verifies that the core Human Infra Claim-Evidence Matrix keeps required source anchors, claim IDs, evidence gates, prohibited-use boundaries, method URLs, and index links.
- `audit_human_infra_maturity_gap_register.py`: verifies that the 100% maturity gap register keeps value, research-framework, and quantitative-model gates aligned with the maturity roadmap, local evidence paths, and blocked-state boundaries.
- `audit_human_infra_page_claim_consistency.py`: verifies that major README, Web and paper pages keep required Human Infra Claim IDs, claim-spine labels and prohibited-use boundary phrases from `docs/reference/human-infra-page-claim-consistency.json`.
- `audit_human_infra_paper_claim_register.py`: verifies that every arXiv-style paper page has paper-specific strong claims, core Claim IDs, falsifiers, downgrade actions, registered source data paths and prohibited-use boundaries from `docs/reference/human-infra-paper-claim-register.json`.
- `audit_human_infra_domain_falsifier_coverage.py`: verifies that C1 and the current 20 priority C2 research domains keep falsifier, downgrade-condition, variable-interface and prohibited-use scaffolding from `docs/reference/human-infra-domain-falsifier-coverage.json`.
- `audit_human_infra_domain_claim_evidence_matrix.py`: verifies that the current 26 priority research domains are joined to domain claims, variable-contract sources, falsifier sources and extracted Source Card IDs from `docs/reference/human-infra-domain-claim-evidence-matrix.json`.
- `audit_human_infra_domain_source_card_field_extraction.py`: verifies that each current domain matrix seed row has endpoint candidates, source IDs, population-boundary slots, uncertainty-channel slots, transfer-boundary slots and next field-extraction actions from `docs/reference/human-infra-domain-source-card-field-extraction.json`.
- `audit_human_infra_domain_source_specific_extraction_queue.py`: verifies that the 26 domain field rows derive into 81 domain-source reading tasks over 20 source anchors from `docs/reference/human-infra-domain-source-specific-extraction-queue.json`, while keeping calibrated modeling blocked until exact claim, endpoint, population, uncertainty and transfer-boundary fields are extracted.
- `audit_human_infra_domain_source_specific_extraction_register.py`: verifies the completed 81/81 domain-source extraction rows from `docs/reference/human-infra-domain-source-specific-extraction-register.json`, including source-role decisions, endpoint binding, blocked uses and index links.
- `audit_human_infra_domain_source_card_promotion_queue.py`: verifies that the 81 completed domain-source field rows derive into fresh-review, Source Card, variable-card, endpoint-card, uncertainty-card, transfer-boundary-card and downgrade-check promotion tasks from `docs/reference/human-infra-domain-source-card-promotion-queue.json`, while keeping model admission blocked.
- `audit_human_infra_source_context_local_review_register.py`: verifies that all 20 locally reviewed source anchors match the promotion queue, source evidence, affected tasks, blocked uses and index links from `docs/reference/human-infra-source-context-local-review-register.json`.
- `audit_human_infra_card_promotion_prep_register.py`: verifies that the 81 locally reviewed promotion tasks have prepared Source/variable/endpoint/uncertainty/transfer/downgrade artifact IDs, reviewer questions, blocked uses and index links from `docs/reference/human-infra-card-promotion-prep-register.json`, while keeping independent fresh review and model admission blocked.
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
python3 tools/audit_human_infra_paper_claim_register.py
python3 tools/audit_human_infra_domain_falsifier_coverage.py
python3 tools/audit_human_infra_domain_claim_evidence_matrix.py
python3 tools/audit_human_infra_domain_source_card_field_extraction.py
python3 tools/audit_human_infra_domain_source_specific_extraction_queue.py
python3 tools/audit_human_infra_domain_source_specific_extraction_register.py
python3 tools/audit_human_infra_domain_source_card_promotion_queue.py
python3 tools/audit_human_infra_source_context_local_review_register.py
python3 tools/audit_human_infra_falsifier_source_card_backfill.py
python3 tools/audit_human_infra_falsifier_source_card_extraction.py
python3 tools/update_domain_doc_contracts.py
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
make claim-matrix-audit
make maturity-gap-audit
make page-claim-audit
make paper-claim-audit
make domain-falsifier-audit
make domain-claim-matrix-audit
make domain-field-extraction-audit
make domain-source-queue-audit
make domain-source-extraction-audit
make domain-source-promotion-audit
make source-context-local-review-audit
make falsifier-source-audit
make falsifier-source-extraction-audit
make check
make clean
```
