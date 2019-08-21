from bs4 import BeautifulSoup
import urllib.request
import re
#u='http://dl3.heyserver.in/film/'
urlLst=['http://dl3.heyserver.in/film/','http://dl2.upload08.com/files/Film/']
f=open('dirs.txt','w')
f.write('')
f.close()
f=open('files.txt','w')
f.write('')
f.close()
def fndUrls(u):
    try:
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-agent', 'Mozilla/5.0')]
        r=opener.open(u)
        s=BeautifulSoup(r.read(),'html.parser')
        x=s.findAll('a')
        for a in x:
            p=re.compile('^\?.*|^\.')
            p1=re.compile('\/$')
            p2=re.compile('series\/$|serial\/$|serials\/$|screenshots\/$|screen\/$|E[0-9]*|s[0-9]\/$',re.IGNORECASE)
            l=a.get('href')
            if l==None:
                continue
            if re.search(p,l):
                continue
            #if re.search(p2,l):
                #continue
            url=u+l
            print(url)
            if re.search(p1,l):
                f=open('dirs.txt','a')
                f.write(url)
                f.write('\n')
                f.close()
                continue
            f=open('files.txt','a')
            f.write(url)
            f.write('\n')
            f.close()
    except:
        pass
def crawl():
    for u in urlLst:
        fndUrls(u)
        f=open('dirs.txt','r')
        for line in f:
            lnk=line
            lnk=lnk.strip()
            fndUrls(lnk)
        f.close()

crawl()
