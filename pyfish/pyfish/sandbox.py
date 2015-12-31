#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from utilsh import *
#https://github.com/b3mb4m/PythonVIRUS/blob/master/BombermansLAB/AntiSandbox/antisandbox.py

def antisandbox():
	try:
		win32api.GetModuleHandle("sbiedll.dll")
		return True
	except:
		return False

