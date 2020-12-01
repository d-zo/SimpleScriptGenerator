SOURCE_DIR = ../src
TEMP_DIR = temp_work_dir
OUTPUT_DIR = ../SimpleScriptGenerator

.PHONY: all

all: $(OUTPUT_DIR)/SimpleScriptGenerator.pyz

$(OUTPUT_DIR)/SimpleScriptGenerator.pyz: $(SOURCE_DIR)/__main__.py $(SOURCE_DIR)/SimpleScriptGenerator/*.py
	mkdir -p $(TEMP_DIR)/SimpleScriptGenerator;
	cp -r $(SOURCE_DIR)/* $(TEMP_DIR)/SimpleScriptGenerator/;
	cd $(TEMP_DIR); \
	python3 -m zipapp -c SimpleScriptGenerator;
	mv $(TEMP_DIR)/$(notdir $@) $@;
	rm -r $(TEMP_DIR);
