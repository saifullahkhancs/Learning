#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
int main() {
   int status = fork();
   if (status == 0) {
       printf("Hello from child\n");
       printf("Child work is Completed and terminating.!\n");
   }else if(status > 0){
       printf("Hello from parent\n");
       wait(NULL);
       printf("Parent has terminated\n");
   }
   return 0;
}

/*
A common situation that occurs during the creation of a child
process is that the parent process needs to wait or suspend until the child process
execution is completed. After the child process execution completes, the parent process
resumes execution. The work of the wait system call is to suspend the parent system
call until its child process terminates. This wait system call is available in the sys/wait.h
header file. The process ID is the return type of the wait system call.
*/