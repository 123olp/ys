.PHONY: check structure claim-matrix-audit maturity-gap-audit model-admission-contract-audit public-mortality-anchor-audit page-claim-audit audience-claim-map-audit paper-claim-audit domain-falsifier-audit domain-claim-matrix-audit domain-field-extraction-audit c2-longtail-coverage-audit c2-longtail-first-batch-promotion-audit c2-longtail-first-batch-source-extraction-audit c2-longtail-first-batch-source-extraction-register-audit c2-longtail-first-batch-local-review-audit c2-longtail-first-batch-independent-fresh-review-protocol-audit c2-longtail-first-batch-independent-fresh-review-verdict-audit c2-longtail-first-batch-reviewed-card-artifact-audit c2-longtail-first-batch-blocked-source-resolution-audit c2-longtail-first-batch-source-resolution-fresh-review-verdict-audit c2-longtail-first-batch-corrected-source-reextraction-queue-audit c2-longtail-first-batch-corrected-source-reextraction-register-audit c2-longtail-first-batch-corrected-source-fresh-review-verdict-audit c2-longtail-first-batch-corrected-source-reviewed-card-artifact-audit c2-longtail-second-batch-promotion-audit c2-longtail-second-batch-source-extraction-audit c2-longtail-second-batch-source-extraction-register-audit c2-longtail-second-batch-local-review-audit c2-longtail-second-batch-independent-fresh-review-protocol-audit c2-longtail-second-batch-independent-fresh-review-verdict-audit c2-longtail-second-batch-reviewed-card-artifact-audit c2-longtail-third-batch-promotion-audit c2-longtail-third-batch-source-extraction-audit c2-longtail-third-batch-source-extraction-register-audit c2-longtail-third-batch-local-review-audit c2-longtail-third-batch-source-resolution-audit c2-longtail-third-batch-independent-fresh-review-protocol-audit c2-longtail-third-batch-independent-fresh-review-verdict-audit c2-longtail-third-batch-corrected-source-reextraction-queue-audit c2-longtail-third-batch-corrected-source-reextraction-register-audit c2-longtail-third-batch-corrected-source-fresh-review-verdict-audit c2-longtail-third-batch-reviewed-card-artifact-audit c2-longtail-fourth-batch-promotion-audit c2-longtail-fourth-batch-source-extraction-audit c2-longtail-fourth-batch-source-extraction-register-audit c2-longtail-fourth-batch-local-review-audit c2-longtail-fourth-batch-source-resolution-audit c2-longtail-fourth-batch-manual-fulltext-extraction-audit c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-audit c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-audit c2-longtail-fifth-batch-promotion-audit c2-longtail-fifth-batch-source-extraction-audit c2-longtail-fifth-batch-source-extraction-register-audit c2-longtail-fifth-batch-local-review-audit c2-longtail-fifth-batch-source-resolution-audit c2-longtail-fifth-batch-manual-fulltext-extraction-audit c2-longtail-fifth-batch-independent-fresh-review-verdict-audit c2-longtail-fifth-batch-reviewed-card-artifact-audit domain-source-queue-audit domain-source-extraction-audit domain-source-promotion-audit source-context-local-review-audit card-promotion-prep-audit independent-fresh-review-protocol-audit independent-fresh-review-verdict-audit reviewed-card-artifact-audit future-boundary-route-card-audit falsifier-source-audit falsifier-source-extraction-audit py-compile clean

