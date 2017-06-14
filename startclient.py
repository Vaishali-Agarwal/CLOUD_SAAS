#!/usr/bin/python2

import os,time,sys,commands,socket,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#s_ip is ip of server and s_port is portno. 
s_ip="192.168.122.78"
s_port=8888

print "Cloud service Reloaded plz enter authentication details"
time.sleep(1)

#server username
user=raw_input("Enter username : ")

#server password
password=getpass.getpass("Enter user password : ")

s.sendto(user,(s_ip,s_port))
s.sendto(password,(s_ip,s_port))

#sdata is data received from server
sdata=s.recvfrom(10)

if sdata[0]=="ok":
	print "Authentication successful!"
	print "Wait for the services..."
	time.sleep(1)
	execfile("saas.py")
else:
	print "Invalid Username and password"

