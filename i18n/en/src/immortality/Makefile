# Makefile for Immortality Project Documentation

# --- Variables ---
PANDOC := pandoc
OUT_DIR := out

# Source Markdown files (in order of appearance)
SRC_FILES := \
	README.md \
	i18n/en/human_3.0_technical_blueprint.md \
	i18n/en/immortality_roadmap.md \
	i18n/zh/README.md \
	i18n/zh/docs/core/human_3.0_technical_blueprint.md \
	i18n/zh/docs/core/immortality_27_elements.md \
	i18n/zh/docs/philosophy/emotion_modeling.md \
	i18n/zh/docs/philosophy/ontology_experience_machine.md \
	i18n/zh/archives/audit/物理极限审计.md \
	i18n/zh/archives/reviews/评审清单.md

CONCAT_SRC := $(OUT_DIR)/source.md

# --- Rules ---
all: html pdf

html: $(OUT_DIR)/report.html

pdf: $(OUT_DIR)/report.pdf

$(CONCAT_SRC): $(SRC_FILES)
	@mkdir -p $(OUT_DIR)
	@echo "Concatenating source files..."
	@cat $(SRC_FILES) > $(CONCAT_SRC)

$(OUT_DIR)/report.html: $(CONCAT_SRC)
	@echo "Building HTML report..."
	$(PANDOC) \
		--from=gfm \
		--to=html5 \
		--standalone \
		--toc \
		--toc-depth=2 \
		--metadata-file=metadata.yaml \
		-o $@ $<

$(OUT_DIR)/report.pdf: $(CONCAT_SRC)
	@echo "Building PDF report..."
	$(PANDOC) \
		--from=gfm \
		--to=pdf \
		--standalone \
		--toc \
		--toc-depth=2 \
		--pdf-engine=xelatex \
		-V mainfont="Noto Sans CJK SC" \
		-V monofont="Noto Sans Mono CJK SC" \
		-V geometry:margin=1in \
		--metadata-file=metadata.yaml \
		-o $@ $<

clean:
	@echo "Cleaning output directory..."
	@rm -rf $(OUT_DIR)

.PHONY: all html pdf clean
