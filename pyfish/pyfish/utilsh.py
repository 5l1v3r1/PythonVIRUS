#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from _winreg import ConnectRegistry
from _winreg import OpenKey
from _winreg import EnumValue
from _winreg import CloseKey
from _winreg import HKEY_LOCAL_MACHINE
from _winreg import HKEY_CURRENT_USER
from time import sleep
from win32process import IsWow64Process
from os import path
from netifaces import ifaddresses
from netifaces import interfaces
from win32gui import FindWindow



from win32api import SetLastError
from win32api import GetLastError
from win32api import OutputDebugString


import ctypes.wintypes as wintypes
from ctypes import windll
#from ctypes.wintypes import HWND, HRESULT



LPSECURITY_ATTRIBUTES = wintypes.LPVOID
GENERIC_READ = 0x80000000
FILE_ATTRIBUTE_NORMAL = 0x00000080
OPEN_EXISTING = 3
FILE_SHARE_READ = 0x00000001
NULL = 0
INVALID_HANDLE_VALUE = -1