#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>
 
//Coded By B3mB4m
//gcc masm=intel 

/*
http://www.seculert.com/blog/2015/04/new-dyre-version-evades-sandboxes.html
As many sandboxes are configured with only one processor with one core as a way to save resources, 
the check (Figure 1) performed by Dyre is a good and effective way to avoid being analyzed. 
On the other hand, most of the machines (PCs) in use today have more than one core.*/

DWORD processor(void){
 	__asm__
  	(
  		".intel_syntax noprefix;"
  		"xor eax,eax;"
  		"xor ebx,ebx;"
    	"mov ebx, [fs:0x30];"         
    	"mov eax, [ebx+0x064];"            
    	//+0x064 NumberOfProcessors : Uint4B
     );
 
}
