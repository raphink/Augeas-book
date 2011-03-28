BOOK_NAME=augeas-book
BOOK_TEX=$(BOOK_NAME).tex
BOOK_PDF=$(BOOK_NAME).pdf
BOOK_IDX=$(BOOK_NAME).idx
BOOK_IND=$(BOOK_NAME).ind
BOOK_PS=$(BOOK_NAME).ps
BOOKLET_PDF=$(BOOK_NAME).booklet.pdf
BOOKLET_PS=$(BOOK_NAME).booklet.ps
BOOKLET_TMP_PS=$(BOOK_NAME).booklet.tmp.ps
LATEX_TEMPLATE=latex.template
PANDOC_OPTS=--toc
TEXINPUTS=minted:

all:

$(BOOK_IDX): $(BOOK_TEX)
	TEXINPUTS=$(TEXINPUTS) pdflatex -shell-escape -interaction=batchmode $(BOOK_TEX)
	TEXINPUTS=$(TEXINPUTS) pdflatex -shell-escape -interaction=batchmode $(BOOK_TEX)

$(BOOK_IND): $(BOOK_IDX)
	makeindex $(BOOK_IDX)

pdf: $(BOOK_PDF)
$(BOOK_PDF): $(BOOK_IND)
	TEXINPUTS=$(TEXINPUTS) pdflatex -shell-escape -interaction=batchmode $(BOOK_TEX)

$(BOOK_PS): $(BOOK_PDF)
	pdftops $(BOOK_PDF) $(BOOK_PS)

$(BOOKLET_PS): $(BOOK_PS)
	psbook $(BOOK_PS) $(BOOKLET_TMP_PS)
	pstops "4:0L@.7(21cm,0)+1L@.7(21cm,14.85cm),2R@.7(0,29.7cm)+3R@.7(0,14.85cm)" \
	   $(BOOKLET_TMP_PS) > $(BOOKLET_PS)

booklet: $(BOOKLET_PS)
	ps2pdf $(BOOKLET_PS) $(BOOKLET_PDF)


clean:
	rm -f *.pdf *.ps *.aux *.log *.out
	rm -f *.idx *.ind *.ilg *.toc *.dvi
	rm -f chapters/*.aux

help:
	@echo "To build the book type:"
	@echo "   make pdf  : PDF file"
	@echo "   make booklet     : A5 PDF for recto-version printing"
	@echo
	@echo "make clean : Clean all generated files"


