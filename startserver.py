#!/usr/bin/python2

import os,sys,commands,time,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("",8888))

#data stores the username ,ip and port no.
cdata=s.recvfrom(100)

#data1 stores user password ,ip and port no.
cdata1=s.recvfrom(100)


if cdata[0] == 'test' and cdata1[0] == '123' :
	s.sendto("ok",cdata[1])
else:
	s.sendto("Invalid",cdata[1])
