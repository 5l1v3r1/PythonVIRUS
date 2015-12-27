#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>


//DWORD WINAPI GetTickCount(void);
//https://msdn.microsoft.com/en-us/library/windows/desktop/ms724408%28v=vs.85%29.aspx

/*
Credits for -> http://sysfail.shost.ca/papers/basic_anti_debug/
We can use the fact that a program executes more slowly when run under a debugger to
detect the presence of a debugger. Thus, we can check the time elapsed
since the system started twice in the program. If the difference of time
between both checks is too high, our program is certainly being run under a debugger. 
The GetTickCount() api tells us the time elapsed in milliseconds since the system was started. 
It takes no parameters.*/

bool timedetect(void){
	int x,y;
	x = GetTickCount();
	for (int i = 0; i < 2000; ++i) printf("");
	y = GetTickCount();
	if (y-x > 1000) 
		return TRUE;
	else 
		return FALSE;
}
