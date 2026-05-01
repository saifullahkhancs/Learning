#include<stdio.h>   // Standard I/O Routines Library
#include<unistd.h>  // Unix Standard Library
#include<pthread.h> // POSIX Thread Creation Library

void *sayhello( void *input){
    printf("hello %s \n", (char *)input);
    pthread_exit(NULL);
return NULL;
}

int main(){
    
    char name[50];
    printf("Enter your name \n ");
    fgets(name, 50 , stdin);

    pthread_t thread;// Thread Descript read 1st

    int status;     // Status Variable to store the Status of the thread.
    status = pthread_create(&thread, NULL, sayhello, name);

    pthread_join(thread, NULL);
    /*
    This function waits for the termination of another thread. It takes two parameters as
    arguments and returns the integer type. It returns 0 on successful termination and –1 if
    any failure occurs.

    int pthread_join(pthread_t, *thread,
                 void **thread_return)
    The following describes the parameters.
•   thread takes the ID of the thread that is currently waiting for
    termination
    •thread_return is an argument that points to the exit status of the
    termination thread, which is a NULL value.
    
    */

return 0;
}