#!/usr/bin/python2

import os,time,sys,socket

x="""
  Press 1 to get firefox
  Press 2 to get vlc
  Press 3 to get open office
  Press 4 to get screenshot
  Press 5 to get calculator
  Press 6 to get webcam
  Press 7 to get imageviewer
  Press 0 to exit
 """

print x

ch=raw_input()

if ch=="1":
	execfile("firefox.py")
elif ch=="2":
	execfile("vlc.py")
elif ch=="3":
	execfile("open office.py")
elif ch=="4":
	execfile("screenshot.py")
elif ch=="5":
	execfile("calculator.py")
elif ch=="6":
	execfile("webcam.py")
elif ch=="7":
	execfile("imageviewer.py")
elif ch=="0":
	exit
else:
	print "Wrong Choice"

