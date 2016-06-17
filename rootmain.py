#!/usr/bin/python2.7
try:
	import os
	import Tkinter as tk
	import subprocess
except:
	#!/usr/bin/python3.4
	import os
	import tkinter as tk
	import subprocess


top=tk.Tk()
top.title("Vapour Cloud")
top.configure(background='black')
f=tk.Frame(top)
w,h=128,128
saasImg=tk.PhotoImage(width=w,height=h,file='root/saas.gif')
saasLabel=tk.Label(f,image=saasImg)
saasLabel.image=saasImg
saasBtn=tk.Button(f,text='Flakes',command=lambda:subprocess.Popen(["flakes/flakesmain.py"]))
iaasImg=tk.PhotoImage(width=w,height=h,file='root/iaas.gif')
iaasLabel=tk.Label(f,image=iaasImg)
iaasLabel.image=iaasImg
iaasBtn=tk.Button(f,text='Glacier',command=lambda:subprocess.Popen(["glacier/glaciermain.py"]))
boxImg=tk.PhotoImage(width=w,height=h,file='root/object.gif')
boxLabel=tk.Label(f,image=boxImg)
boxLabel.image=boxImg
boxBtn=tk.Button(f,text='Vapour Box',command=lambda:subprocess.Popen(["vapourbox/boxmain.py"]))
smartImg=tk.PhotoImage(width=w,height=h,file='root/block.gif')
smartLabel=tk.Label(f,image=smartImg)
smartLabel.image=smartImg
smartBtn=tk.Button(f,text='Smart Storage',command=lambda:subprocess.Popen(["smartstorage/smartmain.py"]))

saasLabel.grid(row=0,column=0,padx=15,pady=15,sticky='nsew')
iaasLabel.grid(row=0,column=1,padx=15,pady=15,sticky='nsew')
boxLabel.grid(row=2,column=0,padx=15,pady=15,sticky='nsew')
smartLabel.grid(row=2,column=1,padx=15,pady=15,sticky='nsew')
saasBtn.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
iaasBtn.grid(row=1,column=1,padx=5,pady=5,sticky='ew')
boxBtn.grid(row=3,column=0,padx=5,pady=5,sticky='ew')
smartBtn.grid(row=3,column=1,padx=5,pady=5,sticky='ew')
f.configure(background='black')
f.pack()
quitBtn=tk.Button(top,text='Quit',command=top.quit,bg='green', fg='blue', activeforeground='white', activebackground='red').pack(padx=20,pady=20,)


top.resizable(0,0)
tk.mainloop()


