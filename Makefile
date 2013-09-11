all: html pdf

clean:
	@rm -f articles.html articles.pdf

pdf: articles.md
	@echo "Building articles.pdf"
	@multimarkdown -t latex articles.md > articles.tex
	@pdflatex articles.tex > /dev/null
	@pdflatex articles.tex > /dev/null
	@rm -f articles.tex articles.aux articles.log articles.out articles.toc

html: articles.md
	@echo "Building articles.html"
	@multimarkdown articles.md > articles.html
	@python html/format_html.py articles.html
