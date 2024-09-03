#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

// Global data variable
int a=7 , b=5;

// function that access the globaal data

void* add_two_numbers(void* arg)
{
    a = a+3;
    b = b-1;

    printf("a value is %d and " , a);
    printf(" the value of the b is %d \n", b);
    sleep(1);
    exit(0);
}


int main(){
    
    // creating thread instances 

    pthread_t t1, t2, t3;

    pthread_create(&t1,NULL, add_two_numbers,NULL);
    pthread_create(&t2,NULL, add_two_numbers,NULL);
    pthread_create(&t3,NULL, add_two_numbers,NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);

    // destroying the threads

    pthread_exit(t1);
    pthread_exit(t2);
    pthread_exit(t3);

    return 0;


}