TEXES= $(wildcard outdir/tex/*.tex)
PDFS = $(patsubst outdir/tex/%.tex, outdir/pdf/%.pdf, $(TEXES))


all: outdir/out.pdf

outdir/tex/%.tex: genexam.py latextemplate.tex Makefile
	./genexam.py

outdir/pdf/%.pdf: outdir/tex/%.tex
	pdflatex -output-directory outdir/pdf/ $<

outdir/out.pdf: $(PDFS)
	pdfjam outdir/pdf/*.pdf --a4paper  --nup 1x4 --outfile $@