check:
	$(MAKE) clean
	$(MAKE) structure
	$(MAKE) claim-matrix-audit
	$(MAKE) maturity-gap-audit
	$(MAKE) model-admission-contract-audit
	$(MAKE) public-mortality-anchor-audit
	$(MAKE) page-claim-audit
	$(MAKE) audience-claim-map-audit
	$(MAKE) paper-claim-audit
	$(MAKE) domain-falsifier-audit
	$(MAKE) domain-claim-matrix-audit
	$(MAKE) domain-field-extraction-audit
	$(MAKE) c2-longtail-coverage-audit
	$(MAKE) c2-longtail-first-batch-promotion-audit
	$(MAKE) c2-longtail-first-batch-source-extraction-audit
	$(MAKE) c2-longtail-first-batch-source-extraction-register-audit
	$(MAKE) c2-longtail-first-batch-local-review-audit
	$(MAKE) c2-longtail-first-batch-independent-fresh-review-protocol-audit
	$(MAKE) c2-longtail-first-batch-independent-fresh-review-verdict-audit
	$(MAKE) c2-longtail-first-batch-reviewed-card-artifact-audit
	$(MAKE) c2-longtail-first-batch-blocked-source-resolution-audit
	$(MAKE) c2-longtail-first-batch-source-resolution-fresh-review-verdict-audit
	$(MAKE) c2-longtail-first-batch-corrected-source-reextraction-queue-audit
	$(MAKE) c2-longtail-first-batch-corrected-source-reextraction-register-audit
	$(MAKE) c2-longtail-first-batch-corrected-source-fresh-review-verdict-audit
	$(MAKE) c2-longtail-first-batch-corrected-source-reviewed-card-artifact-audit
	$(MAKE) c2-longtail-second-batch-promotion-audit
	$(MAKE) c2-longtail-second-batch-source-extraction-audit
	$(MAKE) c2-longtail-second-batch-source-extraction-register-audit
	$(MAKE) c2-longtail-second-batch-local-review-audit
	$(MAKE) c2-longtail-second-batch-independent-fresh-review-protocol-audit
	$(MAKE) c2-longtail-second-batch-independent-fresh-review-verdict-audit
	$(MAKE) c2-longtail-second-batch-reviewed-card-artifact-audit
	$(MAKE) c2-longtail-third-batch-promotion-audit
	$(MAKE) c2-longtail-third-batch-source-extraction-audit
	$(MAKE) c2-longtail-third-batch-source-extraction-register-audit
	$(MAKE) c2-longtail-third-batch-local-review-audit
	$(MAKE) c2-longtail-third-batch-source-resolution-audit
	$(MAKE) c2-longtail-third-batch-independent-fresh-review-protocol-audit
	$(MAKE) c2-longtail-third-batch-independent-fresh-review-verdict-audit
	$(MAKE) c2-longtail-third-batch-corrected-source-reextraction-queue-audit
	$(MAKE) c2-longtail-third-batch-corrected-source-reextraction-register-audit
	$(MAKE) c2-longtail-third-batch-corrected-source-fresh-review-verdict-audit
	$(MAKE) c2-longtail-third-batch-reviewed-card-artifact-audit
	$(MAKE) c2-longtail-fourth-batch-promotion-audit
	$(MAKE) c2-longtail-fourth-batch-source-extraction-audit
	$(MAKE) c2-longtail-fourth-batch-source-extraction-register-audit
	$(MAKE) c2-longtail-fourth-batch-local-review-audit
	$(MAKE) c2-longtail-fourth-batch-source-resolution-audit
	$(MAKE) c2-longtail-fourth-batch-manual-fulltext-extraction-audit
	$(MAKE) c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-audit
	$(MAKE) c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-audit
	$(MAKE) c2-longtail-fifth-batch-promotion-audit
	$(MAKE) c2-longtail-fifth-batch-source-extraction-audit
	$(MAKE) c2-longtail-fifth-batch-source-extraction-register-audit
	$(MAKE) c2-longtail-fifth-batch-local-review-audit
	$(MAKE) c2-longtail-fifth-batch-source-resolution-audit
	$(MAKE) c2-longtail-fifth-batch-manual-fulltext-extraction-audit
	$(MAKE) c2-longtail-fifth-batch-independent-fresh-review-verdict-audit
	$(MAKE) c2-longtail-fifth-batch-reviewed-card-artifact-audit
	$(MAKE) domain-source-queue-audit
	$(MAKE) domain-source-extraction-audit
	$(MAKE) domain-source-promotion-audit
	$(MAKE) source-context-local-review-audit
	$(MAKE) card-promotion-prep-audit
	$(MAKE) independent-fresh-review-protocol-audit
	$(MAKE) independent-fresh-review-verdict-audit
	$(MAKE) reviewed-card-artifact-audit
	$(MAKE) future-boundary-route-card-audit
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

model-admission-contract-audit:
	python3 tools/audit_human_infra_model_admission_contract.py

public-mortality-anchor-audit:
	python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_public_mortality_anchor.py

page-claim-audit:
	python3 tools/audit_human_infra_page_claim_consistency.py

audience-claim-map-audit:
	python3 tools/audit_human_infra_audience_claim_map.py

paper-claim-audit:
	python3 tools/audit_human_infra_paper_claim_register.py

