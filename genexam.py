#!/usr/bin/env python3
from ymydata import lesclasses
from CreateClassMap import LesClasses




# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
    lc=LesClasses(lesclasses,None,False)
    cid="4_4"
    a_class=lc.getClasse(cid).getFullArray()
    print(a_class)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
