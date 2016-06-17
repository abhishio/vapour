#!/usr/bin/python3.4
import os
import tkinter

active=os.system('iscsiadm -m session &> /dev/null')
if active ==0:
	os.system("test -d /run/media/root/cloud || mkdir /run/media/root/cloud")
	mountcheck=os.system('grep -q "/dev/sdb" /proc/mounts')
	if mountcheck!=0:
		os.system("mount /dev/sdb /run/media/root/cloud/")
	os.system("nautilus /run/media/root/cloud/")
	
else :
	top = tkinter.Tk()
	top.title('Error')
	top.geometry('400x50')
	label = tkinter.Label(top, text='NO ACTIVE SESSION',font='Helvetica -20 bold')
	label.pack()
	quit = tkinter.Button(top, text='Exit',command=top.quit)
	quit.pack()
tkinter.mainloop()
