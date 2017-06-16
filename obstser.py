#!/usr/bin/python

import  os,commands,sys,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",9999))




#  data  will recv  drive  name 
data=s.recvfrom(20)
d_name=data[0]
#  data1  will recv  drive  size 
data1=s.recvfrom(10)
d_size=data1[0]
#  here  client  address will be stored  
cliaddr=data1[1][0]
print d_name
print d_size
print  cliaddr
# creating  LVM by the name of  client  drive  

os.system('lvcreate -V'+d_size+' --name  '+d_name+'  --thin vaishali/pool')

# now time for  format  client  drive with  ext4 /  xfs  
os.system('mkfs.ext4   /dev/vaishali/'+d_name)
# now creating  mount point  
os.system('mkdir   /mnt/'+d_name)
# now mounting   drive locallly  
os.system('mount  /dev/vaishali/'+d_name+'  /mnt/'+d_name)
#  Now  time  for  NFS server  configuration 

nfs_install=os.system('rpm -q nfs-utils')
if nfs_install== 0 :
	print "Already install"
else : 
	os.system('yum  install   nfs-utils  -y')
#making  entry  in  Nfs export  file 
entry="/mnt/"+d_name+"  "+cliaddr+"(rw,no_root_squash)"
#  appending  this  var  to  /etc/exports  file 
f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()
# finally  starting  nfs  service  and service  persistant 
#os.system('systemctl   restart  nfs-server')
#os.system('systemctl   enable  nfs-server')
check=os.system('exportfs  -r')
if  check  ==    0 :
	s.sendto("done",data1[1])
else :
	print   "plz  check  your  code  "





