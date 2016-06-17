#!/usr/bin/python2.7
import Tkinter as tk
import subprocess
import os
import commands as cmd
import socket as sk
import cPickle as pic
from Crypto.Cipher import AES
import thread
import os
s=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
host=""
port=60101
server=''
s.bind((host,port))
def pick(msg):
	return pic.dumps(msg)
def rpick(msg):
	return pic.loads(msg)
def encrypt(msg):
	block=16
	padd='{'
	pmsg=pick(msg)
	ppmsg=pmsg+(block-len(pmsg)%block)*padd
	cipher=AES.new('\x195"\xd0\xc9\x88\xb8\xfa\x89\x92\x83\x87\x1ai5\xf1')
	ciphertxt=cipher.encrypt(ppmsg)
	return ciphertxt
	
def dcrypt(ciphertxt):
	padd='{'
	cipher=AES.new('\x195"\xd0\xc9\x88\xb8\xfa\x89\x92\x83\x87\x1ai5\xf1')
	plaintxt=cipher.decrypt(ciphertxt)
	rptxt=rpick(plaintxt)
	return rptxt
'''s.sendto(encrypt(sendi),(host,50000))
r=dcrypt(s.recv(1000))'''
def sendto(msg):
	emsg=encrypt(msg)
	s.sendto(emsg,(server,50100))
def recvf():
	r=dcrypt(s.recv(1000))
	return r
LoginStatus=cmd.getstatusoutput('cat flakes/flogin.txt')[1]
top=tk.Tk()
top.title("Flakes")
root=tk.Frame(top)
signup=tk.Frame(top)
login=tk.Frame(top)
logged=tk.Frame(top)

for f in (root, signup, login,logged):
            f.grid(row=0, column=0, sticky="nsew")
def loginfn():
	info={'ch':1,'uname':logEntry1.get(),'passwd':logEntry2.get()}
	if info['uname']==''or info['passwd']=='':
		popinfo("Error","Invalid Entry")
	else:
		sendto(info)
		LoginStatus=recvf()	
		if LoginStatus=='True':
			os.system('echo "True" > flakes/flogin.txt')
			userName=info['uname']
			loggedLabel.configure(text='Hi %s'%userName)
			log()
		else:
			popinfo("Error","Login Failed\nTry Again")
			logEntry2.delete(0,tk.END)
def log():
	logged.tkraise()
	subprocess.Popen(["flakes/flakeslogged.py"])
	
def logout():
	global LoginStatus
	LoginStatus='False'
	os.system('echo "False" > flakes/flogin.txt')
	subprocess.Popen(["killall","-9","flakeslogged.py"])
	root.tkraise()

def popinfo(wtitle,msg):
	topWind=tk.Toplevel()
	topWind.title(wtitle)
	topWind.geometry('300x100')
	tMsg=tk.Message(topWind,text=msg,width=300)
	tMsg.pack(anchor='center',fill=tk.X,padx=2,pady=2)
	tBtn=tk.Button(topWind,text="Close",command=topWind.destroy)
	tBtn.pack(padx=2,pady=2)

def getspin(sb,llimit,hlimit):
	
	sin=int(expandSB.get())
	if sin not in range(llimit,hlimit+1):
		popinfo("Error","Out of Range")
		if sin>=hlimit:
			sb.delete(0,tk.END)
			sb.insert(0,hlimit)
		else:
			sb.delete(0,tk.END)
			sb.insert(0,llimit)
def signcreate():
	uName=signUName.get()
	uPass=signPass.get()
	uCPass=signCPass.get()
	
	e=[]
	if not uName.isalpha() or uName =='':
		e.append("username: alphabet only")
	if uPass!=uCPass or uName =='':
		e.append("Password Not Matched")
	
	def poperror(emsg):
		topWind=tk.Toplevel()
		topWind.title("Error")
		topWind.geometry('300x100')
		for emsg in e:
	        	tMsg=tk.Message(topWind,text=emsg,width=300).pack(expand=1,fill=tk.X)
		tBtn=tk.Button(topWind,text="Close",command=topWind.destroy)
		tBtn.pack(padx=2,pady=2)
	if uName=='' and uPass=='' and uCPass=='':
		popinfo("Error","Incomplete Form")
	elif e !=[]:
		poperror(e)
		signPass.delete(0,tk.END)
		signCPass.delete(0,tk.END)
		
	else:
		info={'ch':2,'uname':uName,'passwd':uPass}
		sendto(info)
		stat=recvf()
		if stat=="True":
			popinfo("Congrats","Account Created")
			login.tkraise()
		else: popinfo("Error","Account Exists")
		   
