BOOK_NAME=augeas-book
BOOK_MARKDOWN=$(BOOK_NAME).markdown
BOOK_HTML=$(BOOK_NAME).html
BOOK_PDF=$(BOOK_NAME).pdf

all:

$(BOOK_MARKDOWN):
	find . -type f -name '*-chapter*\.markdown' | \
	   sort | xargs cat > $(BOOK_MARKDOWN)

html: $(BOOK_MARKDOWN)
	pandoc -o $(BOOK_HTML) $(BOOK_MARKDOWN)

pdf: $(BOOK_MARKDOWN)
	markdown2pdf -o $(BOOK_HTML) $(BOOK_MARKDOWN)

numberedpdf: $(BOOK_MARKDOWN)
	markdown2pdf -N -o $(BOOK_HTML) $(BOOK_MARKDOWN)

clean:
	rm -f $(BOOK_MARKDOWN)
	rm -f *.pdf
	rm -f *.html



