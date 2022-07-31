# This a makefile for getting parser tree 
# image, this is run from main.py script

ANTLR = /usr/local/lib/antlr-4.10.1-complete.jar
GRAMMAR_NAME = YAPL
ANTLR_FLAGS = -no-visitor -no-listener
OUT_DIR = jdist
START_RULE = program
CL_FILE = input/cool.cl
GRUN_FLAGS = -gui -tokens
INPUT_FILE = cool.cl

%: all

all: compile run

compile:
	@echo Generating $(GRAMMAR) Parser and Lex ...
	java -Xmx500M -cp $(ANTLR) org.antlr.v4.Tool $(ANTLR_FLAGS) -o $(OUT_DIR) ./$(GRAMMAR_NAME)/$(GRAMMAR_NAME).g4
	@echo Success!

run:
	@echo Showing parse tree ...
	cd $(OUT_DIR)/$(GRAMMAR_NAME); javac ./*.java; \
	java -Xmx500M -cp $(ANTLR):$(CLASSPATH) org.antlr.v4.gui.TestRig $(GRAMMAR_NAME) $(START_RULE) ../../input/$(INPUT_FILE) $(GRUN_FLAGS); \
	echo Done!

clean:
	rm -r ./$(OUT_DIR)

