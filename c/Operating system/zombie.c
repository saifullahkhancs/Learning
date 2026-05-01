/*
A zombie process is any process that has finished executing, but entry to the process
is available in the process table for reporting to the parent process. A process table is a
data structure that stores all the process-related information in an operating system.
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
    // Making the Parent Process to Sleep for some time.
        sleep(10);
    }else{
        printf("In Child process.!\n");
        exit(0);
    }
    return 0;
}