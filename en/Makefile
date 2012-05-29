BOOK_NAME=augeas-book
BOOK_PDF=$(BOOK_NAME).pdf
BOOK_PS=$(BOOK_NAME).ps
BOOKLET_PDF=$(BOOK_NAME).booklet.pdf
BOOKLET_PS=$(BOOK_NAME).booklet.ps
BOOKLET_TMP_PS=$(BOOK_NAME).booklet.tmp.ps
LATEX_TEMPLATE=latex.template
PANDOC_OPTS=--toc
TEXINPUTS=../minted:microtype:

all: pdf

pdf: $(BOOK_PDF)

ebooks: mobi epub

mobi: $(BOOK_NAME).mobi

epub: $(BOOK_NAME).epub

%.idx: %.tex
	TEXINPUTS=$(TEXINPUTS) lualatex -shell-escape -interaction=batchmode $<
	TEXINPUTS=$(TEXINPUTS) lualatex -shell-escape -interaction=batchmode $<

%.ind: %.idx
	makeindex $<

%.pdf: %.ind
	TEXINPUTS=$(TEXINPUTS) lualatex -shell-escape -interaction=batchmode $*

%.ps: %.pdf
	pdftops $< $@

$(BOOKLET_PS): $(BOOK_PS)
	psbook $(BOOK_PS) $(BOOKLET_TMP_PS)
	pstops "4:0L@.7(21cm,0)+1L@.7(21cm,14.85cm),2R@.7(0,29.7cm)+3R@.7(0,14.85cm)" \
	   $(BOOKLET_TMP_PS) > $(BOOKLET_PS)

booklet: $(BOOKLET_PS)
	ps2pdf $(BOOKLET_PS) $(BOOKLET_PDF)

%.html: %.tex
	TEXINPUTS=$(TEXINPUTS) htlatex $< \
	   'xhtml,charset=utf-8' ' -cunihtf -utf8 -cvalidate' '' '-shell-escape'
	./cleanuphtml.sh $@

%.epub: %.html
	ebook-convert $< $@

%.mobi: %.html
	ebook-convert $< $@

clean:
	rm -f *.pdf *.ps *.aux *.log *.out *.lol
	rm -f ../*.aux
	rm -f *.idx *.ind *.ilg *.toc *.dvi *.tdo
	rm -f chapters/*.aux

help:
	@echo "To build the book type:"
	@echo "   make pdf  : PDF file"
	@echo "   make booklet     : A5 PDF for recto-version printing"
	@echo
	@echo "make clean : Clean all generated files"


