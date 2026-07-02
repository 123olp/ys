.PHONY: check structure claim-matrix-audit maturity-gap-audit py-compile clean

check:
	$(MAKE) clean
	$(MAKE) structure
	$(MAKE) claim-matrix-audit
	$(MAKE) maturity-gap-audit
	$(MAKE) py-compile
	$(MAKE) clean
	$(MAKE) structure

structure:
	python3 tools/check_repository.py

claim-matrix-audit:
	python3 tools/audit_core_claim_evidence_matrix.py

maturity-gap-audit:
	python3 tools/audit_human_infra_maturity_gap_register.py

py-compile:
	python3 -m py_compile \
		tools/audit_core_claim_evidence_matrix.py \
		tools/audit_human_infra_maturity_gap_register.py \
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