domain-falsifier-audit:
	python3 tools/audit_human_infra_domain_falsifier_coverage.py

domain-claim-matrix-audit:
	python3 tools/audit_human_infra_domain_claim_evidence_matrix.py

domain-field-extraction-audit:
	python3 tools/audit_human_infra_domain_source_card_field_extraction.py

c2-longtail-coverage-audit:
	python3 tools/audit_human_infra_c2_longtail_coverage_register.py

c2-longtail-first-batch-promotion-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_promotion_queue.py

c2-longtail-first-batch-source-extraction-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_source_extraction_queue.py

c2-longtail-first-batch-source-extraction-register-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_source_extraction_register.py

c2-longtail-first-batch-local-review-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_local_review_register.py

c2-longtail-first-batch-independent-fresh-review-protocol-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_independent_fresh_review_protocol.py

c2-longtail-first-batch-independent-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_independent_fresh_review_verdict_register.py

c2-longtail-first-batch-reviewed-card-artifact-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_reviewed_card_artifact_register.py

c2-longtail-first-batch-blocked-source-resolution-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_blocked_source_resolution_register.py

c2-longtail-first-batch-source-resolution-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_source_resolution_fresh_review_verdict_register.py

c2-longtail-first-batch-corrected-source-reextraction-queue-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_queue.py

c2-longtail-first-batch-corrected-source-reextraction-register-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_register.py

c2-longtail-first-batch-corrected-source-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_corrected_source_fresh_review_verdict_register.py

c2-longtail-first-batch-corrected-source-reviewed-card-artifact-audit:
	python3 tools/audit_human_infra_c2_longtail_first_batch_corrected_source_reviewed_card_artifact_register.py

c2-longtail-second-batch-promotion-audit:
	python3 tools/audit_human_infra_c2_longtail_second_batch_promotion_queue.py

c2-longtail-second-batch-source-extraction-audit:
	python3 tools/audit_human_infra_c2_longtail_second_batch_source_extraction_queue.py

c2-longtail-second-batch-source-extraction-register-audit:
	python3 tools/audit_human_infra_c2_longtail_second_batch_source_extraction_register.py

c2-longtail-second-batch-local-review-audit:
	python3 tools/audit_human_infra_c2_longtail_second_batch_local_review_register.py

c2-longtail-second-batch-independent-fresh-review-protocol-audit:
	python3 tools/audit_human_infra_c2_longtail_second_batch_independent_fresh_review_protocol.py

c2-longtail-second-batch-independent-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_c2_longtail_second_batch_independent_fresh_review_verdict_register.py

c2-longtail-second-batch-reviewed-card-artifact-audit:
	python3 tools/audit_human_infra_c2_longtail_second_batch_reviewed_card_artifact_register.py

c2-longtail-third-batch-promotion-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_promotion_queue.py

c2-longtail-third-batch-source-extraction-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_source_extraction_queue.py

c2-longtail-third-batch-source-extraction-register-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_source_extraction_register.py

c2-longtail-third-batch-local-review-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_local_review_register.py

c2-longtail-third-batch-source-resolution-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_source_resolution_register.py

c2-longtail-third-batch-independent-fresh-review-protocol-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_independent_fresh_review_protocol.py

c2-longtail-third-batch-independent-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_independent_fresh_review_verdict_register.py

c2-longtail-third-batch-corrected-source-reextraction-queue-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_queue.py

c2-longtail-third-batch-corrected-source-reextraction-register-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_register.py

c2-longtail-third-batch-corrected-source-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_corrected_source_fresh_review_verdict_register.py

c2-longtail-third-batch-reviewed-card-artifact-audit:
	python3 tools/audit_human_infra_c2_longtail_third_batch_reviewed_card_artifact_register.py

c2-longtail-fourth-batch-promotion-audit:
	python3 tools/audit_human_infra_c2_longtail_fourth_batch_promotion_queue.py

c2-longtail-fourth-batch-source-extraction-audit:
	python3 tools/audit_human_infra_c2_longtail_fourth_batch_source_extraction_queue.py

c2-longtail-fourth-batch-source-extraction-register-audit:
	python3 tools/audit_human_infra_c2_longtail_fourth_batch_source_extraction_register.py

c2-longtail-fourth-batch-local-review-audit:
	python3 tools/audit_human_infra_c2_longtail_fourth_batch_local_review_register.py

