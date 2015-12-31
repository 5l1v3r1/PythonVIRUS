#Coded By B3mB4m
#Concat : b3mb4m@protonmail.com

from utils import *


def debug_isdebuggerpresent():
	#It is set to 1 when the process is being debugged, otherwise it's set to 0. 
	IsDebuggerPresent = windll.kernel32.IsDebuggerPresent
	IsDebuggerPresent.restype = wintypes.BOOL
	if IsDebuggerPresent():
		return True;
	else:
		return False;


#That seems like buggy ..
def debug_outputdebugstring():
	err = 9999
	SetLastError(err);
	#If we're been debugging, this shouldn't drop an error.
	OutputDebugString("useless");
	if GetLastError() == err:
		return True;
	else:
		return False;

