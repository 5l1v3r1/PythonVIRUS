import win32api
#Coded By B3mB4m

def antisandbox():
	try:
		win32api.GetModuleHandle("sbiedll.dll")
		return True
	except:
		return False
		
