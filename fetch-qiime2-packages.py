

import os
import hashlib
import re

filename="qiime2.packages"
for line in open(filename):
    line=line.rstrip("\n")
    print(line)
    res=line.split(';')
    furl=res[0]
    fname=re.sub("^.*\/","",furl)
    fhash=res[1]
    while(not os.path.isfile(fname)):
        os.system('wget -c '+furl)
        with open(fname, 'rb') as ff:
            data=ff.read()
        if (hashlib.md5(data).hexdigest()!=fhash):
            print("file has : %s, not match the required hash:%s." % (hashlib.md5(data).hexdigest(), fhash))
            os.system('rm -f '+fname)

