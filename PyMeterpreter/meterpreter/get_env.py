from sys import platform
from _winreg import *

registry_enumvals = [x for x in range(3)]
registry_enumvals[0] = ("HKEY_CURRENT_USER\\Volatile Environment")
registry_enumvals[1] = ("HKEY_CURRENT_USER\\Environment")
registry_enumvals[2] = ("HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment")

def list_env_vars(var_names):
	print ("Getting all System and User Variables")

	for register in var_names:
		if register.startswith("HKEY_CURRENT_USER"):
			openregisters = ConnectRegistry(None,HKEY_CURRENT_USER)
			RunKey = OpenKey(openregisters, "".join(register.split("HKEY_CURRENT_USER\\")))
		else:
			openregisters = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
			RunKey = OpenKey(openregisters, "".join(register.split("HKEY_LOCAL_MACHINE\\")))
		
		for i in range(200):
			try:
				n,v,t = EnumValue(RunKey,i)
				print v,n.lower()
			except:
				pass


if platform.startswith('win'):
	list_env_vars(registry_enumvals)
else:
	print ("This version of Meterpreter is not supported with this Script!")



