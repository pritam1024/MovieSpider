from tkinter import *
from tkinter import ttk
from SearchEngine import *
from threading import Thread
import os

def runCrawl():
    os.system("Crawler.py")
def txtsrch():
    tex.delete(1.0,END)
    result=srch(mname.get())
    #print(result)
    tex.insert(END,result)
def clear():
    film.delete(0,END)
    tex.delete(1.0,END)
    status.set("")
def update():
    t=Thread(target=runCrawl, args=())
    t.start()
    t.join()
    status.set("OPERATION COMPLETED")
def vcsrch():
    os.system("VoiceSearch.py")
def play():
    movie_link = mplay.get()
    os.system("playM.vbs "+movie_link)

root=Tk()
root.title("Movie spider: It's popcorn time")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

bf = ttk.Frame(root)
bf.grid(column=0, row=1)
bf.columnconfigure(0, weight=1)
bf.rowconfigure(0, weight=1)

mname = StringVar()
status = StringVar()
mplay = StringVar()

film = ttk.Entry(mainframe, width=80, textvariable=mname)
film.grid(column=0,row=0)

s = PhotoImage(file="srch.png")
v = PhotoImage(file="mic.png")

ttk.Button(mainframe, image=s, command=txtsrch).grid(column=2, row=0)
ttk.Button(mainframe, image=v, command=vcsrch).grid(column=3,row=0)

Label(mainframe, text="").grid(columnspan=3,row=2)
ttk.Button(mainframe, text="CLEAR", command=clear).grid(columnspan=2,row=2)
Label(mainframe, text="").grid(columnspan=3,row=3)
ttk.Button(mainframe, text="UPDATE", command=update).grid(columnspan=2,row=4)
Label(mainframe, text="").grid(columnspan=3,row=5)
stat=Label(mainframe, textvariable=status,fg="green").grid(columnspan=2,row=6)
tex=Text(bf, height=10, width=100,fg="blue")
tex.grid(row=5)

m_link = ttk.Entry(mainframe, width=100, textvariable=mplay).grid(columnspan=1,row=7)
#m_link.insert(0,'Paste the link to be played')
ttk.Button(mainframe, text="Play", command=play).grid(column=3,row=7)

root.mainloop()
