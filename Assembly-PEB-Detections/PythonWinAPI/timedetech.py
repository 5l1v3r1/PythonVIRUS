import win32api

#Coded By B3mB4m
#Timing detection
#http://sysfail.shost.ca/papers/basic_anti_debug/

def timedetech():
	cache = 0
	start = win32api.GetTickCount()
	for x in xrange(0, 20000): cache=x;
	stop =  win32api.GetTickCount()
	if (stop-start > 1000):
		return True
	else:
		return False
