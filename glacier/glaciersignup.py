#!/usr/bin/python
import os
import Tkinter as tk
import subprocess
import socket as sk
import cPickle as pic
from Crypto.Cipher import AES
import thread
import os
s=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
host=""
port=60202
s.bind((host,port))
server=''

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

def sendto(msg):
	emsg=encrypt(msg)
	s.sendto(emsg,(server,50211))
def recvf():
	r=dcrypt(s.recv(1000))
	return r



signup=tk.Tk()
signup.title("Singup")
signFrame1=tk.Frame(signup)
signFrame2=tk.Frame(signup)

def popinfo(wtitle,msg):
	topWind=tk.Toplevel()
	topWind.title(wtitle)
	topWind.geometry('300x100')
	tMsg=tk.Message(topWind,text=msg,width=300)
	tMsg.pack(anchor='center',fill=tk.X,padx=2,pady=2)
	tBtn=tk.Button(topWind,text="Close",command=topWind.destroy)
	tBtn.pack(padx=2,pady=2)

def signcreate():
	uName=signUName.get()
	uPass=signPass.get()
	uCPass=signCPass.get()
	uRam=int(signRamSB.get())
	uCpu=int(signCpuSB.get())
	uOS=osType.get()
	uVar=osTypeVar.get()	
	uSize=int(signSizeSB.get())
	e=[]
	if not uName.isalpha() or uName =='':
		e.append("username: alphabet only")
	if uPass!=uCPass or uPass =='':
		e.append("Password Not Matched")
	if uRam not in range(512,2049):
		e.append("Ram Out of Range")
	if uCpu not in range(1,3):
		e.append("Cpu Out of Range")
	if uOS=='Select':
		e.append("Select OS")
	if uVar=='Select OS First':
		e.append("Select Variant")
	if  uSize not in range(1,11):
		e.append("Size Out of Range")
	
	def poperror(emsg):
		topWind=tk.Toplevel()
		topWind.title("Error")
		topWind.geometry('300x200')
		for emsg in e:
	        	tMsg=tk.Message(topWind,text=emsg,width=300).pack(expand=1,fill=tk.X)
		tBtn=tk.Button(topWind,text="Close",command=topWind.destroy)
		tBtn.pack(padx=2,pady=2)
	if e !=[]:
		poperror(e)
		signUName.delete(0,tk.END)
		signPass.delete(0,tk.END)
		signCPass.delete(0,tk.END)
		signCpuSB.delete(0,tk.END)
		signCpuSB.insert(0,'1')
		if uRam>=2048:
			signRamSB.delete(0,tk.END)
			signRamSB.insert(0,'2048')
		else:
			signRamSB.delete(0,tk.END)
			signRamSB.insert(0,'512')
		if uSize>=10:
			signSizeSB.delete(0,tk.END)
			signSizeSB.insert(0,'10')
		else:
			signSizeSB.delete(0,tk.END)
			signSizeSB.insert(0,sizeFrom)
	else: 
		info={'ch':2,'uname':uName,'passwd':uPass,'ram':uRam,'cpu':uCpu,'os':uOS,'osvar':uVar,'disksize':uSize}
		sendto(info)
		stat=recvf()
		if stat=="True":
			popinfo("Congrats","Account Created")
			signup.destroy()
		else: popinfo("Error","Account Exists")

osTypeVar=tk.StringVar()
osTypeVar.set("Select OS First")
osTypeVarTuple=["Select OS First"]

def glconfig(osTy):
	global sizeFrom
	if(osTy=="Red Hat"):
		osTypeVarTuple=["Rhel6","Rhel7"]
		signSizeSB.config(from_=6)
	elif (osTy=="Android"):
		osTypeVarTuple=["Kitkat","Lollipop","Marshmallow"]
		sizeFrom=2
		signSizeSB.config(from_=sizeFrom)
		signSizeSB.delete(0,tk.END)
		signSizeSB.insert(0,'2')
	elif (osTy=="Ubuntu"):
		osTypeVarTuple=["Ubuntu","Ubuntu Mate","Kubuntu","Lubuntu"]
		sizeFrom=6
		signSizeSB.config(from_=sizeFrom)
	signTypeVarMod=signVariantOM.children['menu']
	signTypeVarMod.delete(0,tk.END)
	for val in osTypeVarTuple:
		signTypeVarMod.add_command(label=val,command=lambda v=osTypeVar,l=val:v.set(l))
	osTypeVar.set(osTypeVarTuple[0])
	


signUNameBtn=tk.Button(signFrame1,text='Username')
signUName=tk.Entry(signFrame1)
signPassBtn=tk.Button(signFrame1,text='Password')
signPass=tk.Entry(signFrame1,show="*")
signCPassBtn=tk.Button(signFrame1,text='Confirm Password')
signCPass=tk.Entry(signFrame1,show="*")
signRamBtn=tk.Button(signFrame1,text="Ram (MB)")
signRamSB=tk.Spinbox(signFrame1,from_=512,to=1024)
signCpuBtn=tk.Button(signFrame1,text="CPU")
signCpuSB=tk.Spinbox(signFrame1,from_=1,to=2)
signOSTypeBtn=tk.Button(signFrame1,text="OS")
osType=tk.StringVar()
osType.set("Select")
signOSTypeOM=tk.OptionMenu(signFrame1,osType,"Ubuntu","Android","Red Hat",command=glconfig)
signVariantOM=apply(tk.OptionMenu, (signFrame1, osTypeVar) + tuple(osTypeVarTuple))

signVariantBtn=tk.Button(signFrame1,text="Variants")
signSizeBtn=tk.Button(signFrame1,text='Hard Disk(GB)')
sizeFrom=6
signSizeSB=tk.Spinbox(signFrame1,from_=sizeFrom,to=10)

signUNameBtn.grid(row=0,column=0,sticky='we',padx=2,pady=2)
signUName.grid(row=0,column=1,sticky='we',padx=2,pady=2)
signPassBtn.grid(row=1,column=0,sticky='we',padx=2,pady=2)
signPass.grid(row=1,column=1,sticky='we',padx=2,pady=2)
signCPassBtn.grid(row=2,column=0,sticky='we',padx=2,pady=2)
signCPass.grid(row=2,column=1,sticky='we',padx=2,pady=2)
signRamBtn.grid(row=3,column=0,sticky='we',padx=2,pady=2)
signRamSB.grid(row=3,column=1,sticky='we',padx=2,pady=2)
signCpuBtn.grid(row=4,column=0,sticky='we',padx=2,pady=2)
signCpuSB.grid(row=4,column=1,sticky='we',padx=2,pady=2)

signOSTypeBtn.grid(row=6,column=0,sticky='we',padx=2,pady=2)
signOSTypeOM.grid(row=6,column=1,sticky='we',padx=2,pady=2)
signVariantBtn.grid(row=7,column=0,sticky='we',padx=2,pady=2)
signVariantOM.grid(row=7,column=1,sticky='we',padx=2,pady=2)
signSizeBtn.grid(row=8,column=0,sticky='we',padx=2,pady=2)
signSizeSB.grid(row=8,column=1,sticky='we',padx=2,pady=2)
signCreateBtn=tk.Button(signFrame2,text='Create',command=signcreate).pack(side=tk.LEFT,padx=2,pady=2)
signCancelBtn=tk.Button(signFrame2,text='Cancel',command=signup.quit).pack(side=tk.RIGHT,padx=2,pady=2)
signFrame1.pack(anchor=tk.CENTER)
signFrame2.pack(anchor=tk.CENTER)

signup.resizable(0,0)
tk.mainloop()
