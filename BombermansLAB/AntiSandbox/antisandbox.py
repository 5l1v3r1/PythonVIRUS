from win32api import GetModuleHandle
#Coded By B3mB4m

def antisandbox():
	try:
		GetModuleHandle("sbiedll.dll")
		return True
	except:
		return False
