#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>
 
//Coded By B3mB4m
//gcc masm=intel 

/*
http://sysfail.shost.ca/papers/basic_anti_debug/
We'll start by using the PEB with assembly. 
The PEB contains a byte field named BeingDebugged. 
It is set to 1 when the process is being debugged, otherwise it's set to 0. 
We'll use this value to check the presence of a debugger. For this, 
we'll make the fs segment register to point at offset 30h. Thus we'll have the
PEB base offset ([fs:30h] always points to the PEB). Then we'll have to add this offset 2 to 
get the BeingDebugged field inside the PEB, since BeingDebugged is the second field in this 
data structure. Let's code. 
*/

int isdebugged(void){
  __asm__
    (
      ".intel_syntax noprefix;"
      "xor eax,eax;"
      "xor ebx,ebx;"
      "mov ebx, [fs:0x30];"         
      "mov eax, [ebx+0x02];"            

     );
}