c2-longtail-fourth-batch-source-resolution-audit:
	python3 tools/audit_human_infra_c2_longtail_fourth_batch_source_resolution_register.py

c2-longtail-fourth-batch-manual-fulltext-extraction-audit:
	python3 tools/audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_extraction_register.py

c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_fresh_review_verdict_register.py

c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-audit:
	python3 tools/audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_reviewed_card_artifact_register.py

c2-longtail-fifth-batch-promotion-audit:
	python3 tools/audit_human_infra_c2_longtail_fifth_batch_promotion_queue.py

c2-longtail-fifth-batch-source-extraction-audit:
	python3 tools/audit_human_infra_c2_longtail_fifth_batch_source_extraction_queue.py

c2-longtail-fifth-batch-source-extraction-register-audit:
	python3 tools/audit_human_infra_c2_longtail_fifth_batch_source_extraction_register.py

c2-longtail-fifth-batch-local-review-audit:
	python3 tools/audit_human_infra_c2_longtail_fifth_batch_local_review_register.py

c2-longtail-fifth-batch-source-resolution-audit:
	python3 tools/audit_human_infra_c2_longtail_fifth_batch_source_resolution_register.py

c2-longtail-fifth-batch-manual-fulltext-extraction-audit:
	python3 tools/audit_human_infra_c2_longtail_fifth_batch_manual_fulltext_extraction_register.py

c2-longtail-fifth-batch-independent-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_c2_longtail_fifth_batch_independent_fresh_review_verdict_register.py

c2-longtail-fifth-batch-reviewed-card-artifact-audit:
	python3 tools/audit_human_infra_c2_longtail_fifth_batch_reviewed_card_artifact_register.py

domain-source-queue-audit:
	python3 tools/audit_human_infra_domain_source_specific_extraction_queue.py

domain-source-extraction-audit:
	python3 tools/audit_human_infra_domain_source_specific_extraction_register.py

domain-source-promotion-audit:
	python3 tools/audit_human_infra_domain_source_card_promotion_queue.py

source-context-local-review-audit:
	python3 tools/audit_human_infra_source_context_local_review_register.py

card-promotion-prep-audit:
	python3 tools/audit_human_infra_card_promotion_prep_register.py

independent-fresh-review-protocol-audit:
	python3 tools/audit_human_infra_independent_fresh_review_protocol.py

independent-fresh-review-verdict-audit:
	python3 tools/audit_human_infra_independent_fresh_review_verdict_register.py

reviewed-card-artifact-audit:
	python3 tools/audit_human_infra_reviewed_card_artifact_register.py

future-boundary-route-card-audit:
	python3 tools/audit_human_infra_future_boundary_route_card_register.py

falsifier-source-audit:
	python3 tools/audit_human_infra_falsifier_source_card_backfill.py

falsifier-source-extraction-audit:
	python3 tools/audit_human_infra_falsifier_source_card_extraction.py

py-compile:
	python3 -m py_compile \
		tools/audit_core_claim_evidence_matrix.py \
		tools/audit_human_infra_maturity_gap_register.py \
		tools/audit_human_infra_model_admission_contract.py \
		tools/audit_human_infra_page_claim_consistency.py \
		tools/audit_human_infra_audience_claim_map.py \
		tools/audit_human_infra_paper_claim_register.py \
		tools/audit_human_infra_domain_falsifier_coverage.py \
		tools/audit_human_infra_domain_claim_evidence_matrix.py \
		tools/audit_human_infra_domain_source_card_field_extraction.py \
		tools/audit_human_infra_c2_longtail_coverage_register.py \
		tools/audit_human_infra_c2_longtail_first_batch_promotion_queue.py \
		tools/audit_human_infra_c2_longtail_first_batch_source_extraction_queue.py \
		tools/audit_human_infra_c2_longtail_first_batch_source_extraction_register.py \
		tools/audit_human_infra_c2_longtail_first_batch_local_review_register.py \
	tools/audit_human_infra_c2_longtail_first_batch_independent_fresh_review_protocol.py \
	tools/audit_human_infra_c2_longtail_first_batch_independent_fresh_review_verdict_register.py \
	tools/audit_human_infra_c2_longtail_first_batch_reviewed_card_artifact_register.py \
	tools/audit_human_infra_c2_longtail_first_batch_blocked_source_resolution_register.py \
	tools/audit_human_infra_c2_longtail_first_batch_source_resolution_fresh_review_verdict_register.py \
	tools/audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_queue.py \
	tools/audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_register.py \
	tools/audit_human_infra_c2_longtail_first_batch_corrected_source_fresh_review_verdict_register.py \
	tools/audit_human_infra_c2_longtail_first_batch_corrected_source_reviewed_card_artifact_register.py \
	tools/audit_human_infra_c2_longtail_second_batch_promotion_queue.py \
	tools/audit_human_infra_c2_longtail_second_batch_source_extraction_queue.py \
	tools/audit_human_infra_c2_longtail_second_batch_source_extraction_register.py \
