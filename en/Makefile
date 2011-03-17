BOOK_NAME=augeas-book
BOOK_MARKDOWN=$(BOOK_NAME).markdown
BOOK_HTML=$(BOOK_NAME).html
BOOK_TEX=$(BOOK_NAME).tex
BOOK_PDF=$(BOOK_NAME).pdf
BOOK_PS=$(BOOK_NAME).ps
BOOKLET_PDF=$(BOOK_NAME).booklet.pdf
BOOKLET_PS=$(BOOK_NAME).booklet.ps
BOOKLET_TMP_PS=$(BOOK_NAME).booklet.tmp.ps
LATEX_TEMPLATE=latex.template

all:

$(BOOK_MARKDOWN):
	find . -mindepth 2 -type f -name '*\.markdown' | \
	   sort | xargs cat > $(BOOK_MARKDOWN)

html: $(BOOK_HTML)
$(BOOK_HTML): $(BOOK_MARKDOWN)
	pandoc -o $(BOOK_HTML) $(BOOK_MARKDOWN)

tex: $(BOOK_TEX)
$(BOOK_TEX): $(BOOK_MARKDOWN)
	pandoc -s --no-wrap -r markdown -w latex \
	   --template $(LATEX_TEMPLATE) \
	   -o $(BOOK_TEX) $(BOOK_MARKDOWN)

pdf: $(BOOK_PDF)
$(BOOK_PDF): $(BOOK_MARKDOWN)
	#pdflatex -interaction=batchmode $(BOOK_TEX)
	markdown2pdf --template $(LATEX_TEMPLATE) \
	   -o $(BOOK_HTML) $(BOOK_MARKDOWN)

numberedpdf: $(BOOK_MARKDOWN)
	markdown2pdf -N -o $(BOOK_HTML) $(BOOK_MARKDOWN)

$(BOOK_PS): $(BOOK_PDF)
	pdftops $(BOOK_PDF) $(BOOK_PS)

$(BOOKLET_PS): $(BOOK_PS)
	psbook $(BOOK_PS) $(BOOKLET_TMP_PS)
	pstops "4:0L@.7(21cm,0)+1L@.7(21cm,14.85cm),2R@.7(0,29.7cm)+3R@.7(0,14.85cm)" \
	   $(BOOKLET_TMP_PS) > $(BOOKLET_PS)

booklet: $(BOOKLET_PS)
	ps2pdf $(BOOKLET_PS) $(BOOKLET_PDF)


clean:
	rm -f $(BOOK_MARKDOWN)
	rm -f *.tex *.pdf *.ps *.aux *.log *.out
	rm -f *.html

help:
	@echo "To build the book type:"
	@echo "   make html : HTML file"
	@echo "   make tex  : TeX file"
	@echo "   make pdf  : PDF file"
	@echo "   make numberedpdf : PDF with numbered sections"
	@echo "   make booklet     : A5 PDF for recto-version printing"
	@echo
	@echo "make clean : Clean all generated files"


