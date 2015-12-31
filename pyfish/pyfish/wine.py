#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from utils import *


def wine_detect_get_unix_file_name():
	try:
		k32 = win32api.GetModuleHandle("kernel32.dll")
		if win32api.GetProcAddress(k32, "wine_get_unix_file_name"):
			return True
		else:
			return False
	except:
		return False


def wine_reg_key1():
	return pyfish_exists_regkey(HKEY_CURRENT_USER, "SOFTWARE\\Wine");

