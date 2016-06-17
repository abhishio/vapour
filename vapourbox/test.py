#!/usr/bin/python
from Tkinter import *
t=Tk()
v=StringVar(t)
v.set("Select")
t=OptionMenu(t,v,"Red Hat","Ubuntu","Kali").pack()
l=Listbox(t)
l.pack()
l.insert(END,"Fist val")
for i in ["second","third","forth"]:
	l.insert(END,i)
def popinfo(wtitle,msg):
	print("reached 5")
	topWind=Toplevel()
	topWind.title(wtitle)
	topWind.geometry('300x100')
	tMsg=Message(topWind,text=msg)
	tMsg.pack(expand=1,fill=X,padx=2,pady=2)
	tBtn=Button(topWind,text="Close",command=topWind.destroy)
	tBtn.pack(padx=2,pady=2)
	print("reached 6")
def getspin():
	sb,llimit,hlimit=s,512,2048
	print("reached 1")
	sin=int(sb.get())
	print(type(sin))
	print ("reached 1.1")
	print (type(llimit))
	if sin not in range(llimit,hlimit+1):
		print("reached 2")
		popinfo("Error","Out of Range")
		if sin>=hlimit:
			print("reached 4")
			sb.delete(0,tk.END)
			sb.insert(0,hlimit)
		else:
			print("reached 4")
			sb.delete(0,tk.END)
			sb.insert(0,llimit)
	else : print "here"
s=Spinbox(t,from_=512, to=2048,textvariable=1024)
s.pack()
b=Button(t,text="spinbox",command=getspin())
b.pack()

mainloop()
