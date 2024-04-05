#!/usr/bin/env python3
import os

from ymydata import lesclasses
from CreateClassMap import LesClasses

OUTDIR="./outdir"


def item2fn(item):
    return item.lower().replace(' ','_').replace('-','_')

def eleve2filename(e):
    return os.path.join(OUTDIR,item2fn(e.nom)+'_'+item2fn(e.prenom)+".tex")


def generates_student_file(e):
    cl=e.cid.split('_')
    fi=open("latextemplate.tex","rt")
    fo=open(eleve2filename(e),"wt")
    for line in fi.readlines():
        line=line.replace("@PRENOM@",e.prenom)
        line=line.replace("@NOM@",e.nom)
        line=line.replace("@CLASS@",cl[0])
        line=line.replace("@CLNB@",cl[1])
        fo.write(line)
    fo.close()
    fi.close()


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
