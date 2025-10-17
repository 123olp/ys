# Simple doc build
PANDOC?=pandoc
SRC=docs/系统化审阅报告_2025-10-17.md
OUT_DIR=out

all: $(OUT_DIR)/report.html $(OUT_DIR)/report.pdf

$(OUT_DIR)/report.html: $(SRC)
	@mkdir -p $(OUT_DIR)
	$(PANDOC) -f gfm -t html5 -s $< -o $@

$(OUT_DIR)/report.pdf: $(SRC)
	@mkdir -p $(OUT_DIR)
	$(PANDOC) -f gfm -t pdf -V geometry:margin=1in $< -o $@

clean:
	rm -rf $(OUT_DIR)

.PHONY: all clean