label=tk.Label(root, text='Flakes', font='Helvetica -24 bold').pack(fill=tk.Y, expand=1,side=tk.TOP,padx=2,pady=2)
mainFrame1=tk.Frame(root)
mainFrame2=tk.Frame(root)
mainBtn1=tk.Button(mainFrame1,text='login',command=login.tkraise).pack(side=tk.LEFT,padx=2,pady=2)
mainBtn2=tk.Button(mainFrame1,text='Signup',command=signup.tkraise).pack(side=tk.RIGHT,padx=2,pady=2)
mainBtn3=tk.Button(mainFrame2,text='Quit',command=top.quit).pack(side=tk.RIGHT,padx=2,pady=2)
mainFrame1.pack()
mainFrame2.pack()

logFrame1=tk.Frame(login)
logFrame2=tk.Frame(login)
logFrame3=tk.Frame(login)
logBtn1=tk.Button(logFrame1,text='Username').pack(side=tk.LEFT,padx=2,pady=2)
logEntry1=tk.Entry(logFrame1)
logEntry1.pack(side=tk.RIGHT,padx=2,pady=2)
logBtn2=tk.Button(logFrame2,text='password').pack(side=tk.LEFT,padx=2,pady=2)
logEntry2=tk.Entry(logFrame2,show="*")
logEntry2.pack(side=tk.RIGHT,padx=2,pady=2)
logBtn3=tk.Button(logFrame3,text='Login',command=loginfn).pack(side=tk.LEFT,padx=2,pady=2)	
logBtn4=tk.Button(logFrame3,text='Cancel',command=root.tkraise).pack(side=tk.RIGHT,padx=2,pady=2)
logFrame1.pack()
logFrame2.pack()
logFrame3.pack()


loggedFrame=tk.Frame(logged)
loggedLabel=tk.Label(loggedFrame,text="Hi ",font='Helvetica -24 bold')
loggedLabel.pack(fill=tk.Y, expand=1,side=tk.TOP,padx=2,pady=2)
loggedOpenBtn=tk.Button(loggedFrame,text="Open",command=log).pack(padx=2,pady=2)
loggedBtn=tk.Button(loggedFrame,text="Logout",command=logout, bg='green', fg='blue', activeforeground='white', activebackground='red').pack(padx=2,pady=2)
loggedFrame.pack()

signFrame1=tk.Frame(signup)
signFrame2=tk.Frame(signup)
signUNameBtn=tk.Button(signFrame1,text='Username')
signUName=tk.Entry(signFrame1)
signPassBtn=tk.Button(signFrame1,text='Password')
signPass=tk.Entry(signFrame1,show="*")
signCPassBtn=tk.Button(signFrame1,text='Confirm Password')
signCPass=tk.Entry(signFrame1,show="*")
signUNameBtn.grid(row=0,column=0,sticky='we',padx=2,pady=2)
signUName.grid(row=0,column=1,sticky='we',padx=2,pady=2)
signPassBtn.grid(row=1,column=0,sticky='we',padx=2,pady=2)
signPass.grid(row=1,column=1,sticky='we',padx=2,pady=2)
signCPassBtn.grid(row=2,column=0,sticky='we',padx=2,pady=2)
signCPass.grid(row=2,column=1,sticky='we',padx=2,pady=2)
signCreateBtn=tk.Button(signFrame2,text='Create',command=signcreate).pack(side=tk.LEFT,padx=2,pady=2)
signCancelBtn=tk.Button(signFrame2,text='Cancel',command=root.tkraise).pack(side=tk.RIGHT,padx=2,pady=2)
signFrame1.pack()
signFrame2.pack()


root.tkraise()
top.resizable(0,0)
tk.mainloop()


