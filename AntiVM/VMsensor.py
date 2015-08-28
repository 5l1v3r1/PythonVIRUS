from _winreg import *
import os
import psutil

"""	
 ___            _                             ___ 
| _ ) ___ _ __ | |__  ___ _ _ _ __  __ _ _ _ / __|
| _ \/ _ \ '  \| '_ \/ -_) '_| '  \/ _` | ' \\__ \
|___/\___/_|_|_|_.__/\___|_| |_|_|_\__,_|_||_|___/
     				Bomberman & B3mB4m & T-Rex   
Concat : b3mb4m@tuta.io
"""


class TestVM(object):	
	def checkVirtualMachine(self):
		openregisters = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
		RunKey = OpenKey(openregisters, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
		for i in range(20):
			try:
				n,v,t = EnumValue(RunKey,i)
				if "vboxtray" in n.lower() or "vbox" in n.lower():
					return True;
			except:
				pass	
		CloseKey(RunKey)
		self.startupcheck2()


	def startupcheck2(self):
		try:
			for x, xx, files in os.walk(r"C:\Documents and Settings"):
				if len(files) != 0:
					files = [x.lower() for x in files]
					if "vbox" in files: 
						return True;    
		except:
			pass				


	def regeditcheck(self):
		vbox = ["VboxGuest", "VboxMouse", "VboxService", "VboxService", "VboxVideo"]
		for x in vbox:
			try:
				openregisters = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
				path = r"SYSTEM\ControlSet001\Services\%s" % x
				RunKey = OpenKey(openregisters, path)
				return True;
			except:
				pass	
		self.system32()		

	def system32(self):
		try:
			for files in os.listdir("C:\WINDOWS\system32"):
				if "VBox" in files:
					return True;
		except:	
			pass
		self.graphiccard()


	def graphiccard(self):
		if os.path.isdir(r"C:\Program Files\Oracle\VirtualBox Guest Additions"):
			return True;
		if os.path.isdir(r"C:\WINDOWS\system32\DRVSTORE"):
			for folder in os.listdir(r"C:\WINDOWS\system32\DRVSTORE"):
				if folder.startswith("VBox"):
					return True;
		self.pids()			


	def pids(self):
		for proc in psutil.process_iter():
			try:
				if "VBox" in proc.name():
					print proc.name()
			except:
				pass
		return False
				
#from new import TestVM 
#print TestVM().checkVirtualMachine()				
