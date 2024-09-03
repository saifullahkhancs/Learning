/*
exit System Call
An exit system call exits the calling process without executing the rest of the code that is
present in the program. It is available in the stdlib.h library. The return of this system call
is void. It doesn’t return anything on execution.
*/

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
int main(){
   int pid = fork();

   if(pid == 0){
       // Prints the Child Process ID.
       printf("Child Process ID: %d\n", getpid());
       exit(0);
   }else{
       // Prints the Parent Process ID.
       printf("Parent Process Id: %d\n", getppid());
       exit(0);
   }
  printf("Processes are exited and this line will not print\n");
  
    return 0;
}
