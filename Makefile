.PHONY: check structure claim-matrix-audit maturity-gap-audit page-claim-audit paper-claim-audit domain-falsifier-audit domain-claim-matrix-audit domain-field-extraction-audit domain-source-queue-audit domain-source-extraction-audit domain-source-promotion-audit falsifier-source-audit falsifier-source-extraction-audit py-compile clean

check:
	$(MAKE) clean
	$(MAKE) structure
	$(MAKE) claim-matrix-audit
	$(MAKE) maturity-gap-audit
	$(MAKE) page-claim-audit
	$(MAKE) paper-claim-audit
	$(MAKE) domain-falsifier-audit
	$(MAKE) domain-claim-matrix-audit
	$(MAKE) domain-field-extraction-audit
	$(MAKE) domain-source-queue-audit
	$(MAKE) domain-source-extraction-audit
	$(MAKE) domain-source-promotion-audit
	$(MAKE) falsifier-source-audit
	$(MAKE) falsifier-source-extraction-audit
	$(MAKE) py-compile
	$(MAKE) clean
	$(MAKE) structure

structure:
	python3 tools/check_repository.py

claim-matrix-audit:
	python3 tools/audit_core_claim_evidence_matrix.py

maturity-gap-audit:
	python3 tools/audit_human_infra_maturity_gap_register.py

page-claim-audit:
	python3 tools/audit_human_infra_page_claim_consistency.py

paper-claim-audit:
	python3 tools/audit_human_infra_paper_claim_register.py

domain-falsifier-audit:
	python3 tools/audit_human_infra_domain_falsifier_coverage.py

domain-claim-matrix-audit:
	python3 tools/audit_human_infra_domain_claim_evidence_matrix.py

domain-field-extraction-audit:
	python3 tools/audit_human_infra_domain_source_card_field_extraction.py

domain-source-queue-audit:
	python3 tools/audit_human_infra_domain_source_specific_extraction_queue.py

domain-source-extraction-audit:
	python3 tools/audit_human_infra_domain_source_specific_extraction_register.py

domain-source-promotion-audit:
	python3 tools/audit_human_infra_domain_source_card_promotion_queue.py

falsifier-source-audit:
	python3 tools/audit_human_infra_falsifier_source_card_backfill.py

falsifier-source-extraction-audit:
	python3 tools/audit_human_infra_falsifier_source_card_extraction.py

py-compile:
	python3 -m py_compile \
		tools/audit_core_claim_evidence_matrix.py \
		tools/audit_human_infra_maturity_gap_register.py \
		tools/audit_human_infra_page_claim_consistency.py \
		tools/audit_human_infra_paper_claim_register.py \
		tools/audit_human_infra_domain_falsifier_coverage.py \
		tools/audit_human_infra_domain_claim_evidence_matrix.py \
		tools/audit_human_infra_domain_source_card_field_extraction.py \
		tools/audit_human_infra_domain_source_specific_extraction_queue.py \
		tools/audit_human_infra_domain_source_specific_extraction_register.py \
		tools/audit_human_infra_domain_source_card_promotion_queue.py \
		tools/audit_human_infra_falsifier_source_card_backfill.py \
		tools/audit_human_infra_falsifier_source_card_extraction.py \
		tools/arxiv_html_paper_tool.py \
		tools/check_repository.py \
		tools/update_domain_doc_contracts.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_toy_model.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_sensitivity_analysis.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_disclosure_outputs.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_survey_design_plan.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_missingness_route_map.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_route_field_discovery.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_value_label_protocol.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/audit_life_path_toy_model.py

clean:
	find . -type d \( -name __pycache__ -o -name .pytest_cache \) -prune -exec rm -rf {} +
