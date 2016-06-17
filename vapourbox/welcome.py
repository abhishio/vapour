#!/usr/bin/python3.4
import os
from tkinter import *
from tkinter.messagebox import showinfo
from threading import Thread

top=Tk()
top.title('Vapour Box')
top.geometry('300x100')

f1=Frame(top)
f2=Frame(top)

label=Label(top, text='Vapour Box', font='Helvetica -24 bold')
label.pack(fill=Y, expand=1,side=TOP)

def CONNECT():
	os.system('python3.4 open.py')
def SHOWDISK():
	os.system('./showdisk.sh')	
def DISCONNECT():
	os.system('python3.4 disconnect.py')
		
Connect=Button(f1, text='Connect', command=CONNECT, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Connect.pack(fill=X,expand=1,side=LEFT)

Disconnect=Button(f1, text='Disconnect', command=DISCONNECT, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Disconnect.pack(fill=X,expand=1,side=RIGHT)

quit=Button(f2, text='Exit', command=top.quit, bg='red', fg='blue', activeforeground='white', activebackground='green')
quit.pack()
f1.pack()
f2.pack()

top.resizable(width=FALSE, height=FALSE)
mainloop()
