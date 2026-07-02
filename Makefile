.PHONY: check structure py-compile clean

check:
	$(MAKE) clean
	$(MAKE) structure
	$(MAKE) py-compile
	$(MAKE) clean
	$(MAKE) structure

structure:
	python3 tools/check_repository.py

py-compile:
	python3 -m py_compile \
		tools/arxiv_html_paper_tool.py \
		tools/check_repository.py \
		tools/update_domain_doc_contracts.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_toy_model.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_sensitivity_analysis.py \
		domains/c1-boundary-rewriting/longevity-evidence/scripts/audit_life_path_toy_model.py

clean:
	find . -type d \( -name __pycache__ -o -name .pytest_cache \) -prune -exec rm -rf {} +
