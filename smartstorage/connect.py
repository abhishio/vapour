#!/usr/bin/python3.4
import os
import tkinter
top = tkinter.Tk()
top.title('Connected')
top.geometry('400x50')

active=os.system('iscsiadm -m session &> /dev/null')
if active !=0:
	os.system("iscsiadm --mode node --targetname iqn.2003-01.org.linux-iscsi.vapour.x8664:sn.853ebf511960 --portal 192.168.122.234:3260 --login &> /dev/null")
	label = tkinter.Label(top, text='Connected to Vapour Box ', font='Helvetica -20 bold')
	label.pack()
	quit = tkinter.Button(top, text='Exit',command=top.quit)
	quit.pack()
else :
	label = tkinter.Label(top, text='Already Connected',font='Helvetica -20 bold')
	label.pack()
	quit = tkinter.Button(top, text='Exit',command=top.quit)
	quit.pack()
tkinter.mainloop()
