from tkinter import *
from tkinter import ttk
from SearchEngine import *


def txtsrch():
    result=srch(mname.get())
    #print(result)
    tex.insert(END,result)
def vcsrch():
    print("voice")
def clear():
    #print("clear")
    film.delete(0,END)
    tex.delete(1.0,END)
def update():
    print("")

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
#result = StringVar()

film = ttk.Entry(mainframe, width=80, textvariable=mname)
film.grid(column=0,row=0)

s = PhotoImage(file="srch.png")
v = PhotoImage(file="mic.png")

ttk.Button(mainframe, image=s, command=txtsrch).grid(column=1, row=0)
ttk.Button(mainframe, image=v, command=vcsrch).grid(column=2,row=0)

Label(mainframe, text="").grid(columnspan=3,row=2)
ttk.Button(mainframe, text="CLEAR", command=clear).grid(columnspan=2,row=2)
Label(mainframe, text="").grid(columnspan=3,row=3)
ttk.Button(mainframe, text="UPDATE", command=update).grid(columnspan=2,row=4)
Label(mainframe, text="").grid(columnspan=3,row=5)
tex=Text(bf, height=10, width=100)
tex.grid(row=5)

root.mainloop()
