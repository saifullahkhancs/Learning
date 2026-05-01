#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/*
   After fork two same process creaated mean this code is 
   runing 2 times in 
   first parent process cotinuing with parent process id of main
   second is the child pocess id with 0

   so if and if else commmand runs in both but in the parent process
   it prints the parent statement becuse we checling the 
   condition whether it is parent or not

*/

 int  main() {
    printf(" here it gives parent id  before fork%d \n", getpid()); //return parent pid
    int pid=fork();
    
    printf("run in both %d \n", pid); //

    if (pid >0){
        printf("parent created successfull \n");   }

    else if (pid==0){
        printf("child created successfull \n");
        printf(" here it gives chil id %d \n", pid);}
    return 0;
 }