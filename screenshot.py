#!/usr/bin/python2

import os,sys,commands,time,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#s_ip is ip of server and s_port is portno. 
s_ip="192.168.122.78"
s_port=8888

os.system('sshpass -p 123 ssh -X test@'+s_ip+' gnome-screenshot')
execfile('saas.py')
