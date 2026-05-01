/*
A process that does not have a parent process is an orphan process. A child process
becomes an orphan when either of the following occurs.
•When the task of the parent process finishes and terminates without
terminating the child process.
•When an abnormal termination occurs in the parent process.
*/

#include<stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
int main() {
    pid_t child_pid = fork();

   // Parent process
  if (child_pid > 0){
    printf("In Parent Process.!\n");
   }else{
       printf("In Child process.!\n");
       // Making the Child Process to Sleep for some time.
       sleep(10);
       printf("After Sleep Time");
   }
    return 0;
}