tools/audit_human_infra_c2_longtail_second_batch_local_review_register.py \
tools/audit_human_infra_c2_longtail_second_batch_independent_fresh_review_protocol.py \
tools/audit_human_infra_c2_longtail_second_batch_independent_fresh_review_verdict_register.py \
tools/audit_human_infra_c2_longtail_second_batch_reviewed_card_artifact_register.py \
tools/audit_human_infra_c2_longtail_third_batch_promotion_queue.py \
tools/audit_human_infra_c2_longtail_third_batch_source_extraction_queue.py \
tools/audit_human_infra_c2_longtail_third_batch_source_extraction_register.py \
tools/audit_human_infra_c2_longtail_third_batch_local_review_register.py \
tools/audit_human_infra_c2_longtail_third_batch_source_resolution_register.py \
tools/audit_human_infra_c2_longtail_third_batch_independent_fresh_review_protocol.py \
tools/audit_human_infra_c2_longtail_third_batch_independent_fresh_review_verdict_register.py \
tools/audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_queue.py \
tools/audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_register.py \
tools/audit_human_infra_c2_longtail_third_batch_corrected_source_fresh_review_verdict_register.py \
tools/audit_human_infra_c2_longtail_third_batch_reviewed_card_artifact_register.py \
tools/audit_human_infra_c2_longtail_fourth_batch_promotion_queue.py \
tools/audit_human_infra_c2_longtail_fourth_batch_source_extraction_queue.py \
tools/audit_human_infra_c2_longtail_fourth_batch_source_extraction_register.py \
tools/audit_human_infra_c2_longtail_fourth_batch_local_review_register.py \
tools/audit_human_infra_c2_longtail_fourth_batch_source_resolution_register.py \
tools/audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_extraction_register.py \
tools/audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_fresh_review_verdict_register.py \
tools/audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_reviewed_card_artifact_register.py \
tools/audit_human_infra_c2_longtail_fifth_batch_promotion_queue.py \
tools/audit_human_infra_c2_longtail_fifth_batch_source_extraction_queue.py \
tools/audit_human_infra_c2_longtail_fifth_batch_source_extraction_register.py \
tools/audit_human_infra_c2_longtail_fifth_batch_local_review_register.py \
tools/audit_human_infra_c2_longtail_fifth_batch_source_resolution_register.py \
tools/audit_human_infra_c2_longtail_fifth_batch_manual_fulltext_extraction_register.py \
tools/audit_human_infra_c2_longtail_fifth_batch_independent_fresh_review_verdict_register.py \
tools/audit_human_infra_c2_longtail_fifth_batch_reviewed_card_artifact_register.py \
tools/audit_human_infra_domain_source_specific_extraction_queue.py \
		tools/audit_human_infra_domain_source_specific_extraction_register.py \
		tools/audit_human_infra_domain_source_card_promotion_queue.py \
		tools/audit_human_infra_source_context_local_review_register.py \
		tools/audit_human_infra_card_promotion_prep_register.py \
		tools/audit_human_infra_independent_fresh_review_protocol.py \
		tools/audit_human_infra_independent_fresh_review_verdict_register.py \
		tools/audit_human_infra_reviewed_card_artifact_register.py \
		tools/audit_human_infra_future_boundary_route_card_register.py \
		tools/audit_human_infra_falsifier_source_card_backfill.py \
		tools/audit_human_infra_falsifier_source_card_extraction.py \
		tools/arxiv_html_paper_tool.py \
		tools/check_repository.py \
		tools/update_domain_doc_contracts.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/build_public_mortality_anchor.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_public_mortality_anchor.py \
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
