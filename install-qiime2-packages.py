import os
import hashlib
import re

VERSION='2020.2'
info1=os.popen('conda search q2 --info -c qiime2/label/r%s' % VERSION).read()
info2=os.popen('conda search qiime2 --info -c qiime2/label/r%s' % VERSION).read()

content=info1+info2

pat = re.compile("url\W*"+'(.*?)'+"dependencies",re.S)
result = pat.findall(content)
for item in result:
    item=re.sub('\nmd5\W*: ',';',item)
    item=re.sub('\n',';',item)
    if not re.search("qiime2", item):
        continue
    #print(item)
    arr=item.split(';')
    furl=arr[0]
    fhash=arr[1]
    fname=re.sub("^.*\/","",furl)
    #print("name:%s\nrequired hash:%s\n" % (fname,fhash))
    while True:
        try:
            ff = open(fname, "rb")
            data = ff.read()
            nhash=hashlib.md5(data).hexdigest()
            ff.close()
        except IOError:
            nhash=""
        if nhash == fhash:
            print("INFO: name:%s;new hash:%s, match the required hash:%s\n" % (fname, nhash, fhash))
            print("INFO: starting installation of the package : %s" % fname)
            os.popen("conda install --offline %s" % fname)
            print("INFO: complete installation of the package : %s" % fname)
            break
        else:
            print("name:%s\nnew hash:%s, not match the required hash:%s\n" % (fname, nhash, fhash))
            os.system('rm -f '+fname)
        os.system('wget -c '+furl)

