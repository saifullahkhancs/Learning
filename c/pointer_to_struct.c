#include <stdio.h>
#include <string.h>
struct student 
{
   int roll;
   float cgpa;
    char name[10];
};


int main()
{
    struct student s1 = {15,3.4,"ali"};
    printf("roll no= %d\n", s1.roll);

    struct student *ptr = &s1;

    printf("roll no= %d\n", (*ptr).roll);
    
    printf("name = %s\n", ptr->name);
    printf("cgpa = %f\n", ptr->cgpa);


  //  printf("roll no= %d\n", s1.roll);
  //  printf("cgpa = %f\n", s1.cgpa);
   // printf("name = %s\n", s1.name);
    return 0;
}