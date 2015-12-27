import win32api
import win32gui
import win32con
import os

#Coded By B3mB4m
#http://sysfail.shost.ca/papers/basic_anti_debug/

"""
The first trick consists of finding the main window of olly 1 by using it's name.
For this, once again, the WinApi offers us a function called FindWindow().
Giving it a string identifying the parent window name, the function returns a 
window handle (HWND) on this window if it succeeds. Note that the string doesn't have 
to be case sensitive.

The second trick for olly 1 is the use of the function OutputDebugString(). 
This api aims at sending the debugger a string for it to display it. 
We found out that using this function a precise way makes olly 1 crash. 
Thus the following code makes it crash. 
"""

#Well I just add second trick to top of function.So, if olly 1 is presence on computer directly crash.
#Otherwise, return None like useless line.


import win32api
import win32gui
import win32con
import os

def immunityANDollydbg():
	win32api.OutputDebugString("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s")
	#b3mb4m@tuta.io
	name = "Immunity Debugger - %s - [CPU - main thread, module %s]" % (os.path.basename(__file__).split(".py")[0]+".exe",os.path.basename(__file__).split(".py")[0])
	name2 = "OllyDbg - %s - [CPU - main thread, module %s]" % (os.path.basename(__file__).split(".py")[0]+".exe",os.path.basename(__file__).split(".py")[0])
	print name
	for x in [name,name2]:
		handle = win32gui.FindWindow(None, x)
		win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0)
		if handle != 0:
			return True
	return False


