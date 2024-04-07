TEXES= $(wildcard outdir/tex/*.tex)
PDFS = $(patsubst outdir/tex/%.tex, outdir/pdf/%.pdf, $(TEXES))


all: $(PDFS)

outdir/pdf/%.pdf: outdir/tex/%.tex
	pdflatex -output-directory outdir/pdf/ $<

