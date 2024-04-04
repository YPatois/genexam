#!/usr/bin/env python3
import os

from ymydata import lesclasses
from CreateClassMap import LesClasses

OUTDIR="./outdir"


def item2fn(item):
    return item.lower().replace(' ','_').replace('-','_')

def eleve2filename(e):
    return item2fn(e.nom)+'_'+item2fn(e.prenom)


def generates_student_file(e):
    #os.mkdir(OUTDIR)
    fn=eleve2filename(e)+'.txt'
    fn=os.path.join(OUTDIR,fn)
    print(fn)



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
