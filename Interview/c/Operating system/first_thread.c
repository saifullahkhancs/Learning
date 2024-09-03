/* pthread_create creates a new thread with a thread descriptor. A descriptor is an
information container of the thread state, execution status, the process that it belongs to,
related threads, stack reference information, and thread-specific resource information
allocated by the process. This function takes four arguments as parameters. The return
type of this function is an integer.*/


#include<stdio.h>   // Standard I/O Routines Library
#include<unistd.h>  // Unix Standard Library
#include<pthread.h> // POSIX Thread Creation Library

void *customThreadFunction(){
for(int i = 0; i < 15; i++){
printf("I am a Custom Thread Function Created By Programmer.\n");
sleep(1);
}
return NULL;
}
int main(){
pthread_t thread;// Thread Descript read 1st

int status;     // Status Variable to store the Status of the thread.
status = pthread_create(&thread, NULL, customThreadFunction, NULL);
/*
int pthread_create(pthread_t *thread,
                   const pthread_attr_t *attr,
                   void * (*start_routine)(void *),
                   void *arg);

•pthread_t is a thread descriptor variable that takes the thread
descriptor, has an argument, and returns the thread ID, which is an
unsigned long integer.
•pthread_attr_t is an argument that determines all the properties
assigned to a thread. If it is a normal default thread, then you set the
attribute value to NULL; otherwise, the argument is changed based
on the programmer’s requirements.
•start_routine is an argument that points to the subroutines that
execute by thread. The return type for this parameter is an void type
because it typecasts return types explicitly. This argument takes a
single value as a parameter. If you want to pass multiple arguments, a
heterogeneous datatype should be passed that might be a struct.
•args is a parameter that depends on the
*/

/*  status = 0 ==> If thread is created Sucessfully.  status = 1 ==> If thread is unable to create.   */

if(!status){   
    printf("Custom Created Successfully.\n");
}
else{
    printf("Unable to create the Custom Thread.\n");
    
    return 0;
}
// Main Function For loop
for(int i = 0; i < 15; i++){
printf("I am the process thread created by compiler By default.\n");
sleep(1);
}
return 0;
}