# Wetware Engineering - Makefile
# 常用命令集合

.PHONY: help lint paper clean backup

help:
	@echo "可用命令："
	@echo "  make lint    - 检查 Markdown 格式"
	@echo "  make paper   - 编译 LaTeX 论文"
	@echo "  make clean   - 清理编译产物"
	@echo "  make backup  - 执行项目备份"

# Markdown 格式检查
lint:
	npx markdownlint-cli2 "**/*.md"

# 编译 LaTeX 论文
paper:
	cd paper/arxiv && xelatex -interaction=nonstopmode wetware_engineering.tex

# 清理 LaTeX 编译产物
clean:
	cd paper/arxiv && rm -f *.aux *.log *.out *.toc *.bbl *.blg

# 项目备份
backup:
	python backups/快速备份.py
