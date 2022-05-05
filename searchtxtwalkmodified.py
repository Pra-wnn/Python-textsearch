import os 
import re
import codecs

i=0


while i==0:
    pth = input("Enter a path: ")
    kw = input("Enter keyword to search: ")
    if kw and pth != "":
        pat = os.path.dirname(pth)
        clat = pat.replace('\\','/')
        if os.path.exists(clat):
            for dirpath, dirnames,file in os.walk(f"{clat}"):
                for e in file:                                                                      
                    if e.endswith('.txt'):      
                        cad = dirpath+'\\'+e
                        n=0
                        with codecs.open(f'{cad}',encoding="utf-8",errors='ignore') as cfile:
                            for line in cfile:
                                pattern = re.compile(r"{0}".format(str(kw)),re.I) 
                                matches = pattern.finditer(line)
                                n=n+1
                                for match in matches:
                                    print(cad,"-->","LINE:",n)
        else:
            print("Path doesn't exist")
    else:
        i = i+1

