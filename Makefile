TEXES= $(wildcard outdir/tex/*.tex)
PDFS = $(patsubst outdir/tex/%.tex, outdir/pdf/%.pdf, $(TEXES))


all: outdir/out.pdf

outdir/tex/%.tex: genexam.py latextemplate.tex Makefile
	./genexam.py

outdir/pdf/%.pdf: outdir/tex/%.tex
	pdflatex -output-directory outdir/pdf/ $<

outdir/out.tex: $(PDFS) mergepdf.py mergetemplate.tex
	./mergepdf.py

outdir/out.pdf: outdir/out.tex outdir
	pdflatex -output-directory outdir/ $<

outdir:
	mkdir outdir

clean:
	/bin/rm outdir/pdf/*.pdf
	/bin/rm outdir/tex/*.tex
