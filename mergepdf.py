#!/usr/bin/env python3
import os
import glob

OUTDIR="./outdir/"

OUTFILE=os.path.join(OUTDIR,"out.tex")



def print_list(pl):
    # Ensure last page contains 4 names
    nb=len(pl)
    for i in range(4-nb%4):
        pl.append(pl[-1])
    # Init
    s1=""
    s2=""
    s=""
    n=0
    # Loop
    for p in pl:
        #p=p.replace(OUTDIR,"")
        if (n<4):
            s1+=p+',1,\n'
            s2+=p+',2,\n'
        n+=1
        if (n==4):
            s+=s1+s2
            s1=""
            s2=""
            n=0
    return s # removing last comma


# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    pdflist=glob.glob(os.path.join(OUTDIR,"pdf","*.pdf"))
    pdflist.sort()
    #print(pdflist)
    fi=open("mergetemplate.tex","rt")
    fo=open(OUTFILE,"wt")
    for line in fi.readlines():
        if "@PDFLIST@" in line:
            line=line.replace("@PDFLIST@",print_list(pdflist))
        fo.write(line)
    fo.close()
    fi.close()

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
