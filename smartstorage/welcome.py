#!/usr/bin/python3.4
import os
import tkinter as tk

top=tkTk()
top.title('Vapour Smart Disk')
top.geometry('300x150')

f1=tk.Frame(top)
f2=tk.Frame(top)
f3=tk.Frame(top)
label=tk.Label(top, text='Vapour Smart Disk', font='Helvetica -24 bold')
label.pack()

def CONNECT():
	os.system('python3.4 connect.py')
def SHOWDISK():
	os.system('./showdisk.sh')	
def OPEN():
	os.system('python3.4 mount.py')
def FORMAT():
	os.system('python3.4 format.py')
def DISCONNECT():
	os.system('python3.4 disconnect.py')
		
Connect=tk.Button(f1, text='Connect', command=CONNECT, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Connect.pack(fill=X,side=LEFT, expand=1)

Showdisk=tk.Button(f2, text='Show Disk', command=SHOWDISK, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Showdisk.pack(fill=X,side=LEFT, expand=1)

Open=tk.Button(f2, text='Open Disk', command=OPEN, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Open.pack(fill=X,side=RIGHT, expand=1)

Format=tk.Button(f3, text='Format', command=FORMAT, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Format.pack(fill=X, expand=1)

Disconnect=tk.Button(f1, text='Disconnect', command=DISCONNECT, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Disconnect.pack(fill=X,side=RIGHT, expand=1)

quit=tk.Button(f3, text='Exit', command=top.quit, bg='red', fg='blue', activeforeground='white', activebackground='green')
quit.pack(fill=X, expand=1)
f1.pack()
f2.pack()
f3.pack()

mainloop()
