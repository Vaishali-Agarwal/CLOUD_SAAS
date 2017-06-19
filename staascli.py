#!/usr/bin/python

import  os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.122.78"
s_port=9999

print "		......................................."
print "		    Welcome to the STAAS Services"
print "		......................................."
print "\n"
print "   Press 1 for New Storage?"
print "   Press 2 for Extended Storage?"
print "\n"
#choice of the user
choice=raw_input()
if choice == '1' :
	drive_name=raw_input("enter  storage  drive  name  :  ")
	drive_size=raw_input("enter  drive  size (like 300M ,10G) :  ")
	s.sendto(choice,(s_ip,s_port))
	s.sendto(drive_name,(s_ip,s_port))
	s.sendto(drive_size,(s_ip,s_port))

	
elif choice == '2' :
	drive_name=raw_input("enter  storage  drive  name to extend :  ")
	drive_size=raw_input("enter  size(like 300M ,10G ) by which u want to extend the drive :  ")
	s.sendto(choice,(s_ip,s_port))
	s.sendto(drive_name,(s_ip,s_port))
	s.sendto(drive_size,(s_ip,s_port))
else :
	print "Enter your choice correctly"

res=s.recvfrom(4)
if   res[0]  ==  "done" :
	os.system('mkdir   /media/'+drive_name)
	os.system('mount  '+s_ip+':/mnt/'+drive_name+'   /media/'+drive_name)
        print res[0]
else  :
	print   "No response  from  storage  cloud "



