import re
from tkinter import *
root=Tk()
def srch():
    #n=input('Enter the name or part of the name of the movie:')
    n=e.get()
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
            print(name,'\n')
            print(l)
            print('\n')
            i=1
    if i!=1:
        print('Could not find the movie with the name \"'+n+'\"')
    f.close()
e=Entry(root)
b=Button(root, text='Search', command=srch)
e.pack()
b.pack()
root.mainloop()
