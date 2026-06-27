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
		domains/longevity-evidence/scripts/collect_mvp_data.py \
		domains/longevity-evidence/scripts/collect_core_data.py

clean:
	find . -type d \( -name __pycache__ -o -name .pytest_cache \) -prune -exec rm -rf {} +
