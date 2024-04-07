#!/bin/bash

#rm -rf outdir/ && mkdir outdir && 
./genexam.py && cd outdir/tex && pdflatex ob*.tex
