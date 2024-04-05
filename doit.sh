#!/bin/bash

#rm -rf outdir/ && mkdir outdir && 
./genexam.py && cd outdir && pdflatex ob*.tex
