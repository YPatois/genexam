#!/usr/bin/env python3
import unittest
import string
import os
import random
import unicodedata

from ymydata import lesclasses
from CreateClassMap import LesClasses

OUTDIR="./outdir/tex"

class Componant:
    def __init__(self):
        self.I=0
        self.ukn=False

    def compute_intensity(self,cpn):
        s=0
        for c in cpn:
            s+=c.I
        self.I=-s

    def set_i_label(self,il):
        self.i_label=il

    def set_ukn(self):
        self.ukn=True

    def no_negative(self):
        return (self.I>0)

    def arrow(self):
        return ("<")


    def iblock(self,p):
        if (p==0):
            return "i_"+self.arrow()+"="
        if (p==1):
            return "i"+self.arrow()+"_="
        return "i^"+self.arrow()+"="

class Generator(Componant):
    def __init__(self):
        super().__init__()

    def set_intensity(self):
        clist=[ 1000+200*i for i in range(1,19)]
        self.I=-random.choice(clist)

    def no_negative(self):
        return (self.I<0)

    def arrow(self):
        return (">")

    def circuitikz(self,p):
        if (not self.ukn):
            istr=self.i_label+"=\SI{"+str(-self.I/1000)+"}{\A}"
        else:
            istr=self.i_label
        s1="american voltage source, invert, "
        s2=self.iblock(p)+"${"+istr+"}$"
        return (s1+s2)

class Lamp(Componant):
    lidx=0
    def __init__(self):
        self.idx=Lamp.lidx
        Lamp.lidx+=1
        super().__init__()

    def set_intensity(self):
        clist=[ 20*i for i in range(1,10)]
        self.I=random.choice(clist)

    def circuitikz(self,p):
        if (not self.ukn):
            istr=self.i_label+"=\SI{"+str(self.I)+"}{\mA}"
        else:
            istr=self.i_label
        s1="lamp=$L_"+str(self.idx)+"$, "
        s2=self.iblock(p)+"${"+istr+"}$"
        return (s1+s2)


class Motor(Componant):
    def __init__(self):
        super().__init__()

    def set_intensity(self):
        clist=[ 1000+200*i for i in range(1,19)]
        self.I=random.choice(clist)

    def circuitikz(self,p):
        if (not self.ukn):
            istr=self.i_label+"=\SI{"+str(self.I)+"}{\mA}"
        else:
            istr=self.i_label
        s1="rmeter, t={\\textbf M}, "
        s2=self.iblock(p)+"${"+istr+"}$"
        return (s1+s2)

class Circuit:
    def __init__(self,level):
        self.level=level
        if (level<11):
            self.components=[Generator(),Lamp(),Lamp()]
            ukn=0
        elif (level<15):
            if (random.getrandbits(1)):
                self.components=[Generator(),Lamp(),Motor()]
            else:
                self.components=[Generator(),Motor(),Lamp()]
            ukn=0
        else:
            self.components=([Generator(),Lamp(),Motor()])
            random.shuffle(self.components)
            ukn=random.randint(0, 2)
        i_label=["i_1","i_2","i_3"]
        random.shuffle(i_label)
        for i in range(3):
            self.components[i].set_i_label(i_label[i])
            if (ukn==i):
                self.components[i].set_ukn()
        s=0
        for c in self.components:
            if (type(c)!=Generator):
                c.set_intensity()
                s+=c.I

        for c in self.components:
            if (type(c)==Generator):
                c.I=-s

    def circuitikz(self):
        sl=[]
        i=0
        for c in self.components:
            x=c.circuitikz(i)
            i+=1
            sl.append(x)
            #sl.append(x2)
            if (c.ukn):
                s=get_random_string(5)+str(c.I)+get_random_string(5)
                s=str(c.I)
                il=c.i_label
        return (sl[0],sl[1],sl[2],il,s)

    def sum_I(self):
        s=0
        for c in self.components:
            s+=c.I
        return s

    def no_negative(self):
        for c in self.components:
            if (not c.no_negative()): return False
        return True

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase+string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def item2fn(item):
    item=unicodedata.normalize('NFKD', item).encode('ascii', 'ignore').decode('ascii')
    return item.lower().replace(' ','_').replace('-','_')

