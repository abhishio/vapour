#!/usr/bin/python3.4
import os
from tkinter import *
def formatdisk():
	top.quit()	
	os.system('umount /run/media/root/cloud")')
	os.system('gnome-disks --block-device /dev/sdb --format-device &')
	top.quit
	
top=Tk()
top.title('Format')
top.geometry('450x100')
active=os.system('iscsiadm -m session &> /dev/null')
if active ==0:
	label=Label(top, text='Warning!\nFormating will Delete all data', font='Helvetica -15 bold')
	label.pack()
	formatit=Button(top, text='Yes Format', command=formatdisk, bg='grey', fg='blue', activeforeground='white', activebackground='red')
	formatit.pack()
	exit=Button(top, text='Exit', command=top.quit, bg='grey', fg='blue', activeforeground='black', activebackground='white')
	exit.pack()

else :
	label=Label(top, text='\nNO ACTIVE SESSION\n', font='Helvetica -15 bold')
	label.pack()
	exit=Button(top, text='Exit', command=top.quit, bg='grey', fg='blue', activeforeground='black', activebackground='white')
	exit.pack()
	
mainloop()
