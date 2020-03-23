import os
import hashlib
import re

filename="qiime2.packages"
fp=open(filename,'r')
content=fp.read()
fp.close()

pat = re.compile("url\W*"+'(.*?)'+'timestamp',re.S)
result = pat.findall(content)
for item in result:
    item=re.sub('\nmd5\W*: ',';',item)
    item=re.sub('\n','',item)
    if not re.search("qiime2", item):
        continue
    (furl, fhash)=item.split(';')
    fname=re.sub("^.*\/","",furl)
    while True:
        try:
            ff = open(fname, "rb")
            data = ff.read()
            nhash=hashlib.md5(data).hexdigest()
            ff.close()
        except IOError:
            nhash=""
        if nhash == fhash:
            print("name:%s\nnew hash:%s, match the required hash:%s\n" % (fname, nhash, fhash))
            break
        else:
            print("name:%s\nnew hash:%s, not match the required hash:%s\n" % (fname, nhash, fhash))
            os.system('rm -f '+fname)
        os.system('wget -c '+furl)
