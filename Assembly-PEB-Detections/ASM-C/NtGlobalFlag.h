#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>

//Coded By B3mB4m
//Love you ferrie <3 


/*
http://sysfail.shost.ca/papers/basic_anti_debug/files/antidebugPFerrie.pdf

The NtGlobalFlag field exists at offset 0x68 in the Process Environment Block
on the 32-bit versions of Windows, and at offset 0xBC on the 64-bit versions of 
Windows. The value in that field is zero by default. 
*/


int NtGlobalFlag32(void){
 	__asm__
  	(
  		".intel_syntax noprefix;"
  		"xor eax,eax;"
  		"xor ebx,ebx;"
    	"mov ebx,[fs:0x30];"         
    	"mov al,[ebx+0x68];"
		"and al,0x70;"          
		//+0x068 NtGlobalFlag : Uint4B
     );
 
}
/*A common mistake is to use a direct comparison without 
masking the other bits first.  In that case, if any 
other bits are set, then t
he presence of the debugger 
will be missed.*/
int NtGlobalFlag64(void){
 	__asm__
  	(
  		".intel_syntax noprefix;"
  		"xor eax,eax;"
  		"xor ebx,ebx;"
    	"mov ebx,[fs:0x30];"         
		"mov al, [eax+0x10bc];"
		"and al, 0x70;"       
		//+0x10bc NtGlobalFlag : Uint4B (64bit)
     );
 
}


