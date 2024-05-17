TEXES= $(wildcard outdir/tex/*.tex)
PDFS = $(patsubst outdir/tex/%.tex, outdir/pdf/%.pdf, $(TEXES))


all: outdir/out_4_3.pdf outdir/out_4_4.pdf outdir/out_4_5.pdf

outdir/tex/%.tex: genexam.py latextemplate.tex Makefile
	./genexam.py


.PRECIOUS: outdir/pdf/%.pdf

outdir/pdf/%.pdf: outdir/tex/%.tex
	pdflatex -output-directory outdir/pdf/ $<

outdir/out_%.tex: $(PDFS) mergepdf.py mergetemplate.tex
	./mergepdf.py

outdir/out_%.pdf: outdir/out_%.tex
	pdflatex -output-directory outdir/ $<

clean:
	/bin/rm outdir/pdf/*.*
	/bin/rm outdir/tex/*.tex
	/bin/rm outdir/*.tex
	/bin/rm outdir/*.pdf
