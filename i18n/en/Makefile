# Wetware Engineering - Makefile
# Common Commands Collection

.PHONY: help lint paper clean backup

help:
	@echo "Available commands:"
	@echo "  make lint    - Check Markdown formatting"
	@echo "  make paper   - Compile LaTeX paper"
	@echo "  make clean   - Clean build artifacts"
	@echo "  make backup  - Execute project backup"

# Markdown format check
lint:
	npx markdownlint-cli2 "**/*.md"

# Compile LaTeX paper
paper:
	cd paper/arxiv && xelatex -interaction=nonstopmode wetware_engineering.tex

# Clean LaTeX build artifacts
clean:
	cd paper/arxiv && rm -f *.aux *.log *.out *.toc *.bbl *.blg

# Project backup
backup:
	python backups/快速备份.py