def eleve2filename(e):
    return os.path.join(OUTDIR,item2fn(e.nom)+'_'+item2fn(e.prenom)+".tex")

def replace_braces(s):
    s=s.replace('@','{')
    s=s.replace('£','}')
    return s

def build_lmA(idx):
    clist=[ 20*i for i in range(1,10)]
    i=random.choice(clist)
    s="$@i_{}=\SI@{}£@\mA££$".format(idx,i)
    s=replace_braces(s)
    return (i,s)

def build_lA(idx):
    clist=[ 10+2*i for i in range(1,9)]
    i=random.choice(clist)/10
    #print(i)
    s="$@i_{}=\SI@{}£@\A££$".format(idx,i)
    s=replace_braces(s)
    return (i,s)

def problem_stuffing_basic():
    (i2,s2)=build_lmA(2)
    (i3,s3)=build_lmA(3)
    i1=i2+i3
    ia="${i_1}$"
    ib=s2
    ic=s3
    solstring=get_random_string(5)+str(i1)+get_random_string(5)
    si="to [lamp=$L_2$, i>_=@IC@] (4,0) to[short, -*] (2,0);"
    return (si,ia,ib,ic,solstring)

def problem_stuffing_higher():
    (i2,s2)=build_lmA(2)
    (i3,s3)=build_lA(3)
    i1=(i2+i3*1000)/1000
    ia="${i_1}$"
    ib=s2
    ic=s3
    solstring=get_random_string(5)+str(i1).replace('.','')+get_random_string(5)
    si="to [Telmech=$M$] (4,0) to[short, -*, i>_=@IC@] (2,0);"
    return (si,ia,ib,ic,solstring)


def problem_stuffing(level):
    level=int(level)
    if (level<11):
        return problem_stuffing_basic()
    else:
        return problem_stuffing_higher()

def generates_student_file(e):
    cl=e.cid.split('_')
    fi=open("latextemplate.tex","rt")
    fo=open(eleve2filename(e),"wt")
    c=Circuit(e.phynote)
    (a,b,c,il,sl)=c.circuitikz()
    for line in fi.readlines():
        line=line.replace("@PRENOM@",e.prenom)
        line=line.replace("@NOM@",e.nom)
        line=line.replace("@CLASS@",cl[0])
        line=line.replace("@CLNB@",cl[1])
        line=line.replace("@A@",a)
        line=line.replace("@B@",b)
        line=line.replace("@C@",c)
        line=line.replace("@IL@",il)
        line=line.replace("@SOLSTRING@",sl)
        fo.write(line)
    fo.close()
    fi.close()

class TestCircuit(unittest.TestCase):
    def test_circuit_zero(self):
        for l in [10,12,14,16]:
            c=Circuit(l)
            self.assertEqual(c.sum_I(),0)

    def test_circuit_zero_deeper(self):
        for i in range(100):
            c=Circuit(16)
            self.assertEqual(c.no_negative(),True)

    def test_circuit_has_generator(self):
        l=[10,12,14,16]
        for i in range(100):
            has_gen=False
            c=Circuit(random.choice(l))
            for c in c.components:
                if (type(c)==Generator):
                    has_gen=True
            self.assertEqual(has_gen,True)

# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    #random.seed(10)
    #unittest.main()
    #return
    #G=Generator()
    #for i in range(30):
    #    G.set_intensity()
    #    print(G.I)
    #return

    lc=LesClasses(lesclasses,False)
    cid="4_3"
    a_class=lc.getClasse(cid)
    for e in a_class.eleves:
        generates_student_file(e)
        #return

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
