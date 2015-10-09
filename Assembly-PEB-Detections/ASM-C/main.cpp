#include "processor.h"
#include "isdebugged.h"

//Coded By B3mB4m

int main( void )
{
	if(processor() == 1)
		//printf("Virual box detected ..\n");
		exit(0);
	else{
		if(isdebugged() == 1)
			//printf("Virual box detected ..\n");
			exit(0);}

	printf("Virtual Box not detected !");
	
}


