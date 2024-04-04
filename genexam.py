#!/usr/bin/env python3
import os

from ymydata import lesclasses
from CreateClassMap import LesClasses

OUTDIR="./outdir"



def generates_student_file(e):
    print(e)



# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    lc=LesClasses(lesclasses,None,False)
    cid="4_4"
    a_class=lc.getClasse(cid)
    for e in a_class.eleves:
        generates_student_file(e)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
