#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from utilsh import *



def pyfish_iswow64():
	return True if IsWow64Process() else False


#return pafish_exists_regkey(HKEY_LOCAL_MACHINE, "SOFTWARE\\Oracle\\VirtualBox Guest Additions");
def pyfish_exists_regkey(HKEY, regkey_s):
	try:
		register = ConnectRegistry(None, HKEY)
		OpenKey(register, regkey_s)
		return True
	except:
		return False


#pafish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, "HARDWARE\\Description\\System", "VideoBiosVersion", "VIRTUALBOX");
def pyfish_exists_regkey_value_str(HKEY, regkey_s, value_s, lookup):
	openregisters = ConnectRegistry(None,HKEY)
	RunKey = OpenKey(openregisters, regkey_s)
	for i in range(1024):
		try:
			n,v,t = EnumValue(RunKey,i)
			sleep(0.1)
			if n == value_s:
				if lookup in str(v):
					return True
		except:
			pass
	CloseKey(RunKey)
	return False


def pyfish_exists_file( filename):
	return True if path.isfile(filename) else False
	

def pyfish_check_mac_vendor( mac_vendor): 
	#pip install netifaces
	if list(ifaddresses(interfaces()[0]).iteritems())[0][1][0]['addr'].startswith(mac_vendor):
		return True
	else:
		return False


#int pafish_check_adapter_name(char * name) {}
#int wmi_initialize(const wchar_t *query_namespace, IWbemServices **services) {}
#void wmi_cleanup(IWbemServices *services) {}
