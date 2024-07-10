#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
// Global data variable
int a=7 , b=5;

pthread_mutex_t mutex;
// function that access the globaal data

void* add_two_numbers(void* arg)
{
    sem_wait(&mutex);
    a = a+3;
    b = b-1;

    printf("a value is %d and " , a);
    printf(" the value of the b is %d \n", b);
    sleep(1);
    sem_post(&mutex);
}



int main(){
    
    sem_init(&mutex , 0 ,1);
    
    // creating thread instances 
    

    pthread_t t1, t2, t3;

    pthread_create(&t1,NULL, add_two_numbers,NULL);
    sleep(1);
    pthread_create(&t2,NULL, add_two_numbers,NULL);
    sleep(1);
    pthread_create(&t3,NULL, add_two_numbers,NULL);
    sleep(1);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);

    // destroying the threads

    sem_destroy(&mutex);

    return 0;


}
