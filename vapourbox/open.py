#!/usr/bin/python3.4
import os
os.system("test -d /run/media/root/vapourbox/ || mkdir /run/media/root/vapourbox")
mountcheck=os.system('df -hT | grep nfs4 &> /dev/null')
if mountcheck!=0:
	os.system("mount -t nfs 192.168.122.234:/root/vapourbox/box1 /run/media/root/vapourbox/")
os.system("nautilus /run/media/root/vapourbox/")

