#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from utils import *


#SCSI registry key check
def vbox_reg_key1():
	return pyfish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, "HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port 0\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0", "Identifier", "VBOX");


#SystemBiosVersion registry key check
def vbox_reg_key2():
	return pyfish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, "HARDWARE\\Description\\System", "SystemBiosVersion", "VBOX");


#VirtualBox Guest Additions key check
def vbox_reg_key3():
	return pyfish_exists_regkey(HKEY_LOCAL_MACHINE, "SOFTWARE\\Oracle\\VirtualBox Guest Additions");


#VideoBiosVersion key check
def vbox_reg_key4():
	return pyfish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, "HARDWARE\\Description\\System", "VideoBiosVersion", "VIRTUALBOX");


#ACPI Regkey detection
def vbox_reg_key5():
	return pyfish_exists_regkey(HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\DSDT\\VBOX__");


#FADT ACPI Regkey detection
def vbox_reg_key7():
	return pyfish_exists_regkey(HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\FADT\\VBOX__");


#RSDT ACPI Regkey detection
def vbox_reg_key8():
	return pyfish_exists_regkey(HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\RSDT\\VBOX__");


#VirtualBox Services Regkey detection
def vbox_reg_key9( writelogs=None):
	res = False
	strs = ["" for x in range(5)]
	strs[0] = "SYSTEM\\ControlSet001\\Services\\VBoxGuest";
	strs[1] = "SYSTEM\\ControlSet001\\Services\\VBoxMouse";
	strs[2] = "SYSTEM\\ControlSet001\\Services\\VBoxService";
	strs[3] = "SYSTEM\\ControlSet001\\Services\\VBoxSF";
	strs[4] = "SYSTEM\\ControlSet001\\Services\\VBoxVideo";
	for i in range(5):
		if (pyfish_exists_regkey(HKEY_LOCAL_MACHINE, strs[i])):
			message = "VirtualBox traced using Reg key HKLM\\%s" % (strs[i]);
			print message
			if writelogs != None:
				write_logs(message)
				res = True
	return res


#HARDWARE\\DESCRIPTION\\System SystemBiosDate == 06/23/99
def vbox_reg_key10():
	return pyfish_exists_regkey_value_str(HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System", "SystemBiosDate", "06/23/99");


#VirtualBox driver files in \\WINDOWS\\system32\\drivers\\
def vbox_sysfile1( writelogs=None):
	res = False
	strs = ["" for x in range(4)]
	strs[0] = "C:\\WINDOWS\\system32\\drivers\\VBoxMouse.sys";
	strs[1] = "C:\\WINDOWS\\system32\\drivers\\VBoxGuest.sys";
	strs[2] = "C:\\WINDOWS\\system32\\drivers\\VBoxSF.sys";
	strs[3] = "C:\\WINDOWS\\system32\\drivers\\VBoxVideo.sys";
	for i in range(4):
		if (pyfish_exists_file(strs[i])):
			message = "VirtualBox traced using driver file %s" % (strs[i]);
			print message
			if writelogs != None:
				write_logs(message)
				res = True
	return res;


#VirtualBox other system files
def vbox_sysfile2( writelogs=None):
	res = False
	strs = ["" for x in range(14)]
	strs[0] = "C:\\WINDOWS\\system32\\vboxdisp.dll";
	strs[1] = "C:\\WINDOWS\\system32\\vboxhook.dll";
	strs[2] = "C:\\WINDOWS\\system32\\vboxmrxnp.dll";
	strs[3] = "C:\\WINDOWS\\system32\\vboxogl.dll";
	strs[4] = "C:\\WINDOWS\\system32\\vboxoglarrayspu.dll";
	strs[5] = "C:\\WINDOWS\\system32\\vboxoglcrutil.dll";
	strs[6] = "C:\\WINDOWS\\system32\\vboxoglerrorspu.dll";
	strs[7] = "C:\\WINDOWS\\system32\\vboxoglfeedbackspu.dll";
	strs[8] = "C:\\WINDOWS\\system32\\vboxoglpackspu.dll";
	strs[9] = "C:\\WINDOWS\\system32\\vboxoglpassthroughspu.dll";
	strs[10] = "C:\\WINDOWS\\system32\\vboxservice.exe";
	strs[11] = "C:\\WINDOWS\\system32\\vboxtray.exe";
	strs[12] = "C:\\WINDOWS\\system32\\VBoxControl.exe";
	strs[13] = "C:\\program files\\oracle\\virtualbox guest additions\\";
	for i in range(14):
		if (pyfish_exists_file(strs[i])):
			message = "VirtualBox traced using system file %s" % (strs[i])
			print message
			if writelogs != None:
				write_logs(message)
				res = True
	return res;


#NIC MAC check
def vbox_mac():
	#VirtualBox mac starts with 08:00:27
	return pyfish_check_mac_vendor("08:00:27")


def _CreateFile(filename):
    CreateFile_Fn = windll.kernel32.CreateFileW
    CreateFile_Fn.argtypes = [
            wintypes.LPWSTR,                    # _In_          LPCTSTR lpFileName
            wintypes.DWORD,                     # _In_          DWORD dwDesiredAccess
            wintypes.DWORD,                     # _In_          DWORD dwShareMode
            LPSECURITY_ATTRIBUTES,              # _In_opt_      LPSECURITY_ATTRIBUTES lpSecurityAttributes
            wintypes.DWORD,                     # _In_          DWORD dwCreationDisposition
            wintypes.DWORD,                     # _In_          DWORD dwFlagsAndAttributes
            wintypes.HANDLE]                    # _In_opt_      HANDLE hTemplateFile
    CreateFile_Fn.restype = wintypes.HANDLE

    return wintypes.BOOL(CreateFile_Fn(filename,
                         GENERIC_READ,
                         FILE_SHARE_READ,
                         NULL,
                         OPEN_EXISTING,
                         FILE_ATTRIBUTE_NORMAL,
                         NULL))

#VirtualBox devices
def vbox_devices( writelogs=None):
	res = False
	strs = ["" for x in range(4)]
	strs[0] = "\\\\.\\VBoxMiniRdrDN";
	strs[1] = "\\\\.\\pipe\\VBoxMiniRdDN";
	strs[2] = "\\\\.\\VBoxTrayIPC";
	strs[3] = "\\\\.\\pipe\\VBoxTrayIPC";

	for i in range(4):
		h  = _CreateFile( strs[i])
		if h.value != INVALID_HANDLE_VALUE:
			message = "VirtualBox traced using device %s" % strs[i]
			print message
			if writelogs != None:
				write_logs(message)
				res = True
	return res


#Checking for Tray window
#https://twitter.com/waleedassar
def vbox_traywindow():
	h = FindWindow("VBoxTrayToolWndClass", None);
	h2 = FindWindow(None, "VBoxTrayToolWnd");

	if h | h2:
		return True
	else:
		return False


#int vbox_network_share(){}


#Checking for virtual box processes
def vbox_processes( writelogs=None):
	res = False
	processlist = ["vboxservice.exe", "vboxtray.exe"]
	for proc in psutil.process_iter():
		try:
			if proc.name() in processlist:
				message = "VirtualBox traced using %s process" % proc.name()
				print message
				if writelogs != None:
					write_logs(message)
					res = True
		except:
			pass
	return res

#int vbox_wmi_check_row(IWbemClassObject *row) {}
#int vbox_wmi_devices() {}