#include <stdio.h>
#include <stdlib.h>
#include<pthread.h>

// data collector 
struct arguments {
    char * name;
    int age;
    char *bloodgroup;
};

void sayhello(void *data){
   printf("Name: %s", ((struct arguments*)data)->name);
   printf("Age: %d\n", ((struct arguments*)data)->age);
   printf("Blood Group: %s\n", ((struct arguments*)data)->bloodgroup);
   return NULL;   
}

int main() {
    struct arguments *person = (struct arguments *)malloc(sizeof(struct arguments));
    printf("This is a Simple data collection application");
    char bloodgroup[5] , name[50];
    int age;
    printf("Enter the name of the person: ");
    fgets(name, 50, stdin);
    printf("Enter the age of the person: ");
    scanf("%d",&age);
    printf("Enter the person's Blood Group: ");
    scanf("%s", bloodgroup);

    person->name = name;
    person->age = age;
    person->bloodgroup= bloodgroup;

    pthread_t thread;
    pthread_create(&thread, NULL, sayhello, (void *)person);
    pthread_join(thread, NULL);
    return 0;
    }
