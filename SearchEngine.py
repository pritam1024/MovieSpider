import re
def srch(n):
    res=""
    p=re.compile(n,re.IGNORECASE)
    f=open('files.txt','r')
    i=0
    print('\n')
    for m in f:
        l=m
        l=l.strip('\n')
        name=l.split('/')[-1]
        name=name.replace('%20',' ')
        name=name.replace('%28','(')
        name=name.replace('%29',')')
        name=name.replace('mkv','')
        name=name.replace('.',' ')
        name=name.replace('_',' ')
        if re.search(p,name):
            #print("-->"+name,'\n')
            #print(l)
            #print('------------------------------------------------------------------------------')
            #print('\n')
            res=res+"-->"+name+'\n\n'+l+'\n------------------------------------------------------------------------------\n\n'
            i=1
    if i!=1:
        #print('Could not find the movie with the name \"'+n+'\"')
        res='Could not find the movie with the name \"'+n+'\"'
    f.close()
    return res
