

import os
import hashlib

prefix="https://conda.anaconda.org/qiime2/label/r2019.10/osx-64/"
filename="qiime2.packages"
for line in open(filename):
    print(line)
    res=line.split(':')
    fname=res[0]
    fhash=res[1]
    while(not os.path.isfile(fname)):
        os.system('wget -c '+prefix+fname)
        with open(res[0], 'rb') as ff:
            data=ff.read()
        if (hashlib.md5(data).hexdigest()!=fhash):
            #print(hashlib.md5(data).hexdigest())
            #print(fhash)
            os.system('rm -f '+fname)

