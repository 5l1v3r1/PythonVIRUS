#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from utils import *

def vmware_reg_key1():
	res = False
	for x in range(3):
		path = "HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port %s\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0" % str(x)
		try:
			if pyfish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, path, "Identifier", "VMWARE"):
				res = True;
			else:
				res = False;
		except:
			continue
	return res

def vmware_reg_key2():
	return pyfish_exists_regkey(HKEY_LOCAL_MACHINE, "SOFTWARE\\VMware, Inc.\\VMware Tools");

def vmware_sysfile1():
	return pyfish_exists_file("C:\\WINDOWS\\system32\\drivers\\vmmouse.sys");

def vmware_sysfile2():
	return pyfish_exists_file("C:\\WINDOWS\\system32\\drivers\\vmhgfs.sys");


def vmware_mac():
	"""
		VMware is any of
		00:05:69
		00:0C:29
		00:1C:14
		00:50:56
	"""
	if pyfish_check_mac_vendor("00:05:69"):
		return True
	elif pyfish_check_mac_vendor("00:0C:29"):
		return True
	elif pyfish_check_mac_vendor("00:1C:14"):
		return True
	elif pyfish_check_mac_vendor("00:50:56"):
		return True
	else:
		return False


#int vmware_adapter_name() {}
#int vmware_devices(int writelogs) {}
#int vmware_wmi_check_row(IWbemClassObject *row) {}
#int vmware_wmi_serial() {}