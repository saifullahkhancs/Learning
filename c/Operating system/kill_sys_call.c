/*
kill System Call
A kill system call kills processes and signals. Killing a signal or process is the termination
of a program/process/signal. The return type of this kill system call is an integer value.
It returns 0 on the successful execution of the system call; otherwise, it returns –1 for an
error.
*/

#include<stdio.h>
#include<unistd.h>
#include<signal.h>
int main(){
   int pid = fork();
   if(pid == 0){
       printf("Child PID: %d\n",getpid());

   }else{
       printf("Parent PID: %d\n", getppid());
   }
   sleep(2);
   kill(getpid(), SIGQUIT);


/*
int kill(pid_t pid, int sig);
•pid takes the process identifier of the process.
•sig takes the built-in signal parameter that needs to send to the
process.
*/
   return 0;
}