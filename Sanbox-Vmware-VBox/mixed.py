from win32api import GetModuleHandle
from os import listdir
from _winreg import *
from platform import node
from psutil import process_iter
from ctypes import *


#Coded by B3mB4m
#This script include Sandbox,Virtualbox and Vmware detections .. 
#http://joe4security.blogspot.com.tr/2012/08/vm-and-sandbox-detections-become-more.html
#https://vazermind.wordpress.com/2013/01/04/c-bypass-sandboxiesunbeltsb-sandboxvmware-by-modules/



def systemfiles():
	banlist = ["hgfs.sys","VBoxVideo.sys","VBoxSF.sys","VBoxMouse.sys","VBoxGuest.sys",
	"vmhgfs.sys","prleth.sys","prlfs.sys","prlmouse.sys","prlvideo.sys","prl_pv32.sys",
	"vpc-s3.sys","vmsrvc.sys","vmx86.sys","vmnet.sys"]

	if [x for x in listdir("C:\\WINDOWS\\system32\\drivers") if x in banlist]:
		return True
	else:
		return False

def anti():
	#SbieDll.dll => To Bypass SandBoxie
	#api_log.dll => To Bypass SunBelt
	#dir_watch.dll => To Bypass SunBelt SandBox
	#dbghelp.dll => To Bypass vmware
	x = ["sbiedll.dll","api_log.dll","dir_watch.dll","dbghelp.dll"]
	for i in x:
		try:
			GetModuleHandle(x)
			return True
		except:
			return False

def usernames():
	#https://msdn.microsoft.com/en-us/library/windows/desktop/ms724432%28v=vs.85%29.aspx
	list = ["currentuser","sandbox","honey","vmware","nepenthes","snort","andy","roo"]
	if [x for x in list if x == node()]:
		return True
	else:
		return False

def registers():
	list = ["vmicheartbeat","vmicvss","vmicshutdown","vmicexchange","vmci","vmdebug"
	 "vmmouse","VMTools","VMMEMCTL","vmware","vmx86","vpcbus","vpc-s3","vpcuhub","msvmmouf"
	 "VBoxMouse","VBoxGuest","VBoxSF","xenevtchn","xennet","xennet6","xensvc","xenvdb"]
	for x in list:
		try:
			openregisters = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
			path = r"SYSTEM\ControlSet001\Services\%s" % x
			RunKey = OpenKey(openregisters, path)
			return True;
		except:
			pass	
	return False

def identifier():
	for x in ["HARDWARE\ACPI\DSDT", "HARDWARE\ACPI\FADT", "HARDWARE\ACPI\RDTSC"]:
		try:
			openregisters = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
			path = r"%s\Vbox__" % x
			RunKey = OpenKey(openregisters, path)
			return True;
		except:
			pass	
	return False

def process():
	list = [ "vmware","vmount2","vmusrvc","vmsrvc","VBoxService","vboxtray","xenservice"
	 "joeboxserver","joeboxcontrol","wireshark","sniff_hit","sysAnalyzer","filemon"
	 "procexp","procmon","regmon","autoruns"]
	for x in list: 
		for proc in process_iter():
			if x.lower()+".exe" == proc.name().lower():
				return True
	return False

def resolve_function():
    handle = windll.kernel32.GetModuleHandleA("kernel32.dll")
    address = windll.kernel32.GetProcAddress(handle, "wine_get_unix_file_name")
    windll.kernel32.CloseHandle(handle)
    if address != 0:
    	return True
    else:
    	return False

def start():
	if True in[systemfiles(),anti(),usernames(),registers(),identifier(),process(),resolve_function()]:
		return True
	else:
		return False
