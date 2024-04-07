#!/usr/bin/env python3
import os
import random
import unicodedata

from ymydata import lesclasses
from CreateClassMap import LesClasses

OUTDIR="./outdir/tex"


def item2fn(item):
    item=unicodedata.normalize('NFKD', item).encode('ascii', 'ignore').decode('ascii')
    return item.lower().replace(' ','_').replace('-','_')

def eleve2filename(e):
    return os.path.join(OUTDIR,item2fn(e.nom)+'_'+item2fn(e.prenom)+".tex")


def replace_braces(s):
    s=s.replace('@','{')
    s=s.replace('£','}')
    return s

def build_l(idx):
    clist=[ 10*i for i in range(1,10)]
    i=random.choice(clist)
    s="$@i_{}=\SI@{}£@\mA££$".format(idx,i)
    s=replace_braces(s)
    return (i,s)

def problem_stuffing():
    (i2,s2)=build_l(2)
    (i3,s3)=build_l(3)
    i1=i2+i3
    ia="${i_1}$"
    ib=s2
    ic=s3
    solstring=str(i1)
    return (ia,ib,ic,solstring)


def generates_student_file(e):
    cl=e.cid.split('_')
    fi=open("latextemplate.tex","rt")
    fo=open(eleve2filename(e),"wt")
    (ia,ib,ic,sl)=problem_stuffing()
    for line in fi.readlines():
        line=line.replace("@PRENOM@",e.prenom)
        line=line.replace("@NOM@",e.nom)
        line=line.replace("@CLASS@",cl[0])
        line=line.replace("@CLNB@",cl[1])
        line=line.replace("@IA@",ia)
        line=line.replace("@IB@",ib)
        line=line.replace("@IC@",ic)
        line=line.replace("@SOLSTRING@",sl)
        fo.write(line)
    fo.close()
    fi.close()


# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    random.seed(10)
    lc=LesClasses(lesclasses,None,False)
    cid="4_4"
    a_class=lc.getClasse(cid)
    for e in a_class.eleves:
        generates_student_file(e)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
